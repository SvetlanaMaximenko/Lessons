# 2
# Написать функцию, которая принимает число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Для проверки на четность использовать функцию из задания 1.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.


def chetnost(number : int) -> bool:
    if number % 2 == 0 :
        return True
    else :
        return False


def print_(n: int = None):
    if n.isdigit() == True:
        n = int(n)
        for i in range(n):
            if i % 4 == 0 and i % 7 == 0 and i != 0:
                break
            elif chetnost(i) == True:
                print(f'{i ** 2}')
            else:
                print(f'{i}')
    else:
        print("Введенные данные не являются числом")
    

n_ = input("Введите число ")
print_(n_)
