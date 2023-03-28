# Дополнительная задача:
# Написать программу телефонная книга используя классы.
# Написать класс телефонной книги, который хранит список контактов.
# Он должен иметь возможность искать контакты по имени и по телефону (два разных метода),
# добавлять новые контакты и удалять контакты по имени или телефону. Контакты реализовать в виде объектов класса Контакт.
# Данные телефонной книги хранить в json файле.

import json


class Contact:
    books = []

    def __init__(self, name, telephone):
        self.name = name
        self.telephone = telephone
        Contact.books.append(self)

    def search_name(self, telephone1: str):
        if self.telephone == telephone1:
            print(f"Телефон {self.telephone} у {self.name}")

    def search_tel(self, name1: str):
        if self.name == name1:
            print(f"Для {self.name} телефон {self.telephone}")

    def del_contact_name(self, name1: str):
        if self.name == name1:
            Contact.books.remove(self)

    def __str__(self):
        return f'{self.name} - {self.telephone}'


kol = 2
for i in range(0, kol):
    book = Contact(input('Введите ФИО -> '), input('Введите телефон -> '))
    print(Contact.books[i].__str__())

name_ = input('Введите ФИО, телефон которого нужно найти -> ')
for i in range(len(Contact.books)):
    Contact.books[i].search_tel(name_)
telephone_ = input('Введите телефон абонента -> ')
for i in range(len(Contact.books)):
    Contact.books[i].search_name(telephone_)

# name_ = input('Введите ФИО, контакт которого нужно удалить -> ')
# for i in range(len(Contact.books)):
#     Contact.books[i].del_contact_name(name_)











