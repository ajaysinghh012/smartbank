from sqlalchemy.orm import Session
from smartbank.entity.base import engine
from smartbank.entity.bank import Bank
from smartbank.entity.account import Account


def seed():
    with Session(engine) as session:
    a1 = Account(
        account_no="1",

    )