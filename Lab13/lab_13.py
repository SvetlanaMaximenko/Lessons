# Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.
# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.


import random


class MyIterator:

    def __init__(self, begin_diapason: int, end_diapason: int, begin_num: int, end_num: int = None):
        self.current_num = begin_num
        self.end_num = end_num
        self.begin_diapason = begin_diapason
        self.end_diapason = end_diapason

    def __next__(self):
        if self.end_num is not None and self.current_num >= self.end_num:
            raise StopIteration
        result = random.randint(self.begin_diapason, self.end_diapason)
        self.current_num += 1
        return result

    def __iter__(self):
        return self


print('Работает итератор')
iterator = MyIterator(10, 1000, 5, 15)
for num in iterator:
    print(num)


# Генератор
def my_generator(begin_diapason: int, end_diapason: int, num: int, end_num: int = None):
    while True:
        if end_num is not None and num >= end_num:
            break
        yield random.randint(begin_diapason, end_diapason)
        num += 1


stop_number = 10
iterator = my_generator(5, 20, 1)
print('Работает генератор')
for i in iterator:
    print(i)
    if i == stop_number:
        break



