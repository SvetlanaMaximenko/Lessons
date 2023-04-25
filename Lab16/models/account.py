# from sqlalchemy import ForeignKey, UniqueConstraint
# from sqlalchemy.orm import Mapped, mapped_column, relationship, backref, column_property
from sqlalchemy import Column, Integer, String, DateTime
from models import Base


class Account(Base):
    __tablename__ = "account"

    name = Column(String, primary_key=True)
    balance = Column(Integer)

    def __repr__(self):
       return f'{self.name}: {self.balance}'



