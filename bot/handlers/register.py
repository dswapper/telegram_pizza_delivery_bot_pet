from aiogram import types, Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from bot.db.requests import register_user, is_registered
from bot.db.models import User
from bot.handlers.states import Registration

router = Router()


@router.message(Text(text=['Зарегистрироваться', '/register'])) # ), Command(commands=["register"])
async def cmd_register(message:types.Message, state: FSMContext, session: AsyncSession) -> None:
    if await is_registered(message.from_user.id, session):
        await message.answer('Вы уже зареганы)')
        await state.clear()
    else:
        await message.answer('Введите желаемый ник:')
        await state.set_state(Registration.set_nickname)


@router.message(Registration.set_nickname)
async def setting_nickname(message: types.Message, state: FSMContext) -> None:
    await state.update_data(nickname=message.text.lower())
    await message.answer(
        'Теперь введите свою Фамилию и Имя'
    )
    await state.set_state(Registration.set_fullname)


@router.message(Registration.set_fullname)
async def setting_fullname(message: types.Message, state: FSMContext) -> None:
    await state.update_data(fullname=message.text)
    user_data = await state.get_data()
    await message.answer(
        f"Отлично, {user_data['nickname']}, теперь мне нужен твой адресс"
    )
    await state.set_state(Registration.set_address)


@router.message(Registration.set_address)
async def setting_address(message: types.Message, state: FSMContext) -> None:
    await state.update_data(address=message.text)
    await message.answer(
        f"Супер, теперь последний шаг, номер телефона? (обещаю не звонить по путякам)"
    )
    await state.set_state(Registration.set_phone_number)


@router.message(Registration.set_phone_number)
async def setting_phone_number(message: types.Message, state: FSMContext) -> None:
    await state.update_data(phone_number=message.text)
    user_data = await state.get_data()
    await message.answer(
        f"Вы ввели данные: \n{user_data['nickname']} \n{user_data['fullname']} \n{user_data['address']} \n{user_data['phone_number']} \nВерно?"
    )
    await state.set_state(Registration.confirming)


@router.message(Registration.confirming)
async def registration_confirming(message: types.Message, state: FSMContext, session: AsyncSession) -> None:
    user_data = await state.get_data()
    if message.text.lower() == 'да':
        try:
            user = User()
            user.fullname = user_data['fullname']
            user.address = user_data['address']
            user.phone_number = user_data['phone_number']
            user.nickname = user_data['nickname']
            user.telegram_id = message.from_user.id
            await register_user(session, user)
        except IntegrityError:
            await message.answer('Вы уже зареганы или произошла ошибка(')
        else:
            await message.answer('Вы успешно зареганы!')
        await state.clear()
    elif message.text.lower() == 'нет':
        await message.answer('Хорошо, попробуйте ввести данные снова или напишите /cancel чтобы отменить регистрацию.')
        await message.answer('Введите Ник:')
        await state.set_state(Registration.set_nickname)
    else:
        await message.answer('Введите да или нет')
