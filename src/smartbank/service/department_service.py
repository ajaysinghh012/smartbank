from smartbank.domain.department_request import DepartmentRequest
from smartbank.entity import Department
from smartbank.repository import department_repository


def find_all():
    return department_repository.find_all()


def add(payload: DepartmentRequest):
    department = Department(
        name=payload.name,
        bank_id=payload.bank_id,
    )
    department_repository.save(department)


def update_department(department_id: int, payload: DepartmentRequest):
    department_repository.update(department_id, payload.name, payload.bank_id)


def remove_department(department_id: int):
    department_repository.delete_department(department_id)