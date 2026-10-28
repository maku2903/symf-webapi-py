from __future__ import annotations

from typing import Any, TypedDict

class CompanyInfoJSON(TypedDict):
    Name: str
    NIP: str | None
    Address: str
    LicensesInfo: list[LicenceInfoJSON]

class LicenceInfoJSON(TypedDict):
    Module: str
    Feature: str
    ValueInt: int
    ValueDecimal: float | int
    ValueBool: bool
    ValueString: str
    ValueDateTime: str | None
    ValueObject: Any
