from __future__ import annotations

from typing import Any, TypedDict

class PaymentRegistryJSON(TypedDict):
    Name: str
    Type: Any
    DefaultPaymentFormId: int | None
    BankName: str | None
    BankAccountId: int
    Id: int | None
    Code: str
    AccountNumber: str | None
