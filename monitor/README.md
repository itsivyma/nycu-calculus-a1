# 課程網站自動追蹤

GitHub Actions 每天 18:00（Asia/Taipei）檢查：

1. 老師課程網站的 Homework 區
2. 陽明交大微積分小組的 9E 共同習題表格

只有偵測到內容變更時才會建立 GitHub Issue，並在 Issue 中標記 `@itsivyma`。`course-websites.json` 保存上一次確認過的內容；`latest-change.md` 保存最近一次變更摘要。

GitHub 的排程工作可能因平台負載延遲數分鐘。也可以在 Actions 頁面選擇 **Track course website updates**，使用 **Run workflow** 手動檢查。

