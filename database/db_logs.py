from database.db import AbstractDatabase


class DatabaseLogs(AbstractDatabase):
    def __init__(self, db_name: str):
        super().__init__(db_name)

    def insert_one(self, log: dict) -> None:
        self._collection.insert_one(log)
