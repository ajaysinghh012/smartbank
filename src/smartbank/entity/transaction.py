from smartbank.entity.base import Base
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column


class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id: Mapped[int] = mapped_column(primary_key=True)
    money: Mapped[float] = mapped_column(nullable=False)
    txn_type: Mapped[str] = mapped_column(nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.account_no'), nullable=False)
    counterparty_id: Mapped[int] = mapped_column(ForeignKey('accounts.account_no'), nullable=False)

    __table_args__ = (
        CheckConstraint("txn_type IN ('sent', 'received')", name='ck_txn_type'),
    )