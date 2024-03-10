import pymongo

from config import MONGO_CLIENT, MONGO_DATABASE


class AbstractDatabase:
    def __init__(self, collection: str) -> None:
        from pymongo.errors import PyMongoError
        try:
            self._client = pymongo.MongoClient(MONGO_CLIENT, serverSelectionTimeoutMS=2000)
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
            lst = [ex for ex in self._collection.find()]
            return lst

        data = enumerate(self._collection.find(
            find_filter, {"_id": 0}))
        return [{"id": i, **ex} for i, ex in data]


def _insert_validation_form(lst: list) -> bool:
    for example in lst:
        if not isinstance(example, dict):
            return False
    return True
