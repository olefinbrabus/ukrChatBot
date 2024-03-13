from database.db import AbstractDatabase


class DatabaseManagerExamples(AbstractDatabase):

    def __init__(self, db_name: str) -> None:
        super().__init__(db_name)

    def update_db(self, list_examples: list) -> None:
        if not self._validate_db(list_examples):
            self.drop_collection()
            self.insert(list_examples)

    def _validate_db(self, list_examples: list) -> bool:
        return self.get_collection() == list_examples
