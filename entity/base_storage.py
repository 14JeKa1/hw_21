from typing import Dict
from entity.abstract_storage import AbstractStorage

class BaseStorage(AbstractStorage):
    def __init__(self, items: dict, capacity: int = 100):
        self.__items = items
        self.__capacity = capacity
        super.__init__(items, capacity)

    def add(self, name: str, amount: int) -> bool:
        # TODO: Проверить, достаточно места
        if self.get_free_space() < amount:
            print("не хватает места")
            return False

        # TODO: Добавить товар
        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount
        return True

    def remove(self, name: str, amount: int) -> bool:
        # TODO: Проверить, есть товар
        if name not in self.__items:
            print("Такого товара нет")
            return False
        if self.__items[name] < amount:
            print("Недостаточно товара")
            return False

        # TODO: Вычесть необходимое количество
        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)
        return True

    def get_free_space(self) -> int:
        # TODO: Посчитать сумму значений
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)