from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    set_nickname = State()
    set_fullname = State()
    set_address = State()
    set_phone_number = State()
    confirming = State()


class OrderPosition(StatesGroup):
    """
    user_data: [{'name_of_position', 'size_of_position', 'amount' }, ..] -> SQL: add to cart with order_id, timings
    """
    choose_position = State()
    choose_size = State()
    next_position = State()
    confirming = State()
    deleting_position = State()
    confirming_deleting = State()
