# 課程網站自動追蹤

GitHub Actions 每天 08:00 與 18:00（Asia/Taipei）各檢查一次：

1. 老師課程網站的 Homework 區
2. 老師課程網站的 Lecture notes（自動下載 PDF）
3. 陽明交大微積分小組的 9E 共同習題表格

只有偵測到內容變更時才會建立 GitHub Issue，並在 Issue 中標記 `@itsivyma`。新增或改版的講義會下載到 `course-materials/lecture-notes/`。同時會更新根目錄的 `course-updates.md`、追蹤基準與變更摘要，然後自動提交並推送到 `main`。

- `course-updates.md`：網站目前公布的最新內容
- `course-websites.json`：上一次確認過的追蹤基準
- `latest-change.md`：最近一次變更摘要

GitHub 的排程工作可能因平台負載延遲數分鐘。也可以在 Actions 頁面選擇 **Track course website updates**，使用 **Run workflow** 手動檢查。
