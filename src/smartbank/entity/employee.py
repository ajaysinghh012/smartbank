from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    phone_no: str
    address: str
