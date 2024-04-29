import httpx
from dataclasses import dataclass, asdict

from bs4 import BeautifulSoup

from config import SITE_API_EXAMPLES, SITE_API_CATEGORIES, SITE_URL


@dataclass
class RulesUkrMovaApiParam:
    _id: int
    category_name: str
    title: str
    content: str
    image: str
    url: str


class SiteManager:
    _instance = None

    examples_from_site = httpx.get(SITE_API_EXAMPLES).json()
    categories_from_site = httpx.get(SITE_API_CATEGORIES).json()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @property
    def get_proceed_rules(self) -> list[dict]:
        data = self._json_request_handler()

        return [asdict(example) for example in data]

    def _json_request_handler(self) -> list[RulesUkrMovaApiParam]:
        name_of_category = self.get_proceed_categories
        sorted_data = sorted(self.examples_from_site, key=lambda x: x["category"])

        data = []
        errors_message: str = ""
        for i, message in enumerate(sorted_data):
            try:
                content = _remove_html_tags(message["content"])

                rule = RulesUkrMovaApiParam(
                    _id=i,
                    category_name=name_of_category[message["category"]],
                    title=message["title"],
                    content=content,
                    image=SITE_URL + message["image"],
                    url=SITE_URL + message["uri"]
                )
                data.append(rule)
            except TypeError as e:
                errors_message += e
                errors_message += "\n"

        if errors_message != "":
            raise TypeError(errors_message)
        return data

    @property
    def get_proceed_categories(self) -> dict[int, str]:
        list_categories = {}
        for category in self.categories_from_site:
            list_categories[category["id"]] = category["title"]

        return list_categories


def _remove_html_tags(html) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    text = text.replace('\n', "")
    text = text.replace('\xa0', "")
    text = text.replace(';', "\n")
    text = text.replace(':', ":\n")
    return text
