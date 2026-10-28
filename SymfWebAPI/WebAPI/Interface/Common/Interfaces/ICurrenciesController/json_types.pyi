from __future__ import annotations

from typing import Any, TypedDict

class CurrencyJSON(TypedDict):
    Id: int
    Shortcut: str
    Name: str
    Active: bool
