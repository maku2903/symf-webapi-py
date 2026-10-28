from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PaymentRegistryBase
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumDocumentReservationType,
    enumJPK_V7DocumentAttribute,
    enumPriceKind,
    enumSalePriceType,
)
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import (
    SaleDocumentIssueCatalog,
    SaleDocumentIssueContractor,
    SaleDocumentIssueKind,
    SaleDocumentIssuePosition,
)

class Sales_ViewModels_DocumentIssue_V2026_1_SaleDocumentIssue(BaseModel):
    ThirdPartyContractor: "SaleDocumentIssueContractor"
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    Department: str
    Warehouse: str
    ReservationType: Optional["enumDocumentReservationType"]
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: int
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Currency: str
    CurrencyRate: Decimal
    CurrencyRateCIT: Decimal
    SalePriceType: "enumSalePriceType"
    PriceKind: "enumPriceKind"
    SplitPayment: bool
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    eArchiveId: Optional[str]
    NumberKSeF: Optional[str]
    IssueDateKSeF: Optional[datetime]
    Buyer: "SaleDocumentIssueContractor"
    Recipient: "SaleDocumentIssueContractor"
    Positions: List["SaleDocumentIssuePosition"]
    Catalog: "SaleDocumentIssueCatalog"
    Kind: "SaleDocumentIssueKind"
    Marker: int
    ReceivedBy: str
    Description: str
    Note: Optional[str]
    OssProcedure: Optional[bool]
    OssShippingCountry: str
    OssDeliveryCountry: str
    TypeExternal: Optional[int]
    IdExternal: Optional[int]
    Id2External: Optional[str]
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
SaleDocumentIssue = Sales_ViewModels_DocumentIssue_V2026_1_SaleDocumentIssue
