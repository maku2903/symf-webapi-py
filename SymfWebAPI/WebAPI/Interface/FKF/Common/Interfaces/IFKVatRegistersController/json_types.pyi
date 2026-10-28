from __future__ import annotations

from typing import Any, TypedDict

class VatRegisterJSON(TypedDict):
    Id: int
    Name: str
    Type: Any
    Kind: Any
    Active: bool
    Correction: bool
    Period: int | None
