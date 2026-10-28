from __future__ import annotations

from typing import Any, TypedDict

class SettlementJSON(TypedDict):
    Id: int
    DocumentId: int | None
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    IssueDate: str | None
    MaturityDate: str | None
    SettlementDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    ContractorId: int | None
    SubjectId: int | None
    Description: str
    Currency: str
    CurrencyRate: float | int
    TotalValue: float | int
    PaidValue: float | int
    PaidValuePLN: float | int
    LeftToPayValue: float | int
    LeftToPayValuePLN: float | int
    PaymentRegistryId: int
    SettlementType: Any
    SubjectType: Any
    Positions: list[SettlementPositionJSON]

class SettlementListElementJSON(TypedDict):
    Id: int
    DocumentId: int | None
    DocumentNumber: str
    ContractorId: int | None
    SubjectId: int | None
    IssueDate: str | None
    MaturityDate: str | None
    SettlementDate: str | None
    SettlementType: Any
    SubjectType: Any
    Currency: str
    CurrencyRate: float | int
    TotalValue: float | int
    PaidValue: float | int
    PaidValuePLN: float | int
    LeftToPayValue: float | int
    LeftToPayValuePLN: float | int

class SettlementPositionJSON(TypedDict):
    Id: int
    DocumentNumber: str
    ValuePLN: float | int
    ValueSettlement: float | int
    ValuePayment: float | int
    CurrencyRateSettlement: float | int
    CurrencyRatePayment: float | int
