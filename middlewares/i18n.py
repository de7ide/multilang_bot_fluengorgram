import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.fsm.storage.memory import MemoryStorage

from fluentogram import TranslatorHub


logger = logging.getLogger(__name__)

# список, в который будет записываться callback_data
# по умолчанию 'en'
language: list[str] = ['en',]


class TranslatorRunnerMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        # извлекает из update callback
        event_callback = event.callback_query
        if event_callback:
            # если в update поступил callback запрос, то он вернет что находится в data и запишет в список language
            event_callback = event_callback.data
            language.append(event_callback)

        data['callback_data'] = language[-1]
        hub: TranslatorHub = data.get('_translator_hub')
        data['i18n'] = hub.get_translator_by_locale(
            locale=data['callback_data'])
        return await handler(event, data)
