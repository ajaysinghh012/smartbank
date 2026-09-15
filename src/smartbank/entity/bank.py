
from sqlalchemy.orm import Mapped, mapped_column

from smartbank.entity.base import Base


class Bank(Base):
    __tablename__ = "banks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    address: Mapped[str]

