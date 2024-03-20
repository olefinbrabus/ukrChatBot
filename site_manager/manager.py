import httpx
from bs4 import BeautifulSoup
from dataclasses import dataclass, asdict

from config import SITE_API_EXAMPLES, SITE_API_CATEGORIES, SITE_URL


@dataclass
class RulesUkrMovaApiParam:
    _id: int
    category_id: int
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
    def get_proceed_rules(self):
        data = self._json_request_handler()

        return [asdict(example) for example in data]

    @property
    def get_proceed_categories(self):
        return self._json_categories_handler()

    def _json_request_handler(self) -> list:
        name_of_category = self._json_categories_handler()
        sorted_data = sorted(self.examples_from_site, key=lambda x: x["category"])

        data = []
        for i, message in enumerate(sorted_data):
            msg = _remove_html_tags(message["content"])

            data.append(
                RulesUkrMovaApiParam(
                    _id=i,
                    category_id=message["category"],
                    category_name=name_of_category[message["category"]],
                    title=message["title"],
                    content=msg,
                    image=SITE_URL + message["image"],
                    url=SITE_URL + message["uri"]
                )
            )

        return data

    def _json_categories_handler(self) -> dict:
        list_categories = {}
        for category in self.categories_from_site:
            list_categories[category["id"]] = category["title"]

        return list_categories


# def _check_validation_status(validation_status: httpx.Response) -> None:
#     if validation_status.status_code != 200:
#         raise Exception('site didnt work')


def _remove_html_tags(html) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    text = text.replace('\n', "")
    text = text.replace('\xa0', "")
    text = text.replace(';', "\n")
    text = text.replace(':', ":\n")
    return text

