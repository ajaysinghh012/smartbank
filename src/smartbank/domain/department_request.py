from pydantic import BaseModel


class DepartmentRequest(BaseModel):
    name: str
    bank_id: int