import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command, state, Text
from aiogram.types import Message, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import text, bold, italic, code, pre

from tgbot.keyboards.main import mes_kb_data, inline_keyboard


async def user_start(message: Message):
    sticker_mes = await message.answer_sticker(
        sticker="CAACAgIAAxkBAAEBIDBioPXUu5rKDuhnPS3T_K7v5AJaGwAC3Q4AAk1d8Eso_al4IJZSniQE")
    await asyncio.sleep(1)
    kb_mes = await message.answer("Привет, " + message.from_user.first_name +
                                  "! Это бот техподдержки доставки рационов питания" + text(
        bold(' Mealkit') + "\nМеня зовут "
                           "Кит. Чем могу "
                           "помочь?"),
                                  parse_mode=ParseMode.MARKDOWN)
    # inline_keyboard = InlineKeyboardMarkup(row_width=2,
    #                                        inline_keyboard=[
    #                                            [
    #                                                InlineKeyboardButton(
    #                                                    text="🏁 Сделать заказ",
    #                                                    callback_data=mes_kb_data.new(action="order",
    #                                                                                  stick_mes_id=sticker_mes.message_id,
    #                                                                                  mes_id=kb_mes.message_id)
    #                                                )
    #                                            ],
    #                                            [
    #                                                InlineKeyboardButton(
    #                                                    text="🌍 Мы в Соцсетях",
    #                                                    callback_data=mes_kb_data.new(action="social",
    #                                                                                  stick_mes_id=sticker_mes.message_id,
    #                                                                                  mes_id=kb_mes.message_id)
    #                                                ),
    #                                                InlineKeyboardButton(
    #                                                    text="📝 Оставить отзыв",
    #                                                    callback_data=mes_kb_data.new(action="feedback",
    #                                                                                  stick_mes_id=sticker_mes.message_id,
    #                                                                                  mes_id=kb_mes.message_id)
    #                                                )
    #                                            ],
    #                                            [
    #                                                InlineKeyboardButton(
    #                                                    text="🦸‍ Поддержка",
    #                                                    callback_data=mes_kb_data.new(action="support",
    #                                                                                  stick_mes_id=sticker_mes.message_id,
    #                                                                                  mes_id=kb_mes.message_id)
    #                                                ),
    #                                                InlineKeyboardButton(
    #                                                    text="🆘 Что выбрать?",
    #                                                    callback_data=mes_kb_data.new(action="metabolism",
    #                                                                                  stick_mes_id=sticker_mes.message_id,
    #                                                                                  mes_id=kb_mes.message_id)
    #                                                )
    #                                            ]
    #                                        ]
    #
    #                                        )
    await kb_mes.edit_reply_markup(inline_keyboard)
    # await message.answer("Меня зовут Кит. Чем могу помочь?", reply_markup=inline_keyboard)


# async def user_start(message: Message):
# await message.reply("Hello, user!")

async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/feedback', '/photo', '/group', '/note', '/file, /testpre', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(process_help_command, commands=["help"], state="*")
