from utils.api import GoogleMapsApi
from utils.checking import Checking

"""Создание, изменение и удаление новой локации"""


class TestCreatePlace:

    def test_create_new_place(self):
        print('Метод POST')  # Маркер для информированности
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ('status', 'place_id', 'scope', 'reference', 'id'))

        print('Метод GET')  # Маркер для информированности
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ('location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'))

        print("Метод PUT")  # Маркер для информированности
        result_put = GoogleMapsApi.put_new_place(place_id)  # Создание переменной со значением вызова метода
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ('msg'))

        print("Метод GET для PUT")  # Маркер для информированности
        result_get = GoogleMapsApi.get_new_place(place_id)  # Создание переменной со значением вызова метода
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ('location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'))

        print("Метод DELETE")  # Маркер для информированности
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # Создание переменной со значением вызова метода
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ('status'))

        print("Метод GET для DELETE")  # Маркер для информированности
        result_get = GoogleMapsApi.get_new_place(place_id)  # Создание переменной со значением вызова метода
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ('msg'))
        print("Тестирование создания, изменения и удаления новой локации прошло успешно!")
