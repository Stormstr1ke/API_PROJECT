import datetime
import os

class Logger():
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n----------\n"
        data_to_add += f"Тест: {test_name}\n"
        data_to_add += f"Дата и время: {str(datetime.datetime.now())}\n"
        data_to_add += f"Метод запроса: {method}\n"
        data_to_add += f"URL запроса: {url}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_responce(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"Статус код ответа: {result.status_code}\n"
        data_to_add += f"Ответ: {result.text}\n"
        data_to_add += f"Заголовки ответа: {headers_as_dict}\n"
        data_to_add += f"\n----------\n"

        cls.write_log_to_file(data_to_add)