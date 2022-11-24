from app.telegram.main_bot import dispatcher
from aiogram import types
from aiogram.filters import Command


@dispatcher.message(Command(commands=["start"]))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Привет, если что это Pet-проект, а не настоящая пиццерия, хихих")
