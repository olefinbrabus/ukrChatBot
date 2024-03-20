import unittest

from site_manager.manager import SiteManager


class TestCategories(unittest.TestCase):
    def setUp(self):
        self.manager = SiteManager()

    def test_phraseological_unit(self):
        examples = self.manager.get_proceed_rules
        examples = [x for x in examples if x["category_name"] == "Фразеологізми"]
        self.assertEqual(len(examples), 93)

    def test_quotes(self):
        categories = self.manager.get_proceed_categories
        self.assertEqual(len(categories), 10)


if __name__ == '__main__':
    unittest.main()
