import asyncio
from telegram import Bot
from telegram.request import HTTPXRequest
from datetime import datetime
import os

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def get_market_news():
    today = datetime.now().strftime("%Y-%m-%d")
    return f"""📈 {today} 주식 동향 알림입니다.

- 🇰🇷 국내 증시 흐름
- 🇺🇸 미국 증시 및 나스닥
- ⭐ 추천 ETF: KODEX 200, TIGER 미국나스닥100
- 📊 주요 경제 일정 확인
"""

async def send_telegram_message(msg):
    request = HTTPXRequest()   # ✅ 여기 수정됨
    bot = Bot(token=TELEGRAM_BOT_TOKEN, request=request)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)

if __name__ == "__main__":
    asyncio.run(send_telegram_message(get_market_news()))
