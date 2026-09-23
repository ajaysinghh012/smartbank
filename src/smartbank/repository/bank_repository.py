from sqlalchemy import select
from sqlalchemy.orm import Session

from smartbank.entity import Bank


def create(session: Session, bank: Bank) -> Bank:
    session.add(bank)
    return bank


def find(session: Session):
    return session.scalars(select(Bank)).all()


def find_by_name(session: Session, name: str):
    return session.scalars(select(Bank).where(Bank.name == name)).all()


def find_by_id(session: Session, bank_id: int):
    return session.scalars(select(Bank).where(Bank.id == bank_id)).one()


def delete(session: Session, bank: Bank):
    session.delete(bank)
