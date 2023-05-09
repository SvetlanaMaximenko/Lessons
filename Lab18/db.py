from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# url = URL.create(
#         drivername="postgresql",
#         username="sveta",
#         password="0310",
#         host="127.0.0.1",
#         database="sv"
#     )
#
# global engine
# engine = create_engine(url)
# connection = engine.connect()
# Base.metadata.create_all(engine)
# session = sessionmaker(engine)
#
#

engine = None
Session = sessionmaker()


def configure_engine():
    global engine
    if engine is None:
        engine = create_engine("postgresql://sveta:0310@localhost:5432/sv")
        Session.configure(bind=engine)

