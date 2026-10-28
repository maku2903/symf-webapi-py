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

class OrderWZJSON(TypedDict):
    Id: int
    DocumentNumber: str
    IssueDate: str | None
    OperationDate: str | None
    RecipientId: int

class VatRateBaseJSON(TypedDict):
    Id: int | None
    Code: str
