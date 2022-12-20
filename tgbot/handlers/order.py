import logging

from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
from aiogram.utils.markdown import hide_link

from tgbot.keyboards.order_kb import meal_types_kb, menu_by_days_kb, meal_type_cb, back_to_menu
from tgbot.misc.meal_day_data import results_dict
from tgbot.misc.states import Order


async def order_start(cb: CallbackQuery, state: FSMContext):
    await Order.Meal_type.set()
    await cb.message.answer_sticker(sticker="CAACAgIAAxkBAAEBcPBjaZsnaYo0ScyRSN4g4QlhhYefNQACERMAAu40sEmMXcn13VOhOysE")
    await cb.message.answer("Выберите тип рациона:", reply_markup=meal_types_kb)


async def display_menu(cb: CallbackQuery, state: FSMContext, callback_data: dict):
    await state.update_data(meal_type=callback_data['type'], calories=callback_data['calories'],
                            price_day=callback_data['price_day'],
                            image_url=callback_data['image_url'])
    await Order.Menu.set()
    for i in range(1, 4):
        menu_by_days_kb.insert(
            InlineKeyboardButton(
                text=f"День {i}",
                switch_inline_query_current_chat=callback_data['type'] + f" день {i}"
            )
        )
    menu_by_days_kb.insert(
        InlineKeyboardButton(
            text="Хочу это меню 😋",
            callback_data="payment_start"
        )
    )

    await cb.message.edit_text(f"Вы выбрали рацион <b>{callback_data['type']}</b>"
                               f" на <b>{callback_data['calories']} ккал/день.</b>\n"
                               f"С помощью клавиш ниже можно ознакомиться с меню на ближайшие дни.",
                               reply_markup=menu_by_days_kb)
    # menu_by_days_kb.inline_keyboard.clear()


async def days_menu(query: InlineQuery):
    c = query.query #'Похудение день 1'
    await query.answer(
        results=results_dict[c],
        is_personal=True
    )


async def back(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    meal_type = data.get("meal_type")
    bot = Bot.get_current()
    await bot.send_sticker(chat_id=cb.from_user.id,sticker="CAACAgIAAxkBAAEBcOxjaZpHK9uS3paY3cP95teF4yVXygACLxEAAqqKMUk-rp0rmZs2YCsE")
    menu_by_days_kb.insert(InlineKeyboardButton(text="К выбору рациона",callback_data="back"))
    await bot.send_message(chat_id=cb.from_user.id,text=f"Вы вернулись к меню рациона {meal_type}.", reply_markup=menu_by_days_kb)
    menu_by_days_kb.inline_keyboard.pop()


async def back_2(cb: CallbackQuery, state: FSMContext):
    menu_by_days_kb.inline_keyboard.clear()
    await Order.Meal_type.set()
    await cb.message.edit_text("Выберите тип рациона:", reply_markup=meal_types_kb)
# async def
# f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-1-768x963.png')}"
#                                  f"Состав:\n"
#                                  f"Бла Бла\n"
#                                  f"Бла"


def register_order(dp: Dispatcher):
    dp.register_callback_query_handler(order_start, lambda callback_query: callback_query.data == "order", state="*")
    dp.register_callback_query_handler(display_menu, meal_type_cb.filter(), state=Order.Meal_type)
    dp.register_inline_handler(days_menu, state=Order.Menu)
    dp.register_callback_query_handler(back, lambda callback_query: callback_query.data == "назад", state=Order.Menu)
    dp.register_callback_query_handler(back_2, lambda callback_query: callback_query.data == "back", state=Order.Menu)
