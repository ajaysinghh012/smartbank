from sqlalchemy.orm import Session

from smartbank.domain.bank_request import BankRequest
from smartbank.domain.bank_response import BankResponse
from smartbank.domain.banks_response import BanksResponse
from smartbank.entity import Bank
from smartbank.entity.base import engine
from smartbank.repository import bank_repository


def add(payload: BankRequest):
    with Session(engine) as session:
        bank = Bank(name=payload.name, address=payload.address)
        bank_repository.create(session, bank)
        session.commit()


def find_all():
    with Session(engine) as session:
        banks = bank_repository.find(session)
        response = [BankResponse(id=bank.id, name=bank.name, address=bank.address) for bank in banks]
        return BanksResponse(banks=response)


def update(bank_id: int, payload: BankRequest):
    with Session(engine) as session:
        bank = bank_repository.find_by_id(session, bank_id)
        bank.name = payload.name
        bank.address = payload.address
        session.commit()


def remove(bank_id: int):
    with Session(engine) as session:
        bank = bank_repository.find_by_id(session, bank_id)
        bank_repository.delete(session, bank)
        session.commit()