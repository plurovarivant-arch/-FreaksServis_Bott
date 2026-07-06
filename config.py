import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv "8768438638:AAGWgS28BfiAwkdhxMzXPKY9e4uIu3j9fM0"

COMPANY_INFO = {
    'name': 'FreaksServis',
    'description': """Мы предоставляем полный спектр услуг в сфере:
- Дроп-сервис
- Отрисовки и дизайна
- Скупки товаров
- Услуги Boxera
- Профессионального обучения

Обратитесь к нашим менеджерам для получения подробной информации о каждой услуге!"""
}

SERVICES = {
    'drop_service': {
        'name': 'Дроп сервис',
        'emoji': '📦',
        'description': 'Полный спектр услуг и дроп-сервиса для вас'
    },
    'drawing': {
        'name': 'Отрисовка',
        'emoji': '🎨',
        'description': 'Профессиональная отрисовка и дизайнерские услуги'
    },
    'purchase': {
        'name': 'Скуп товаров',
        'emoji': '💰',
        'description': ''
    },
    'boxing': {
        'name': 'Услуги Boxera',
        'emoji': '📦',
        'description': ''
    },
    'education': {
        'name': 'Обучение',
        'emoji': '📚',
        'description': 'Профессиональное обучение по различным направлениям'
    }
}

MANAGERS = {
    'drop_service': {
        'name': 'Drop сервис',
        'username': 'f_ran_kli_n'
    },
    'drawing': {
        'name': 'Отрисовка',
        'username': 'risujudljatebja'
    },
    'purchase': {
        'name': 'Скуп товаров',
        'username': 'PROF_HARDI'
    },
    'boxing': {
        'name': 'Boxer Manager',
        'username': 'ASDSDA88'
    },
    'education': {
        'name': 'Скуп',
        'username': 'PROF_HARDI'
    }
}

ARTICLE_LINK = "https://telegra.ph/INFO-07-04-60"
PRICE_LINK = "https://telegra.ph/Tarify-na-priyom-posylok-07-05"

DEBUG = os.getenv("DEBUG", "False").lower() == "true"
