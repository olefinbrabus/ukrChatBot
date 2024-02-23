from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import views.keyboard
import views.text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(views.text.greet.format(name=msg.from_user.full_name), reply_markup=views.keyboard.menu)


@router.message(F.text == "Меню")
@router.message(F.text == "меню")
@router.message(F.text == "menu")
async def message_handler(msg: Message):
    await msg.answer(views.text.menu, reply_markup=views.keyboard.menu)

