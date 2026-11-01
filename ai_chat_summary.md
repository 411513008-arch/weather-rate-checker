# AI 對話摘要 — 天氣 & 匯率查詢小工具

> 本文件為期中專題開發過程中，與 AI 助理（Google Antigravity）的對話摘要。

---

## 開發時間
2026 年 11 月 1 日（15:00 – 16:00）

---

## 對話摘要

### 1. 題目選擇階段

**我的需求**：期中作業要做一個程式專題，1 小時內完成，目標 80 分以上。

**AI 建議**：提供 5 個方案，分析各方案的技術棧、完成時間、展示效果、優缺點。方案 B（天氣/匯率查詢工具）因為展示效果強、無需 API Key、實用性高而被推薦為首選。

**決定**：選擇方案 B。

---

### 2. 程式架構設計

**討論重點**：
- 使用哪些免費 API（無需 API Key，符合作業規範）
- 最終確認：Open-Meteo（天氣 + 地理編碼）、Open Exchange Rates（匯率）
- 程式結構：拆分為 `main.py`、`weather.py`、`exchange.py` 三個模組

---

### 3. 程式碼生成

**AI 生成的程式**：
- `weather.py`：呼叫 Open-Meteo Geocoding API 將城市名稱轉為經緯度，再呼叫 Forecast API 取得即時天氣，以 WMO 天氣代碼對應中文天氣描述
- `exchange.py`：呼叫 Open Exchange Rates API 取得匯率，支援自訂換算金額
- `main.py`：整合兩個模組，支援互動模式與命令列模式，加入完整的指令解析

---

### 4. 偵錯階段

**問題 1**：Windows 終端機 `cp950` 編碼問題，導致 emoji 無法顯示
- **解法**：在 `main.py` 最上方加入 `sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")`，並透過環境變數 `PYTHONIOENCODING=utf-8` 執行

**問題 2**：Frankfurter API 不支援 TWD（新台幣）
- **解法**：改用 `open.er-api.com`，支援 170+ 種貨幣，同樣免費且無需 API Key

---

### 5. 測試驗證

**測試結果**：
- `weather Tokyo` → 成功顯示東京即時天氣（19.3°C，部分多雲）
- `rate USD TWD 100` → 成功顯示 1 USD = 32.6103 TWD，100 USD = 3261.03 TWD

---

### 6. 文件生成

**AI 協助撰寫**：
- README.md（專案說明、安裝指南、使用範例、API 說明）
- 專題報告草稿（做什麼、給誰用、怎麼做、怎麼測、下一步）
- 本 AI 對話摘要

---

## 關鍵技術決策

| 決策 | 選擇 | 原因 |
|------|------|------|
| 天氣 API | Open-Meteo | 完全免費、無需 Key、準確度高 |
| 匯率 API | Open Exchange Rates | 支援 TWD、無需 Key、每日更新 |
| 語言 | Python | 簡潔、套件豐富、易於展示 |
| 介面 | CLI（命令列） | 1 小時內最快實作，90 秒 demo 效果佳 |
| 架構 | 多模組分離 | 程式碼可讀性高、易於擴充 |

---

## 學習收穫

1. 了解如何串接 REST API，處理 JSON 回應格式
2. 學會處理 Windows 環境的 UTF-8 編碼問題
3. 理解如何設計 CLI 工具，支援互動和非互動兩種模式
4. 體驗 AI 輔助開發的流程：需求描述 → 代碼生成 → 測試偵錯 → 文件撰寫
