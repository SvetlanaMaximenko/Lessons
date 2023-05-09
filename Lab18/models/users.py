from sqlalchemy.orm import Mapped, mapped_column
from models import Base
import db


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    points: Mapped[int]

    @staticmethod
    def is_exist(username_: str):
        db.configure_engine()
        session = db.Session

        us = session.query(Users.username).all()
        print(us)


