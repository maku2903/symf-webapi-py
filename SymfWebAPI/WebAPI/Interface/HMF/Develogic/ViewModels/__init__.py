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

class DevelogicAdvancePayment(BaseModel):
    Value: Decimal
    IsFinal: bool

class DevelogicContractInvoiceIssue(BaseModel):
    TypeCode: str
    Series: str
    CorrectionTypeCode: str
    CorrectionSeries: str
    NumberInSeries: Optional[int]
    ReservationType: Optional["enumDocumentReservationType"]
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: int
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    SalePriceType: "enumSalePriceType"
    SplitPayment: bool
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    Catalog: "SaleDocumentIssueCatalog"
    Kind: "SaleDocumentIssueKind"
    Marker: int
    ReceivedBy: str
    Note: Optional[str]
    Positions: List["DevelogicContractInvoiceIssuePosition"]

class DevelogicContractInvoiceIssuePosition(BaseModel):
    ContractPositionId: int
    Quantity: int
    Value: Decimal

class HMF_Develogic_ViewModels_DevelogicDocumentIssue(BaseModel):
    SubAccountNumber: str
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
DevelogicDocumentIssue = HMF_Develogic_ViewModels_DevelogicDocumentIssue

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
