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
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels.Common import (
    OssCatalog,
    OssContractor,
    OssDelivery,
    OssKind,
)

class OssOrder(BaseModel):
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: int
    Currency: str
    CurrencyRate: Decimal
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
    Country: str
    ShopOrderId: str
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: Optional[str]
    Positions: List["OssOrderPosition"]

class OssOrderPosition(BaseModel):
    Elements: List["OssOrderPositionElement"]
    ErpProductId: Optional[int]
    ShopProductId: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Description: str
    Deliveries: List["OssDelivery"]

class OssOrderPositionElement(BaseModel):
    ErpProductId: Optional[int]
    ShopProductId: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Description: str
    Deliveries: List["OssDelivery"]
