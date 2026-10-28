from __future__ import annotations

from typing import Any, TypedDict

class PaymentFormJSON(TypedDict):
    Name: str
    Days: int
    Type: Any
    Active: bool
    Id: int | None
    Client: int
