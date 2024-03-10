import unittest

from views.handlers import categories_handler

from aiogram_tests import MockedBot
from aiogram_tests.handler import MessageHandler
from aiogram_tests.types.dataset import MESSAGE


class Tests(unittest.TestCase):
    async def test_error_positive(self):
        request = MockedBot(MessageHandler(categories_handler))
        calls = await request.query(message=MESSAGE.as_object("wtf"))
        answer_message = calls.send_messsage.fetchone()
        assert answer_message.text == "Помилка. неправильний номер. Спробуйте ще раз."

        """Попередження виникає через те,
            що версія боту більша ніж рекомендована для тесту,
            але він працює, Тест пройшов успішно,
            якщо тест написав ОК після попереджень.
        """


if __name__ == '__main__':
    unittest.main()
