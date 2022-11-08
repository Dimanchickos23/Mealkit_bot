from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from aiogram.utils.markdown import hide_link

from tgbot.keyboards.order_kb import back_to_menu

results_dict = {
    'Похудение день 1':
        [
            InlineQueryResultArticle(
                id="1.1.1",
                title="Белковый омлет с салатом",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-1-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-1-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="1.1.2",
                title="Чечевица с рваной говядиной",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-2-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-2-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="1.1.3",
                title="Салат из томатов с творогом",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-3-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-3-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="1.1.4",
                title="Печеные кабачки с филе цыпленка",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-4-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П1-4-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            )
        ],
    'Похудение день 2':
        [
            InlineQueryResultArticle(
                id="1.2.1",
                title="Творожная запеканка с облепихой",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П2-1-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П2-1-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="1.2.2",
                title="Печеная куриная голень с белой фасолью",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П2-2-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П2-2-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="1.2.3",
                title="Салат с огурцами, грейпфрутом и тофу",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П2-3-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П2-3-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="1.2.4",
                title="Печеная индейка с вешенками",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П2-4-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П2-4-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            )

        ],
    'Похудение день 3':
        [
            InlineQueryResultArticle(
                id="1.3.1",
                title="Гранола с йогуртом, тыквенными семечками и яблоком",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П3-1-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П3-1-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="1.3.2",
                title="Печеная куриная голень с белой фасолью",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П3-2-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П3-2-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="1.3.3",
                title="Салат с огурцами, грейпфрутом и тофу",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П3-3-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П3-3-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="1.3.4",
                title="Печеная индейка с вешенками",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П3-4-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/П3-4-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            )

        ],
    'Баланс день 1':
        [
            InlineQueryResultArticle(
                id="2.1.1",
                title="Творог с абрикосом и брусникой",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б1-1-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б1-1-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="2.1.2",
                title="Полба с мясным соусом",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б1-2-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б1-2-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="2.1.3",
                title="Зеленый салат с сыром и свеклой",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б1-3-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б1-3-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="2.1.4",
                title="Плов с куриным филе",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б1-4-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б1-4-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            )

        ],
    'Баланс день 2':
        [
            InlineQueryResultArticle(
                id="2.2.1",
                title="Запеканка из кабачков со шпинатом",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б2-1-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б2-1-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="2.2.2",
                title="Говядина с черной смородиной и картофелем",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б2-2-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б2-2-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="2.2.3",
                title="Овощной салат с нутом",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б2-3-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б2-3-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="2.2.4",
                title="Яичная лапша с отварной грудкой",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б2-4-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б2-4-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            )

        ],
    'Баланс день 3':
        [
            InlineQueryResultArticle(
                id="2.3.1",
                title="Рисовая каша с яблоком и сливой",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б3-1-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б3-1-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="2.3.2",
                title="Куриное рагу с гречей и вешенками",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б3-2-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б3-2-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="2.3.3",
                title="Боул с диким рисом и тунцом",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б3-3-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б3-3-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="2.3.4",
                title="Лазанья с курицей и кабачками",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б3-4-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Б3-4-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            )

        ],
'Набор день 1':
        [
            InlineQueryResultArticle(
                id="3.1.1",
                title="Фруктовый салат",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н1-1-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н1-1-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="3.1.2",
                title="Пастуший пирог с курицей",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н1-2-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н1-2-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="3.1.3",
                title="Фасоль в томатном соусе с курицей",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н1-3-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н1-3-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="3.1.4",
                title="Пенне со свининой и сливой",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н1-4-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н1-4-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            )

        ],
'Набор день 2':
        [
            InlineQueryResultArticle(
                id="3.2.1",
                title="Пшеная каша с тыквой",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н2-1-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н2-1-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="3.2.2",
                title="Жаркое из говядины с перловкой",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н2-2-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н2-2-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="3.2.3",
                title="Рис с овощами и минтаем на пару",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н2-3-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н2-3-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="3.2.4",
                title="Пенне с индейкой и шпинатом",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н2-4-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н2-4-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            )

        ],
'Набор день 3':
        [
            InlineQueryResultArticle(
                id="3.3.1",
                title="Белкоблако с лечо и булгуром",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н3-1-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н3-1-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="3.3.2",
                title="Гороховая каша с индейкой на пару",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н3-2-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н3-2-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="3.3.3",
                title="Паровой кекс из кабачка",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н3-3-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н3-3-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            ),
            InlineQueryResultArticle(
                id="3.3.4",
                title="Гречка с говядиной и подливой",
                input_message_content=InputTextMessageContent(
                    message_text=f"{hide_link('http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н3-4-768x963.png')}"
                                 f"Состав:\n"
                                 f"Бла Бла\n"
                                 f"Бла",
                    parse_mode="HTML"
                ),
                thumb_url="http://cc42190.tmweb.ru/wp-content/uploads/2022/10/Н3-4-768x963.png",
                description="БЖУ",
                reply_markup=back_to_menu
            )

        ]
}
