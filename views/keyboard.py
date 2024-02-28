from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,
                           ReplyKeyboardMarkup, ReplyKeyboardRemove)

from site_manager.manager import TYPE_OF_CATEGORIES

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🗓️ Словосполучення/слово дня")],
    [KeyboardButton(text="📝 Пошук правила")],
    [KeyboardButton(text="🔎 Допомога")],

],
    resize_keyboard=True)

"""Створення категорій частин мови"""
categories = []

from_dict = list(TYPE_OF_CATEGORIES.values())

for category in range(0, len(from_dict), 2):
    list_category = [KeyboardButton(text=from_dict[category]),
                     KeyboardButton(text=from_dict[category + 1])]
    categories.append(list_category)

categories.append([KeyboardButton(text="До меню")])

categories = ReplyKeyboardMarkup(keyboard=categories, resize_keyboard=True)
