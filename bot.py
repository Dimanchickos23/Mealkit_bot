import asyncio
import logging
from loader import dp, bot

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.echo import register_echo
from tgbot.handlers.order import register_order
from tgbot.handlers.user import register_user
from tgbot.handlers.feedback import register_feedback
from tgbot.handlers.about_us import register_about_us
from tgbot.handlers.support_call import register_support
from tgbot.middlewares.db import DbMiddleware
from tgbot.middlewares.support_middleware import SupportMiddleware

logger = logging.getLogger(__name__)

#!важен порядок, именно Middlewares, filters, handlers

def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())
    dp.setup_middleware(SupportMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_order(dp)
    register_feedback(dp)
    register_about_us(dp)
    register_support(dp)

    # register_echo(dp)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        session = await bot.get_session()
        await session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
