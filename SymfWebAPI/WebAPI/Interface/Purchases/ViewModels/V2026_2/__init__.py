from __future__ import annotations

from pydantic import BaseModel

from typing import Any, List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentAddress, VatRateBase
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumCancelationType,
    enumFiscalizationStatus,
    enumJPK_V7DocumentAttribute,
    enumPriceKind,
)
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import (
    PurchaseCorrectionPosition,
    PurchaseCorrectionPositionElement,
    PurchaseDocumentPosition,
)

class PurchaseCorrectionPositionElementResponeV2026_2(BaseModel):
    ReverseCharge: bool
    Id: int
    SetHeaderId: Optional[int]
    ProductId: Optional[int]
    ProductCode: str
    Description: str
    Quantity: Decimal
    WrittenQuantity: Decimal
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    VatRate: "VatRateBase"
    PriceKind: "enumPriceKind"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal
    Duty: Decimal
    Excise: Decimal

class PurchaseCorrectionPositionResponseV2026_2(BaseModel):
    BeforeCorrection: "PurchaseCorrectionPositionElementResponeV2026_2"
    AfterCorrection: "PurchaseCorrectionPositionElementResponeV2026_2"
    No: int
    BeforeCorrection: "PurchaseCorrectionPositionElement"
    AfterCorrection: "PurchaseCorrectionPositionElement"

class PurchaseCorrectionResponseV2026_2(BaseModel):
    Positions: List["PurchaseCorrectionPositionResponseV2026_2"]
    ThirdPartyContractor: Optional[int]
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
    Note: str
    ForeignDocumentDate: Optional[datetime]
    PurchaseDate: Optional[datetime]
    VoluntarySplitPayment: bool
    WhiteList: bool
    ForeignDocumentNumber: str
    StatusKSeF: Optional[int]
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
    eArchiveId: Optional[str]
    IsSmeProcedure: bool
    IsIssuedByBuyer: bool
    InvoiceKind: Any
    Positions: List["PurchaseCorrectionPosition"]
    SellerAddress: "DocumentAddress"
    DelivererAddress: "DocumentAddress"

class PurchaseDocumentPositionResponseV2026_2(BaseModel):
    ReverseCharge: bool
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
    VatRate: "VatRateBase"
    PriceKind: "enumPriceKind"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal
    Duty: Decimal
    Excise: Decimal

class PurchaseDocumentResponseV2026_2(BaseModel):
    Positions: List["PurchaseDocumentPositionResponseV2026_2"]
    ThirdPartyContractor: Optional[int]
    ThirdPartyContractorAddress: "DocumentAddress"
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
    Note: str
    StatusKSeF: Optional[int]
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
    InvoiceKind: Any
    eArchiveId: Optional[str]
    IsSmeProcedure: bool
    IsIssuedByBuyer: bool
    Positions: List["PurchaseDocumentPosition"]
    SellerAddress: "DocumentAddress"
    DelivererAddress: "DocumentAddress"
