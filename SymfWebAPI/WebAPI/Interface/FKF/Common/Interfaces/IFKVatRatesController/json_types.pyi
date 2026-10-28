from __future__ import annotations

from typing import Any, TypedDict

class VatRateJSON(TypedDict):
    Id: int
    Code: str
    Rate: str
    IsActive: bool
    DateFrom: str | None
    DateTo: str | None
