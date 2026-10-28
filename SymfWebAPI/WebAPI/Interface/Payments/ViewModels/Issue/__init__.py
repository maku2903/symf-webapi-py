from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PaymentRegistryBase

class DocumentIssueSubject(BaseModel):
    Id: Optional[int]
    Code: str

class PaymentIssue(BaseModel):
    Series: str
    TypeCode: str
    Currency: str
    CurrencyRate: Decimal
    Note: Optional[str]
    TotalValue: Optional[Decimal]
    PaymentDate: Optional[datetime]
    Subject: "DocumentIssueSubject"
    PaymentRegistry: "PaymentRegistryBase"
    Settlements: List["DocumentIssueSettlement"]

class Payments_ViewModels_Issue_DocumentIssueSettlement(BaseModel):
    Id: Optional[int]
    DocumentId: Optional[int]
    DocumentNumber: str
    SettlementDate: Optional[datetime]
    Value: Decimal
DocumentIssueSettlement = Payments_ViewModels_Issue_DocumentIssueSettlement

class SettlementIssue(BaseModel):
    MaturityDate: Optional[datetime]
    Series: str
    TypeCode: str
    Currency: str
    CurrencyRate: Decimal
    Note: Optional[str]
    TotalValue: Optional[Decimal]
    PaymentDate: Optional[datetime]
    Subject: "DocumentIssueSubject"
    PaymentRegistry: "PaymentRegistryBase"
    Settlements: List["DocumentIssueSettlement"]
