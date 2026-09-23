from pydantic import BaseModel


class CustomerRequest(BaseModel):
    name: str
    phone: int
    email: str
    bank_id: int