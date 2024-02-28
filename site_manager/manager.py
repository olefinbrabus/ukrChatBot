import httpx
import json

from json import JSONDecodeError
from bs4 import BeautifulSoup
from typing import Final
from os import remove

from config import SITE_API, SITE_URL

"""
В API сайту категорії розбиті по таким числам категорії,
але вони не написані явно
"""
TYPE_OF_CATEGORIES: Final = {
    14: "Фразеологізми",
    37: "Орфографія",
    38: "Антисуржик",
    42: "Синоніми",
    58: "Пароніми",
    73: "Інше",
    83: "Цитати",
    85: "Для дітей",
    87: "Наголос",
    617: "Правопис 2019",
}


class SiteManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @property
    def proceed_data(self):
        response = httpx.get(SITE_API)
        _check_validation_status(response)
        new_json = response.json()
        actual = _validation_json()
        if new_json != actual:
            _create_or_overwrite_json(response)
        return json_request_handler(actual)

    def get_category(self, category: str):
        data_in_category = []
        identy = 0
        for i, data in enumerate(self.proceed_data):
            if data["category"] == category:
                identy += 1
                data["id_in_category"] = identy

                data_in_category.append(data)

        return data_in_category


def _check_validation_status(validation_status: httpx.Response) -> None:
    if validation_status.status_code != 200:
        raise Exception('site didnt work')


def _remove_html_tags(html) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    text = soup.get_text()

    text = text.replace('\n', "")
    text = text.replace('\xa0', "")
    text = text.replace(';', "\n")
    text = text.replace(':', ":\n")
    return text


def json_request_handler(file: list) -> list:
    data = sorted(file, key=lambda x: x["category"])

    sorted_data = []

    for message in data:
        msg = _remove_html_tags(message["content"])
        sorted_data.append(
            {
                "id": message["id"],
                "category_id": message["category"],
                "category": TYPE_OF_CATEGORIES[message["category"]],
                "title": message["title"],
                "content": msg,
                "image": SITE_URL + message["image"],
                "url": SITE_URL + message["uri"]
            }
        )
    return sorted_data


def _validation_json():
    try:
        _read_json()

    except FileNotFoundError:
        response = httpx.get(SITE_API)
        _create_or_overwrite_json(response)

    except JSONDecodeError:
        response = httpx.get(SITE_API)
        _create_or_overwrite_json(response)

    finally:
        data_file = _read_json()

    return data_file


def _read_json():
    with open('data.json', 'r') as file:
        return json.load(file)


def _create_or_overwrite_json(response: httpx.Response) -> None:
    with open('data.json', 'w') as data:
        json.dump(response.json(), data, ensure_ascii=False)
