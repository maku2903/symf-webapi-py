from __future__ import annotations

from pydantic import BaseModel

import importlib
from typing import TYPE_CHECKING
from typing import Any, List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import (
    DocumentAddress,
    PaymentRegistryBase,
    VatRateBase,
)
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumCancelationType,
    enumDocumentStatus,
    enumFiscalizationStatus,
    enumJPK_V7DocumentAttribute,
    enumManualSettledState,
    enumPriceKind,
    enumRDFStatus,
)

class PurchaseCorrectionIssue(BaseModel):
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
    Note: Optional[str]
    ForeignDocumentNumber: str
    VoluntarySplitPayment: bool
    WhiteList: bool

class PurchaseCorrectionIssueContractor(BaseModel):
    RecalculatePrices: bool
    Data: "PurchaseDocumentIssueContractorData"
    DeliveryAddressCode: str

class PurchaseCorrectionIssuePosition(BaseModel):
    No: Optional[int]
    VatRate: Optional["VatRateBase"]
    Elements: List["PurchaseCorrectionIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Duty: Decimal
    Excise: Decimal
    PriceValue: Decimal

class PurchaseCorrectionIssuePositionElement(BaseModel):
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Duty: Decimal
    Excise: Decimal
    PriceValue: Decimal

class PurchaseCorrectionPosition(BaseModel):
    No: int
    BeforeCorrection: "PurchaseCorrectionPositionElement"
    AfterCorrection: "PurchaseCorrectionPositionElement"

class PurchaseCorrectionPositionElement(BaseModel):
    Id: int
    SetHeaderId: Optional[int]
    ProductId: Optional[int]
    ProductCode: str
    Description: str
    Quantity: Decimal
    WrittenQuantity: Decimal
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    VatRate: Optional["VatRateBase"]
    PriceKind: "enumPriceKind"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal
    Duty: Decimal
    Excise: Decimal

class PurchaseDocumentCorrection(BaseModel):
    No: int
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    ReceiveDate: Optional[datetime]
    ForeignDocumentDate: Optional[datetime]

class PurchaseDocumentIssueCatalog(BaseModel):
    FullPath: str
    AddIfNotExist: bool

class PurchaseDocumentIssueContractor(BaseModel):
    Id: Optional[int]
    Code: str
    RecalculatePrices: bool
    Data: "PurchaseDocumentIssueContractorData"
    DeliveryAddressCode: str

class PurchaseDocumentIssueContractorData(BaseModel):
    Name: str
    NIP: Optional[str]
    Country: str
    City: Optional[str]
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]

class PurchaseDocumentIssueKind(BaseModel):
    Code: str
    AddIfNotExist: bool

