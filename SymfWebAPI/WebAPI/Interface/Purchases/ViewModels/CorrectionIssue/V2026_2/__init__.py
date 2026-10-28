from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PaymentRegistryBase, VatRateBase
from SymfWebAPI.WebAPI.Interface.Enums import enumJPK_V7DocumentAttribute
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import (
    PurchaseCorrectionIssueContractor,
    PurchaseCorrectionIssuePosition,
    PurchaseCorrectionIssuePositionElement,
    PurchaseDocumentIssueCatalog,
    PurchaseDocumentIssueKind,
)

class PurchaseCorrectionIssuePositionRequestV2026_2(BaseModel):
    No: Optional[int]
    VatRate: "VatRateBase"
    Elements: List["PurchaseCorrectionIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Duty: Decimal
    Excise: Decimal
    PriceValue: Decimal

class PurchaseCorrectionIssueRequestV2026_2(BaseModel):
    IssueDateKSeF: Optional[datetime]
    NumberKSeF: str
    Positions: List["PurchaseCorrectionIssuePositionRequestV2026_2"]
    MasterDocumentId: Optional[int]
    MasterDocumentNumber: str
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    SplitPayment: bool
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    Seller: "PurchaseCorrectionIssueContractor"
    Deliverer: "PurchaseCorrectionIssueContractor"
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: Optional[int]
    IssueDate: Optional[datetime]
    ReceiveDate: Optional[datetime]
    PurchaseDate: Optional[datetime]
    ForeignDocumentDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    CurrencyRate: Optional[Decimal]
    Positions: List["PurchaseCorrectionIssuePosition"]
    Catalog: "PurchaseDocumentIssueCatalog"
    Kind: "PurchaseDocumentIssueKind"
    Marker: int
    CorrectionReason: str
    Note: str
    ForeignDocumentNumber: str
    VoluntarySplitPayment: bool
    WhiteList: bool
