from pydantic import BaseModel


class BranchRequest(BaseModel):
    name: str
    bank_id: int