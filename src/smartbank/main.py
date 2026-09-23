# from sqlalchemy import select
# from sqlalchemy.orm import Session
#
# from smartbank.entity.base import engine
# from smartbank.entity.bank import Bank
# from smartbank.entity.branch import Branch
#
# with Session(engine) as session:
#     existing = session.scalar(select(Bank).where(Bank.name == "HDFC Bank"))
#     if existing:
#         print("HDFC Bank already exists, skipping insert.")
#     else:
#         bank = Bank(name="HDFC Bank", address="Mumbai, India")
#         bank.branches.append(Branch(name="HDFC01"))
#         session.add(bank)
#         session.commit()
#         print("Inserted HDFC Bank and branch.")

from smartbank.apis.app import app