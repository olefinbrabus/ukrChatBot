from aiogram.types import Message

from datetime import datetime

from dataclasses import dataclass, asdict

from database.db_logs import DBLogs


@dataclass
class Logging:
    full_name: str
    username: str
    username_id: int
    username_message: str
    bot_answer: str
    time: str


def message_format_to_logging(msg: Message, answer: str = "") -> None:
    _database = DBLogs("logs")

    log = Logging(
        full_name=msg.from_user.full_name,
        username=msg.from_user.username,
        username_id=msg.from_user.id,
        username_message=msg.text,
        bot_answer=answer,
        time=datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
    )
    _database.insert_one(asdict(log))




