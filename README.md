# 🌍 天氣 & 匯率查詢小工具

> **Weather & Exchange Rate Checker** — 在終端機快速查詢全球即時天氣與匯率，無需帳號、無需 API Key。

---

## ✨ 功能

| 功能 | 說明 |
|------|------|
| 🌤️ 天氣查詢 | 輸入城市名稱，顯示即時氣溫、體感溫度、濕度、風速、天氣狀況 |
| 💱 匯率換算 | 輸入來源/目標貨幣與金額，顯示即時匯率與換算結果 |
| 📋 貨幣列表 | 列出常見貨幣代碼（TWD、USD、JPY…） |
| 🖥️ 雙模式 | 支援互動模式（持續輸入）與命令列模式（單次執行） |

---

## 🚀 快速開始

### 安裝需求

- Python 3.10 以上
- 安裝套件（只需一個）：

```bash
pip install -r requirements.txt
```

### 執行方式

**互動模式**（持續輸入指令）：

```bash
python main.py
```

**命令列模式**（一次執行）：

```bash
python main.py weather Tokyo
python main.py weather "New York"
python main.py rate USD TWD 100
python main.py rate JPY TWD 10000
python main.py currencies
```

---

## 📖 指令說明

```
weather  <城市名稱>              查詢天氣（英文城市名稱）
rate     <來源> <目標> [金額]    查詢匯率（預設金額=1）
currencies                       顯示常見貨幣代碼
help                             顯示說明
quit                             離開程式
```

---

## 🖥️ 執行畫面

```
╔══════════════════════════════════════════╗
║   🌍 天氣 & 匯率查詢小工具 v1.0         ║
║   Weather & Exchange Rate Checker        ║
║   資料來源：Open-Meteo & Frankfurter     ║
╚══════════════════════════════════════════╝

>>> weather Tokyo

🔍 正在查詢「Tokyo」的天氣資訊...

========================================
  📍 Tokyo，日本
  🕐 更新時間：2026-11-01T14:00
========================================
  天氣狀況：🌤️  大致晴朗
  🌡️  氣溫：18.5 °C
  🌡️  體感溫度：16.8 °C
  💧 相對濕度：55 %
  💨 風速：12.3 km/h
========================================

>>> rate USD TWD 100

🔍 正在查詢 USD → TWD 的匯率...

========================================
  💱 匯率資訊（資料日期：2026-11-01）
========================================
  USD (美元)
    ↓
  TWD (新台幣)
  匯率：1 USD = 32.45 TWD
  換算：100 USD = 3245.0 TWD
========================================
```

---

## 📡 使用的 API

| API | 用途 | 是否需要 Key |
|-----|------|------------|
| [Open-Meteo](https://open-meteo.com/) | 天氣查詢 | ❌ 不需要 |
| [Open-Meteo Geocoding](https://open-meteo.com/en/docs/geocoding-api) | 城市名稱轉經緯度 | ❌ 不需要 |
| [Frankfurter](https://www.frankfurter.app/) | 匯率查詢 | ❌ 不需要 |

---

## 📁 檔案結構

```
weather-rate-tool/
├── main.py          # 主程式（互動 & 命令列入口）
├── weather.py       # 天氣查詢模組
├── exchange.py      # 匯率查詢模組
├── requirements.txt # 套件需求
└── README.md        # 說明文件
```

---

## 🔮 未來改進方向

- [ ] 支援查詢未來 7 天天氣預報
- [ ] 加入歷史匯率折線圖（matplotlib）
- [ ] 打包成 `.exe` 可執行檔（PyInstaller）
- [ ] 新增 LINE Bot 或 Telegram Bot 通知整合

---

## 📄 授權

MIT License
