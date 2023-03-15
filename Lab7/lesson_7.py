# Написать декоратор, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров


import time
from collections.abc import Callable
from functools import wraps


def decorator(func: Callable) -> Callable:
    @wraps(func)
    def inner(*Args, **Kwargs):
        if Args == () and len(Kwargs) == 0:
            return print(f'Функция {func.__name__} вызвана в {time.strftime("%Y-%m-%d %X")} без параметров', end='\n')
        print(f'Функция {func.__name__} вызвана в {time.strftime("%Y-%m-%d %X")} c', end=" ")
        if Args != ():
            print(f"позиционными параметрами {Args}", end=" ")
        if len(Kwargs) != 0:
            print(f"именованными параметрами {Kwargs}", end=" ")
        print(end="\n")
        func(*Args, **Kwargs)
    return inner


# @decorator
# def add(a, b: int) -> int:
#     return print(a+b)


@decorator
def add(*Number, **Numbers1) -> int:
    s = 0
    for i in Number:
        s += i
    for i in Numbers1:
        s += Numbers1[i]
    return print(s)

add(2, 3)
add(a=4, b=5)
add(1, b=2)
add()
add(2, 3, 9, 8, 10)
add(a=4, b=5, c=1)
add(1, b=2, d=1, h=9)
