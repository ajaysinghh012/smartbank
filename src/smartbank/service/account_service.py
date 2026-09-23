from sqlalchemy.orm import Session

from smartbank.domain.account_request import AccountRequest
from smartbank.domain.transfer import TransferRequest
from smartbank.entity import Account
from smartbank.entity.base import engine
from smartbank.repository import account_repository
from smartbank.repository.account_repository import find_by_account_no


def find_all():
    return account_repository.find_all()


def add(payload: AccountRequest):
    account = Account(
        phone_no=payload.phone_no,
        email=payload.email,
        aadhaar=payload.aadhaar,
        balance=payload.balance,
        bank_id=payload.bank_id,
        customer_id=payload.customer_id,
        branch_id=payload.branch_id,
    )
    account_repository.save(account)


def transfer(request: TransferRequest):
    with Session(engine) as session:
        from_account = find_by_account_no(session, request.from_account_no)
        to_account = find_by_account_no(session, request.to_account_no)

        if from_account.balance < request.amount:
            raise ValueError("Insufficient funds")

        from_account.balance -= request.amount
        to_account.balance += request.amount
        session.commit()


def remove_account(account_id: int):
    account_repository.remove_by_id(account_id)