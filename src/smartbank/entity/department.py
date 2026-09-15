from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from smartbank.entity.base import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str]
    name: Mapped[str]

    __table_args__ = (UniqueConstraint("code", name="uq_department_code"),)
