from __future__ import annotations

from typing import Any, TypedDict

class CurrencyRateJSON(TypedDict):
    CurrencyId: int
    Date: str
    Rate: float | int
