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

class PurchaseDocumentCorrectionJSON(TypedDict):
    No: int
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    ReceiveDate: str | None
    ForeignDocumentDate: str | None

class PurchaseDocumentListElementJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    IssueDate: str | None
    PurchaseDate: str | None
    ReceiveDate: str | None
    MaturityDate: str | None
    ForeignDocumentDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SellerId: int | None
    DelivererId: int | None
    DepartmentId: int
    NetValuePLN: float | int
    VatValuePLN: float | int
    NetValue: float | int
    GrossValue: float | int
    Currency: str
    Description: str
    IsSmeProcedure: bool
    IsIssuedByBuyer: bool
    InvoiceKind: Any

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

class PurchaseDocumentStatusJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: Any
    ManualSettled: Any
    DocumentStatus: Any
    DocumentStatusText: str

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

class GetPagedDocumentJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[PurchaseDocumentListElementJSON]
