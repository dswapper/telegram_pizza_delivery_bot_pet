"""
Package for telegram API
"""

import asyncio
from app.telegram.main_bot import bot_pooling
import app.telegram.commands


def run() -> None:
    asyncio.run(bot_pooling())
