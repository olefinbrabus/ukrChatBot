from aiogram.types import Message
from config import AUTH_INCLUDED
from typing import Union


def login_required(func) -> callable:
    async def wrapper(msg: Message) -> Union[callable, None]:
        if AUTH_INCLUDED:

            return await msg.answer("dd")
        return await func(msg)
    return wrapper

