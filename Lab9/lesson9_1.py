# Создать родительский класс auto у которого есть атрибуты brand age cоlor mark
# и weight А так же методы move birthday и stop Методы move и stop выводят :
# сообщение на экран «move» и «stop» а birthday увеличивает атрибут age на  1.
# Атрибуты brand age и mark являются обязательными при объявлении объекта .


class Auto:

    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1


auto1 = Auto("Tayota", 10, "Avensis", "silver", 2000)
auto2 = Auto("Audi", 2, "A4")
print(auto1.brand, auto1.age, auto1.mark, auto1.color, auto1.weight)
print(auto2.brand, auto2.age, auto2.mark, auto2.color, auto2.weight)
auto1.move()
auto1.stop()
auto1.birthday()
print(auto1.brand, auto1.age, auto1.mark, auto1.color, auto1.weight)
