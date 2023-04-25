from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from models import Base
from sqlalchemy import URL


class Operations(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True)
    name_ac = mapped_column(ForeignKey("account.name"))
    amount = Column(Integer)  # положительное число - пополнение, отрицательное - снятие со счёта
    date = Column(DateTime)

    def __repr__(self):
        return f'{self.name_ac}: {self.amount}: {self.date}'

    def add_operation(self):
        pass
