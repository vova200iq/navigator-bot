from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()


class ChoseType(StatesGroup):
    Start = State()
    At = State()
    Cafe = State()
    Fact = State()
    Hotel = State()