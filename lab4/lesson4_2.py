# Написать программу, используя функции input() и print().
# Программа запрашивает ввести произвольную строку.
# Затем необходимо создать 2 строковые переменные,
# первая из которых состоит только из чётных символов введённой строки,
# а вторая только из не чётных (сделать это двумя способами: через слайсы и через цикл).
# Вначале вывести введённую строку без начальных и завершающих пробелов
# в формате "Введена строка <введённая строка>”.
# Сделать 2 отступа (используя аргументы функции print)
# и затем обе переменные вывести одной функцией print, разделяя их между собой пятью
# пробелами и закончить вывод переводом строки и тремя восклицательными знаками.

string = input("Введите произвольную строку ")
string.strip()
print(f'Введена строка {string}\n\n')
string1 = string[0:len(string):2]
string2 = string[1:len(string):2]
print(f'{string1}     {string2}\n!!!')
string1 = ""
string2 = ""
for i in range(len(string)):
    if i%2 == 0:
        string1 += string[i]
    else:
        string2 += string[i]
print(f'{string1}     {string2}\n!!!')

