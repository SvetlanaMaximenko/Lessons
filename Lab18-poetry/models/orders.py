from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from models import Base


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    count: Mapped[int]