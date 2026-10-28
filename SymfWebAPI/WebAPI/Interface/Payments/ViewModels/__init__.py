from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumCancelationType,
    enumPaymentSubjectType,
    enumPaymentType,
    enumSettlementType,
)

class Payment(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    IssueDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    SettlementDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SubjectId: Optional[int]
    ReceivingPaymentRegistryId: Optional[int]
    Description: str
    Currency: str
    CurrencyRate: Decimal
    TotalValue: Decimal
    SettledValue: Decimal
    SettledValuePLN: Decimal
    PaymentRegistryId: int
    PaymentType: "enumPaymentType"
    SubjectType: "enumPaymentSubjectType"
    Positions: List["PaymentPosition"]

class PaymentListElement(BaseModel):
    Id: int
    DocumentNumber: str
    SubjectId: Optional[int]
    ReceivingPaymentRegistryId: Optional[int]
    PaymentRegistryId: Optional[int]
    IssueDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    SettlementDate: Optional[datetime]
    PaymentType: "enumPaymentType"
    SubjectType: "enumPaymentSubjectType"
    Currency: str
    CurrencyRate: Decimal
    TotalValue: Decimal
    SettledValue: Decimal
    SettledValuePLN: Decimal

class PaymentPosition(BaseModel):
    Id: int
    DocumentNumber: str
    ValuePLN: Decimal
    ValueSettlement: Decimal
    ValuePayment: Decimal
    CurrencyRateSettlement: Decimal
    CurrencyRatePayment: Decimal

class Settlement(BaseModel):
    Id: int
    DocumentId: Optional[int]
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    IssueDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    SettlementDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    ContractorId: Optional[int]
    SubjectId: Optional[int]
    Description: str
    Currency: str
    CurrencyRate: Decimal
    TotalValue: Decimal
    PaidValue: Decimal
    PaidValuePLN: Decimal
    LeftToPayValue: Decimal
    LeftToPayValuePLN: Decimal
    PaymentRegistryId: int
    SettlementType: "enumSettlementType"
    SubjectType: "enumPaymentSubjectType"
    Positions: List["SettlementPosition"]

class SettlementListElement(BaseModel):
    Id: int
    DocumentId: Optional[int]
    DocumentNumber: str
    ContractorId: Optional[int]
    SubjectId: Optional[int]
    IssueDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    SettlementDate: Optional[datetime]
    SettlementType: "enumSettlementType"
    SubjectType: "enumPaymentSubjectType"
    Currency: str
    CurrencyRate: Decimal
    TotalValue: Decimal
    PaidValue: Decimal
    PaidValuePLN: Decimal
    LeftToPayValue: Decimal
    LeftToPayValuePLN: Decimal

class SettlementPosition(BaseModel):
    Id: int
    DocumentNumber: str
    ValuePLN: Decimal
    ValueSettlement: Decimal
    ValuePayment: Decimal
    CurrencyRateSettlement: Decimal
    CurrencyRatePayment: Decimal
