# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.

from datetime import datetime
from enum import Enum, IntEnum
import csv


class ReplenishmentEnum(IntEnum):
    PLUS = 1
    MINUS = 0


class Operation:

    def __init__(self, summa: int, replenishment: ReplenishmentEnum):
        self.summa = summa
        self.replenishment = replenishment
        self.data = datetime.now()


class Account:

    def __init__(self, name: str, balans: int) -> None:
        self.name = name
        self.balans = balans
        self.list_operation: list[Operation] = []

    def add_operation(self, operation: Operation):
        self.list_operation.append(operation)
        if operation.replenishment == ReplenishmentEnum.PLUS:
            self.balans += operation.summa
        else:
            self.balans -= operation.summa

    def print_list(self):
        print(f"Текущее состояние счета {self.name}: {self.balans}")
        for i, item in enumerate(self.list_operation):
            if self.list_operation[i].replenishment == ReplenishmentEnum.PLUS:
                print(f" {i+1}, +{self.list_operation[i].summa}, {self.list_operation[i].data}")
            else:
                print(f" {i+1}, -{self.list_operation[i].summa}, {self.list_operation[i].data}")


user = Account("Sveta", 200)
print(f"Открытие счета {user.name}: {user.balans}")
operation1 = Operation(100, ReplenishmentEnum.PLUS)
user.add_operation(operation1)
operation2 = Operation(2000, ReplenishmentEnum.PLUS)
user.add_operation(operation2)
operation3 = Operation(220, ReplenishmentEnum.MINUS)
user.add_operation(operation3)
user.print_list()

user1 = Account("Ivan", 1000)
print(f"Открытие счета {user1.name}: {user1.balans}")
operation1 = Operation(150, ReplenishmentEnum.MINUS)
user1.add_operation(operation1)
operation2 = Operation(250, ReplenishmentEnum.MINUS)
user1.add_operation(operation2)
operation3 = Operation(17, ReplenishmentEnum.PLUS)
user1.add_operation(operation3)
operation4 = Operation(5, ReplenishmentEnum.PLUS)
user1.add_operation(operation4)
user1.print_list()
