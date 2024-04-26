from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from controller.main_controller import MainController

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🗓️ Словосполучення/слово дня")],
    [KeyboardButton(text="📝 Пошук правила")],
    [KeyboardButton(text="🔎 Допомога")],

],
    resize_keyboard=True)

"""Створення категорій частин мови"""
categories = []

from_dict = MainController().get_categories

for category in range(0, len(from_dict), 2):
    list_category = [
        KeyboardButton(text=from_dict[category]), KeyboardButton(text=from_dict[category + 1])
    ]
    categories.append(list_category)

categories.append([KeyboardButton(text="До меню")])

categories = ReplyKeyboardMarkup(keyboard=categories, resize_keyboard=True)
