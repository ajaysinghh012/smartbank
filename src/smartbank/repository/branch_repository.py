from sqlalchemy import select
from sqlalchemy.orm import Session

from smartbank.entity import Branch


def find_all(session: Session):
    return session.scalars(select(Branch)).all()


def find_by_id(session: Session, branch_id: int):
    return session.scalars(select(Branch).where(Branch.id == branch_id)).one()


def create(session: Session, branch: Branch) -> Branch:
    session.add(branch)
    return branch


def delete(session: Session, branch: Branch):
    session.delete(branch)
