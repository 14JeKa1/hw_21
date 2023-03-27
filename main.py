#from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
#from exceptions import CourierError

store = Store(
    items={
        "печенька": 25,
        "собачка": 25,
        "елка": 25,
        "пончик": 3,
        "зонт": 5,
        "ноутбук": 1,
    },
)

shop = Shop(
    items={
        "печенька": 2,
        "собачка": 2,
        "елка": 2,
        "зонт": 1,
        "пончик": 1,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}

def main():
    print('Добрый день!')

    while True:
        #TODO: Вывести содержание складов
        for storage_name in storages:
           print(f'Сейчас в {storage_name}:\n{storages[storage_name].get_items()}')
        break

        # TODO: Запросить ввод от пользователя
        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склада в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ('стоп', 'stop'):
            break

        #TODO: Провалидировать ввод
        request = Request(request=user_input, storages=storages)


        #TODO: Запустить доставку
        if storages[request.destination].remove(request.product, request.amount):
            print(f'Курьер забрал {request.amount}{request.product} из {request.departure}')

            if storages[request.destination].add(request.product, request.amount):
                print(f'Курьер доставил{request.amount}{request.product} в {request.destination}')
            else:
                storages[request.departure].add(request.product, request.amount)
                print(f'Курьер вернул {request.amount}{request.product} в {request.departure}')

if __name__ == '__main__':
    main()