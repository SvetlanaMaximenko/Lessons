#Ввести с клавиатуры строки и сохранить их в разные переменные Создать
#файл и записать в него первые строки и закрыть файл. Затем открыть файл
#на редактирование и дозаписать оставшиеся строки. В итогом файле должны быть
#4 строки каждая из которых должна начинаться с новой строки.


string1 = input('Введите 1ую строку -> ')
string2 = input('Введите 2ую строку -> ')
string3 = input('Введите 3ью строку -> ')
string4 = input('Введите 4ую строку -> ')
with open('strings.txt', 'w') as file:
    file.write(f'{string1} \n')
    file.write(f'{string2} \n')
with open('strings.txt', 'a') as file:
    file.write(f'{string3} \n')
    file.write(f'{string4} \n')
    
