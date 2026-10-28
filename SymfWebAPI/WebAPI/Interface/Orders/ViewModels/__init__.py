from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import (
    DocumentAddress,
    PaymentRegistryBase,
    RelatedDocumentPosition,
    VatRateBase,
)
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumCancelationType,
    enumDocumentReservationType,
    enumDocumentStatus,
    enumManualSettledState,
    enumPriceKind,
    enumRDFStatus,
    enumSalePriceType,
)

class Order(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    SplitPayment: bool
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    BuyerId: Optional[int]
    BuyerAddressId: Optional[int]
    RecipientId: Optional[int]
    RecipientAddressId: Optional[int]
    ReceivedBy: str
    DepartmentId: int
    PriceKind: "enumPriceKind"
    SalePriceType: "enumSalePriceType"
    NetValuePLN: Decimal
    VatValuePLN: Decimal
    NetValue: Decimal
    GrossValue: Decimal
    Currency: str
    CurrencyRate: Decimal
    PaymentRegistryId: int
    PaymentFormId: int
    Description: str
    Note: Optional[str]
    CatalogId: int
    KindId: int
    Marker: int
    Positions: List["OrderPosition"]
    BuyerAddress: "DocumentAddress"
    RecipientAddress: "DocumentAddress"
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: Optional[str]
    DocumentExternalMetadata: str

class OrderBase(BaseModel):
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    Department: str
    Warehouse: str
    ReservationType: "enumDocumentReservationType"
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: int
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Currency: str
    CurrencyRate: Decimal
    SalePriceType: "enumSalePriceType"
    PriceKind: "enumPriceKind"
    SplitPayment: bool
    Buyer: "OrderIssueContractor"
    Recipient: "OrderIssueContractor"
    Catalog: "OrderIssueCatalog"
    Kind: "OrderIssueKind"
    Marker: int
    ReceivedBy: str
    Description: str
    Note: Optional[str]
    DocumentExternalMetadata: str

class OrderEdit(BaseModel):
    Id: int
    Positions: List["OrderEditPosition"]
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    Department: str
    Warehouse: str
    ReservationType: "enumDocumentReservationType"
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: int
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Currency: str
    CurrencyRate: Decimal
    SalePriceType: "enumSalePriceType"
    PriceKind: "enumPriceKind"
    SplitPayment: bool
    Buyer: "OrderIssueContractor"
    Recipient: "OrderIssueContractor"
    Catalog: "OrderIssueCatalog"
    Kind: "OrderIssueKind"
    Marker: int
    ReceivedBy: str
    Description: str
    Note: Optional[str]
    DocumentExternalMetadata: str

class OrderEditPosition(BaseModel):
    PositionId: Optional[int]
    Delete: bool
    VatRate: Optional["VatRateBase"]
    Elements: List["OrderIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Deliveries: List["OrderIssueDelivery"]

class OrderFV(BaseModel):
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    BuyerId: int
    RecipientId: int

class OrderIssue(BaseModel):
    Positions: List["OrderIssuePosition"]
    TypeExternal: Optional[int]
    IdExternal: Optional[int]
    Id2External: Optional[str]
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    Department: str
    Warehouse: str
    ReservationType: "enumDocumentReservationType"
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: int
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Currency: str
    CurrencyRate: Decimal
    SalePriceType: "enumSalePriceType"
    PriceKind: "enumPriceKind"
    SplitPayment: bool
    Buyer: "OrderIssueContractor"
    Recipient: "OrderIssueContractor"
    Catalog: "OrderIssueCatalog"
    Kind: "OrderIssueKind"
    Marker: int
    ReceivedBy: str
    Description: str
    Note: Optional[str]
    DocumentExternalMetadata: str

class OrderIssueCatalog(BaseModel):
    FullPath: str
    AddIfNotExist: bool

class OrderIssueContractor(BaseModel):
    Id: Optional[int]
    Code: str
    RecalculatePrices: bool
    Data: "OrderIssueContractorData"
    DeliveryAddressCode: str

class OrderIssueContractorData(BaseModel):
    Name: str
    NIP: Optional[str]
    Country: str
    City: Optional[str]
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]

class OrderIssueDelivery(BaseModel):
    Id: Optional[int]
    Code: str
    Quantity: Decimal

class OrderIssueKind(BaseModel):
    Code: str
    AddIfNotExist: bool

class OrderIssuePosition(BaseModel):
    VatRate: Optional["VatRateBase"]
    Elements: List["OrderIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Deliveries: List["OrderIssueDelivery"]

class OrderIssuePositionElement(BaseModel):
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal
    Deliveries: List["OrderIssueDelivery"]

class OrderListElement(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    BuyerId: Optional[int]
    RecipientId: Optional[int]
    DepartmentId: int
    NetValuePLN: Decimal
    VatValuePLN: Decimal
    NetValue: Decimal
    GrossValue: Decimal
    Currency: str
    Description: str
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: Optional[str]

class OrderPosition(BaseModel):
    Id: int
    No: int
    SetHeaderId: Optional[int]
    ProductId: Optional[int]
    ProductCode: str
    Description: str
    Quantity: Decimal
    WrittenQuantity: Decimal
    EnteredQuantity: Decimal
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    EnteredUnitOfMeasurement: str
    VatRate: Optional["VatRateBase"]
    PriceKind: "enumPriceKind"
    SalePriceType: "enumSalePriceType"
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal

class OrderPositionRelation(BaseModel):
    Id: int
    No: int
    ProductId: Optional[int]
    ProductCode: str
    Description: str
    Quantity: Decimal
    NetValuePLN: Decimal
    OrderId: int
    OrderNumber: str
    RelatedFV: List["RelatedDocumentPosition"]
    RelatedWZ: List["RelatedDocumentPosition"]

class OrderStatus(BaseModel):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: "enumRDFStatus"
    ManualSettled: "enumManualSettledState"
    DocumentStatus: "enumDocumentStatus"
    DocumentStatusText: str

class OrderWZ(BaseModel):
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    RecipientId: int
