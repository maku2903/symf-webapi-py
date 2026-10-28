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

class VatRateBaseJSON(TypedDict):
    Id: int | None
    Code: str
