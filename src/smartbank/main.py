from sqlalchemy import select
from sqlalchemy.orm import Session

from smartbank.entity.account import Account
from smartbank.entity.base import engine

with Session(engine) as session:
    session.scalars(select(Account))
