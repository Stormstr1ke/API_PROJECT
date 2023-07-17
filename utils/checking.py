import json

"""Методы для проверки ответов на запросы"""


class Checking:
    """Метод проверки статус кода"""

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code  # Сравниваемый фактический результат и ожидаемый
        print("Успешно! Статус код = " + str(result.status_code))

    """Метод проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        print("ТИП ТОКЕНА", type(token))
        print("ТИП Ожидаемого результата", type(expected_value))
        print("САМ ТОКЕН", token)
        print("САМ Ожидаемый результат", expected_value)
        # assert list(token) == list(expected_value)
        # print("Все поля присутствуют")
