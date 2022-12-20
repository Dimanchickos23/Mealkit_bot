from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery, ContentType

from tgbot.keyboards.main import inline_keyboard
from tgbot.keyboards.order_kb import days_kb
from tgbot.misc.states import Order


async def payment_start(query: CallbackQuery, state: FSMContext):
    await query.answer()
    data = await state.get_data()
    meal_type = data.get('meal_type')
    calories = data.get('calories')
    price_day = data.get('price_day')
    await query.message.answer(f"На сколько дней вы хотите заказать рацион <b>{meal_type} ({calories} ккал/день)</b>?\n"
                               f"Стоимость за день = <b>{price_day} руб</b>",
                               reply_markup=days_kb)


async def days_answer(query: CallbackQuery, state: FSMContext):
    await query.answer()
    bot = Bot.get_current()
    config = bot.get('config')
    data = await state.get_data()
    meal_type = data.get('meal_type')
    calories = data.get('calories')
    days = query.data
    price_day = data.get('price_day')
    image_url = data.get('image_url')
    PRICE = LabeledPrice(label="Руб", amount=int(price_day)*int(days)*10)
    PAYMENTS_PROVIDER_TOKEN = config.tg_bot.payment_provider_token
    # provider_data = {"shopId":506751,"shopArticleId":538350}
    if PAYMENTS_PROVIDER_TOKEN.split(':')[1] == 'TEST':
        await query.message.answer("Так как сейчас я запущен в тестовом режиме, для оплаты "
                                   "используйте данные тестовой карты: 1111 1111 1111 1026, 12/22, CVC 000")
    await bot.send_invoice(
        query.message.chat.id,
        title=f"Рацион {meal_type}",
        description=f"{calories} ккал/день.\n"
                    f"Количество дней: {query.data}",
        provider_token=PAYMENTS_PROVIDER_TOKEN,
        # send_email_to_provider=True,
        # provider_data={"receipt":{
        #     "items":[
        #         {
        #             "description": f"{calories} ккал/день.\n"
        #             f"Количество дней: {query.data}",
        #             "quantity": "1.00",
        #             "amount": {
        #                 "value": f"{int(price_day)*int(days)}",
        #                 "currency": "RUB"
        #             },
        #             "payment_method_data": {
        #                 "type": "bank_card"
        #             },
        #             "vat_code": 1
        #         }
        #     ]
        # }
        # },
        currency="RUB",
        photo_url="https://chef.tm/public/pics/689/689884_0.jpg",
        # photo_url="https://cc42190.tmweb.ru/wp-content/uploads/" + image_url,
        photo_height=1024,  # !=0/None, иначе изображение не покажется
        photo_width=1024,
        photo_size=1024,
        is_flexible=False,  # True если конечная цена зависит от способа доставки
        prices=[PRICE],
        start_parameter="test",
        payload='some-invoice-payload-for-our-internal-use'
    )


async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    bot = Bot.get_current()
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def process_pay(message: types.Message, state: FSMContext):
    bot = Bot.get_current()
    await state.finish()
    if message.successful_payment.invoice_payload == 'some-invoice-payload-for-our-internal-use':
        await bot.send_message(message.from_user.id, "Спасибо за покупку!\n"
                                                     "Заказ оформлен.", reply_markup=inline_keyboard)


def register_payment(dp: Dispatcher):
    dp.register_callback_query_handler(payment_start, lambda callback_query: callback_query.data == "payment_start",
                                       state=Order.Menu)
    dp.register_callback_query_handler(days_answer, state=Order.Menu)
    dp.register_pre_checkout_query_handler(process_pre_checkout_query, state=Order.Menu)
    dp.register_message_handler(process_pay, content_types=ContentType.SUCCESSFUL_PAYMENT, state=Order.Menu)