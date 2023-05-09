from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models.products import Products
from models.users import Users
import db


db.configure_engine()
Base.metadata.drop_all(db.engine)
Base.metadata.create_all(db.engine)

session = db.Session()


def init_db():

    def print_products():
        print("Список доступных товаров")
        print("{:<5} {:<10} {:<10} {:<20}".format("ID", "Стоимость", "Количество", "Название"))
        list_products = session.query(Products).all()
        for i in list_products:
            print("{:<5d} {:<10d} {:<10d} {:<20}".format(i.id, i.cost, i.count, i.name))

    def login():
        input_username = input("Имя -> ")
        if Users.is_exist(input_username):
            passw = input("Пароль -> ")
        else:
            print("Такого пользователя нет. Необходимо зарегистрироваться")
        print(input_username)

    with session.begin() as db.Session:
        while True:
            comand = str(input('Введите команду: Товары, Зарегистрироваться, Войти, Выйти -> '))
            if comand == 'Товары':
                # prod1 = Products(name="Карандаш", cost=5, count=2)
                # session.add(prod1)
                # prod2 = Products(name="Ручка", cost=10, count=3)
                # session.add(prod2)
                print_products()
            elif comand == 'Зарегистрироваться':
                print(f'Выбрали "Зарегистрироваться"')
            elif comand == 'Войти':
                # user_ = Users(username="Sveta", password="0310", points=0)
                # session.add(user_)
                print(f'Выбрали "Войти"')
                login()
            elif comand == 'Выйти':
                print(f'Выбрали "Выйти"')
                break
        session.commit()


if __name__ == '__main__':
    init_db()

