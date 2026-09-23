from sqlalchemy import select
from sqlalchemy.orm import Session

from smartbank.entity import Account
from smartbank.entity.base import engine


def find_all():
    with Session(engine) as session:
        return session.query(Account).all()


def find_by_account_no(session: Session, account_no: int):
    return session.query(Account).filter(Account.account_no == account_no).first()


def save(account: Account):
    with Session(engine) as session:
        session.add(account)
        session.commit()


def remove_by_id(account_id: int):
    with Session(engine) as session:
        account = session.scalars(
            select(Account).where(Account.account_no == account_id)
        ).one()
        session.delete(account)
        session.commit()