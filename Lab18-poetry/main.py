from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models.users import Users


def init_db():

    url = URL.create(
        drivername="postgresql",
        username="sveta",
        password="0310",
        host="127.0.0.1",
        database="sv"
    )

    engine = create_engine(url)
    connection = engine.connect()
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    user_ = Users(username="Ivan", password="123", points=0)
    with session.begin() as session:
        session.add(user_)
        session.commit()


if __name__ == '__main__':
    init_db()


