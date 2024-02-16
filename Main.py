from dotenv import dotenv_values
from aiogram import *


async def main():
    bot = Bot(token=dotenv_values()["KEY"])
