from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

# kb = [
#         [
#             types.KeyboardButton(text="🌍 Мы в Соцсетях"),
#             types.KeyboardButton(text="📝 Оставить отзыв")
#         ],
#         [
#             types.KeyboardButton(text="🏁 Сделать заказ"),
#             types.KeyboardButton(text="🦸‍ Связь с оператором")
#         ]
#     ]
#
# keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         one_time_keyboard=True,
#         input_field_placeholder="Нажмите")

mes_kb_data = CallbackData('storage', 'action', 'stick_mes_id', 'mes_id')

inline_keyboard = InlineKeyboardMarkup(row_width=2,
                          inline_keyboard= [
                              [
                                InlineKeyboardButton(
                                            text="🏁 Сделать заказ",
                                            callback_data="order"
                                            )
                              ],
                              [
                              InlineKeyboardButton(
                                            text="🌍 Мы в Соцсетях",
                                            callback_data="social"
                                            ),
                              InlineKeyboardButton(
                                            text="📝 Оставить отзыв",
                                            callback_data="feedback"
                                                  )
                                            ],
                                            [
                                              InlineKeyboardButton(
                                                            text="🦸‍ Поддержка",
                                                            callback_data="support"
                                                            ),
                                              InlineKeyboardButton(
                                                            text="🆘 Что выбрать?",
                                                            callback_data="metabolism"
                                                                  )
                                                            ]
                                            ]

                          )
