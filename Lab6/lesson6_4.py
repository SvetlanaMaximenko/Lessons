# Написать декоратор к 2м любым функциям который бы считал 
# и выводил время их выполнения. 


from datetime import datetime


def time_decorator(func):
    def wrapper_to_func(*args):
        time_start = datetime.now()
        func(args[0],args[1])
        print(datetime.now() - time_start)
    return wrapper_to_func


@time_decorator
def find_mean(x, y: int) -> int:
    return print(f'Среднее значение чисел {x} и {y} = {(x + y) / 2}')
    

@time_decorator
def max_x_y(x, y: int) -> int:
    return print(f'Максимальное из чисел {x} и {y} = {max(x,y)}')


x = int(input('Введите 1ое число '))
y = int(input('Введите 2ое число '))
find_mean(x,y)
max_x_y(x,y)        
