from __future__ import annotations

from typing import Any, TypedDict

class IncrementalSyncListElementJSON(TypedDict):
    Id: int
    ModifyType: Any
    ModifiedAt: str
    Object: Any

class PriceListJSON(TypedDict):
    Id: int
    Code: str
    Description: str
    Active: bool
    DateFrom: str | None
    DateTo: str | None
    DepartmentId: int | None
    IsPriceListHistoryEnabled: bool
    IsCurrencyPriceList: bool
    PriceListCurrency: str
    ForAllContractors: bool
    Priority: int
    MinimalPriority: int
    ConnectionType: Any
    Type: Any
    SpecificWeekdays: bool
    AvailableOnMonday: bool
    AvailableOnTuesday: bool
    AvailableOnWednesday: bool
    AvailableOnThursday: bool
    AvailableOnFriday: bool
    AvailableOnSaturday: bool
    AvailableOnSunday: bool
    Products: list[PriceListSubjectDetailsJSON]
    ProductKinds: list[PriceListSubjectDetailsJSON]
    Contractors: list[PriceListSubjectJSON]
    ContractorKinds: list[PriceListSubjectJSON]

class PriceListDetailsJSON(TypedDict):
    Value: float | int | None
    Currency: str
    PriceType: Any
    PriceKind: Any
    Type: Any

class PriceListListElementJSON(TypedDict):
    Id: int
    Code: str
    Active: bool
    DateFrom: str | None
    DateTo: str | None
    DepartmentId: int | None
    IsPriceListHistoryEnabled: bool
    IsCurrencyPriceList: bool
    PriceListCurrency: str

class PriceListSubjectJSON(TypedDict):
    Id: int
    Code: str
    Name: str

class PriceListSubjectDetailsJSON(TypedDict):
    Prices: list[PriceListDetailsJSON]
    Id: int
    Code: str
    Name: str
