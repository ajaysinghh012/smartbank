from fastapi import APIRouter
from smartbank.domain.department_request import DepartmentRequest
from smartbank.service import department_service

router = APIRouter(
    prefix="/departments",
    tags=["departments"],
)


@router.get("")
async def get_departments():
    return department_service.find_all()


@router.post("")
async def create_department(payload: DepartmentRequest):
    department_service.add(payload)


@router.put("/{department_id}")
async def update_department(department_id: int, payload: DepartmentRequest):
    department_service.update_department(department_id, payload)


@router.delete("/{department_id}")
async def delete_department(department_id: int):
    department_service.remove_department(department_id)