import os
import requests
import asyncio
from telegram import Bot

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
WP_USERNAME = os.environ['WP_USERNAME']
WP_PASSWORD = os.environ['WP_PASSWORD']
WP_URL = 'http://printtechlab.ru/wp-json/wp/v2/posts'
CATEGORY_ID = 8  # ID вашей категории

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def create_post(title, content, category_id=None):
    data = {
        'title': title,
        'content': content,
        'status': 'publish',
    }
    if category_id:
        data['categories'] = [category_id]
    response = requests.post(WP_URL, auth=(WP_USERNAME, WP_PASSWORD), json=data)
    print(f"Status: {response.status_code}")
    print(response.json())

async def main():
    last_update_id = None
    updates = await bot.get_updates(offset=last_update_id, timeout=10)
    for update in updates:
        last_update_id = update.update_id + 1
        if update.message and update.message.text:
            text = update.message.text
            title = text[:50]
            content = text
            if '#НашиРаботы' in text:
                create_post(title, content, CATEGORY_ID)
            else:
                create_post(title, content)

if __name__ == "__main__":
    asyncio.run(main())

