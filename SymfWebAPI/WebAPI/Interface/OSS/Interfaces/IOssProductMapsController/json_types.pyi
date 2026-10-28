from __future__ import annotations

from typing import Any, TypedDict

class ProductMapJSON(TypedDict):
    Id: int
    ShopName: str
    ErpProductId: int
    ShopProductId: str
    CountryId: int
