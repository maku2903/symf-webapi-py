from __future__ import annotations

from typing import Any, TypedDict

class CatalogJSON(TypedDict):
    Id: int
    ParentId: int
    Name: str
    FullPath: str

class DocumentTypeJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Active: bool
    JPKDocumentKind: Any
    JPK_V7Attributes: Any
    Character: Any
    CorrectionTypeId: int | None
    CorrectionSerieId: int | None
    RelatedTypeId: int | None
    RelatedSerieId: int | None
    DefaultDateRegister: int | None
    IsIssuedByBuyer: bool
    IsThirdPartyContractorEnabled: bool
    SelfTaxation: int
    IdRejestr: int

class MarkerJSON(TypedDict):
    Subtype: int
    Name: str
    Active: bool

class DocumentAddressJSON(TypedDict):
    Name: str | None
    NIP: str | None
    City: str | None
    PostCode: str | None
    Street: str | None
    HouseNo: str | None
    ApartmentNo: str | None
    CountryId: int | None

class DocumentSeriesJSON(TypedDict):
    Id: int
    Code: str

class IncrementalSyncListElementJSON(TypedDict):
    Id: int
    ModifyType: Any
    ModifiedAt: str
    Object: Any

class KindJSON(TypedDict):
    Id: int | None
    Code: str
    Active: bool

class PDFJSON(TypedDict):
    Hash_SHA1: str
    ContentFile_Base64: str
    CreateDate: str

class PageJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[Any]

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

class SaleDocumentCorrectionJSON(TypedDict):
    No: int
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    SaleDate: str | None

class SaleDocumentListElementJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: int
    Settled: int
    IssueDate: str | None
    SaleDate: str | None
    MaturityDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    BuyerId: int | None
    ThirdPartyContractorId: int | None
    RecipientId: int | None
    DepartmentId: int
    NetValuePLN: float | int
    VatValuePLN: float | int
    NetValue: float | int
    GrossValue: float | int
    IncomeValue: float | int
    Currency: str
    Description: str
    IsSmeProcedure: bool
    TypeExternal: int
    IdExternal: int | None
    Id2External: str | None
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

class SaleDocumentStatusJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: Any
    ManualSettled: Any
    DocumentStatus: Any
    DocumentStatusText: str

class SaleDocumentWZJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    OperationDate: str | None
    RecipientId: int

class SaleDocumentZMOJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    SaleDate: str | None
    BuyerId: int
    RecipientId: int

class VatRateBaseJSON(TypedDict):
    Id: int | None
    Code: str

class GetPagedDocumentJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[SaleDocumentListElementJSON]
