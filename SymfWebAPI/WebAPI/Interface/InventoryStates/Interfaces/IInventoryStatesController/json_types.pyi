from __future__ import annotations

from typing import Any, TypedDict

class InventoryStateJSON(TypedDict):
    ProductId: int
    WarehouseId: int
    AmountInStore: float | int
    AmountToSale: float | int
