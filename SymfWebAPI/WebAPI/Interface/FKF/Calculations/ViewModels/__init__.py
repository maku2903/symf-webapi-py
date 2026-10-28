from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    AccountBalanceTurnoverType,
    enumCalculationState,
    enumCalculationType,
    enumSideType,
    enumSubjectType,
)

class BalanceAndTurnoverFilterOptions(BaseModel):
    Account01: str
    Account02: str
    Account03: str
    Account04: str
    Account05: str
    Account06: str
    Account07: str
    Account08: str
    Account09: str
    Account10: str
    Account11: str
    Account12: str
    Account13: str
    Account14: str
    Account15: str
    Account16: str
    Account17: str
    Account18: str
    Account19: str
    Account20: str
    FromCalculationDate: Optional[datetime]
    ToCalculationDate: Optional[datetime]

class BalanceAndTurnoverListElement(BaseModel):
    Type: "AccountBalanceTurnoverType"
    YearId: int
    AccountFull: str
    Synthetic: int
    Analytic1: Optional[int]
    Analytic2: Optional[int]
    Analytic3: Optional[int]
    Analytic4: Optional[int]
    Analytic5: Optional[int]
    Account01: str
    Account02: str
    Account03: str
    Account04: str
    Account05: str
    Account06: str
    Account07: str
    Account08: str
    Account09: str
    Account10: str
    Account11: str
    Account12: str
    Account13: str
    Account14: str
    Account15: str
    Account16: str
    Account17: str
    Account18: str
    Account19: str
    Account20: str
    Value: Decimal
    BO: Decimal
    OR: Decimal
    Value1: Decimal
    Value2: Decimal
    Value3: Decimal
    Value4: Decimal
    Value5: Decimal
    Value6: Decimal
    Value7: Decimal
    Value8: Decimal
    Value9: Decimal
    Value10: Decimal
    Value11: Decimal
    Value12: Decimal
    Value13: Decimal
    Value14: Decimal
    Value15: Decimal
    Value16: Decimal
    Value17: Decimal
    Value18: Decimal
    Value19: Decimal
    Value20: Decimal
    Value21: Decimal
    Value22: Decimal
    Value23: Decimal
    CalculationDate: datetime

class CalculationFilterAccountOptions(BaseModel):
    Synthetic: int
    Analytic1: int
    Analytic2: int
    Analytic3: int
    Analytic4: int
    Analytic5: int

class CalculationFilterOptions(BaseModel):
    ForDay: Optional[datetime]
    DateFrom: Optional[datetime]
    DateTo: Optional[datetime]
    WithoutDate: Optional[bool]
    ValueFrom: Optional[Decimal]
    ValueTo: Optional[Decimal]
    Currency: str
    SubjectPosition: Optional[int]
    SubjectType: Optional["enumSubjectType"]
    DocumentName: str
    Type: Optional["enumCalculationType"]
    State: Optional["enumCalculationState"]
    Account: "CalculationFilterAccountOptions"
    GroupBy: List[str]
    OrderBy: List[str]

class CalculationListElement(BaseModel):
    DocumentId: int
    TransactionId: int
    SettlementId: int
    YearId: int
    Buffer: bool
    MaturityDate: datetime
    DocumentDate: datetime
    PeriodDate: datetime
    DaysToMaturity: int
    State: "enumCalculationState"
    Side: "enumSideType"
    RecordNumber: str
    DocumentNumber: str
    SubjectType: "enumSubjectType"
    SubjectPosition: int
    Account: str
    Currency: str
    CurrencyRate: Decimal
    ValuePLN: Decimal
    Value: Decimal
    Note: Optional[str]

class CalculationListElementGrouped(BaseModel):
    SubjectType: "enumSubjectType"
    SubjectPosition: int
    ValuePLN: Decimal
