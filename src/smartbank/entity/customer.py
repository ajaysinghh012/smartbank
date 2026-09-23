from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from smartbank.entity.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[int] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    bank_id: Mapped[int] = mapped_column(ForeignKey("banks.id"), nullable=False)

    accounts: Mapped[list["Account"]] = relationship(back_populates="customer")
    # bank: Mapped["Bank"] = relationship(back_populates="customers")