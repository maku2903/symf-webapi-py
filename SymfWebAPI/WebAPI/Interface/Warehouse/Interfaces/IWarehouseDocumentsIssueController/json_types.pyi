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
    Reservations: list[WarehouseDocumentPositionReservationJSON] | None
    Deliveries: list[WarehouseDocumentPositionDeliveryJSON] | None

class WarehouseDocumentPositionDeliveryJSON(TypedDict):
    Id: int
    Code: str
    Quantity: float | int
    Date: str
    ReservationId: int | None

class WarehouseDocumentPositionReservationJSON(TypedDict):
    Id: int
    Quantity: float | int
