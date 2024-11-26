import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from fluentogram import TranslatorHub

from config_data.config import Config, load_config
from handlers.user import user_router
from middlewares.i18n import TranslatorRunnerMiddleware
from utils.i18n import create_translator_hub


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
    '%(lineno)d - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def main():
    config: Config = load_config()

    bot = Bot(
        token=config.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=MemoryStorage())

    translator_hub: TranslatorHub = create_translator_hub()

    dp.include_router(user_router)

    dp.update.middleware(TranslatorRunnerMiddleware())

    await dp.start_polling(bot, _translator_hub=translator_hub)

asyncio.run(main())
