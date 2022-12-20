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


# Создаем группу состояний Metabolism - для перечня вопросов для сбора исходных данных для формулы расчета
class Metabolism(StatesGroup):
    gender = State()  # пол мужской/женский
    age = State()  # возраст, полных лет
    height = State()  # рост, см
    weight = State()  # вес, кг
    activity = State()  # коэффициент уровня активности