from database.db_manager_rules import DatabaseManagerRules
from site_manager.manager import SiteManager


class MainController:
    _instance = None

    _database_manager = DatabaseManagerRules("examples")
    _site_manager = SiteManager()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @property
    def get_categories(self):
        return list([x for x in self._site_manager.
                    get_proceed_categories.values()])

    @property
    def get_examples(self):
        return self._database_manager.get_collection()

    def get_filter_examples(self, category: dict):
        return self._database_manager.get_collection(category)
