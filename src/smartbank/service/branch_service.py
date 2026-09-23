from sqlalchemy.orm import Session

from smartbank.domain.branch_request import BranchRequest
from smartbank.entity import Branch
from smartbank.entity.base import engine
from smartbank.repository import branch_repository


def find_all():
    with Session(engine) as session:
        return branch_repository.find_all(session)


def add(payload: BranchRequest):
    with Session(engine) as session:
        branch = Branch(name=payload.name, bank_id=payload.bank_id)
        branch_repository.create(session, branch)
        session.commit()


def update(branch_id: int, payload: BranchRequest):
    with Session(engine) as session:
        branch = branch_repository.find_by_id(session, branch_id)
        branch.name = payload.name
        branch.bank_id = payload.bank_id
        session.commit()


def remove(branch_id: int):
    with Session(engine) as session:
        branch = branch_repository.find_by_id(session, branch_id)
        branch_repository.delete(session, branch)
        session.commit()