class PurchaseDocumentIssuePosition(BaseModel):
    VatRate: Optional["VatRateBase"]
    Elements: List["PurchaseDocumentIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Duty: Decimal
    Excise: Decimal
    PriceValue: Decimal

class PurchaseDocumentIssuePositionElement(BaseModel):
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Duty: Decimal
    Excise: Decimal
    PriceValue: Decimal

class PurchaseDocumentListElement(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    IssueDate: Optional[datetime]
    PurchaseDate: Optional[datetime]
    ReceiveDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    ForeignDocumentDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SellerId: Optional[int]
    DelivererId: Optional[int]
    DepartmentId: int
    NetValuePLN: Decimal
    VatValuePLN: Decimal
    NetValue: Decimal
    GrossValue: Decimal
    Currency: str
    Description: str
    IsSmeProcedure: bool
    IsIssuedByBuyer: bool
    InvoiceKind: Any

class PurchaseDocumentPZ(BaseModel):
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    DelivererId: int

class PurchaseDocumentPosition(BaseModel):
    Id: int
    No: int
    SetHeaderId: Optional[int]
    ProductId: Optional[int]
    ProductCode: str
    Description: str
    Quantity: Decimal
    WrittenQuantity: Decimal
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    VatRate: Optional["VatRateBase"]
    PriceKind: "enumPriceKind"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal
    Duty: Decimal
    Excise: Decimal

class PurchaseDocumentStatus(BaseModel):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: "enumRDFStatus"
    ManualSettled: "enumManualSettledState"
    DocumentStatus: "enumDocumentStatus"
    DocumentStatusText: str

class Purchases_ViewModels_PurchaseCorrection(BaseModel):
    Id: int
    DocumentNumber: str
    MasterDocumentOid: Optional[int]
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    Fisacal: "enumFiscalizationStatus"
    eInvoice: bool
    SplitPayment: bool
    JPK_V7Attributes: "enumJPK_V7DocumentAttribute"
    IssueDate: Optional[datetime]
    ReceiveDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SellerId: Optional[int]
    SellerAddressId: Optional[int]
    DelivererId: Optional[int]
    DelivererAddressId: Optional[int]
    ReceivedBy: str
    DepartmentId: int
    PriceKind: "enumPriceKind"
    NetValuePLN: Decimal
    VatValuePLN: Decimal
    NetValue: Decimal
    GrossValue: Decimal
    Currency: str
    CurrencyRate: Decimal
    CurrencyRateCIT: Decimal
    PaymentRegistryId: int
    PaymentFormId: int
    CorrectionReason: str
    CatalogId: int
    KindId: int
    Marker: int
    Note: Optional[str]
    ForeignDocumentDate: Optional[datetime]
    PurchaseDate: Optional[datetime]
    VoluntarySplitPayment: bool
    WhiteList: bool
    ForeignDocumentNumber: str
    StatusKSeF: Optional[int]
    NumberKSeF: Optional[str]
    IssueDateKSeF: Optional[datetime]
    eArchiveId: Optional[str]
    IsSmeProcedure: bool
    IsIssuedByBuyer: bool
    InvoiceKind: Any
    Positions: List["PurchaseCorrectionPosition"]
    SellerAddress: "DocumentAddress"
    DelivererAddress: "DocumentAddress"
PurchaseCorrection = Purchases_ViewModels_PurchaseCorrection

class Purchases_ViewModels_PurchaseDocument(BaseModel):
    Id: int
    DocumentNumber: str
    ForeignDocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    Fisacal: "enumFiscalizationStatus"
    eInvoice: bool
    SplitPayment: bool
    VoluntarySplitPayment: bool
    WhiteList: bool
    JPK_V7Attributes: "enumJPK_V7DocumentAttribute"
    IssueDate: Optional[datetime]
    ReceiveDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    ForeignDocumentDate: Optional[datetime]
    PurchaseDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SellerId: Optional[int]
    SellerAddressId: Optional[int]
    DelivererId: Optional[int]
    DelivererAddressId: Optional[int]
    ReceivedBy: str
    DepartmentId: int
    PriceKind: "enumPriceKind"
    NetValuePLN: Decimal
    VatValuePLN: Decimal
    NetValue: Decimal
    GrossValue: Decimal
    Currency: str
    CurrencyRate: Decimal
    CurrencyRateCIT: Decimal
    PaymentRegistryId: int
    PaymentFormId: int
    Description: str
    CatalogId: int
    KindId: int
    Marker: int
    Note: Optional[str]
    StatusKSeF: Optional[int]
    NumberKSeF: Optional[str]
    IssueDateKSeF: Optional[datetime]
    InvoiceKind: Any
    eArchiveId: Optional[str]
    IsSmeProcedure: bool
    IsIssuedByBuyer: bool
    Positions: List["PurchaseDocumentPosition"]
    SellerAddress: "DocumentAddress"
    DelivererAddress: "DocumentAddress"
PurchaseDocument = Purchases_ViewModels_PurchaseDocument

class Purchases_ViewModels_PurchaseDocumentIssue(BaseModel):
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
    NumberKSeF: Optional[str]
    IssueDateKSeF: Optional[datetime]
    Seller: "PurchaseDocumentIssueContractor"
    Deliverer: "PurchaseDocumentIssueContractor"
    Positions: List["PurchaseDocumentIssuePosition"]
    Catalog: "PurchaseDocumentIssueCatalog"
    Kind: "PurchaseDocumentIssueKind"
    Marker: int
    ForeignDocumentNumber: str
    Description: str
    Note: Optional[str]
    IsSmeProcedure: bool
PurchaseDocumentIssue = Purchases_ViewModels_PurchaseDocumentIssue

_VERSIONED_CHILDREN = ['V2026_1', 'V2026_2']

_VERSIONED_EXPORTS = {
    'PurchaseCorrectionPositionElementResponeV2026_2': 'V2026_2',
    'PurchaseCorrectionPositionResponseV2026_2': 'V2026_2',
    'PurchaseCorrectionResponseV2026_2': 'V2026_2',
    'PurchaseDocumentPositionResponseV2026_2': 'V2026_2',
    'PurchaseDocumentResponseV2026_2': 'V2026_2',
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
    from . import V2026_2
    from .V2026_2 import PurchaseCorrectionPositionElementResponeV2026_2, PurchaseCorrectionPositionResponseV2026_2, PurchaseCorrectionResponseV2026_2, PurchaseDocumentPositionResponseV2026_2, PurchaseDocumentResponseV2026_2
