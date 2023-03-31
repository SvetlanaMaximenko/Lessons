# 2
# Добавить обработку исключений в следующие задания:
    # 3* (из ДЗ номер 3)
    # Написать мини-игру «Камень ножницы бумага с ботом», в которой пользователь должен выбрать либо камень,
    # либо ножницы, либо бумагу. Бот делает случайный выбор (случайное число).
    # Вывести результат если, например, игрок выбрал бумагу, а бот ножницы:
    # Бот выбрал ножницы, вы проиграли!
    # Подсказка: я не показывала, как в Pyhon получить случайное число, попробуйте найти это сами

# 1 - камень
# 2 - ножницы
# 3 - бумага

import random


class Error_input(Exception):

    def __init__(self, text):
        self.txt = text


try:
    player = int(input('Выберите 1 - камень, 2 - ножницы, 3 - бумага '))
    if player < 1 or player > 3:
        raise Error_input("You entered not 1, 2, 3")
except ValueError:
    print("Error type of value!")
except Error_input:
    print("You entered not 1, 2, 3")
else:
    bot = random.randint(1, 3)
    print(f'Вы выбрали {player}')
    print(f'Бот выбрал {bot}')
    if player == bot:
        print('Ничья')
    elif player == 1 and bot == 2:
        print('Вы выиграли')
    elif player == 1 and bot == 3:
        print('Вы проиграли')
    elif player == 2 and bot == 1:
        print('Вы проиграли')
    elif player == 3 and bot == 1:
        print('Вы выиграли')
    elif player == 3 and bot == 2:
        print('Вы проиграли')
    elif player == 2 and bot == 3:
        print('Вы выиграли')
