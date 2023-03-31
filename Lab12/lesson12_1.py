# 1
# Реализовать декоратор ЧЕРЕЗ КЛАСС!, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров

import time


class decorator():

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        if len(args) ==0  and len(kwargs) == 0:
            return print(f'Функция {self.func.__name__} вызвана в {time.strftime("%Y-%m-%d %X")} без параметров', end='\n')
        print(f'Функция {self.func.__name__} вызвана в {time.strftime("%Y-%m-%d %X")} c', end=" ")
        if args != ():
            print(f"позиционными параметрами {args}", end=" ")
        if len(kwargs) != 0:
            print(f"именованными параметрами {kwargs}", end=" ")
        print(end="\n")
        self.func(*args, **kwargs)
        return self.func(*args, **kwargs)


@decorator
def my_add(*Number, **Numbers1) -> int:
    s = 0
    for i in Number:
        s += i
    for i in Numbers1:
        s += Numbers1[i]
    return s


print(my_add(4, 6))
print(my_add(a=1, b=2))
print(my_add(1, b=8))
print(my_add())
