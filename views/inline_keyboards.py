from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import SITE_URL


ib1 = InlineKeyboardButton(text="Джерело", url=SITE_URL)
ib2 = InlineKeyboardButton(text="Меню бота", url="github.com")
lst = [ib1, ib2]

chat_main = InlineKeyboardMarkup(row_width=2, inline_keyboard=[lst])
