from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select

from smartbank.entity.base import Base, engine
from smartbank.entity.bank import Bank
from smartbank.entity.branch import Branch
from smartbank.entity.employee import Employee

Base.metadata.create_all(engine)

with Session(engine) as session:
    banks = session.scalars(select(Bank)).all()
    print(banks)
    # bank = Bank(name="HDFC Bank", address="Mumbai, India")
    # bank.branches.append(Branch(name="HDFC01"))
    # session.add(bank)
    # session.commit()