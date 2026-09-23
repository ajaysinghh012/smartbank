from pydantic import BaseModel


class BankRequest(BaseModel):
    name: str
    address: str
