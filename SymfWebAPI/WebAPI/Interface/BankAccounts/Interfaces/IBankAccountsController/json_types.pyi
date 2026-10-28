from __future__ import annotations

from typing import Any, TypedDict

class BankAccountJSON(TypedDict):
    Id: int
    AccountNumber: str | None
    BankName: str | None
    Active: bool
    Main: bool
    SWIFT_BIC: str
    WhiteList: bool | None
    WhiteListDate: str | None
