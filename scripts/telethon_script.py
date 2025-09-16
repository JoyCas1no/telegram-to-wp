import telethon
from telethon import TelegramClient

# Введите свои API ID и API Hash, полученные на my.telegram.org
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

# Создайте клиента
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    # Замените 'channel_username' на имя пользователя или ID канала
    channel = await client.get_entity('channel_username')
    # Получите все сообщения из канала
    async for message in client.iter_messages(channel):
        if message.text and '#вашхэштег' in message.text:
            print(message.text)
            # Здесь добавьте код для публикации в WordPress

import asyncio
asyncio.run(main())
