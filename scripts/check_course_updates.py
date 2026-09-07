#!/usr/bin/env python3
"""Track homework-related changes on the course websites."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.request
from pathlib import Path


TEACHER_URL = "https://catalin-carstea.github.io/courses/calculus1-2026.html"
COMMON_EXERCISES_URL = (
    "https://calculus.math.nycu.edu.tw/calculusmath/ch/app/artwebsite/view"
    "?module=artwebsite&id=39529&serno=3e458c4c-38ac-4e7a-b6c2-4499670c07ba"
)

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "monitor" / "course-websites.json"
REPORT_PATH = ROOT / "monitor" / "latest-change.md"
CURRENT_PATH = ROOT / "course-updates.md"


def fetch(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "nycu-calculus-a1-course-monitor/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def plain_text(fragment: str) -> str:
    fragment = re.sub(r"<script\b.*?</script>", " ", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<style\b.*?</style>", " ", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(fragment)).strip()


def teacher_homework(page: str) -> str:
    match = re.search(
        r'<section\b[^>]*\bid=["\']homework["\'][^>]*>(.*?)</section>',
        page,
        flags=re.I | re.S,
    )
    if not match:
        raise RuntimeError("找不到老師網站的 Homework 區塊")
    return re.sub(r"^Homework\s+", "", plain_text(match.group(1)), flags=re.I)


def common_exercises(page: str) -> dict[str, str]:
    table_match = re.search(
        r'<table\b[^>]*class=["\'][^"\']*ed_table[^"\']*["\'][^>]*>(.*?)</table>',
        page,
        flags=re.I | re.S,
    )
    if not table_match:
        raise RuntimeError("找不到微積分小組的共同習題表格")

    result: dict[str, str] = {}
    for row in re.findall(r"<tr\b[^>]*>(.*?)</tr>", table_match.group(1), flags=re.I | re.S):
        cells = re.findall(r"<td\b[^>]*>(.*?)</td>", row, flags=re.I | re.S)
        if len(cells) >= 2:
            section = plain_text(cells[0])
            exercises = plain_text(cells[1])
            if section and exercises:
                result[section] = exercises
    if not result:
        raise RuntimeError("共同習題表格中沒有可辨識的題號")
    return result


def snapshot() -> dict[str, object]:
    return {
        "teacher_homework": teacher_homework(fetch(TEACHER_URL)),
        "common_exercises": common_exercises(fetch(COMMON_EXERCISES_URL)),
    }


def differences(old: dict[str, object], new: dict[str, object]) -> list[str]:
    changes: list[str] = []

    old_homework = str(old.get("teacher_homework", ""))
    new_homework = str(new.get("teacher_homework", ""))
    if old_homework != new_homework:
        changes.extend(
            [
                "## 老師課程網站 Homework 區更新",
                "",
                f"- 更新前：{old_homework or '（空白）'}",
                f"- 更新後：{new_homework or '（空白）'}",
                f"- 來源：{TEACHER_URL}",
                "",
            ]
        )

    old_exercises = dict(old.get("common_exercises", {}))
    new_exercises = dict(new.get("common_exercises", {}))
    exercise_changes: list[str] = []
    for section in sorted(set(old_exercises) | set(new_exercises), key=section_key):
        before = old_exercises.get(section)
        after = new_exercises.get(section)
        if before != after:
            exercise_changes.append(
                f"- **{section}**：`{before or '（無）'}` → `{after or '（無）'}`"
            )
    if exercise_changes:
        changes.extend(
            [
                "## 微積分小組 9E 共同習題更新",
                "",
                *exercise_changes,
                "",
                f"來源：{COMMON_EXERCISES_URL}",
                "",
            ]
        )
    return changes


def section_key(value: str) -> tuple[int, ...]:
    try:
        return tuple(int(part) for part in value.split("."))
    except ValueError:
        return (9999,)


def write_state(data: dict[str, object]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_course_updates(data: dict[str, object]) -> None:
    homework = str(data.get("teacher_homework", ""))
    exercises = dict(data.get("common_exercises", {}))
    checked_at = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime(
        "%Y-%m-%d %H:%M Asia/Taipei"
    )
    rows = [
        f"| {section} | {exercises[section]} |"
        for section in sorted(exercises, key=section_key)
    ]
    content = "\n".join(
        [
            "# 課程網站最新資訊",
            "",
            "> 本頁由 GitHub Actions 自動產生，請勿手動編輯。",
            "",
            f"追蹤基準更新時間：{checked_at}",
            "",
            "## 老師網站 Homework 區",
            "",
            homework or "（目前沒有內容）",
            "",
            f"來源：{TEACHER_URL}",
            "",
            "## 微積分小組 9E 共同習題",
            "",
            "| 節次 | 題號 |",
            "| --- | --- |",
            *rows,
            "",
            f"來源：{COMMON_EXERCISES_URL}",
            "",
        ]
    )
    CURRENT_PATH.write_text(content, encoding="utf-8")


def set_output(changed: bool) -> None:
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with Path(github_output).open("a", encoding="utf-8") as output:
            output.write(f"changed={'true' if changed else 'false'}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--initialize", action="store_true")
    args = parser.parse_args()

    current = snapshot()
    if args.initialize or not STATE_PATH.exists():
        write_state(current)
        write_course_updates(current)
        print(f"Initialized {STATE_PATH.relative_to(ROOT)}")
        set_output(False)
        return 0

    previous = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    changes = differences(previous, current)
    if not changes:
        print("No course website changes detected.")
        set_output(False)
        return 0

    checked_at = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime(
        "%Y-%m-%d %H:%M Asia/Taipei"
    )
    report = "\n".join(
        [
            "# 微積分課程網站更新",
            "",
            "@itsivyma 偵測到課程題目或作業資訊變更。",
            "",
            f"檢查時間：{checked_at}",
            "",
            *changes,
        ]
    )
    REPORT_PATH.write_text(report, encoding="utf-8")
    write_state(current)
    write_course_updates(current)
    print(report)
    set_output(True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
