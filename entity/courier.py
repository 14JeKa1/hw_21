from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str,AbstractStorage]):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self.__request.destination in storages:
            self.__to = storages[self.__request.destination]

    def move(self):
        # TODO: Забрать товар со склада отправления
        self.__from.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.departure}')

        # TODO: Добавить товар на склад назначения
        self.__to.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}')


    def cancel(self):
        ...