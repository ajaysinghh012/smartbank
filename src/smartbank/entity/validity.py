from pydantic import BaseModel


class Validity(BaseModel):
    month: int
    year: int