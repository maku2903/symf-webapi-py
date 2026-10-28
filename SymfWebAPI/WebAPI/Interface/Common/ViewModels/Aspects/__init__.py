from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import enumSplitValueType

class Aspect(BaseModel):
    Index: int
    Value: str
    DictionaryValue: str

class AspectDocument(BaseModel):
    Id: int
    DocumentNumber: str
    Buffer: bool
    IssueDate: Optional[datetime]
    Positions: List["AspectPositionDetails"]

class AspectPosition(BaseModel):
    Id: int

class AspectPositionDetails(BaseModel):
    No: int
    ProductId: Optional[int]
    Quantity: Decimal
    NetValuePLN: Decimal
    AspectSplits: List["AspectSplitDetails"]
    Id: int

class AspectPositionEdit(BaseModel):
    SplitValueType: "enumSplitValueType"
    AspectSplits: List["AspectSplit"]
    Id: int

class AspectSplit(BaseModel):
    SplitValue: Decimal
    Aspects: List["Aspect"]

class AspectSplitDetails(BaseModel):
    Percent: Decimal
    SplitValue: Decimal
    Aspects: List["Aspect"]
