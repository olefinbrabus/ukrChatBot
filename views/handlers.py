import datetime

from aiogram import F, Router
from aiogram.types import Message, URLInputFile
from aiogram.filters import Command

import views.inline_keyboards
import views.keyboard
import views.text
from controller.main_controller import MainController
from controller.log_controller import message_format_to_logging
from auth.authorize import login_required

router = Router()
data_category = None


@router.message(Command("start"))
async def start_handler(msg: Message):
    if msg.chat.type == "private":
        message_format_to_logging(msg, f"start {msg.from_user.first_name} private")
        await msg.answer(views.text.greet.format(
            name=msg.from_user.full_name),
            reply_markup=views.keyboard.main
        )
    else:
        message_format_to_logging(msg, f"start {msg.from_user.first_name} chat")
        await msg.answer(views.text.chat_greet.format(
            name=msg.from_user.full_name),
            reply_markup=views.inline_keyboards.chat_main
        )


@router.message(F.text == "Меню")
@router.message(F.text == "меню")
@router.message(F.text == "До меню")
@login_required
async def menu_handler(msg: Message):
    if msg.chat.type == "private":
        message_format_to_logging(msg, "Menu")
        await msg.answer(views.text.menu, reply_markup=views.keyboard.main)

    else:
        await msg.answer(text="космонавти")
        print(msg.chat.type)


@router.message(F.text == "🔎 Допомога")
async def help_handler(msg: Message):
    message_format_to_logging(msg, "Help")
    await msg.answer(views.text.help_bot, reply_markup=views.keyboard.main)


@router.message(F.text == "📝 Пошук правила")
async def categories_handler(msg: Message):
    message_format_to_logging(msg, "Show categories")
    await msg.answer("Виберіть категорію", reply_markup=views.keyboard.categories)


@router.message(F.text == "🗓️ Словосполучення/слово дня")
async def word_of_day_handler(msg: Message):
    controller = MainController()
    index = (datetime.datetime.now().day * 2 // datetime.datetime.now().month)
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
            number += f"\n {data["id"] + 1} - {data["title"]}"
        message_format_to_logging(msg, "Categories")
        await msg.answer(number, reply_markup=views.keyboard.main)

    else:
        text = "Помилка, такої команди не існує, спробуйте іншу."
        message_format_to_logging(msg, "Wrong command")
        await msg.answer(text=text, reply_markup=views.keyboard.main)


async def show_data(msg: Message, data: list, index: int):
    try:
        if index == -1:
            raise IndexError

        data = data[index]
        image = URLInputFile(data["image"])
        text_to_answer = f"{data["title"]}\n\n" \
                         f"{data["category_name"]}\n\n" \
                         f"{data["content"]}\n\n" \
                         f"{data["url"]}"

        message_format_to_logging(msg, data["title"])
        await msg.answer_photo(
            photo=image,
            caption=text_to_answer,
            disable_web_page_preview=True
        )
        if msg.text != "🗓️ Словосполучення/слово дня":
            await msg.answer("Напишить номер якій вас цікавить\n"
                             "або вийдіть до категорії чи меню")
    except IndexError:
        message_format_to_logging(msg, "Wrong index")
        await msg.answer("Помилка. неправильний номер. Спробуйте ще раз.")
