from __future__ import annotations

from pydantic import BaseModel

from typing import Any, List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType

class CompanyInfo(BaseModel):
    Name: str
    NIP: Optional[str]
    Address: str
    LicensesInfo: List["LicenceInfo"]

class InstanceInfo(BaseModel):
    Seed: str
    ServerName: str
    DatabaseName: str
    Firm: str
    User: str

class LicenceInfo(BaseModel):
    Module: str
    Feature: str
    ValueInt: int
    ValueDecimal: Decimal
    ValueBool: bool
    ValueString: str
    ValueDateTime: Optional[datetime]
    ValueObject: Any

class LoadedModuleInfo(BaseModel):
    AssemblyName: str
    ModuleName: str
    ModuleVersion: str

class Page_1(BaseModel):
    NextPage: Optional[str]
    PreviousPage: Optional[str]
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: "enumOrderByType"
    Data: List[Any]
Page = Page_1

class Ping(BaseModel):
    OpenSessionsNumber: int
    ActiveHMFInfo: List["InstanceInfo"]
    ActiveITGInfo: List["InstanceInfo"]
    LoadedModuleInfo: List["LoadedModuleInfo"]

class SessionInformation(BaseModel):
    Token: str
    DeviceName: str
    RegisterTime: datetime
    ExpireTime: datetime
    TotalSessionsCount: int
