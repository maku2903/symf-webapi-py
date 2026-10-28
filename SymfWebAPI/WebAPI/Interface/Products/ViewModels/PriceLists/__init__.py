from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumPriceFactorType,
    enumPriceKind,
    enumPriceListConnectionType,
    enumSalePriceType,
)

class PriceList(BaseModel):
    Id: int
    Code: str
    Description: str
    Active: bool
    DateFrom: Optional[datetime]
    DateTo: Optional[datetime]
    DepartmentId: Optional[int]
    IsPriceListHistoryEnabled: bool
    IsCurrencyPriceList: bool
    PriceListCurrency: str
    ForAllContractors: bool
    Priority: int
    MinimalPriority: int
    ConnectionType: "enumPriceListConnectionType"
    Type: "enumPriceFactorType"
    SpecificWeekdays: bool
    AvailableOnMonday: bool
    AvailableOnTuesday: bool
    AvailableOnWednesday: bool
    AvailableOnThursday: bool
    AvailableOnFriday: bool
    AvailableOnSaturday: bool
    AvailableOnSunday: bool
    Products: List["PriceListSubjectDetails"]
    ProductKinds: List["PriceListSubjectDetails"]
    Contractors: List["PriceListSubject"]
    ContractorKinds: List["PriceListSubject"]

class PriceListDetails(BaseModel):
    Value: Optional[Decimal]
    Currency: str
    PriceType: "enumSalePriceType"
    PriceKind: "enumPriceKind"
    Type: "enumPriceFactorType"

class PriceListListElement(BaseModel):
    Id: int
    Code: str
    Active: bool
    DateFrom: Optional[datetime]
    DateTo: Optional[datetime]
    DepartmentId: Optional[int]
    IsPriceListHistoryEnabled: bool
    IsCurrencyPriceList: bool
    PriceListCurrency: str

class PriceListSubject(BaseModel):
    Id: int
    Code: str
    Name: str

class PriceListSubjectDetails(BaseModel):
    Prices: List["PriceListDetails"]
    Id: int
    Code: str
    Name: str
