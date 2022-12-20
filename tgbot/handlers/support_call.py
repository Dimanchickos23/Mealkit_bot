import emoji
from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp, bot
# from tgbot.keyboards.main import keyboard
from tgbot.keyboards.main import inline_keyboard

from tgbot.keyboards.support import support_keyboard, support_callback, check_support_available, get_support_manager, \
    cancel_support, cancel_support_callback

#@dp.message_handler(Command("support_call"))
async def ask_support_call(cb: CallbackQuery):
    text="Чтобы связаться с техподдержкой, нажмите на кнопку ниже."
    kb = await support_keyboard(messages="many")
    await cb.message.answer(text, reply_markup=kb)


#@dp.callback_query_handler(support_callb ack.filter(messages="many", as_user="yes"))
async def send_to_support_call(call: types.CallbackQuery, state: FSMContext,callback_data: dict):
    await call.message.edit_text("Вы обратились в техподдержку. Ждем ответа от оператора!")

    user_id = int(callback_data.get("user_id"))
    if not await check_support_available(user_id):
        support_id = await get_support_manager()
    else:
        support_id = user_id

    if not support_id:
        await call.message.edit_text("К сожалению, сейчас нет свободных операторов. Попробуйте позже.")
        await state.reset_state()
        return

    await state.set_state("wait_in_support")
    await state.update_data(second_id=support_id)

    kb = await support_keyboard(messages="many", user_id=call.from_user.id)

    await bot.send_message(support_id,
                           f"С вами хочет связаться пользователь {call.from_user.full_name}",
                           reply_markup=kb
                           )

#@dp.callback_query_handler(support_callback.filter(messages="many", as_user="no"))
async def answer_to_support_call(call: types.CallbackQuery, state: FSMContext,callback_data: dict):
    second_id = int(callback_data.get("user_id"))
    user_state = dp.current_state(user=second_id, chat=second_id)

    if str(await user_state.get_state()) != "wait_in_support":
        await call.message.edit_text("К сожалению, пользователь уже передумал.")
        return

    await state.set_state("in_support")
    await user_state.set_state("in_support")

    await state.update_data(second_id=second_id)

    kb = cancel_support(second_id)
    keyboard_second_user = cancel_support(call.from_user.id)

    await call.message.edit_text("Вы на связи с пользователем!\n"
                                 "Чтобы завершить общение нажмите на кнопку.",
                                 reply_markup=kb
                                 )
    await bot.send_message(second_id,
                           "Техподдержка на связи! Можете писать сюда свое сообщение. \n"
                           "Чтобы завершить общение нажмите на кнопку.",
                           reply_markup=keyboard_second_user
                           )


#@dp.message_handler(state="wait_in_support", content_types=types.ContentTypes.ANY)
async def not_supported(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get("second_id")

    kb = cancel_support(second_id)
    await message.answer("Дождитесь ответа оператора или отмените сеанс", reply_markup=kb)


#@dp.callback_query_handler(cancel_support_callback.filter(), state=["in_support", "wait_in_support", None])
async def exit_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    user_id = int(callback_data.get("user_id"))
    second_state = dp.current_state(user=user_id, chat=user_id)

    if await second_state.get_state() is not None:
        data_second = await second_state.get_data()
        second_id = data_second.get("second_id")
        if int(second_id) == call.from_user.id:
            await second_state.reset_state()
            await bot.send_message(user_id, "Пользователь завершил сеанс техподдержки")

    await call.message.edit_text("Вы завершили сеанс")
    await state.reset_state()
    await call.message.answer_sticker(sticker="CAACAgIAAxkBAAEBI8NiqOKtCL6CGHjP6ZddTWavbnjcXwACXw8AAoMo-EsCNiHWZ-EzbSQE")
    await call.message.answer("Я могу чем-то еще помочь?", reply_markup=inline_keyboard)


def register_support(dp: dp):
    dp.register_callback_query_handler(ask_support_call, lambda callback_query: callback_query.data == "support", state="*")
    dp.register_callback_query_handler(send_to_support_call,support_callback.filter(messages="many", as_user="yes"))
    dp.register_callback_query_handler(answer_to_support_call, support_callback.filter(messages="many", as_user="no"))
    dp.register_message_handler(not_supported,state="wait_in_support", content_types=types.ContentTypes.ANY)
    dp.register_callback_query_handler(exit_support,cancel_support_callback.filter(), state=["in_support", "wait_in_support", None])
