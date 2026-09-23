from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from smartbank.entity.base import Base, engine
from sqlalchemy.orm import Session


class Bank(Base):
    __tablename__ = "banks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    address: Mapped[str]
    branches: Mapped[list["Branch"]] = relationship(back_populates="bank")

    def __repr__(self):
        return f"Bank(name='{self.name}', address='{self.address}')"