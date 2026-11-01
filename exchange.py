"""
exchange.py
使用 Open Exchange Rates API（免費、無需 API Key）查詢即時匯率
API：https://open.er-api.com/
"""

import requests

BASE_URL = "https://open.er-api.com/v6/latest"

# 常見貨幣中文說明
CURRENCY_NAMES = {
    "TWD": "新台幣",
    "USD": "美元",
    "EUR": "歐元",
    "JPY": "日圓",
    "GBP": "英鎊",
    "CNY": "人民幣",
    "KRW": "韓元",
    "HKD": "港幣",
    "SGD": "新加坡元",
    "AUD": "澳幣",
    "CAD": "加拿大元",
    "THB": "泰銖",
    "MYR": "馬來西亞令吉",
    "VND": "越南盾",
    "PHP": "菲律賓披索",
}


def get_exchange_rate(from_currency: str, to_currency: str, amount: float = 1.0) -> None:
    """查詢並印出兩種貨幣之間的即時匯率"""
    from_c = from_currency.upper()
    to_c   = to_currency.upper()

    print(f"\n🔍 正在查詢 {from_c} → {to_c} 的匯率...")

    try:
        resp = requests.get(f"{BASE_URL}/{from_c}", timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        print(f"  [錯誤] 匯率查詢失敗：{e}")
        print("  💡 請確認貨幣代碼是否正確（例：USD、EUR、TWD、JPY）")
        return

    if data.get("result") != "success":
        print(f"  ❌ 查詢失敗：{data.get('error-type', '未知錯誤')}")
        return

    rates = data.get("rates", {})
    if to_c not in rates:
        print(f"  ❌ 找不到貨幣代碼「{to_c}」，請輸入 currencies 查看支援清單。")
        return

    rate      = rates[to_c]
    update_t  = data.get("time_last_update_utc", "N/A")
    converted = round(amount * rate, 4)

    from_name = CURRENCY_NAMES.get(from_c, from_c)
    to_name   = CURRENCY_NAMES.get(to_c, to_c)

    print("\n" + "=" * 40)
    print(f"  💱 匯率資訊")
    print(f"  📅 更新時間：{update_t}")
    print("=" * 40)
    print(f"  {from_c} ({from_name})")
    print(f"    ↓")
    print(f"  {to_c} ({to_name})")
    print(f"  匯率：1 {from_c} = {rate:.4f} {to_c}")
    print(f"  換算：{amount} {from_c} = {converted} {to_c}")
    print("=" * 40)


def list_currencies() -> None:
    """列出常用貨幣代碼"""
    print("\n📋 常用貨幣代碼：")
    print("-" * 30)
    for code, name in CURRENCY_NAMES.items():
        print(f"  {code}  →  {name}")
    print("-" * 30)
    print("  （支援全球 170+ 種貨幣）")
