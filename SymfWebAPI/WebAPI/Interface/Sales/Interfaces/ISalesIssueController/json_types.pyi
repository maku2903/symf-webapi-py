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

class SaleCorrectionJSON(TypedDict):
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
    SaleDate: str | None
    MaturityDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    BuyerId: int | None
    BuyerAddressId: int | None
    RecipientId: int | None
    RecipientAddressId: int | None
    ThirdPartyContractorId: int | None
    ThirdPartyContractorAddressId: int | None
    ReceivedBy: str
    DepartmentId: int
    PriceKind: Any
    SalePriceType: Any
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
    StatusKSeF: int | None
    NumberKSeF: str | None
    IssueDateKSeF: str | None
    eArchiveId: str | None
    Positions: list[SaleCorrectionPositionJSON]
    BuyerAddress: DocumentAddressJSON
    RecipientAddress: DocumentAddressJSON
    ThirdPartyContractorAddress: DocumentAddressJSON
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
    InvoiceKind: Any

class SaleCorrectionPositionJSON(TypedDict):
    No: int
    BeforeCorrection: SaleCorrectionPositionElementJSON
    AfterCorrection: SaleCorrectionPositionElementJSON

class SaleCorrectionPositionElementJSON(TypedDict):
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
    SalePriceType: Any
    PriceValuePLN: float | int
    PriceValue: float | int
    NetValuePLN: float | int
    NetValue: float | int
    VatValuePLN: float | int
    GrossValue: float | int

class SaleDocumentJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    Fisacal: Any
    eInvoice: bool
    SplitPayment: bool
    JPK_V7Attributes: Any
    IssueDate: str | None
    SaleDate: str | None
    MaturityDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    BuyerId: int | None
    BuyerAddressId: int | None
    RecipientId: int | None
    RecipientAddressId: int | None
    ThirdPartyContractorId: int | None
    ThirdPartyContractorAddressId: int | None
    ReceivedBy: str
    DepartmentId: int
    PriceKind: Any
    SalePriceType: Any
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
    eArchiveId: str | None
    Positions: list[SaleDocumentPositionJSON]
    BuyerAddress: DocumentAddressJSON
    RecipientAddress: DocumentAddressJSON
    ThirdPartyContractorAddress: DocumentAddressJSON
    TypeExternal: int
    IdExternal: int | None
    Id2External: str | None
    DocumentExternalMetadata: str
    IsSmeProcedure: bool
    InvoiceKind: Any

class SaleDocumentPositionJSON(TypedDict):
    Id: int
    No: int
    SetHeaderId: int | None
    ProductId: int | None
    ProductCode: str
    Description: str
    Quantity: float | int
    WrittenQuantity: float | int
    EnteredQuantity: float | int
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    EnteredUnitOfMeasurement: str
    VatRate: VatRateBaseJSON | None
    PriceKind: Any
    SalePriceType: Any
    PriceValuePLN: float | int
    PriceValue: float | int
    NetValuePLN: float | int
    NetValue: float | int
    VatValuePLN: float | int
    GrossValue: float | int

class SaleDocumentWZJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    OperationDate: str | None
    RecipientId: int

class VatRateBaseJSON(TypedDict):
    Id: int | None
    Code: str
