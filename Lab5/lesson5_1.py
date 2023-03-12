# Написать функцию, которая проверяет является ли целое число четным.
# Функция возвращает True, если число четное, False если нет.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.
# Ввод и вывод результата производится вне функции проверки


def chetnost(number : int) -> bool:
    if number % 2 == 0 :
        return True
    else :
        return False
    
    
number_ = input("Введите целое число ")
if number_.isdigit() == False:
    print("Введенные данные не являются целым числом!")
else:
    number_ = int(number_)
    if chetnost(number_) == True:
        print(f"Число {number_} четное")
    else:
        print(f"Число {number_} нечетное")
    
