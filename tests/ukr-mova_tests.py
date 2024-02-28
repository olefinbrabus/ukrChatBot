import unittest

from os import remove

from site_manager.manager import SiteManager


class TestCategories(unittest.TestCase):
    def setUp(self):
        self.manager = SiteManager()

    def test_phraseological_unit(self):
        categories = self.manager.get_category("Фразеологізми")
        remove('data.json')
        self.assertEqual(len(categories), 93)

    def test_quotes(self):
        categories = self.manager.get_category("Цитати")
        remove('data.json')
        self.assertEqual(len(categories), 22)


if __name__ == '__main__':
    unittest.main()
