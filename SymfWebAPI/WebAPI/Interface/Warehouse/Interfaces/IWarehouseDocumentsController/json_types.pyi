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

class WarehouseDocumentJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    IssueDate: str | None
    OperationDate: str | None
    MaturityDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    ContractorId: int | None
    ContractorAddressId: int | None
    ReceivingWarehouseId: int | None
    WarehouseId: int
    NetValue: float | int
    DocumentValue: float | int
    IncomeValue: float | int
    OutcomeValue: float | int
    Description: str
    CatalogId: int
    KindId: int
    Marker: int
    Note: str | None
    TypeExternal: int
    IdExternal: int | None
    Id2External: str | None
    Positions: list[WarehouseDocumentPositionJSON]
    ContractorAddress: DocumentAddressJSON

class WarehouseDocumentFVJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    OperationDate: str | None
    Contractor1Id: int
    Contractor2Id: int

class WarehouseDocumentListElementJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    IssueDate: str | None
    OperationDate: str | None
    MaturityDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    ContractorId: int | None
    ReceivingWarehouseId: int | None
    WarehouseId: int
    NetValue: float | int
    DocumentValue: float | int
    IncomeValue: float | int
    OutcomeValue: float | int
    Description: str
    TypeExternal: int
    IdExternal: int | None
    Id2External: str | None

class WarehouseDocumentPositionJSON(TypedDict):
    Id: int
    No: int
    SetHeaderId: int | None
    ProductId: int
    ProductCode: str
    Description: str
    Quantity: float | int
    WrittenQuantity: float | int
    EnteredQuantity: float | int
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    EnteredUnitOfMeasurement: str
    PriceValue: float | int
    NetValue: float | int
    Reservations: list[WarehouseDocumentPositionReservationJSON]
    Deliveries: list[WarehouseDocumentPositionDeliveryJSON]

class WarehouseDocumentPositionDeliveryJSON(TypedDict):
    Id: int
    Code: str
    Quantity: float | int
    Date: str
    ReservationId: int | None

class WarehouseDocumentPositionReservationJSON(TypedDict):
    Id: int
    Quantity: float | int

class WarehouseDocumentStatusJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: Any
    ManualSettled: Any
    DocumentStatus: Any
    DocumentStatusText: str

class WarehouseRegistryJSON(TypedDict):
    Id: int
    Code: str
    Name: str

class GetPagedDocumentJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[WarehouseDocumentListElementJSON]
