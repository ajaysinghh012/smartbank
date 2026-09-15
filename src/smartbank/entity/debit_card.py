# import datetime
# from typing import Any
#
# from pydantic import BaseModel
# from sqlalchemy.testing.schema import mapped_column
#
# from smartbank.entity.validity import Validity
from sqlalchemy.orm import Mapped, mapped_column

from smartbank.entity.base import Base


class DebitCard(Base):
    __tablename__ = "debit_cards"
    card_number: Mapped[int] = mapped_column(primary_key=True)
    valid_from: Mapped[int] = mapped_column(nullable=False)
    valid_to: Mapped[int] = mapped_column(nullable=False)
    cvv: Mapped[int] = mapped_column(nullable=False)
