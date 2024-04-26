from database.db import AbstractDatabase


class DatabaseLogs(AbstractDatabase):
    def __init__(self, db_name: str) -> None:
        super().__init__(db_name)

    def insert_one(self, log: dict) -> None:
        self._collection.insert_one(log)
