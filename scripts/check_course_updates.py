#!/usr/bin/env python3
"""Track course updates and download the teacher's lecture-note PDFs."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse


TEACHER_URL = "https://catalin-carstea.github.io/courses/calculus1-2026.html"
COMMON_EXERCISES_URL = (
    "https://calculus.math.nycu.edu.tw/calculusmath/ch/app/artwebsite/view"
    "?module=artwebsite&id=39529&serno=3e458c4c-38ac-4e7a-b6c2-4499670c07ba"
)

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "monitor" / "course-websites.json"
REPORT_PATH = ROOT / "monitor" / "latest-change.md"
CURRENT_PATH = ROOT / "course-updates.md"
LECTURE_NOTES_DIR = ROOT / "course-materials" / "lecture-notes"
MAX_PDF_BYTES = 50 * 1024 * 1024


def fetch(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "nycu-calculus-a1-course-monitor/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_pdf(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "nycu-calculus-a1-course-monitor/1.0"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        content = response.read(MAX_PDF_BYTES + 1)
    if len(content) > MAX_PDF_BYTES:
        raise RuntimeError(f"Lecture note exceeds 50 MiB: {url}")
    if not content.startswith(b"%PDF-"):
        raise RuntimeError(f"Lecture note is not a PDF: {url}")
    return content


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


def lecture_note_links(page: str) -> list[dict[str, str]]:
    match = re.search(
        r'<section\b[^>]*\bid=["\']lecture-notes["\'][^>]*>(.*?)</section>',
        page,
        flags=re.I | re.S,
    )
    if not match:
        raise RuntimeError("找不到老師網站的 Lecture notes 區塊")

    notes: list[dict[str, str]] = []
    filenames: set[str] = set()
    for attrs, label in re.findall(
        r"<a\b([^>]*)>(.*?)</a>", match.group(1), flags=re.I | re.S
    ):
        href_match = re.search(r'\bhref=["\']([^"\']+)["\']', attrs, flags=re.I)
        if not href_match:
            continue
        url = urljoin(TEACHER_URL, html.unescape(href_match.group(1)))
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc != urlparse(TEACHER_URL).netloc:
            raise RuntimeError(f"Lecture note points to an unexpected host: {url}")
        filename = unquote(Path(parsed.path).name)
        if not filename.lower().endswith(".pdf"):
            continue
        if not re.fullmatch(r"[A-Za-z0-9._-]+\.pdf", filename, flags=re.I):
            raise RuntimeError(f"Unsafe lecture-note filename: {filename}")
        if filename in filenames:
            raise RuntimeError(f"Duplicate lecture-note filename: {filename}")
        filenames.add(filename)
        notes.append(
            {
                "title": re.sub(r"\s*\(PDF\)\s*$", "", plain_text(label), flags=re.I),
                "url": url,
                "filename": filename,
            }
        )
    return notes


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


def snapshot() -> tuple[dict[str, object], dict[str, bytes]]:
    teacher_page = fetch(TEACHER_URL)
    notes = lecture_note_links(teacher_page)
    assets: dict[str, bytes] = {}
    for note in notes:
        content = fetch_pdf(note["url"])
        note["sha256"] = hashlib.sha256(content).hexdigest()
        assets[note["filename"]] = content
    return (
        {
            "teacher_homework": teacher_homework(teacher_page),
            "lecture_notes": notes,
            "common_exercises": common_exercises(fetch(COMMON_EXERCISES_URL)),
        },
        assets,
    )


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

    old_notes = {
        str(note.get("url")): note
        for note in old.get("lecture_notes", [])
        if isinstance(note, dict)
    }
    new_notes = {
        str(note.get("url")): note
        for note in new.get("lecture_notes", [])
        if isinstance(note, dict)
    }
    note_changes: list[str] = []
    for url in sorted(set(old_notes) | set(new_notes)):
        before = old_notes.get(url)
        after = new_notes.get(url)
        if before is None and after is not None:
            note_changes.append(f"- 新增：**{after['title']}** (`{after['filename']}`)")
        elif after is None and before is not None:
            note_changes.append(f"- 網站已移除：**{before['title']}**（本地檔案保留）")
        elif before != after and after is not None:
            note_changes.append(f"- 更新：**{after['title']}** (`{after['filename']}`)")
    if note_changes:
        changes.extend(
            [
                "## 老師講義 Lecture notes 更新",
                "",
                *note_changes,
                "",
                f"來源：{TEACHER_URL}#lecture-notes",
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


def write_lecture_notes(assets: dict[str, bytes]) -> list[str]:
    LECTURE_NOTES_DIR.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    for filename, content in assets.items():
        destination = LECTURE_NOTES_DIR / filename
        if destination.exists() and destination.read_bytes() == content:
            continue
        temporary = destination.with_suffix(destination.suffix + ".tmp")
        temporary.write_bytes(content)
        temporary.replace(destination)
        written.append(filename)
    return written


def write_course_updates(data: dict[str, object]) -> None:
    homework = str(data.get("teacher_homework", ""))
    notes = [note for note in data.get("lecture_notes", []) if isinstance(note, dict)]
    exercises = dict(data.get("common_exercises", {}))
    checked_at = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime(
        "%Y-%m-%d %H:%M Asia/Taipei"
    )
    rows = [
        f"| {section} | {exercises[section]} |"
        for section in sorted(exercises, key=section_key)
    ]
    note_rows = [
        f"- [{note['title']}](course-materials/lecture-notes/{note['filename']})"
        for note in notes
    ] or ["（目前沒有講義）"]
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
            "## 老師講義 Lecture notes",
            "",
            *note_rows,
            "",
            f"來源：{TEACHER_URL}#lecture-notes",
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

    current, lecture_assets = snapshot()
    written_notes = write_lecture_notes(lecture_assets)
    if args.initialize or not STATE_PATH.exists():
        write_state(current)
        write_course_updates(current)
        print(f"Initialized {STATE_PATH.relative_to(ROOT)}")
        set_output(False)
        return 0

    previous = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    changes = differences(previous, current)
    if written_notes and not any("Lecture notes" in line for line in changes):
        changes.extend(
            [
                "## 老師講義 Lecture notes 檔案補齊",
                "",
                *(f"- `{filename}`" for filename in written_notes),
                "",
            ]
        )
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
            "@itsivyma 偵測到課程網站內容變更。",
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
