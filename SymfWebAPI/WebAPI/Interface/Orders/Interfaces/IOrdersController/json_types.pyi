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

class OrderJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    SplitPayment: bool
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
    PaymentRegistryId: int
    PaymentFormId: int
    Description: str
    Note: str | None
    CatalogId: int
    KindId: int
    Marker: int
    Positions: list[OrderPositionJSON]
    BuyerAddress: DocumentAddressJSON
    RecipientAddress: DocumentAddressJSON
    TypeExternal: int
    IdExternal: int | None
    Id2External: str | None
    DocumentExternalMetadata: str

class OrderFVJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    SaleDate: str | None
    BuyerId: int
    RecipientId: int

class OrderListElementJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    IssueDate: str | None
    SaleDate: str | None
    MaturityDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    BuyerId: int | None
    RecipientId: int | None
    DepartmentId: int
    NetValuePLN: float | int
    VatValuePLN: float | int
    NetValue: float | int
    GrossValue: float | int
    Currency: str
    Description: str
    TypeExternal: int
    IdExternal: int | None
    Id2External: str | None

class OrderPositionJSON(TypedDict):
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

class OrderPositionRelationJSON(TypedDict):
    Id: int
    No: int
    ProductId: int | None
    ProductCode: str
    Description: str
    Quantity: float | int
    NetValuePLN: float | int
    OrderId: int
    OrderNumber: str
    RelatedFV: list[RelatedDocumentPositionJSON]
    RelatedWZ: list[RelatedDocumentPositionJSON]

class OrderStatusJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: Any
    ManualSettled: Any
    DocumentStatus: Any
    DocumentStatusText: str

class OrderWZJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    OperationDate: str | None
    RecipientId: int

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

class RelatedDocumentPositionJSON(TypedDict):
    Id: int
    No: int
    Quantity: float | int
    NetValuePLN: float | int
    DocumentId: int
    DocumentNumber: str
    QuantityCorrected: float | int
    NetValuePLNCorrected: float | int

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
    Data: list[OrderListElementJSON]
