# Сделать функцию которая на вход принимает строку Анализирует её
# исключительно методом isdigit без доп библиотек и переводит строку в число    . ()    .           . 
# Функция умеет распознавать отрицательные числа и десятичные дроби Примеры               .  :
# -6.7 : -6.7 → Вы ввели отрицательное дробное число
# 5 : 5 → Вы ввели положительное целое число
# 5.4r : 5.4r → Вы ввели не корректное число
# -.777 : -0.777 → Вы ввели отрицательное дробное число


def parse_string(string: str) -> float:
    # flag = 1 есть знак минус
    # flag = 0 нет знака минус

    print(f'{string} -> ')
    flag = 0
    if string[0] == '-':
        flag = 1              
        string = string[1:len(string)]

    list_ = string.split('.')
    
    for number in list_:
        if not(number.isdigit):
            return print('Вы ввели некорректное число')
    if len(list_) > 2:
        return print('Вы ввели некорректное число')
    if len(list_) == 1 and flag == 0:
        return print('Вы ввели положительное целое число')
    elif len(list_) == 1 and flag == 1:
        return print('Вы ввели отрицательное целое число')
    elif len(list_) == 2 and flag == 1:
        return print('Вы ввели отрицательное дробное число') 
    elif len(list_) == 2 and flag == 0:
        return print('Вы ввели положительное дробное число')
    
        
string = input('Введите число -> ')
parse_string(string)

