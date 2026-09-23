from fastapi import APIRouter
from smartbank.domain.customer_request import CustomerRequest
from smartbank.service import customer_service

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
)


@router.get("")
async def get_customers():
    return customer_service.find_all()


@router.post("")
async def add_customer(payload: CustomerRequest):
    customer_service.add(payload)


@router.put("/{customer_id}")
async def update_customer(customer_id: int, payload: CustomerRequest):
    customer_service.update_customer(customer_id, payload)


@router.delete("/{customer_id}")
async def delete_customer(customer_id: int):
    customer_service.remove_customer(customer_id)