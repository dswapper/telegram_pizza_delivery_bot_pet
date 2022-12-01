import os

DATABASE_URL = os.environ['DATABASE_URL'].replace('postgres://', 'postgresql+asyncpg://')
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']