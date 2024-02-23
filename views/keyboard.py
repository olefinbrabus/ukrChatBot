from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,
                           ReplyKeyboardMarkup, ReplyKeyboardRemove)

menu = [
    [InlineKeyboardButton(text="🗓️ слово дня", callback_data="word_of_day"),
     InlineKeyboardButton(text="📝 Пошук правила", callback_data="rule_seek")],
    [InlineKeyboardButton(text="🗂️ Перерахування усіх правил", callback_data="all_rules")],
    [InlineKeyboardButton(text="🔎 Допомога", callback_data="help")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

