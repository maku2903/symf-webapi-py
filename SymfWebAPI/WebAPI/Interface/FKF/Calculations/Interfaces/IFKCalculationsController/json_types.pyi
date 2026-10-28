from __future__ import annotations

from typing import Any, TypedDict

class CalculationListElementJSON(TypedDict):
    DocumentId: int
    TransactionId: int
    SettlementId: int
    YearId: int
    Buffer: bool
    MaturityDate: str
    DocumentDate: str
    PeriodDate: str
    DaysToMaturity: int
    State: Any
    Side: Any
    RecordNumber: str
    DocumentNumber: str
    SubjectType: Any
    SubjectPosition: int
    Account: str
    Currency: str
    CurrencyRate: float | int
    ValuePLN: float | int
    Value: float | int
    Note: str | None

class CalculationListElementGroupedJSON(TypedDict):
    SubjectType: Any
    SubjectPosition: int
    ValuePLN: float | int
