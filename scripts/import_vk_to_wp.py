import requests
import os

# Переменные окружения
VK_TOKEN = os.environ['VK_TOKEN']
GROUP_ID = '232610166'  # ID вашей группы VK (без 'club', только цифры)
WP_USERNAME = os.environ['WP_USERNAME']
WP_PASSWORD = os.environ['WP_PASSWORD']
WP_URL = 'http://printtechlab.ru/wp-json/wp/v2/posts'
CATEGORY_ID = 8  # ID вашей категории в WordPress

def get_vk_posts():
    url = 'https://api.vk.com/method/wall.get'
    params = {
        'owner_id': f'-{GROUP_ID}',  # для групп нужен минус перед ID
        'count': 100,
        'access_token': VK_TOKEN,
        'v': '5.131'
    }
    response = requests.get(url, params=params)
    data = response.json()
    print("VK API ответ:", data)  # <--- добавьте эту строку
    return data['response']['items']

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

def main():
    posts = get_vk_posts()
    for post in posts:
        text = post.get('text', '')
        if '#НашиРаботы' in text:
            title = text[:50]
            content = text
            create_post(title, content, CATEGORY_ID)

if __name__ == '__main__':
    main()
