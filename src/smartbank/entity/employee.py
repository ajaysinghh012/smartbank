from sqlalchemy import ForeignKey
from smartbank.entity.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Employee(Base):
    __tablename__ = 'employee'
    employee_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    phone_no: Mapped[int] = mapped_column(nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("banks.id"), nullable=False)
    bank_id: Mapped[int] = mapped_column(ForeignKey("banks.id"), nullable=False)
    branch_id: Mapped[int] = mapped_column(ForeignKey("branches.id"), nullable=True)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"), nullable=False)

