import unittest

from math import sqrt

from database.db_manager_rules import DatabaseManagerRules


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.db_manager = DatabaseManagerRules("test")

    def tearDown(self):

        index = self.db_manager.get_collection()
        print(index[8])

        print(len(index))
        self.db_manager.drop_collection()

    def test_update_data(self):
        big_data = [
            {"_id": x,
             f"data_{x}": sqrt(x),
             f"data_{x + 1}": sqrt(x + 1),
             f"data_{x + 2}": sqrt(x + 2),
             }
            for x in range(10000)]

        self.db_manager.update_db(big_data)
        eq = len(self.db_manager.get_collection())
        self.assertEqual(eq, 10000)


if __name__ == "__main__":
    unittest.main()
