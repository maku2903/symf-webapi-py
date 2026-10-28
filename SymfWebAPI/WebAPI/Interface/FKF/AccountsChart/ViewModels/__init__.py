from __future__ import annotations

from pydantic import BaseModel

from typing import List
from SymfWebAPI.WebAPI.Interface.Enums import enumSubjectType
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Account

class AccountChartElement(BaseModel):
    Childs: List["AccountChartElement"]
    Id: int
    Code: str
    Name: str
    Level: int
    Account: str
    Account_Full: "Account"
    SubjectType: "enumSubjectType"
    SubjectCode: str
    Settlement: bool

class AccountChartElementSimple(BaseModel):
    Id: int
    Code: str
    Name: str
    Level: int
    Account: str
    Account_Full: "Account"
    SubjectType: "enumSubjectType"
    SubjectCode: str
    Settlement: bool
