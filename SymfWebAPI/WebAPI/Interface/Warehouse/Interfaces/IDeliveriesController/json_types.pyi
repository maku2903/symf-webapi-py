from __future__ import annotations

from typing import Any, TypedDict

class DeliveryListElementJSON(TypedDict):
    Id: int
    Code: str
    QuantityForSale: float | int
    QuantityInWarehouse: float | int
    DeliveryDate: str
    WarehouseId: int
    ProductId: int
    ContractorId: int | None
    TypeExternal: int
    IdExternal: int | None
    Id2External: str | None
