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
    SaleDocumentIssueDelivery,
    SaleDocumentIssueKind,
    SaleDocumentIssuePosition,
)

class SaleDocumentIssuePositionElementV2026_2(BaseModel):
    ServiceExport: bool
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Deliveries: List["SaleDocumentIssueDelivery"]
    OssService: Optional[bool]

class SaleDocumentIssueRequestV2026_2(BaseModel):
    Positions: List["SaleDocumentIssuePositionV2026_2"]
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
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
    Buyer: "SaleDocumentIssueContractor"
    Recipient: "SaleDocumentIssueContractor"
    Positions: List["SaleDocumentIssuePosition"]
    Catalog: "SaleDocumentIssueCatalog"
    Kind: "SaleDocumentIssueKind"
    Marker: int
    ReceivedBy: str
    Description: str
    Note: str
    OssProcedure: Optional[bool]
    OssShippingCountry: str
    OssDeliveryCountry: str
    TypeExternal: Optional[int]
    IdExternal: Optional[int]
    Id2External: str
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
