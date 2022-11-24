from aiogram import Bot, Dispatcher

import app.settings

bot = Bot(token=app.settings.TELEGRAM_TOKEN, parse_mode='HTML')
dispatcher = Dispatcher()


async def bot_pooling() -> None:
    await dispatcher.start_polling(bot)
