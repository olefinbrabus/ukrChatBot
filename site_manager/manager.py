import httpx
import json

from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
from typing import Final

from config import SITE_API, SITE_URL

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
    def __init__(self, url: str) -> None:
        self.proceed_data = url

    @property
    def proceed_data(self):
        return self._proceed_data

    @proceed_data.setter
    def proceed_data(self, url: str) -> None:
        response = httpx.get(url)
        check_validation_status(response)
        new_json = response.json()
        actual = actual_json()
        if new_json != actual:
            create_or_overwrite_json(response)
        self._proceed_data = json_request_handler(actual)


def check_validation_status(validation_status: httpx.Response) -> None:
    if validation_status.status_code != 200:
        raise Exception('site didnt work')


def photos_show(mngr: SiteManager, index: int) -> None:
    index_dict = mngr.proceed_data[index]
    img = httpx.get(index_dict["image"])
    img = Image.open(BytesIO(img.content))
    img.show()


def remove_html_tags(html) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    text = soup.get_text()

    text = text.replace('\n', "")
    text = text.replace('\xa0', "")
    return text


def json_request_handler(file: list) -> list:
    data = sorted(file, key=lambda x: x["category"])

    sorted_data = []

    for message in data:
        msg = remove_html_tags(message["content"])
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


def actual_json():
    try:
        with open("data.json", "r") as file:
            data_file = json.load(file)

    except FileNotFoundError:
        response = httpx.get(SITE_URL)
        create_or_overwrite_json(response)
        with open('data.json', 'r') as data:
            data_file = json.load(data)

    return data_file


def create_or_overwrite_json(response: httpx.Response) -> None:
    with open('data.json', 'w') as data:
        json.dump(response.json(), data, ensure_ascii=False)


if __name__ == "__main__":
    manager = SiteManager(SITE_API)

    for data in manager.proceed_data:
        print(data)


