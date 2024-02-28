from aiogram import F, Router
from aiogram.types import Message, URLInputFile
from aiogram.filters import Command

import views.keyboard
import views.text
import datetime

from site_manager.manager import SiteManager, TYPE_OF_CATEGORIES

router = Router()
data_category = None


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(views.text.greet.format(name=msg.from_user.full_name), reply_markup=views.keyboard.main)


@router.message(F.text == "Меню")
@router.message(F.text == "меню")
@router.message(F.text == "menu")
@router.message(F.text == "До меню")
async def menu_handler(msg: Message):
    await msg.answer(views.text.menu, reply_markup=views.keyboard.main)


@router.message(F.text == "🗓️ Словосполучення/слово дня")
async def word_of_day_handler(msg: Message):
    manager = SiteManager()
    index = datetime.datetime.now().day * 2 // datetime.datetime.now().month
    indexed_data = manager.proceed_data
    await show_data(msg, indexed_data, index)


async def show_data(msg: Message, data: list, index: int):
    try:
        if index == -1:
            raise IndexError

        data = data[index]
        image = URLInputFile(data["image"])

        await msg.answer_photo(
            photo=image,
            caption=f"{data["title"]}\n\n"
                    f"{data["category"]}\n\n"
                    f"{data["content"]}\n\n"
                    f"{data["url"]}",
            disable_web_page_preview=True
        )
        if msg.text != "🗓️ Словосполучення/слово дня":
            await msg.answer("Напишить номер якій вас цікавить\n"
                             "або вийдіть до категорії чи меню")
    except IndexError:
        await msg.answer("Помилка. неправильний номер. Спробуйте ще раз.")


@router.message(F.text == "🔎 Допомога")
async def help_handler(msg: Message):
    await msg.answer(views.text.help_bot, reply_markup=views.keyboard.main)


@router.message(F.text == "📝 Пошук правила")
async def categories_handler(msg: Message):
    await msg.answer("Виберіть категорію", reply_markup=views.keyboard.categories)


@router.message()
async def categories_contains_handler(msg: Message):
    global data_category
    category = msg.text

    if category.isdigit() and data_category is not None:
        """в індекс - 1 написаний через вдобство кліента,
         щоб не починати індекс з нуля"""
        i = int(category) - 1
        await show_data(msg, data_category, i)

    elif category in TYPE_OF_CATEGORIES.values():
        number = "Напишіть словосполучення по номеру 👇"
        manager = SiteManager()
        data_category = manager.get_category(category)
        for data in data_category:
            number += f"\n {data["id_in_category"]} - {data["title"]}"
        await msg.answer(number, reply_markup=views.keyboard.main)

    else:
        await msg.answer(
            text="Помилка, такої команди не існує, спробуйте іншу.",
            reply_markup=views.keyboard.main
        )
