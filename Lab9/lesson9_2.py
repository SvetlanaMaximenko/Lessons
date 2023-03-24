# Создать класса truck и car которые являются наследниками класса auto Класс
# truck имеет дополнительный обязательный атрибут max_load Переопределённый
# метод move перед появлением надписи «move» выводит надпись «attention» его
# реализацию сделать при помощи оператора super А так же дополнительный метод
# load При его вызове происходит пауза сек затем выдаётся сообщение «load» и
# снова пауза сек Класс car имеет дополнительный обязательный атрибут
# max_speed и при вызове метода move после появления надписи «move» должна ,
# появиться надпись «max speed is <max_speed>» Создать по объекта для каждого
# из классов truck и car проверить все их методы и атрибуты , .

import time


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


class Truck(Auto):

    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        print(f'max_speed is {self.max_speed}')
        super().move()


auto1 = Auto("Tayota", 10, "Avensis", "silver", 2000)
auto2 = Auto("Audi", 2, "A4")
print(auto1.brand, auto1.age, auto1.mark, auto1.color, auto1.weight)
print(auto2.brand, auto2.age, auto2.mark, auto2.color, auto2.weight)
auto1.move()
auto1.stop()
auto1.birthday()
print(auto1.brand, auto1.age, auto1.mark, auto1.color, auto1.weight)
auto3 = Truck("Ford", 3, "Passat", 3000, "black", 1500)
print(auto3.brand, auto3.age, auto3.mark, auto3.color, auto3.weight, auto3.max_load)
auto3.move()
auto3.load()
auto4 = Truck("Audi", 4, "Q6", 4000)
print(auto4.brand, auto4.age, auto4.mark, auto4.color, auto4.weight, auto4.max_load)
auto4.move()
auto4.load()
auto5 = Car("Lada", 15, "Kalina", 200, "red", 1000)
print(auto5.brand, auto5.age, auto5.mark, auto5.color, auto5.weight, auto5.max_speed)
auto5.move()
auto6 = Car("BMW", 6, "X5", 400, "white")
print(auto6.brand, auto6.age, auto6.mark, auto6.color, auto6.weight, auto6.max_speed)
auto6.move()


