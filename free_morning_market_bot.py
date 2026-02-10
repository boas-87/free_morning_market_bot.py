import asyncio
from telegram import Bot
from datetime import datetime
import os
from openai import OpenAI

# 🔐 GitHub Secrets
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)

def get_market_news():
    today = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
    오늘은 {today}입니다.
    한국 개인 투자자 관점에서
    오늘 아침 주식·증시·경제와 관련해
    꼭 알아야 할 핵심 이슈 3가지를
    간결하게 정리해 주세요.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    ai_text = response.choices[0].message.content.strip()

    return f"""📈 {today} 아침 시장 업데이트

{ai_text}

📌 본 메시지는 자동 생성되었습니다.
"""

async def send_telegram_message():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=get_market_news()
    )

if __name__ == "__main__":
    asyncio.run(send_telegram_message())
