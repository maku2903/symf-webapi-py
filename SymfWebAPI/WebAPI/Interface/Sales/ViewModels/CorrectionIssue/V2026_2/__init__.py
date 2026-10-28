from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PaymentRegistryBase, VatRateBase
from SymfWebAPI.WebAPI.Interface.Enums import enumJPK_V7DocumentAttribute
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import (
    SaleCorrectionIssueContractor,
    SaleCorrectionIssuePosition,
    SaleCorrectionIssuePositionElement,
    SaleDocumentIssueCatalog,
    SaleDocumentIssueKind,
)

class SaleCorrectionIssueRequestPositionV2026_2(BaseModel):
    ServiceExport: Optional[bool]
    No: Optional[int]
    VatRate: "VatRateBase"
    Elements: List["SaleCorrectionIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal

class SaleCorrectionIssueRequestV2026_2(BaseModel):
    Positions: List["SaleCorrectionIssueRequestPositionV2026_2"]
    ThirdPartyContractor: "SaleCorrectionIssueContractor"
    MasterDocumentId: Optional[int]
    MasterDocumentNumber: str
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    SplitPayment: bool
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    Buyer: "SaleCorrectionIssueContractor"
    Recipient: "SaleCorrectionIssueContractor"
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: Optional[int]
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    CurrencyRate: Optional[Decimal]
    Positions: List["SaleCorrectionIssuePosition"]
    Catalog: "SaleDocumentIssueCatalog"
    Kind: "SaleDocumentIssueKind"
    Marker: int
    ReceivedBy: str
    CorrectionReason: str
    Note: str
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
