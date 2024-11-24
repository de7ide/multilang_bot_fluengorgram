import asyncio
import random

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove, User
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from fluentogram import TranslatorRunner
from lexicon.lexicon import LEXICON_EN, LEXICON_RU, LEXICON_HINDI
from kbds.reply import get_kbd
from kbds.inline import get_inline_kbd
from utils.state import ChooseScheme, ChooseScheme2


user_router = Router()


@user_router.message(CommandStart())
async def start_comm(message: Message):
    await message.answer(text="Language 🌏", reply_markup=get_inline_kbd(
        btns={
            "English 🇺🇸": 'en',
            "Русский 🇷🇺": 'ru',
            "हिन्दी 🇮🇳": 'hi',
        }))


@user_router.message(Command('help'))
async def help(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.button.pressed())


###start menu
@user_router.callback_query(F.data)
async def press_en_but(callback: CallbackQuery, i18n: TranslatorRunner, state: FSMContext):
    await callback.message.delete() # type: ignore
    await callback.message.answer_photo(photo=FSInputFile(f'{i18n.photo.send()}'), caption=i18n.photo.caption(), reply_markup=get_kbd(i18n.schemes(), i18n.my.chanal(), i18n.reviews(), size=(2,)))
    await callback.answer()


###
@user_router.message(F.text == '📖 Schemes')
@user_router.message(F.text == '📖 Схемы')
@user_router.message(F.text == '📖 योजनाएँ')
async def cheki18n(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.schemes.pressed(), reply_markup=get_kbd(i18n.ai.analisys(), i18n.cheat.luck(), i18n.tic.tac.toe(), i18n.back.first(), size=(2,1)))


@user_router.message(F.text == 'AI Analysis🤖')
@user_router.message(F.text == 'AI Анализ🤖')
@user_router.message(F.text == 'एआई विश्लेषण🤖')
async def ai_ru(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.ai.analisys.pressed(), reply_markup=get_kbd(i18n.schema(), i18n.ai.analisys2(), i18n.back.sec(), size=(1,)))


@user_router.message(F.text == "📄 Scheme")
@user_router.message(F.text == "📄 Схема")
@user_router.message(F.text == "📄 योजना")
async def scheme_ru(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.schema.pressed())


@user_router.message(StateFilter(None), F.text == '🤖AI Analysis')
@user_router.message(StateFilter(None), F.text == '🤖AI Анализ')
@user_router.message(StateFilter(None), F.text == '🤖एआई विश्लेषण')
async def ai_st_ru(message: Message, state: FSMContext, i18n: TranslatorRunner):
    await message.answer(text=i18n.send.id() ,reply_markup=ReplyKeyboardRemove())
    await state.set_state(ChooseScheme.ai_ru)


@user_router.message(ChooseScheme.ai_ru, F.text)
async def answ_ai_ru(message: Message, state: FSMContext, i18n: TranslatorRunner):
    await state.update_data(ai=message.text)
    await message.answer(text=i18n.successfully(), reply_markup=get_kbd(i18n.schema(), i18n.ai.analisys2(), i18n.back.sec(), size=(1,)))
    await state.set_state(ChooseScheme.ai_scrin_ru)


@user_router.message(ChooseScheme.ai_scrin_ru, F.photo)
async def ai_scrin_ru(message: Message, state: FSMContext, bot: Bot, i18n: TranslatorRunner):
    await message.answer(text=i18n.analysis())
    await message.bot.send_chat_action(chat_id=message.from_user.id, action='typing') # type: ignore
    await asyncio.sleep(2)
    rn = random.randint(00, 99)
    rn2 = random.randint(70, 99)
    await message.answer(text=f"{i18n.pick.up()}{rn}\n📊 {i18n.chance()} {rn2}%")
    await state.clear()


#back button 1
@user_router.message(F.text == '🔙 Back')
@user_router.message(F.text == '🔙 Назад')
@user_router.message(F.text == '🔙 पीछे')
async def back1_ru(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.back.menu.f(), reply_markup=get_kbd(i18n.schemes(), i18n.my.chanal(), i18n.reviews(), size=(2,)))


#back button 2
@user_router.message(F.text == '🔙Back')
@user_router.message(F.text == '🔙Назад')
@user_router.message(F.text == '🔙पीछे')
async def back2_ru(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.back.menu.f(), reply_markup=get_kbd(i18n.ai.analisys(), i18n.cheat.luck(), i18n.tic.tac.toe(), i18n.back.first(), size=(1,)))


@user_router.message(StateFilter(None), F.text == '🎲 Cheat Luck')
@user_router.message(StateFilter(None), F.text == '🎲 Накрутка Удачи')
@user_router.message(StateFilter(None), F.text == '🎲 धोखा किस्मत')
async def nakr_ru(message: Message, state: FSMContext, i18n: TranslatorRunner):
    await message.answer(text=i18n.send.id(), reply_markup=get_kbd(i18n.schema2(), i18n.back.sec(), size=(1,)))
    await state.set_state(ChooseScheme2.ai2_ru)


@user_router.message(ChooseScheme2.ai2_ru, F.text)
async def nakr2_ru(message: Message, state: FSMContext, i18n: TranslatorRunner):
    await message.answer(text=i18n.successfully())
    await state.clear()


@user_router.message(ChooseScheme2.ai2_ru, F.text == '🔙Back')
@user_router.message(ChooseScheme2.ai2_ru, F.text == '🔙Назад')
@user_router.message(ChooseScheme2.ai2_ru, F.text == '🔙पीछे')
async def back_clear(state: FSMContext):
    await state.clear()



#scheme but2
@user_router.message(F.text == '📄Scheme')
@user_router.message(F.text == '📄Схема')
@user_router.message(F.text == '📄योजना')
async def schem_buttru2(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.schema2())


#chanal button
@user_router.message(F.text == '📣 My chanal')
@user_router.message(F.text == '📣 Мой канал')
@user_router.message(F.text == '📣 मेरा चॅनल')
async def chan_ru(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.choose.action(), reply_markup=get_kbd(i18n.my.chanal2(), i18n.back.first()))


#revies butt
@user_router.message(F.text == '💬 Reviews')
@user_router.message(F.text == '💬 Отзывы')
@user_router.message(F.text == '💬 समीक्षा')
async def rev_ru(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.rev())
