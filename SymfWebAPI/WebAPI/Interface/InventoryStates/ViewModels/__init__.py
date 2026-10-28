from __future__ import annotations

from pydantic import BaseModel

from decimal import Decimal

class InventoryState(BaseModel):
    ProductId: int
    WarehouseId: int
    AmountInStore: Decimal
    AmountToSale: Decimal
