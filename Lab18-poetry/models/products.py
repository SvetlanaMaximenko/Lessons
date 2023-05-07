from sqlalchemy.orm import Mapped, mapped_column
from models import Base


class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    cost: Mapped[int]
    count: Mapped[int]
