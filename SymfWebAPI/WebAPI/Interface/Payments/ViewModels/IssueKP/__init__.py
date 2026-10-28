from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PaymentRegistryBase

class PaymentKPIssue(BaseModel):
    Series: str
    TypeCode: str
    Currency: str
    CurrencyRate: Decimal
    Note: Optional[str]
    TotalValue: Optional[Decimal]
    PaymentDate: Optional[datetime]
    Contractor: "PaymentKPIssueContractor"
    PaymentRegistry: "PaymentRegistryBase"
    Invoices: List["PaymentKPIssueInvoice"]

class PaymentKPIssueContractor(BaseModel):
    Id: Optional[int]
    Code: str

class PaymentKPIssueInvoice(BaseModel):
    Id: Optional[int]
    DocumentNumber: str
    SettlementDate: Optional[datetime]
    Value: Decimal
