# Дан список чисел Вернуть список где при помощи функции map каждое число
# переведено в строку В качестве функции в map использовать lambda


list_ = [5, 8, -3, 8, 0, 2]
print(list_)
list_new = list(map(lambda i: str(i), list_))
print(list_new)
