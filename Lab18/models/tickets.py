from sqlalchemy.orm import Mapped, mapped_column
from models import Base
from sqlalchemy import ForeignKey


class Tickets(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[str]
    available: Mapped[bool]
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
