"""
weather.py
使用 Open-Meteo API（免費、無需 API Key）查詢即時天氣
"""

import requests

# WMO 天氣代碼對應中文說明
WMO_CODES = {
    0: "☀️  晴天",
    1: "🌤️  大致晴朗",
    2: "⛅ 部分多雲",
    3: "☁️  陰天",
    45: "🌫️  霧",
    48: "🌫️  霧淞",
    51: "🌦️  毛毛雨（弱）",
    53: "🌦️  毛毛雨（中）",
    55: "🌧️  毛毛雨（強）",
    61: "🌧️  小雨",
    63: "🌧️  中雨",
    65: "🌧️  大雨",
    71: "🌨️  小雪",
    73: "🌨️  中雪",
    75: "❄️  大雪",
    80: "🌦️  陣雨（弱）",
    81: "🌧️  陣雨（中）",
    82: "⛈️  陣雨（強）",
    95: "⛈️  雷陣雨",
    99: "⛈️  強雷陣雨",
}

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL   = "https://api.open-meteo.com/v1/forecast"


def geocode_city(city_name: str) -> dict | None:
    """將城市名稱轉換為經緯度（使用 Open-Meteo Geocoding API）"""
    try:
        resp = requests.get(
            GEOCODING_URL,
            params={"name": city_name, "count": 1, "language": "zh", "format": "json"},
            timeout=10,
        )
        resp.raise_for_status()
        results = resp.json().get("results")
        if not results:
            return None
        return results[0]  # 回傳第一筆最相關結果
    except requests.RequestException as e:
        print(f"  [錯誤] 城市查詢失敗：{e}")
        return None


def get_weather(city_name: str) -> None:
    """查詢並印出指定城市的當前天氣"""
    print(f"\n🔍 正在查詢「{city_name}」的天氣資訊...")

    # Step 1：地理編碼
    location = geocode_city(city_name)
    if not location:
        print(f"  ❌ 找不到城市「{city_name}」，請確認城市名稱（建議使用英文）。")
        return

    lat  = location["latitude"]
    lon  = location["longitude"]
    name = location.get("name", city_name)
    country = location.get("country", "")

    # Step 2：取得天氣
    try:
        resp = requests.get(
            WEATHER_URL,
            params={
                "latitude": lat,
                "longitude": lon,
                "current": [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "apparent_temperature",
                    "wind_speed_10m",
                    "weathercode",
                ],
                "timezone": "auto",
                "forecast_days": 1,
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        print(f"  [錯誤] 天氣查詢失敗：{e}")
        return

    current = data.get("current", {})
    code    = current.get("weathercode", -1)
    desc    = WMO_CODES.get(code, "🌡️  未知天氣")

    # Step 3：格式化輸出
    print("\n" + "=" * 40)
    print(f"  📍 {name}，{country}")
    print(f"  🕐 更新時間：{current.get('time', 'N/A')}")
    print("=" * 40)
    print(f"  天氣狀況：{desc}")
    print(f"  🌡️  氣溫：{current.get('temperature_2m', 'N/A')} °C")
    print(f"  🌡️  體感溫度：{current.get('apparent_temperature', 'N/A')} °C")
    print(f"  💧 相對濕度：{current.get('relative_humidity_2m', 'N/A')} %")
    print(f"  💨 風速：{current.get('wind_speed_10m', 'N/A')} km/h")
    print("=" * 40)
