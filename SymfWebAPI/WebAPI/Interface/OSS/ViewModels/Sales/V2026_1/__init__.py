from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PaymentRegistryBase
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumDocumentReservationType,
    enumPriceKind,
    enumSalePriceType,
)
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels.Common import OssCatalog, OssContractor, OssKind
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels.Sales import OssSaleDocumentPosition

class OSS_ViewModels_Sales_V2026_1_OssSaleDocument(BaseModel):
    ThirdPartyContractor: "OssContractor"
    Currency: str
    CurrencyRate: Decimal
    Country: str
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: int
    SalePriceType: "enumSalePriceType"
    PriceKind: "enumPriceKind"
    ReservationType: "enumDocumentReservationType"
    Buyer: "OssContractor"
    Recipient: "OssContractor"
    Catalog: "OssCatalog"
    Kind: "OssKind"
    Marker: int
    ReceivedBy: str
    Description: str
    Note: Optional[str]
    ShopOrderId: str
    ShippingCountry: str
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: Optional[str]
    Positions: List["OssSaleDocumentPosition"]
OssSaleDocument = OSS_ViewModels_Sales_V2026_1_OssSaleDocument
