from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

meal_type_cb = CallbackData('meal', 'type', 'calories', 'days', 'price')


meal_types_kb = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=
                                     [
                                         [
                                             InlineKeyboardButton(
                                                 text="Похудение 🦋",
                                                 callback_data=meal_type_cb.new(
                                                     type="Похудение",
                                                     calories="1500",
                                                     days="",
                                                     price=""
                                                 )
                                             )
                                         ],
                                         [
                                             InlineKeyboardButton(
                                                 text="Баланс 🐬",
                                                 callback_data=meal_type_cb.new(
                                                     type="Баланс",
                                                     calories="2000",
                                                     days="",
                                                     price=""
                                                 )
                                             )
                                         ],
                                         [
                                             InlineKeyboardButton(
                                                 text="Набор 🐳",
                                                 callback_data=meal_type_cb.new(
                                                     type="Набор",
                                                     calories="2400",
                                                     days="",
                                                     price=""
                                                 )
                                             )
                                         ]
                                     ])

menu_by_days_kb = InlineKeyboardMarkup(row_width=1)