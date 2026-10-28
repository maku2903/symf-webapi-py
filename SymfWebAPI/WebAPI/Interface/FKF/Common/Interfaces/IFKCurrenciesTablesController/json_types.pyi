from __future__ import annotations

from typing import Any, TypedDict

class CurrencyTableJSON(TypedDict):
    Id: int
    Date: str
    CurrencyId: int
    Table: str
    Description: str
    SaleCurrencyRate: float | int
    PurchaseCurrencyRate: float | int
