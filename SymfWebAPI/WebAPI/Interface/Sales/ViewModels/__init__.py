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
    FiscalCommunicationInterfaceStatus,
    FiscalDeviceStatus,
    enumCancelationType,
    enumDocumentReservationType,
    enumDocumentStatus,
    enumFiscalizationStatus,
    enumJPK_V7DocumentAttribute,
    enumManualSettledState,
    enumPriceKind,
    enumRDFStatus,
    enumSalePriceType,
)

class AdvancePaymentOptions(BaseModel):
    Value: Decimal
    IsLast: bool
    AutomaticFillPositions: bool

class FiscalPrinterStatus(BaseModel):
    IsConnected: bool
    ChargerConnected: Optional[bool]
    CommandQueueEmpty: Optional[bool]
    PaperRunningOut: Optional[bool]
    CommunicationInterfaceStatus: Optional["FiscalCommunicationInterfaceStatus"]
    DeviceStatus: Optional["FiscalDeviceStatus"]

class FiscalizationResult(BaseModel):
    Success: bool
    ReceiptNumber: Optional[int]
    FiscalDeviceNo: str
    ErrorMessage: str

class SaleCorrection(BaseModel):
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
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    BuyerId: Optional[int]
    BuyerAddressId: Optional[int]
    RecipientId: Optional[int]
    RecipientAddressId: Optional[int]
    ThirdPartyContractorId: Optional[int]
    ThirdPartyContractorAddressId: Optional[int]
    ReceivedBy: str
    DepartmentId: int
    PriceKind: "enumPriceKind"
    SalePriceType: "enumSalePriceType"
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
    StatusKSeF: Optional[int]
    NumberKSeF: Optional[str]
    IssueDateKSeF: Optional[datetime]
    eArchiveId: Optional[str]
    Positions: List["SaleCorrectionPosition"]
    BuyerAddress: "DocumentAddress"
    RecipientAddress: "DocumentAddress"
    ThirdPartyContractorAddress: "DocumentAddress"
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
    InvoiceKind: Any

class SaleCorrectionIssueContractor(BaseModel):
    RecalculatePrices: bool
    Data: "SaleDocumentIssueContractorData"
    DeliveryAddressCode: str

class SaleCorrectionIssuePosition(BaseModel):
    No: Optional[int]
    VatRate: Optional["VatRateBase"]
    Elements: List["SaleCorrectionIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    ServiceExport: Optional[bool]

class SaleCorrectionIssuePositionElement(BaseModel):
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    ServiceExport: Optional[bool]

class SaleCorrectionPosition(BaseModel):
    No: int
    BeforeCorrection: "SaleCorrectionPositionElement"
    AfterCorrection: "SaleCorrectionPositionElement"

class SaleCorrectionPositionElement(BaseModel):
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
    SalePriceType: "enumSalePriceType"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal

class SaleDocument(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    Fisacal: "enumFiscalizationStatus"
    eInvoice: bool
    SplitPayment: bool
    JPK_V7Attributes: "enumJPK_V7DocumentAttribute"
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    BuyerId: Optional[int]
    BuyerAddressId: Optional[int]
    RecipientId: Optional[int]
    RecipientAddressId: Optional[int]
    ThirdPartyContractorId: Optional[int]
    ThirdPartyContractorAddressId: Optional[int]
    ReceivedBy: str
    DepartmentId: int
    PriceKind: "enumPriceKind"
    SalePriceType: "enumSalePriceType"
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
    eArchiveId: Optional[str]
    Positions: List["SaleDocumentPosition"]
    BuyerAddress: "DocumentAddress"
    RecipientAddress: "DocumentAddress"
    ThirdPartyContractorAddress: "DocumentAddress"
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: Optional[str]
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
    InvoiceKind: Any

class SaleDocumentCorrection(BaseModel):
    No: int
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]

class SaleDocumentIssueCatalog(BaseModel):
    FullPath: str
    AddIfNotExist: bool

class SaleDocumentIssueContractor(BaseModel):
    Id: Optional[int]
    Code: str
    RecalculatePrices: bool
    Data: "SaleDocumentIssueContractorData"
    DeliveryAddressCode: str

class SaleDocumentIssueContractorData(BaseModel):
    Name: str
    NIP: Optional[str]
    Country: str
    City: Optional[str]
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]

class SaleDocumentIssueDelivery(BaseModel):
    Id: Optional[int]
    Code: str
    Quantity: Decimal

class SaleDocumentIssueKind(BaseModel):
    Code: str
    AddIfNotExist: bool

class SaleDocumentIssuePosition(BaseModel):
    VatRate: Optional["VatRateBase"]
    Elements: List["SaleDocumentIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Deliveries: List["SaleDocumentIssueDelivery"]
    OssService: Optional[bool]

class SaleDocumentIssuePositionElement(BaseModel):
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Deliveries: List["SaleDocumentIssueDelivery"]
    OssService: Optional[bool]

class SaleDocumentListElement(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: int
    Settled: int
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    BuyerId: Optional[int]
    ThirdPartyContractorId: Optional[int]
    RecipientId: Optional[int]
    DepartmentId: int
    NetValuePLN: Decimal
    VatValuePLN: Decimal
    NetValue: Decimal
    GrossValue: Decimal
    IncomeValue: Decimal
    Currency: str
    Description: str
    IsSmeProcedure: bool
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: Optional[str]
    InvoiceKind: Any

class SaleDocumentPosition(BaseModel):
    Id: int
    No: int
    SetHeaderId: Optional[int]
    ProductId: Optional[int]
    ProductCode: str
    Description: str
    Quantity: Decimal
    WrittenQuantity: Decimal
    EnteredQuantity: Decimal
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    EnteredUnitOfMeasurement: str
    VatRate: Optional["VatRateBase"]
    PriceKind: "enumPriceKind"
    SalePriceType: "enumSalePriceType"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal

class SaleDocumentStatus(BaseModel):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: "enumRDFStatus"
    ManualSettled: "enumManualSettledState"
    DocumentStatus: "enumDocumentStatus"
    DocumentStatusText: str

class SaleDocumentWZ(BaseModel):
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    RecipientId: int

class SaleDocumentZMO(BaseModel):
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    BuyerId: int
    RecipientId: int

class Sales_ViewModels_SaleCorrectionIssue(BaseModel):
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
    Note: Optional[str]
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
SaleCorrectionIssue = Sales_ViewModels_SaleCorrectionIssue

class Sales_ViewModels_SaleDocumentIssue(BaseModel):
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
SaleDocumentIssue = Sales_ViewModels_SaleDocumentIssue

_VERSIONED_CHILDREN = ['V2026_2']

_VERSIONED_EXPORTS = {
    'SaleCorrectionPositionElementV2026_2': 'V2026_2',
    'SaleCorrectionPositionElementV2026_2WithServiceExport': 'V2026_2',
    'SaleCorrectionResponsePositionV2026_2': 'V2026_2',
    'SaleCorrectionResponseV2026_2': 'V2026_2',
    'SaleDocumentPositionV2026_2': 'V2026_2',
    'SaleDocumentResponseV2026_2': 'V2026_2',
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
    from . import V2026_2
    from .V2026_2 import SaleCorrectionPositionElementV2026_2, SaleCorrectionPositionElementV2026_2WithServiceExport, SaleCorrectionResponsePositionV2026_2, SaleCorrectionResponseV2026_2, SaleDocumentPositionV2026_2, SaleDocumentResponseV2026_2
