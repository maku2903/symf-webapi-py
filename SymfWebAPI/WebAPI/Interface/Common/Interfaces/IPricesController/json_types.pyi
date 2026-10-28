from __future__ import annotations

from typing import Any, TypedDict

class PriceTypeJSON(TypedDict):
    Type: Any
    Code: str
    Name: str
    Kind: Any
    Active: bool
