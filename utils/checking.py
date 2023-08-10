import json

"""Методы для проверки ответов на запросы"""


class Checking:
    """Метод проверки статус кода"""

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code  # Сравниваемый фактический результат и ожидаемый
        print("1) Успешно! Статус код = " + str(result.status_code))

    """Метод проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("2) Все поля присутствуют")

    """Метод для проверки содержимого полей"""

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'3) Значение в поле {field_name} верно')

    """Метод для проверки значений обязательных полей в ответе запроса по заданному словосочетанию или слову"""

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f'4) В поле {field_name} присутствует словосочетание {search_word}')
