from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    set_nickname = State()
    set_fullname = State()
    set_address = State()
    set_phonenumber = State()
    cofirming = State()