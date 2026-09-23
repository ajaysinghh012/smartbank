from sqlalchemy import select

from smartbank.entity.customer import Customer
from smartbank.entity.base import engine
from sqlalchemy.orm import Session


def find_all():
    with Session(engine) as session:
        return session.query(Customer).all()


def save(customer: Customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()


def update(customer_id: int, name: str, phone: int, email: str, bank_id: int):
    with Session(engine) as session:
        customer = session.scalars(select(Customer).where(Customer.id == customer_id)).one()
        customer.name = name
        customer.phone = phone
        customer.email = email
        customer.bank_id = bank_id
        session.commit()


def delete_customer(customer_id: int):
    with Session(engine) as session:
        customer = session.scalars(select(Customer).where(Customer.id == customer_id)).one()
        session.delete(customer)
        session.commit()