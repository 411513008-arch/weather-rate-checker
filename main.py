"""
main.py - 天氣 & 匯率查詢小工具
========================================
使用方式（命令列）：
  python main.py weather <城市>
  python main.py rate <來源貨幣> <目標貨幣> [金額]
  python main.py currencies
  python main.py   （互動模式）

範例：
  python main.py weather Tokyo
  python main.py weather "New York"
  python main.py rate USD TWD 100
  python main.py rate JPY TWD 10000
"""

import sys
import io
# 設定標準輸出為 UTF-8，解決 Windows cp950 編碼問題
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from weather import get_weather
from exchange import get_exchange_rate, list_currencies

BANNER = """
╔══════════════════════════════════════════╗
║   🌍 天氣 & 匯率查詢小工具 v1.0         ║
║   Weather & Exchange Rate Checker        ║
║   資料來源：Open-Meteo & Frankfurter     ║
╚══════════════════════════════════════════╝
"""

HELP_TEXT = """
📖 指令說明：
  [1] weather  <城市名稱>              查詢天氣
  [2] rate     <來源> <目標> [金額]    查詢匯率（預設金額=1）
  [3] currencies                       顯示貨幣代碼列表
  [4] help                             顯示此說明
  [5] quit / exit                      離開程式

範例：
  weather Tokyo
  weather "New York"
  rate USD TWD 100
  rate JPY TWD 10000
"""


def run_command(args: list[str]) -> bool:
    """執行單一指令，回傳 False 代表離開"""
    if not args:
        return True

    cmd = args[0].lower()

    if cmd in ("quit", "exit", "q"):
        print("\n👋 掰掰！")
        return False

    elif cmd in ("help", "h", "?"):
        print(HELP_TEXT)

    elif cmd == "weather":
        if len(args) < 2:
            print("  ⚠️  請提供城市名稱。例：weather Tokyo")
        else:
            city = " ".join(args[1:])
            get_weather(city)

    elif cmd == "rate":
        if len(args) < 3:
            print("  ⚠️  請提供兩種貨幣代碼。例：rate USD TWD")
        else:
            from_c  = args[1]
            to_c    = args[2]
            amount  = float(args[3]) if len(args) >= 4 else 1.0
            get_exchange_rate(from_c, to_c, amount)

    elif cmd == "currencies":
        list_currencies()

    else:
        print(f"  ❓ 不認識的指令「{cmd}」，輸入 help 查看說明。")

    return True


def interactive_mode() -> None:
    """互動模式：持續讀取使用者輸入"""
    print(BANNER)
    print("  輸入 help 查看指令說明，輸入 quit 離開。\n")

    while True:
        try:
            raw = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 掰掰！")
            break

        if not raw:
            continue

        args = raw.split()
        if not run_command(args):
            break


def cli_mode(argv: list[str]) -> None:
    """命令列模式：一次性執行後結束"""
    print(BANNER)
    run_command(argv)


if __name__ == "__main__":
    args = sys.argv[1:]  # 去掉程式名稱本身

    if args:
        cli_mode(args)
    else:
        interactive_mode()
