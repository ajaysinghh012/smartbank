from pydantic import BaseModel


class AccountRequest(BaseModel):
    phone_no: int
    email: str
    aadhaar: int
    balance: int
    bank_id: int
    customer_id: int
    branch_id: int
