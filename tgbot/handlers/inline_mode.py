from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

allowed_users = []

async def inline_handler(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите какой-то запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не обязательно жать при этом на кнопку"
                )
            )
        ],
        cache_time=5
    )

async def some_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in allowed_users:
        await query.answer(
            results=[],
            switch_pm_text="Бот недоступен. Подключить бота",
            switch_pm_parameter="connect_user",
            cache_time=5
        )
        return
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Название, которое отображается в инлайн режиме!",
                input_message_content=types.InputTextMessageContent(
                    message_text="Тут какой-то <b>текст</b>, который будет отправлен при нажатии на кнопку"
                ),
                url="https://core.telegram.org/bots/api#inline-mode",
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-1-768x963.png",
                description="Описание, в инлайн режиме"
            ),
            types.InlineQueryResultVideo(
                id="4",
                video_url="https://youtu.be/g6xvW2FOuPw",
                caption="Подпись к видео",
                title="Какое-то видео",
                description="Какое то описание",
                thumb_url="https://i.ytimg.com/vi/g6xvW2FOuPw/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCUZf6pJf0_U1JGMm-5f_kT-sGDdA",
                mime_type="video/mp4"
                # input_message_content=types.InputTextMessageContent(
                #     message_text="https://youtu.be/g6xvW2FOuPw",
                #     entities=[types.MessageEntity(type="pre",
                #                                   offset=1,
                #                                   length=1,
                #                                   url="https://youtu.be/g6xvW2FOuPw")],
                #     disable_web_page_preview=False
                # )
            )
            # types.InlineQueryResultCachedPhoto(
            #     id="2",
            #     photo_file_id="AgACAgIAAxkBAAEBcDFjZ_5NFvkOUHhYoyP5d0-qbedSOAAC38MxG4ikQUv52Oy6DBKyuQEAAwIAA3gAAysE",
            #     title="Токамак",
            #     description="T-10",
            #     caption="T-10"
            # )
        ]
    )


async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer("Вы подключены",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="Войти в инлайн",
                                                      switch_inline_query_current_chat="Запрос")
                                 ]
                             ]
                         )
                         )



def register_inline_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_handler, text="")
    dp.register_inline_handler(some_query)
    dp.register_message_handler(connect_user, CommandStart(deep_link="connect_user"))