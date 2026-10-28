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
    enumSalePriceType,
)
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import (
    SaleCorrectionPosition,
    SaleCorrectionPositionElement,
    SaleDocumentPosition,
)

class SaleCorrectionPositionElementV2026_2(BaseModel):
    VatUe: Optional[bool]
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
    SalePriceType: "enumSalePriceType"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal

class SaleCorrectionPositionElementV2026_2WithServiceExport(BaseModel):
    ServiceExport: Optional[bool]
    VatUe: Optional[bool]
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
    SalePriceType: "enumSalePriceType"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal

class SaleCorrectionResponsePositionV2026_2(BaseModel):
    BeforeCorrection: "SaleCorrectionPositionElementV2026_2"
    AfterCorrection: "SaleCorrectionPositionElementV2026_2WithServiceExport"
    No: int
    BeforeCorrection: "SaleCorrectionPositionElement"
    AfterCorrection: "SaleCorrectionPositionElement"

class SaleCorrectionResponseV2026_2(BaseModel):
    Positions: List["SaleCorrectionResponsePositionV2026_2"]
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
    Note: str
    StatusKSeF: Optional[int]
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
    eArchiveId: Optional[str]
    Positions: List["SaleCorrectionPosition"]
    BuyerAddress: "DocumentAddress"
    RecipientAddress: "DocumentAddress"
    ThirdPartyContractorAddress: "DocumentAddress"
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
    InvoiceKind: Any

class SaleDocumentPositionV2026_2(BaseModel):
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
    ReverseCharge: bool
    VatRate: "VatRateBase"
    PriceKind: "enumPriceKind"
    SalePriceType: "enumSalePriceType"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal
    VatUe: Optional[bool]
    ServiceExport: Optional[bool]

class SaleDocumentResponseV2026_2(BaseModel):
    Positions: List["SaleDocumentPositionV2026_2"]
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
    Note: str
    StatusKSeF: Optional[int]
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
    eArchiveId: Optional[str]
    Positions: List["SaleDocumentPosition"]
    BuyerAddress: "DocumentAddress"
    RecipientAddress: "DocumentAddress"
    ThirdPartyContractorAddress: "DocumentAddress"
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: str
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
    InvoiceKind: Any
