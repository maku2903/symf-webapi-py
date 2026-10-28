from __future__ import annotations

from typing import Any, TypedDict

class AccountJSON(TypedDict):
    Synthetic: int
    Analytic1: int
    Analytic2: int
    Analytic3: int
    Analytic4: int
    Analytic5: int

class AccountChartElementJSON(TypedDict):
    Childs: list[AccountChartElementJSON]
    Id: int
    Code: str
    Name: str
    Level: int
    Account: str
    Account_Full: AccountJSON
    SubjectType: Any
    SubjectCode: str
    Settlement: bool

class AccountChartElementSimpleJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Level: int
    Account: str
    Account_Full: AccountJSON
    SubjectType: Any
    SubjectCode: str
    Settlement: bool
