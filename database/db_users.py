from database.db import AbstractDatabase


class DatabaseUsers(AbstractDatabase):

    def __init__(self, db_name: str) -> None:
        super().__init__(db_name)