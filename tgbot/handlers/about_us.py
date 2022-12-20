from aiogram import Dispatcher, types, Bot
from aiogram.types import Message, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, \
    CallbackQuery

from tgbot.keyboards.main import mes_kb_data, inline_keyboard


async def cmd_inline_url(cb: CallbackQuery):
    await cb.message.answer_sticker(sticker="CAACAgIAAxkBAAEBI29ip3ZIuMMHyiB0gWp-CV-A7qo4GwAC9AwAArUtoUijwMN9owLvYiQE")
    choice = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=
                                  [
                                      [
                                          InlineKeyboardButton(
                                              text="🌐 Vk",
                                              url="https://vk.com/mealk1t"
                                          ),
                                          InlineKeyboardButton(
                                              text="📸 Instagram",
                                              url="https://instagram.com/mealkit.rnd?igshid=YmMyMTA2M2Y="
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(text="🔵 В главное меню",
                                                               callback_data='В главное меню')
                                      ]
                                  ]
                                  )
    await cb.message.answer("Подписывайтесь на нас!",reply_markup=choice)

async def main_menu(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Вы вернулись в главное меню.",reply_markup=inline_keyboard)

def register_about_us(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_inline_url, lambda callback_query: callback_query.data == "social")
    dp.register_message_handler(cmd_inline_url, lambda message: message.text == "🌍 Мы в Соцсетях", state="*")
    dp.register_callback_query_handler(main_menu, lambda callback_query: callback_query.data == "В главное меню")
