from pydantic import BaseModel


class BankResponse(BaseModel):
    id: int
    name: str
    address: str