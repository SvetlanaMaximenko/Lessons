string1 = input('Введите 1-ую строку ')
string2 = input('Введите 2-ую строку ')
list1 = set(string1)
list2 = set(string2)

if list1 == list2:
    print(True)
else:
    print(False)

