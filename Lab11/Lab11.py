# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.

from datetime import datetime
from enum import Enum, IntEnum
import csv


class Account:

    def __init__(self, name: str, balans: int) -> None:
        self.name = name
        self.balans = balans


class ReplenishmentEnum(IntEnum):
    PLUS = 1
    MINUS = 0


class Operation:

    def __init__(self, summa: int, replenishment: ReplenishmentEnum, account: Account):
        self.summa = summa
        self.replenishment = replenishment
        self.data = datetime.now()
        self.account = account

    def add_summa(self):
        if self.replenishment == 1:
            self.account.balans += self.summa
        else:
            self.account.balans -= self.summa


class History:

    def __init__(self):
        self.list_operation: list[Operation] = []

    def add_operation(self, operation: Operation):
        self.list_operation.append(Operation)

    def print_list(self):
        print(len(self.list_operation))
        for i, item in enumerate(self.list_operation):
            print(i, item)
            print(self.list_operation[i].summa, self.list_operation[i].data)


user = Account("Sveta", 200)
print(user.name, user.balans)
operation1 = Operation(100, ReplenishmentEnum.PLUS, user)
operation1.add_summa()
list_operation = History()
list_operation.add_operation(operation1)
print(user.name, user.balans)
operation2 = Operation(150, ReplenishmentEnum.MINUS, user)
list_operation.add_operation(operation2)
print(user.name, user.balans)

list_operation.print_list()

user1 = Account("Ivan", 1000)
print(user1.name, user1.balans)

