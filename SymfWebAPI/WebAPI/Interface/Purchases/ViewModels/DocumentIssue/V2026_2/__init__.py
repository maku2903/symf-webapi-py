from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PaymentRegistryBase, VatRateBase
from SymfWebAPI.WebAPI.Interface.Enums import enumJPK_V7DocumentAttribute, enumPriceKind
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import (
    PurchaseDocumentIssueCatalog,
    PurchaseDocumentIssueContractor,
    PurchaseDocumentIssueKind,
    PurchaseDocumentIssuePosition,
    PurchaseDocumentIssuePositionElement,
)

class PurchaseDocumentIssuePositionRequestV2026_2(BaseModel):
    ReverseCharge: Optional[bool]
    VatRate: "VatRateBase"
    Elements: List["PurchaseDocumentIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Duty: Decimal
    Excise: Decimal
    PriceValue: Decimal

class PurchaseDocumentIssueRequestV2026_2(BaseModel):
    Positions: List["PurchaseDocumentIssuePositionRequestV2026_2"]
    ThirdPartyContractor: "PurchaseDocumentIssueContractor"
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    Department: str
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: int
    IssueDate: Optional[datetime]
    ReceiveDate: Optional[datetime]
    PurchaseDate: Optional[datetime]
    ForeignDocumentDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Currency: str
    CurrencyRate: Decimal
    CurrencyRateCIT: Decimal
    PriceKind: "enumPriceKind"
    SplitPayment: bool
    VoluntarySplitPayment: bool
    WhiteList: bool
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    eArchiveId: Optional[str]
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
    Seller: "PurchaseDocumentIssueContractor"
    Deliverer: "PurchaseDocumentIssueContractor"
    Positions: List["PurchaseDocumentIssuePosition"]
    Catalog: "PurchaseDocumentIssueCatalog"
    Kind: "PurchaseDocumentIssueKind"
    Marker: int
    ForeignDocumentNumber: str
    Description: str
    Note: str
    IsSmeProcedure: bool
