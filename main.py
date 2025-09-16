import requests
import time
from telegram import Bot

# Ваши данные
TELEGRAM_BOT_TOKEN = '7538707363:AAFgCzDNTHzdn7stuXAxltnp50uEX9PrOZc'  # ваш токен
TELEGRAM_CHANNEL_ID = '@printtechnics'  # замените на ваш канал или ID
WP_URL = 'http://printtechlab.ru/wp-json/wp/v2/posts'
WP_USERNAME = 'Telegram bot'  # ваш логин в WordPress
WP_PASSWORD = 'nxNE WhDS NBXX rX0F VpSm sfH2'  # ваш пароль или Application Password

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Для хранения последнего обновления
last_update_id = None

def get_updates():
    global last_update_id
    updates = bot.get_updates(offset=last_update_id, timeout=10)
    for update in updates:
        last_update_id = update.update_id + 1
        if update.message:
            process_message(update.message)

def process_message(message):
    title = message.text[:50]  # Заголовок — первые 50 символов
    content = message.text
    create_post(title, content)

def create_post(title, content):
    auth = (WP_USERNAME, WP_PASSWORD)
    data = {
        'title': title,
        'content': content,
        'status': 'publish'
    }
    response = requests.post(WP_URL, auth=auth, json=data)
    print(f"Status: {response.status_code}")
    print(response.json())

# Основной цикл
while True:
    get_updates()
    time.sleep(4 * 60 * 60)  # 4 часа в секундах
