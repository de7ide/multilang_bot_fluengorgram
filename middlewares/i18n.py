import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User, CallbackQuery, Message
from aiogram.fsm.storage.memory import MemoryStorage

from fluentogram import TranslatorHub


logger = logging.getLogger(__name__)

cdata: list[str] = ['en',]


class TranslatorRunnerMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:


        def upload_clbk(callback):
            cdata.append(callback)


        dd = event.callback_query
        if dd:
            dd = dd.data
            upload_clbk(dd)


        data['cdata'] = cdata[-1]
        hub: TranslatorHub = data.get('_translator_hub') # type: ignore
        data['i18n'] = hub.get_translator_by_locale(locale=data['cdata'])
        print(data)
        return await handler(event, data)