from fastapi import APIRouter

from smartbank.domain.branch_request import BranchRequest
from smartbank.service import branch_service

router = APIRouter(
    prefix="/branches",
    tags=["branches"],
)


@router.get("")
async def get_branches():
    return branch_service.find_all()


@router.post("")
async def add_branch(payload: BranchRequest):
    branch_service.add(payload)


@router.put("/{branch_id}")
async def update_branch(branch_id: int, payload: BranchRequest):
    branch_service.update(branch_id, payload)


@router.delete("/{branch_id}")
async def delete_branch(branch_id: int):
    branch_service.remove(branch_id)