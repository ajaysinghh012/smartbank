from pydantic import BaseModel

from smartbank.domain.bank_response import BankResponse


class BanksResponse(BaseModel):
    banks: list[BankResponse]