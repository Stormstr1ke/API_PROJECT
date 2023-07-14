# API_PROJECT
Написание проекта по автоматизации тестирования API

Тестируется учебная API Google Maps (https://rahulshettyacademy.com)

В проекте используются кастомные методы для отправки запросов вместо стандартных из библиотеки requests

Для создания новой локации используется метод POST
Для проверки, что локация cоздзана используется метод GET
Для изменения адреса локации используется метод PUT
Для проверки, что адрес локации изменился используется метод GET
Для удаления локации используется метод DELETE
Для проверки, что локация удалена используется метод GET

Дополнительно созданы следующие методы для проверки ответов на запросы:
- метод проверки статус кода;
- метод проверки наличия обязательных полей в ответе запроса.
