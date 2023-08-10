from utils.api import GoogleMapsApi
from utils.checking import Checking
from utils.logger import Logger

"""Создание, изменение и удаление новой локации"""


class TestCreatePlace:

    def test_create_new_place(self):
        print("\n")  # Пустая строка для удобства чтения результатов
        print('Метод POST')  # Маркер для информированности
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print()  # Пустая строка для удобства чтения результатов
        print('Метод GET')  # Маркер для информированности
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print()  # Пустая строка для удобства чтения результатов
        print("Метод PUT")  # Маркер для информированности
        result_put = GoogleMapsApi.put_new_place(place_id)  # Создание переменной со значением вызова метода
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        
        print()  # Пустая строка для удобства чтения результатов
        print("Метод GET для PUT")  # Маркер для информированности
        result_get = GoogleMapsApi.get_new_place(place_id)  # Создание переменной со значением вызова метода
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'])
        Checking.check_json_value(result_get, 'address', '23 Lenina street, RU')

        print()  # Пустая строка для удобства чтения результатов
        print("Метод DELETE")  # Маркер для информированности
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # Создание переменной со значением вызова метода
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print()  # Пустая строка для удобства чтения результатов
        print("Метод GET для DELETE")  # Маркер для информированности
        result_get = GoogleMapsApi.get_new_place(place_id)  # Создание переменной со значением вызова метода
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', 'Get operation failed, looks like place_id  doesn\'t exists')
        Checking.check_json_search_word_in_value(result_get, 'msg', 'doesn\'t exists')
        print("Тестирование создания, изменения и удаления новой локации прошло успешно!")
        print(f'Результаты теста записаны в следующий лог файл "{Logger.file_name}"')
        