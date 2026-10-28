from __future__ import annotations

from typing import Any, TypedDict

class VatRateJSON(TypedDict):
    Description: str
    Value: float | int
    Active: bool
    DateTo: str | None
    DateFrom: str | None
    Type: Any
    Fiscal: bool
    RR: bool
    Id: int | None
    Code: str
