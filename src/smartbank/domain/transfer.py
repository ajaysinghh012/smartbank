from pydantic import BaseModel


class TransferRequest(BaseModel):
    from_account_no: int
    to_account_no: int
    amount: int
