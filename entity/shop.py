from entity.abstract_storage import AbstractStorage
from entity.base_storage import BaseStorage

class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):

        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> bool:
        #TODO: Проверить, что места достаточно
        if name not in self.get_unique_items_count() >= 5:
            print("Много разных товаров")
            return False
        return super().add(name, amount)
