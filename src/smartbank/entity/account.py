
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from smartbank.entity.base import Base


class Account(Base):
    __tablename__ = 'accounts'
    account_no: Mapped[str] = mapped_column(primary_key=True)
    phone_no: Mapped[int] = mapped_column(nullable = False )
    email: Mapped[str] = mapped_column(nullable = False )
    aadhaar: Mapped[int] = mapped_column(nullable = False)
    bank_id: Mapped[int] = mapped_column(ForeignKey("banks.id"), nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)




