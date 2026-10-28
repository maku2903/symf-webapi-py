from __future__ import annotations

from typing import Any, TypedDict

class CountryItemJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Products: list[ProductItemJSON]

class CountryProductListJSON(TypedDict):
    Countries: list[CountryItemJSON]

class ProductItemJSON(TypedDict):
    ErpId: int
    Code: str
    Name: str
    VatRateId: int
    ForeignName: str
    ForeignDescription: str
    ShopProducts: list[ProductShopItemJSON]

class ProductShopItemJSON(TypedDict):
    ShopId: str
