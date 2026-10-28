from __future__ import annotations

from typing import Any, TypedDict

class TaxOfficeJSON(TypedDict):
    Id: int
    Position: int
    Code: str
    Name: str
    City: str | None
    IsActive: bool
