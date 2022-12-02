from aiogram import types, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(message: types.Message) -> None:
    register_button = KeyboardButton(text='Зарегистрироваться')
    keyboard = ReplyKeyboardMarkup(keyboard=[[register_button]], one_time_keyboard = True, resize_keyboard=True)
    await message.answer("Привет, если что это Pet-проект, а не настоящая пиццерия, хихих", reply_markup=keyboard)


@router.message(Command(commands=["help"]))
async def cmd_help(message: types.Message) -> None:
    await message.reply("Тут пока ничего не написано, но <b>скоро</b> будет")


@router.message(Command(commands=["cancel"]))
async def cmd_cancel(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.reply("Действие отменено")