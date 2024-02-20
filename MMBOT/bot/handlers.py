from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram import F, Router

router = Router()


@router.message(Command(commands="start"))
async def start_message(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="Хочу узнать больше о направлениях",
            callback_data="study_courses"),
        InlineKeyboardButton(
            text="Хочу задать вопрос",
            callback_data="enrolle_question"),
        InlineKeyboardButton(
            text="Хочу посмотреть учебный план",
            callback_data="study_catalog"),
        InlineKeyboardButton(
            text="Хочу крутануть каз",
            callback_data="want_casino"),
        width=1
    )
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!", reply_markup=builder.as_markup())


@router.callback_query(F.data == "study_courses")
async def study_courses(callback: CallbackQuery):
    await callback.message.answer('Запрос обрабатывается')


@router.callback_query(F.data == "want_casino")
async def want_casino(callback: CallbackQuery):
    await callback.message.answer_dice(emoji=DiceEmoji.SLOT_MACHINE)
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=" ДААААА",
            callback_data="want_casino"),
        InlineKeyboardButton(
            text="нет(",
            callback_data="no"))
    await callback.message.answer("Повторить?", reply_markup=builder.as_markup())


@router.callback_query(F.data == "no")
async def no(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=" ДААААА",
            callback_data="want_casino"),
        InlineKeyboardButton(
            text="нет(",
            callback_data="no"))
    await callback.message.answer("крути дальше", reply_markup=builder.as_markup())

