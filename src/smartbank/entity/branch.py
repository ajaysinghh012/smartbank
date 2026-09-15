from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from smartbank.entity.base import Base


class Branch(Base):
    __tablename__ = "branches"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    bank_id: Mapped[int] = mapped_column(ForeignKey("banks.id"), nullable=False)
