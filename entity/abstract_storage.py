from abc import ABC, abstractmethod
from typing import Dict

class AbstractStorage(ABC):

    def __init__(self, items: Dict[str,int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    @abstractmethod
    def add(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

    @abstractmethod
    def get_items(self):
        pass