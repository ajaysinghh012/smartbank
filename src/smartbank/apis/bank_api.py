from fastapi import APIRouter

from smartbank.domain.bank_request import BankRequest
from smartbank.service import bank_service


router = APIRouter(
    prefix="/banks",
    tags=["banks"],
)


@router.post("")
async def add_bank(payload: BankRequest):
    bank_service.add(payload)


@router.get("")
async def get_banks():
    return bank_service.find_all()


@router.put("/{bank_id}")
async def update_bank(bank_id: int, payload: BankRequest):
    bank_service.update(bank_id, payload)


@router.delete("/{bank_id}")
async def delete_bank(bank_id: int):
    bank_service.remove(bank_id)