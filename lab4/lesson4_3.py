# Сделать программу, в которой нужно будет угадывать число
import random

number = random.randint(1,10)
x = 0
while x != number:
    x = int(input('Угадай число от 1 до 10 '))
print(f'Угадали. Это число {number}')
