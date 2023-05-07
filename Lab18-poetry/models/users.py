from sqlalchemy.orm import Mapped, mapped_column
from models import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    # id = Column(Integer, primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    points: Mapped[int]
