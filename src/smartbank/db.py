from smartbank.entity.base import Base, engine
from smartbank.entity.bank import Bank
from smartbank.entity.branch import Branch
from smartbank.entity.employee import Employee

Base.metadata.create_all(engine)
print("Tables created (or already exist).")
