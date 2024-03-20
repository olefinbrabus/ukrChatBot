import pymongo

from pymongo.errors import PyMongoError

from config import MONGO_CLIENT, MONGO_DATABASE


class AbstractDatabase:
    def __init__(self, collection: str) -> None:

        try:
            self._client = pymongo.MongoClient(MONGO_CLIENT)
            self._database = self._client[MONGO_DATABASE]
            self._collection = self._database[collection]
        except pymongo.errors.ServerSelectionTimeoutError as e:
            print(e)
            raise

    def insert(self, lst: list) -> None:
        if _insert_validation_form(lst):
            self._collection.insert_many(lst)
        else:
            raise ValueError("in list, value may be  dict.")

    def drop_collection(self) -> None:
        self._collection.drop()

    def get_collection(self, find_filter: dict = None):
        if find_filter is None:
            return [rules for rules in self._collection.find()]

        data = enumerate(self._collection.find(find_filter, {"_id": 0}))
        return [{"id": i, **collection} for i, collection in data]


def _insert_validation_form(collection: list) -> bool:
    for example in collection:
        if not isinstance(example, dict):
            return False
    return True
