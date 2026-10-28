from __future__ import annotations

from pydantic import BaseModel

from typing import Any, List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentAddress, PaymentRegistryBase
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumCancelationType,
    enumFiscalizationStatus,
    enumJPK_V7DocumentAttribute,
    enumPriceKind,
)
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import (
    PurchaseCorrectionPosition,
    PurchaseDocumentIssueCatalog,
    PurchaseDocumentIssueContractor,
    PurchaseDocumentIssueKind,
    PurchaseDocumentIssuePosition,
    PurchaseDocumentPosition,
)

class Purchases_ViewModels_V2026_1_PurchaseCorrection(BaseModel):
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
PurchaseCorrection = Purchases_ViewModels_V2026_1_PurchaseCorrection

class Purchases_ViewModels_V2026_1_PurchaseDocument(BaseModel):
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
PurchaseDocument = Purchases_ViewModels_V2026_1_PurchaseDocument

class Purchases_ViewModels_V2026_1_PurchaseDocumentIssue(BaseModel):
    ThirdPartyContractor: "PurchaseDocumentIssueContractor"
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
PurchaseDocumentIssue = Purchases_ViewModels_V2026_1_PurchaseDocumentIssue
