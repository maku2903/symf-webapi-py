from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumDocumentReservationType,
    enumReservationDocumentType,
    enumReservationKind,
    enumReservationMode,
    enumReservationPositionType,
    enumReservationType,
)

class AdvancedReservationNew(BaseModel):
    DocumentId: int
    PositionId: int
    DocumentType: int
    PositionType: int
    Mode: "enumReservationMode"
    Warehouse: "ReservationNewWarehouse"
    Contractor: "ReservationNewContractor"
    Product: "ReservationNewProduct"
    Type: "enumDocumentReservationType"
    ReservationDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Quantity: Optional[Decimal]
    ReserveToMax: bool
    MustReserveAllIndicatedDeliveries: bool
    Deliveries: List["ReservationNewDelivery"]

class Reservation(BaseModel):
    Deliveries: List["ReservationDelivery"]
    Id: int
    Type: "enumReservationType"
    Kind: "enumReservationKind"
    ContractorId: Optional[int]
    ProductId: Optional[int]
    WarehouseId: Optional[int]
    ReservationDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Quantity: Decimal
    Value: Decimal
    DocumentType: int
    PositionType: int
    StandardDocumentType: Optional["enumReservationDocumentType"]
    StandardPositionType: Optional["enumReservationPositionType"]
    DocumentId: Optional[int]
    PositionId: Optional[int]

class ReservationDelivery(BaseModel):
    Id: int
    Code: str
    Date: datetime
    Quantity: Decimal
    RealizedQuantity: Decimal
    Value: Decimal

class ReservationListElement(BaseModel):
    Id: int
    Type: "enumReservationType"
    Kind: "enumReservationKind"
    ContractorId: Optional[int]
    ProductId: Optional[int]
    WarehouseId: Optional[int]
    ReservationDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Quantity: Decimal
    Value: Decimal
    DocumentType: int
    PositionType: int
    StandardDocumentType: Optional["enumReservationDocumentType"]
    StandardPositionType: Optional["enumReservationPositionType"]
    DocumentId: Optional[int]
    PositionId: Optional[int]

class ReservationNew(BaseModel):
    Warehouse: "ReservationNewWarehouse"
    Contractor: "ReservationNewContractor"
    Product: "ReservationNewProduct"
    Type: "enumDocumentReservationType"
    ReservationDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    Quantity: Optional[Decimal]
    ReserveToMax: bool
    MustReserveAllIndicatedDeliveries: bool
    Deliveries: List["ReservationNewDelivery"]

class ReservationNewContractor(BaseModel):
    Id: Optional[int]
    Code: str

class ReservationNewDelivery(BaseModel):
    Id: Optional[int]
    Code: str
    Quantity: Decimal

class ReservationNewProduct(BaseModel):
    Id: Optional[int]
    Code: str

class ReservationNewUnitInfo(BaseModel):
    Id: Optional[int]
    Code: str

class ReservationNewWarehouse(BaseModel):
    Id: Optional[int]
    Code: str
