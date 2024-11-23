import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from fluentogram import TranslatorHub


logger = logging.getLogger(__name__)


class CallbackMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        hub: TranslatorHub = data.get('_translator_hub') # type: ignore
        data['i18n'] = hub.get_translator_by_locale(locale=event.data)
        return await handler(event, data)