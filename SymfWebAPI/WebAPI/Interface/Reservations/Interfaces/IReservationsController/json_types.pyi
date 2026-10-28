from __future__ import annotations

from typing import Any, TypedDict

class ReservationJSON(TypedDict):
    Deliveries: list[ReservationDeliveryJSON]
    Id: int
    Type: Any
    Kind: Any
    ContractorId: int | None
    ProductId: int | None
    WarehouseId: int | None
    ReservationDate: str | None
    MaturityDate: str | None
    Quantity: float | int
    Value: float | int
    DocumentType: int
    PositionType: int
    StandardDocumentType: Any | None
    StandardPositionType: Any | None
    DocumentId: int | None
    PositionId: int | None

class ReservationDeliveryJSON(TypedDict):
    Id: int
    Code: str
    Date: str
    Quantity: float | int
    RealizedQuantity: float | int
    Value: float | int

class ReservationListElementJSON(TypedDict):
    Id: int
    Type: Any
    Kind: Any
    ContractorId: int | None
    ProductId: int | None
    WarehouseId: int | None
    ReservationDate: str | None
    MaturityDate: str | None
    Quantity: float | int
    Value: float | int
    DocumentType: int
    PositionType: int
    StandardDocumentType: Any | None
    StandardPositionType: Any | None
    DocumentId: int | None
    PositionId: int | None
