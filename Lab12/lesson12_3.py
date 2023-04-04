# 2 (из ДЗ номер 5)
# Написать функцию, которая принимает целое число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.

class Input_Error(Exception):

    def __init__(self, text):
        self.text = text


try:
    number = int(input("Введите целое число -> "))
    if (number % 7) == 0 and (number % 4) == 0:
        raise Input_Error("The number is divisible by 7 and 4")
    if number % 2 == 0:
        print(f"Число четное. Квадрат числа {number} = {number ** 2}")
    else:
        print(number)
except ValueError:
    print("Error type of value!")
except Input_Error:
    print("The number is divisible by 7 and 4")
