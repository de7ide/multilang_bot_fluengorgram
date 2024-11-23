import asyncio
import random

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext

from lexicon.lexicon import LEXICON_EN, LEXICON_RU, LEXICON_HINDI
from kbds.reply import get_kbd
from kbds.inline import get_inline_kbd
from utils.state import ChooseScheme, ChooseScheme2


# ru_handler_router = Router()

# ###start ru menu
# @ru_handler_router.callback_query(F.data == 'ru_butt')
# async def press_ru_but(callback: CallbackQuery):
#     await callback.message.delete() # type: ignore
#     await callback.message.answer_photo(photo=photoRu, caption=LEXICON_RU['caption'], reply_markup=get_kbd("📖 Схемы", "📣 Мой канал", "💬 Отзывы", size=(2,))) # type: ignore
#     await callback.answer()
    #await callback.message.answer_photo(photo=photoEn, caption=LEXICON_EN['caption'], reply_markup=get_kbd("📖 Schemes", "📣 My chanal", "💬 Reviews", size=(2,1))) # type: ignore



# @user_router.callback_query(F.data == 'ru')
# async def press_ru_but(callback: CallbackQuery):
#     langu = 'ru'
#     await callback.message.delete() # type: ignore
#     await callback.message.answer_photo(photo=photoRu, caption=LEXICON_RU['caption'], reply_markup=get_kbd("📖 Схемы", "📣 Мой канал", "💬 Отзывы", size=(2,))) # type: ignore
#     await callback.answer()

# ###start hi menu
# @user_router.callback_query(F.data == 'hi')
# async def press_hi_but(callback: CallbackQuery):
#     await callback.message.delete() # type: ignore
#     await callback.message.answer_photo(photo=photoHI, caption=LEXICON_HINDI['caption'], reply_markup=get_kbd("📖 योजनाओं", "📣 मेरा चैनल", "💬 समीक्षा ", size=(2,1))) # type: ignore
#     langu = 'hi'
#     await callback.answer()