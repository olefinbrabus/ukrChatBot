from aiogram import F, Router
from aiogram.types import Message, URLInputFile
from aiogram.filters import Command

import views.keyboard
import views.text
import datetime

from controller.main_controller import MainController

router = Router()
data_category = None


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(views.text.greet.format(
        name=msg.from_user.full_name),
        reply_markup=views.keyboard.main)


@router.message(F.text == "Меню")
@router.message(F.text == "меню")
@router.message(F.text == "До меню")
async def menu_handler(msg: Message):
    await msg.answer(
        views.text.menu,
        reply_markup=views.keyboard.main)


@router.message(F.text == "🔎 Допомога")
async def help_handler(msg: Message):
    await msg.answer(views.text.help_bot,
                     reply_markup=views.keyboard.main)


@router.message(F.text == "📝 Пошук правила")
async def categories_handler(msg: Message):
    await msg.answer("Виберіть категорію",
                     reply_markup=views.keyboard.categories)


@router.message(F.text == "🗓️ Словосполучення/слово дня")
async def word_of_day_handler(msg: Message):
    controller = MainController()
    index = (datetime.datetime.now().day * 2
             // datetime.datetime.now().month)
    indexed_data = controller.get_examples
    await show_data(msg, indexed_data, index)


@router.message()
async def categories_contains_handler(msg: Message):
    global data_category
    category = msg.text

    if category.isdigit() and data_category is not None:
        i = int(category) - 1  # index -1 because the array starts from zero
        await show_data(msg, data_category, i)

    elif category in MainController().get_categories:
        number = "Напишіть словосполучення по номеру 👇"

        data = {"category_name": category}
        data_category = MainController().get_filter_examples(data)

        for data in data_category:
            number += f"\n {data["id"]+1} - {data["title"]}"
        await msg.answer(number, reply_markup=views.keyboard.main)

    else:
        await msg.answer(
            text="Помилка, такої команди не існує, спробуйте іншу.",
            reply_markup=views.keyboard.main
        )


async def show_data(msg: Message, data: list, index: int):
    try:
        if index == -1:
            raise IndexError

        data = data[index]
        image = URLInputFile(data["image"])

        await msg.answer_photo(
            photo=image,
            caption=f"{data["title"]}\n\n"
                    f"{data["category_name"]}\n\n"
                    f"{data["content"]}\n\n"
                    f"{data["url"]}",
            disable_web_page_preview=True
        )
        if msg.text != "🗓️ Словосполучення/слово дня":
            await msg.answer("Напишить номер якій вас цікавить\n"
                             "або вийдіть до категорії чи меню")
    except IndexError:
        await msg.answer("Помилка. неправильний номер. Спробуйте ще раз.")
