

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from smartbank.entity.base import Base


class Atm(Base):
    __tablename__ = "atm"
    code: Mapped[int] = mapped_column(primary_key = True,nullable = False)
    location: Mapped[str] = mapped_column(nullable = False)
    balance: Mapped[float] = mapped_column(nullable = False)
    bank_id: Mapped[int] = mapped_column(ForeignKey("banks.id"), nullable=False)






