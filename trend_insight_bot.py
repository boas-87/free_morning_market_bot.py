import asyncio
from datetime import datetime
from telegram import Bot

TELEGRAM_BOT_TOKEN = "${{ 8030801021:AAFRPdbkLH9UFRZZ7Sn2OyIE9GR7OSslhk0 }}"
TELEGRAM_CHAT_ID = "${{ 8579966665 }}"

async def send_message():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    today = datetime.now().strftime("%Y-%m-%d")

    msg = f"""
📌 트렌드 인사이트 큐레이터
({today})

[경제] 글로벌 증시는 AI·금리 변수 혼조
[도서] 느린 사고, 개인 서사 중심 독서 트렌드
[미술] 아카이브·지역성 기반 전시 확산

✔ 키워드: 맥락과 해석
"""

    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)

if __name__ == "__main__":
    asyncio.run(send_message())
