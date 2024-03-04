import pymongo

from config import MONGO_CLIENT, MONGO_DATABASE


class AbstractDatabase:
    def __init__(self, collection: str) -> None:
        self.client = pymongo.MongoClient(MONGO_CLIENT)
        self.database = self.client[MONGO_DATABASE]
        self.collection = self.database[collection]

    def insert(self, lst: list) -> None:
        if _insert_validation_form(lst):
            self.collection.insert_many(lst)
        else:
            raise ValueError("in list, value may be  dict.")

    def _drop_collection(self) -> None:
        self.collection.drop()

    def get_collection(self, find_filter: dict = None):
        if find_filter is None:
            lst = [ex for ex in self.collection.find()]
            return lst

        data = enumerate(self.collection.find(
            find_filter, {"_id": 0}))
        return [{"id": i, **ex} for i, ex in data]

    def database_exist(self) -> None:
        dblist = self.client.list_collection_names()
        if self.database not in dblist:
            raise ReferenceError("database not found")


def _insert_validation_form(lst: list) -> bool:
    for example in lst:
        print(example)
        if not isinstance(example, dict):
            return False
    return True
