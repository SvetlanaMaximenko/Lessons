# 4*
# Ввести строку (считаем, что в начале и в конце строки нет пробелов,
# все слова в строке разделены одним пробелом). Для введенной строки
# изменить порядок символов в каждом слове в предложении,
# сохраняя при этом пробелы и первоначальный порядок слов.
# Примеры:
# "Hello World!" -> "olleH !dlroW"
# "Let's see, how it works" -> "s'teL ,ees woh ti skrow"


string = input('Введите строку ')
string1 = ''
word = ''
string += ' '
list_ = list()
for i in range(len(string)):
    if string[i] == ' ':
        word1 = ''.join(reversed(word))
        list_.append(word1)
        word = ''
    else:
        word = word + string[i]

string1 = ' '.join(list_)
print(string1)

    

