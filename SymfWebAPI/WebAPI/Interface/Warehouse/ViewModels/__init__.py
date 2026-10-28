from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentAddress
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumCancelationType,
    enumDocumentReservationType,
    enumDocumentStatus,
    enumManualSettledState,
    enumRDFStatus,
)

class DeliveryListElement(BaseModel):
    Id: int
    Code: str
    QuantityForSale: Decimal
    QuantityInWarehouse: Decimal
    DeliveryDate: datetime
    WarehouseId: int
    ProductId: int
    ContractorId: Optional[int]
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: Optional[str]

class WarehouseDocument(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    ContractorId: Optional[int]
    ContractorAddressId: Optional[int]
    ReceivingWarehouseId: Optional[int]
    WarehouseId: int
    NetValue: Decimal
    DocumentValue: Decimal
    IncomeValue: Decimal
    OutcomeValue: Decimal
    Description: str
    CatalogId: int
    KindId: int
    Marker: int
    Note: Optional[str]
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: Optional[str]
    Positions: List["WarehouseDocumentPosition"]
    ContractorAddress: "DocumentAddress"

class WarehouseDocumentBase(BaseModel):
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    Warehouse: str
    ReservationType: Optional["enumDocumentReservationType"]
    WarehouseRegistry: str
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Contractor: "WarehouseDocumentIssueContractor"
    ReceivingWarehouse: "WarehouseDocumentIssueReceivingWarehouse"
    Catalog: "WarehouseDocumentIssueCatalog"
    Kind: "WarehouseDocumentssueKind"
    Marker: int
    ReceivedBy: str
    Description: str
    Note: Optional[str]
    TypeExternal: Optional[int]
    IdExternal: Optional[int]
    Id2External: Optional[str]

class WarehouseDocumentEdit(BaseModel):
    Id: int
    Positions: List["WarehouseDocumentEditPosition"]
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    Warehouse: str
    ReservationType: Optional["enumDocumentReservationType"]
    WarehouseRegistry: str
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Contractor: "WarehouseDocumentIssueContractor"
    ReceivingWarehouse: "WarehouseDocumentIssueReceivingWarehouse"
    Catalog: "WarehouseDocumentIssueCatalog"
    Kind: "WarehouseDocumentssueKind"
    Marker: int
    ReceivedBy: str
    Description: str
    Note: Optional[str]
    TypeExternal: Optional[int]
    IdExternal: Optional[int]
    Id2External: Optional[str]

class WarehouseDocumentEditPosition(BaseModel):
    PositionId: Optional[int]
    Delete: bool
    Elements: List["WarehouseDocumentIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Optional[Decimal]
    Deliveries: List["WarehouseDocumentIssueDelivery"]

class WarehouseDocumentFV(BaseModel):
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    Contractor1Id: int
    Contractor2Id: int

class WarehouseDocumentIssue(BaseModel):
    Positions: List["WarehouseDocumentIssuePosition"]
    TypeCode: str
    Series: str
    NumberInSeries: Optional[int]
    Warehouse: str
    ReservationType: Optional["enumDocumentReservationType"]
    WarehouseRegistry: str
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Contractor: "WarehouseDocumentIssueContractor"
    ReceivingWarehouse: "WarehouseDocumentIssueReceivingWarehouse"
    Catalog: "WarehouseDocumentIssueCatalog"
    Kind: "WarehouseDocumentssueKind"
    Marker: int
    ReceivedBy: str
    Description: str
    Note: Optional[str]
    TypeExternal: Optional[int]
    IdExternal: Optional[int]
    Id2External: Optional[str]

class WarehouseDocumentIssueCatalog(BaseModel):
    FullPath: str
    AddIfNotExist: bool

class WarehouseDocumentIssueContractor(BaseModel):
    Id: Optional[int]
    Code: str
    Data: "WarehouseDocumentIssueContractorData"
    DeliveryAddressCode: str

class WarehouseDocumentIssueContractorData(BaseModel):
    Name: str
    NIP: Optional[str]
    Country: str
    City: Optional[str]
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]

class WarehouseDocumentIssueDelivery(BaseModel):
    Id: Optional[int]
    Code: str
    Quantity: Decimal

class WarehouseDocumentIssuePosition(BaseModel):
    Elements: List["WarehouseDocumentIssuePositionElement"]
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Optional[Decimal]
    Deliveries: List["WarehouseDocumentIssueDelivery"]

class WarehouseDocumentIssuePositionElement(BaseModel):
    Code: str
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Value: Optional[Decimal]
    Deliveries: List["WarehouseDocumentIssueDelivery"]

class WarehouseDocumentIssueReceivingWarehouse(BaseModel):
    Id: Optional[int]
    Code: str

class WarehouseDocumentListElement(BaseModel):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: "enumCancelationType"
    Buffer: bool
    Settled: bool
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    ContractorId: Optional[int]
    ReceivingWarehouseId: Optional[int]
    WarehouseId: int
    NetValue: Decimal
    DocumentValue: Decimal
    IncomeValue: Decimal
    OutcomeValue: Decimal
    Description: str
    TypeExternal: int
    IdExternal: Optional[int]
    Id2External: Optional[str]

class WarehouseDocumentPosition(BaseModel):
    Id: int
    No: int
    SetHeaderId: Optional[int]
    ProductId: int
    ProductCode: str
    Description: str
    Quantity: Decimal
    WrittenQuantity: Decimal
    EnteredQuantity: Decimal
    UnitOfMeasurement: str
    WrittenUnitOfMeasurement: str
    EnteredUnitOfMeasurement: str
    PriceValue: Decimal
    NetValue: Decimal
    Reservations: Optional[List["WarehouseDocumentPositionReservation"]]
    Deliveries: Optional[List["WarehouseDocumentPositionDelivery"]]

class WarehouseDocumentPositionDelivery(BaseModel):
    Id: int
    Code: str
    Quantity: Decimal
    Date: datetime
    ReservationId: Optional[int]

class WarehouseDocumentPositionReservation(BaseModel):
    Id: int
    Quantity: Decimal

class WarehouseDocumentStatus(BaseModel):
    Id: int
    DocumentNumber: str
    Buffer: bool
    PaymentSettled: int
    WarehouseSettled: int
    RDFStatus: "enumRDFStatus"
    ManualSettled: "enumManualSettledState"
    DocumentStatus: "enumDocumentStatus"
    DocumentStatusText: str

class WarehouseDocumentssueKind(BaseModel):
    Code: str
    AddIfNotExist: bool

class WarehouseRegistry(BaseModel):
    Id: int
    Code: str
    Name: str
