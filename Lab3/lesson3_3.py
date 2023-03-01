# 1 - камень
# 2 - ножницы
# 3 - бумага

import random

player = int(input('Выберите 1 - камень, 2 - ножницы, 3 - бумага '))
while player != 1 and player != 2 and player != 3:
    player = int(input('Выберите 1 - камень, 2 - ножницы, 3 - бумага '))
    
bot = random.randint(1,3)
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

