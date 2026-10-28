from __future__ import annotations

from typing import Any, TypedDict

class AgriculturalPromotionFundJSON(TypedDict):
    Code: str
    Active: bool
    Rate: float | int
    AccountFK: str
