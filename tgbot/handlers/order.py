from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
from aiogram.utils.markdown import hide_link

from tgbot.keyboards.order_kb import meal_types_kb, menu_by_days_kb, meal_type_cb
from tgbot.misc.states import Order


async def order_start(message: Message, state: FSMContext):
    await Order.Meal_type.set()
    await message.answer("Выберите тип рациона:", reply_markup=meal_types_kb)


async def display_menu(cb: CallbackQuery, state: FSMContext, callback_data: dict):
    await state.update_data(meal_type=callback_data['type'])
    await Order.Menu.set()
    for i in range(1, 4):
        menu_by_days_kb.insert(
            InlineKeyboardButton(
                text=f"День {i}",
                switch_inline_query_current_chat=callback_data['type'] + f" день {i}"
            )
        )
    await cb.message.edit_text(f"Вы выбрали рацион <b>{callback_data['type']}</b>"
                               f" на <b>{callback_data['calories']} ккал/день.</b>\n"
                               f"С помощью клавиш ниже можно ознакомиться с меню на ближайшие дни.",
                               reply_markup=menu_by_days_kb)


async def days_menu(query: InlineQuery):
    await query.answer(
        results=[
            InlineQueryResultArticle(
                id="1",
                title="Белковый омлет с салатом",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-1-768x963.png')}"
                                 f"*Состав*:\n"
                                 f"Бла *Бла*\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                url="https://core.telegram.org/bots/api#inline-mode",
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-1-768x963.png",
                description="БЖУ"
            )
        ]
    )


def register_order(dp: Dispatcher):
    dp.register_message_handler(order_start, lambda message: message.text == "🏁 Сделать заказ", state="*")
    dp.register_callback_query_handler(display_menu, meal_type_cb.filter(), state=Order.Meal_type)
    dp.register_inline_handler(days_menu, text="")
