from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import enumFKSplitPaymentType
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Issue.Business import (
    BusinessDocumentCorrectionIssue,
    BusinessDocumentPositionIssue,
)

class BusinessDocumentIssueV2026_2Request(BaseModel):
    BuyerOrSellerContractorPosition: Optional[int]
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
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
