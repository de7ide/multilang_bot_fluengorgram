import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User, CallbackQuery, Message
from aiogram.fsm.storage.memory import MemoryStorage

from fluentogram import TranslatorHub


logger = logging.getLogger(__name__)

cdata = ['en']


class TranslatorRunnerMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        def upload_clbk(callback):
            cdata.append(callback)

        def return_clbck():
            return "".join(cdata)[-1]


        # state = data['state']
        # data = state.get_data()

        # s = data['raw_state']
        # if s:
        #     print(s.data)

        # s  = data['state']
        # print(event)
        # async with self.storage() as stor:
        #     data['stor'] = stor
        #     print(data)
        #     hub: TranslatorHub = data.get('_translator_hub') # type: ignore
        #     data['i18n'] = hub.get_translator_by_locale(locale=None)
        dd = event.callback_query
        if dd:
            dd = dd.data
            upload_clbk(dd)


        data['cdata'] = return_clbck()
        hub: TranslatorHub = data.get('_translator_hub') # type: ignore
        data['i18n'] = hub.get_translator_by_locale(locale=dd)
        print(data)
        return await handler(event, data)



        # hub: TranslatorHub = data.get('_translator_hub') # type: ignore
        # data['i18n'] = hub.get_translator_by_locale(locale=None)

        # return await handler(event, data)