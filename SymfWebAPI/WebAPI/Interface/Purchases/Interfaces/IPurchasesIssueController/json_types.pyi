from __future__ import annotations

from typing import Any, TypedDict

class DocumentAddressJSON(TypedDict):
    Name: str | None
    NIP: str | None
    City: str | None
    PostCode: str | None
    Street: str | None
    HouseNo: str | None
    ApartmentNo: str | None
    CountryId: int | None

class PurchaseCorrectionPositionJSON(TypedDict):
    No: int
    BeforeCorrection: PurchaseCorrectionPositionElementJSON
    AfterCorrection: PurchaseCorrectionPositionElementJSON

class PurchaseCorrectionPositionElementJSON(TypedDict):
    Id: int
    SetHeaderId: int | None
    ProductId: int | None
    ProductCode: str
    Description: str
    Quantity: float | int
    WrittenQuantity: float | int
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    VatRate: VatRateBaseJSON | None
    PriceKind: Any
    PriceValuePLN: float | int
    PriceValue: float | int
    NetValuePLN: float | int
    NetValue: float | int
    VatValuePLN: float | int
    GrossValue: float | int
    Duty: float | int
    Excise: float | int

class PurchaseDocumentPZJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    OperationDate: str | None
    DelivererId: int

class PurchaseDocumentPositionJSON(TypedDict):
    Id: int
    No: int
    SetHeaderId: int | None
    ProductId: int | None
    ProductCode: str
    Description: str
    Quantity: float | int
    WrittenQuantity: float | int
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    VatRate: VatRateBaseJSON | None
    PriceKind: Any
    PriceValuePLN: float | int
    PriceValue: float | int
    NetValuePLN: float | int
    NetValue: float | int
    VatValuePLN: float | int
    GrossValue: float | int
    Duty: float | int
    Excise: float | int

class PurchaseCorrectionJSON(TypedDict):
    Id: int
    DocumentNumber: str
    MasterDocumentOid: int | None
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    Fisacal: Any
    eInvoice: bool
    SplitPayment: bool
    JPK_V7Attributes: Any
    IssueDate: str | None
    ReceiveDate: str | None
    MaturityDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SellerId: int | None
    SellerAddressId: int | None
    DelivererId: int | None
    DelivererAddressId: int | None
    ReceivedBy: str
    DepartmentId: int
    PriceKind: Any
    NetValuePLN: float | int
    VatValuePLN: float | int
    NetValue: float | int
    GrossValue: float | int
    Currency: str
    CurrencyRate: float | int
    CurrencyRateCIT: float | int
    PaymentRegistryId: int
    PaymentFormId: int
    CorrectionReason: str
    CatalogId: int
    KindId: int
    Marker: int
    Note: str | None
    ForeignDocumentDate: str | None
    PurchaseDate: str | None
    VoluntarySplitPayment: bool
    WhiteList: bool
    ForeignDocumentNumber: str
    StatusKSeF: int | None
    NumberKSeF: str | None
    IssueDateKSeF: str | None
    eArchiveId: str | None
    IsSmeProcedure: bool
    IsIssuedByBuyer: bool
    InvoiceKind: Any
    Positions: list[PurchaseCorrectionPositionJSON]
    SellerAddress: DocumentAddressJSON
    DelivererAddress: DocumentAddressJSON

class PurchaseDocumentJSON(TypedDict):
    Id: int
    DocumentNumber: str
    ForeignDocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    Fisacal: Any
    eInvoice: bool
    SplitPayment: bool
    VoluntarySplitPayment: bool
    WhiteList: bool
    JPK_V7Attributes: Any
    IssueDate: str | None
    ReceiveDate: str | None
    MaturityDate: str | None
    ForeignDocumentDate: str | None
    PurchaseDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SellerId: int | None
    SellerAddressId: int | None
    DelivererId: int | None
    DelivererAddressId: int | None
    ReceivedBy: str
    DepartmentId: int
    PriceKind: Any
    NetValuePLN: float | int
    VatValuePLN: float | int
    NetValue: float | int
    GrossValue: float | int
    Currency: str
    CurrencyRate: float | int
    CurrencyRateCIT: float | int
    PaymentRegistryId: int
    PaymentFormId: int
    Description: str
    CatalogId: int
    KindId: int
    Marker: int
    Note: str | None
    StatusKSeF: int | None
    NumberKSeF: str | None
    IssueDateKSeF: str | None
    InvoiceKind: Any
    eArchiveId: str | None
    IsSmeProcedure: bool
    IsIssuedByBuyer: bool
    Positions: list[PurchaseDocumentPositionJSON]
    SellerAddress: DocumentAddressJSON
    DelivererAddress: DocumentAddressJSON

class VatRateBaseJSON(TypedDict):
    Id: int | None
    Code: str
