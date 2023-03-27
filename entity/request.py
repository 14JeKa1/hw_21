from typing import Dict
from entity.abstract_storage import AbstractStorage

class Request:
    def __int__(self, request: str, storages: Dict[str, AbstractStorage]):
        #TODO: Разделить строку по пробелам
        parsed_request = request.lower().split(' ')
        if len(parsed_request) != 7:
            print("Не правильный запрос")
            return

        #TODO: Внести значение из строки в атрибуты класса
        self.amount = int(parsed_request[1])
        self.product = parsed_request[2]
        self.departure = parsed_request[4]
        self.destination = parsed_request[6]
        #TODO: Провалидировать пункты отправки и назначения
        if self.departure not in storages or self.destination not in storages:
            print("Неизвестный склад")
            return