from sqlalchemy  import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from smartbank.entity.base import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    bank_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("banks.id"), nullable=False)

    # bank: Mapped["Bank"] = relationship(back_populates="departments")