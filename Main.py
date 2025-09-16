import requests
import time
from telegram import Bot

# Ваши данные
TELEGRAM_BOT_TOKEN = '7538707363:AAFgCzDNTHzdn7stuXAxltnp50uEX9PrOZc'  # ваш токен
TELEGRAM_CHANNEL_ID = '@printtehnics'  # замените на ваш канал или ID
WP_URL = 'http://printtechlab.ru/wp-json/wp/v2/posts'
WP_USERNAME = 'telegram bot'  # вставьте ваш логин
WP_PASSWORD = 'ваш_пароль'  # вставьте ваш пароль (или Application Password)

bot = Bot(token=TELEGRAM_BOT_TOKEN)

last_update_id = None

def get_updates():
    global last_update_id
    updates = bot.get_updates(offset=last_update_id, timeout=10)
    for update in updates:
        last_update_id = update.update_id + 1
        if update.message:
            process_message(update.message)

def process_message(message):
    text = message.text
    title = text[:50]  # Заголовок — первые 50 символов
    content = text

    # ID категории "Наши работы"
    category_id = 8

    # Проверка на хэштег
    if '#НашиРаботы' in text:
        create_post(title, content, category_id)
    else:
        create_post(title, content)

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

# Основной цикл
while True:
    get_updates()
    time.sleep(4 * 60 * 60)  # 4 часа в секундах
