from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()


class Order(StatesGroup):
    Meal_type = State()
    Menu = State()
    Choose_days = State()
    Contact = State()
    Geo = State()