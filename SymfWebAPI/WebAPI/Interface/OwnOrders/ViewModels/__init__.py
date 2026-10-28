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
    enumDocumentStatus,
    enumManualSettledState,
    enumPriceKind,
    enumRDFStatus,
)

class OwnOrder(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    IssueDate: Optional[datetime]
    ReceiveDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SellerId: Optional[int]
    SellerAddressId: Optional[int]
    DelivererId: Optional[int]
    DelivererAddressId: Optional[int]
    DepartmentId: int
    PriceKind: "enumPriceKind"
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
    Positions: List["OwnOrderPosition"]
    SellerAddress: "DocumentAddress"
    DelivererAddress: "DocumentAddress"

class OwnOrderFV(BaseModel):
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    BuyDate: Optional[datetime]
    SellerId: int
    DelivererId: int

class OwnOrderIssue(BaseModel):
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    Department: str
    PaymentRegistry: "PaymentRegistryBase"
    PaymentFormId: int
    IssueDate: Optional[datetime]
    ReceiveDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Currency: str
    CurrencyRate: Decimal
    PriceKind: "enumPriceKind"
    Seller: "OwnOrderIssueContractor"
    Deliverer: "OwnOrderIssueContractor"
    Positions: List["OwnOrderIssuePosition"]
    Catalog: "OwnOrderIssueCatalog"
    Kind: "OwnOrderIssueKind"
    Marker: int
    Description: str
    Note: Optional[str]

class OwnOrderIssueCatalog(BaseModel):
    FullPath: str
    AddIfNotExist: bool

class OwnOrderIssueContractor(BaseModel):
    Id: Optional[int]
    Code: str
    RecalculatePrices: bool
    Data: "OwnOrderIssueContractorData"
    DeliveryAddressCode: str

class OwnOrderIssueContractorData(BaseModel):
    Name: str
    NIP: Optional[str]
    Country: str
    City: Optional[str]
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]

class OwnOrderIssueKind(BaseModel):
    Code: str
    AddIfNotExist: bool

class OwnOrderIssuePosition(BaseModel):
    VatRate: Optional["VatRateBase"]
    Elements: List["OwnOrderIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal

class OwnOrderIssuePositionElement(BaseModel):
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Decimal

class OwnOrderListElement(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    IssueDate: Optional[datetime]
    ReceiveDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SellerId: Optional[int]
    DelivererId: Optional[int]
    DepartmentId: int
    NetValuePLN: Decimal
    VatValuePLN: Decimal
    NetValue: Decimal
    GrossValue: Decimal
    Currency: str
    Description: str

class OwnOrderPZ(BaseModel):
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    DelivererId: int

class OwnOrderPosition(BaseModel):
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
    PriceValuePLN: Decimal
    PriceValue: Decimal
    NetValuePLN: Decimal
    NetValue: Decimal
    VatValuePLN: Decimal
    GrossValue: Decimal

class OwnOrderPositionRelation(BaseModel):
    Id: int
    No: int
    ProductId: Optional[int]
    ProductCode: str
    Description: str
    Quantity: Decimal
    NetValuePLN: Decimal
    OwnOrderId: int
    OwnOrderNumber: str
    RelatedFV: List["RelatedDocumentPosition"]
    RelatedPZ: List["RelatedDocumentPosition"]

class OwnOrderStatus(BaseModel):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: "enumRDFStatus"
    ManualSettled: "enumManualSettledState"
    DocumentStatus: "enumDocumentStatus"
    DocumentStatusText: str
