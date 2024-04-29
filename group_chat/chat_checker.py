from typing import Union

from aiogram.types import Message


def only_private(func: callable):
    async def wrapper(msg: Message) -> Union[callable, None]:
        if msg.chat.type == "private":
            return await func(msg)
    return wrapper


def only_groups(func: callable):
    async def wrapper(msg: Message) -> Union[callable, None]:
        if msg.chat.type != "private":
            return await func(msg)
    return wrapper
