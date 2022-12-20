from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

meal_type_cb = CallbackData('meal', 'type', 'calories', 'price_day', 'image_url')

meal_types_kb = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=
                                     [
                                         [
                                             InlineKeyboardButton(
                                                 text="Похудение 🦋",
                                                 callback_data=meal_type_cb.new(
                                                     type="Похудение",
                                                     calories="1500",
                                                     price_day="500",
                                                     image_url="2022/10/П1-1-768x963.png"
                                                 )
                                             )
                                         ],
                                         [
                                             InlineKeyboardButton(
                                                 text="Баланс 🐬",
                                                 callback_data=meal_type_cb.new(
                                                     type="Баланс",
                                                     calories="2000",
                                                     price_day="650",
                                                     image_url="2022/10/Б1-1-768x963.png"
                                                 )
                                             )
                                         ],
                                         [
                                             InlineKeyboardButton(
                                                 text="Набор 🐳",
                                                 callback_data=meal_type_cb.new(
                                                     type="Набор",
                                                     calories="2400",
                                                     price_day="800",
                                                     image_url="2022/10/Н1-1-768x963.png"
                                                 )
                                             )
                                         ]
                                     ])

days_kb = InlineKeyboardMarkup(row_width=2, resize_keyboard=True,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(
                                           text="3",
                                           callback_data="3"
                                       ),
                                       InlineKeyboardButton(
                                           text="6",
                                           callback_data="6"
                                       )
                                   ],
                                   [
                                       InlineKeyboardButton(
                                           text="9",
                                           callback_data="9"
                                       ),
                                       InlineKeyboardButton(
                                           text="12",
                                           callback_data="12"
                                       )
                                   ]
                               ])

menu_by_days_kb = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)

back_to_menu = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Назад в меню",
                                                callback_data="назад"

                                            )]
                                    ]
                                    )
