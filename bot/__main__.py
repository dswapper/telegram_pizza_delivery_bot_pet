from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import bot.settings

from bot.handlers import register, std_commands
from bot.middleware.db import DbSessionMiddleware
from bot.db.base import db_pool


async def bot_pooling() -> None:
    bot_ = Bot(token=bot.settings.TELEGRAM_TOKEN, parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.middleware(DbSessionMiddleware(db_pool))
    dp.callback_query.middleware(DbSessionMiddleware(db_pool))

    dp.include_router(std_commands.router)
    dp.include_router(register.router)

    await dp.start_polling(bot_)
