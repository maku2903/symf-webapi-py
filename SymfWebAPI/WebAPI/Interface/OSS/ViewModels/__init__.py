from __future__ import annotations

from pydantic import BaseModel

from typing import List

class CountryItem(BaseModel):
    Id: int
    Code: str
    Name: str
    Products: List["ProductItem"]

class CountryProductList(BaseModel):
    Countries: List["CountryItem"]

class ProductItem(BaseModel):
    ErpId: int
    Code: str
    Name: str
    VatRateId: int
    ForeignName: str
    ForeignDescription: str
    ShopProducts: List["ProductShopItem"]

class ProductMap(BaseModel):
    Id: int
    ShopName: str
    ErpProductId: int
    ShopProductId: str
    CountryId: int

class ProductMapCreate(BaseModel):
    ErpProductId: int
    ShopProductId: str
    CountryId: int

class ProductShopItem(BaseModel):
    ShopId: str
