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

class OwnOrderJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
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
    DepartmentId: int
    PriceKind: Any
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
    Positions: list[OwnOrderPositionJSON]
    SellerAddress: DocumentAddressJSON
    DelivererAddress: DocumentAddressJSON

class OwnOrderFVJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    BuyDate: str | None
    SellerId: int
    DelivererId: int

class OwnOrderListElementJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    IssueDate: str | None
    ReceiveDate: str | None
    MaturityDate: str | None
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

class OwnOrderPZJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    OperationDate: str | None
    DelivererId: int

class OwnOrderPositionJSON(TypedDict):
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
    PriceValuePLN: float | int
    PriceValue: float | int
    NetValuePLN: float | int
    NetValue: float | int
    VatValuePLN: float | int
    GrossValue: float | int

class OwnOrderPositionRelationJSON(TypedDict):
    Id: int
    No: int
    ProductId: int | None
    ProductCode: str
    Description: str
    Quantity: float | int
    NetValuePLN: float | int
    OwnOrderId: int
    OwnOrderNumber: str
    RelatedFV: list[RelatedDocumentPositionJSON]
    RelatedPZ: list[RelatedDocumentPositionJSON]

class OwnOrderStatusJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: Any
    ManualSettled: Any
    DocumentStatus: Any
    DocumentStatusText: str

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
    Data: list[OwnOrderListElementJSON]
