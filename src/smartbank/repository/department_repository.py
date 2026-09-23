from sqlalchemy import select
from sqlalchemy.orm import Session

from smartbank.entity import Department
from smartbank.entity.base import engine


def find_all():
    with Session(engine) as session:
        return session.query(Department).all()


def save(department: Department):
    with Session(engine) as session:
        session.add(department)
        session.commit()


def find_by_id(session: Session, department_id: int):
    return session.scalars(select(Department).where(Department.id == department_id)).one()


def update(department_id: int, name: str, bank_id: int):
    with Session(engine) as session:
        department = session.scalars(select(Department).where(Department.id == department_id)).one()
        department.name = name
        department.bank_id = bank_id
        session.commit()


def delete_department(department_id: int):
    with Session(engine) as session:
        department = session.scalars(select(Department).where(Department.id == department_id)).one()
        session.delete(department)
        session.commit()