from fastapi import APIRouter

from smartbank.domain.account_request import AccountRequest
from smartbank.domain.transfer import TransferRequest
from smartbank.service import account_service

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
)


@router.get("")
async def get_accounts():
    return account_service.find_all()


@router.get("/{account_id}")
async def get_account(account_id: int):
    return account_service.find_all()

@router.get("/{account_id}/transactions")
async def get_transactions(account_id: int, start_date):
    return account_service.find_all()


@router.post("")
async def add_account(payload: AccountRequest):
    account_service.add(payload)


@router.put("/transfer")
async def transfer(payload: TransferRequest):
    account_service.transfer(payload)


@router.delete("")
async def delete_account(account_id: int):
    account_service.remove_account(account_id)