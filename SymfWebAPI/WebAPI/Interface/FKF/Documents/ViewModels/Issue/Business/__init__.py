from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumAccountingSchemePositionType,
    enumFKSplitPaymentType,
    enumJPK_V7ProductGroup,
)

class BusinessDocumentCorrectionIssue(BaseModel):
    DocumentNumber: str
    DocumentDate: datetime

class BusinessDocumentIssue(BaseModel):
    Marker: int
    DocumentType: str
    DocumentTypeFeature: str
    AccountingScheme: str
    DocumentNumber: str
    Description: str
    Contractor: str
    ContractorPosition: Optional[int]
    ContractorType: str
    Department: str
    IssueDate: Optional[datetime]
    DocumentDate: Optional[datetime]
    OperationDate: Optional[datetime]
    ReceiptDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Currency: str
    CurrencyRate: Optional[Decimal]
    ForManualVerification: bool
    SetTransactionMarker: bool
    SplitPaymentType: "enumFKSplitPaymentType"
    Positions: List["BusinessDocumentPositionIssue"]
    Corrections: List["BusinessDocumentCorrectionIssue"]

class BusinessDocumentPositionIssue(BaseModel):
    PositionType: Optional["enumAccountingSchemePositionType"]
    JPK_V7ProductGroups: Optional["enumJPK_V7ProductGroup"]
    VatRate: Optional[str]
    Product: str
    ProductType: str
    CostType: str
    Description: str
    GrossValue: Decimal
    NetValue: Decimal
    VatValue: Decimal
    GrossValuePLN: Decimal
    NetValuePLN: Decimal
    VatValuePLN: Decimal
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
