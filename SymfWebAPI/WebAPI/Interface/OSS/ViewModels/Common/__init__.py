from __future__ import annotations

from pydantic import BaseModel

from typing import Optional
from decimal import Decimal

class OssCatalog(BaseModel):
    FullPath: str
    AddIfNotExist: bool

class OssContractor(BaseModel):
    Id: Optional[int]
    Code: str
    RecalculatePrices: bool
    Data: "OssOrderContractorData"

class OssDelivery(BaseModel):
    Id: Optional[int]
    Code: str
    Quantity: Decimal

class OssKind(BaseModel):
    Code: str
    AddIfNotExist: bool

class OssOrderContractorData(BaseModel):
    Name: str
    NIP: Optional[str]
    City: Optional[str]
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]
    Country: str
