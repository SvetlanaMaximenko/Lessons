from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base
from models.operations import Operations
from models.account import Account


# connection settings
url = URL.create(
    drivername="postgresql",
    username="sveta",
    password="0310",
    host="127.0.0.1",
    database="sv"
)


def add_account(acc: Account):
    try:
        session.add(acc)
    except IntegrityError:
        return print("Error!")


engine = create_engine(url)
connection = engine.connect()
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
account_ = Account(name="Anna", balance=10)
account1 = Account(name="Olga", balance=100)
operations1 = Operations(name_ac="Anna", amount=5, date=datetime.now())

with Session.begin() as session:
    # add_account(account1)
    session.add(operations1)
    people = session.query(Account).all()
    for p in people:
        print(f"{p.name} {p.balance}")
        if operations1.name_ac == p.name:
            p.balance = p.balance + operations1.amount
            print(f"{p.name} {p.balance}")
    session.commit()



