from io import BytesIO
from typing import Collection

import requests
from PIL import Image


BASE_URL = 'https://ukr-mova.in.ua'
REQUEST_URL = f'{BASE_URL}/api-new?route=categories'
REQUEST_EXAPMLE = f'{BASE_URL}/api-new?route=examples'
USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
              ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
HEADERS = {'User-Agent': USER_AGENT}

ex_response = requests.get(REQUEST_EXAPMLE, headers=HEADERS)
ex_res_collection = ex_response.json()
# print(ex_res_collection)

response = requests.get(REQUEST_URL, headers=HEADERS)
content_data_collection = response.json()


class ContentDataSuit:
    CONTENT_DATA_COLLECTION: Collection[dict] = response.json()
    CONTENT_DATA_EXAMPLE_COLLECTION: Collection[dict] = ex_response.json()


class ContentDataExampleCollectionParam:
    ID = 'id'
    TITLE = 'title'
    CONTENT = 'content'
    CATEGORY = 'category'
    URI = 'uri'
    IMAGE = 'image'
    THUMB = 'thumb'


class ContentDataCollectionParam:
    ID = 'id'
    TITLE = 'title'
    IMAGE = 'image'


def _get_image_url(part_img_url: str) -> str:
    return f'{BASE_URL}/{part_img_url}'


def _get_content(src_content_data_suit):
    for content in src_content_data_suit:
        if content[ContentDataCollectionParam.TITLE] == 'Фразеологізми':
            image_url = _get_image_url(content[ContentDataCollectionParam.IMAGE])
            image_response = requests.get(image_url, headers=HEADERS)
            img = Image.open(BytesIO(image_response.content))
            img.show()

        print(content)


_get_content(ContentDataSuit.CONTENT_DATA_COLLECTION)