from __future__ import annotations

from pydantic import BaseModel

from typing import Optional
from datetime import datetime

class BankAccount(BaseModel):
    Id: int
    AccountNumber: Optional[str]
    BankName: Optional[str]
    Active: bool
    Main: bool
    SWIFT_BIC: str
    WhiteList: Optional[bool]
    WhiteListDate: Optional[datetime]
