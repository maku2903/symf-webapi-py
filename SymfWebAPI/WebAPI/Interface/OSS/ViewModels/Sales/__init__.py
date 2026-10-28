from __future__ import annotations

from pydantic import BaseModel

import importlib
from typing import TYPE_CHECKING
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

class OSS_ViewModels_Sales_OssSaleDocument(BaseModel):
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
OssSaleDocument = OSS_ViewModels_Sales_OssSaleDocument

class OssDomesticSaleDocument(BaseModel):
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

class OssSaleDocumentPosition(BaseModel):
    Elements: List["OssSaleDocumentPositionElement"]
    ErpProductId: Optional[int]
    ShopProductId: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Description: str
    Deliveries: List["OssDelivery"]
    OssService: Optional[bool]

class OssSaleDocumentPositionElement(BaseModel):
    ErpProductId: Optional[int]
    ShopProductId: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Description: str
    Deliveries: List["OssDelivery"]
    OssService: Optional[bool]

_VERSIONED_CHILDREN = ['V2026_1']

_VERSIONED_EXPORTS = {
}

def __getattr__(name: str):
    if name in _VERSIONED_CHILDREN:
        value = importlib.import_module(f".{name}", __name__)
        globals()[name] = value
        return value
    child_name = _VERSIONED_EXPORTS.get(name)
    if child_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = importlib.import_module(f".{child_name}", __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value

def __dir__():
    return sorted(set(_VERSIONED_CHILDREN) | set(_VERSIONED_EXPORTS) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import V2026_1
