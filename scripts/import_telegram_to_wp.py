import os
import requests
from telethon import TelegramClient

# Переменные окружения
api_id = int(os.environ['TG_API_ID'])
api_hash = os.environ['TG_API_HASH']
channel = 'PrintTechnics'  # ваш канал

WP_USERNAME = os.environ['WP_USERNAME']
WP_PASSWORD = os.environ['WP_PASSWORD']
WP_URL = 'http://printtechlab.ru/wp-json/wp/v2/posts'
CATEGORY_ID = 8

client = TelegramClient('session_name', api_id, api_hash)

def create_post(title, content, category_id=None):
    print(f"Создаю пост: {title}")
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
    await client.start()
    count = 0
    async for message in client.iter_messages(channel):
        if message.text and '#НашиРаботы' in message.text:
            title = message.text[:50]
            content = message.text
            create_post(title, content, CATEGORY_ID)
            count += 1
    print(f"Импортировано сообщений: {count}")

with client:
    client.loop.run_until_complete(main())

