from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class Transaction(BaseModel):
    MaturityDate: datetime
    PaymentDate: datetime
    ValuePln: Decimal
    Value: Decimal
    SettledValuePln: Decimal
    SettledValue: Decimal
    LeftToSettledValuePln: Decimal
    LeftToSettledValue: Decimal
    MarkerId: Optional[int]
    Currency: str

class TransactionDocument(BaseModel):
    Code: str
    ValuePln: Decimal
    Value: Decimal
    ContractorId: int
    ContractorCode: str
    ContractorName: str
    ContractorNip: str
    SettledValuePln: Decimal
    SettledValue: Decimal
    LeftToSettledValuePln: Decimal
    LeftToSettledValue: Decimal
    Transactions: List["Transaction"]
