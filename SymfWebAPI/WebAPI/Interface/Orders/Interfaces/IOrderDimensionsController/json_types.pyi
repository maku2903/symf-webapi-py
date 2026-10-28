from __future__ import annotations

from typing import Any, TypedDict

class AspectJSON(TypedDict):
    Index: int
    Value: str
    DictionaryValue: str

class AspectDocumentJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Buffer: bool
    IssueDate: str | None
    Positions: list[AspectPositionDetailsJSON]

class AspectPositionDetailsJSON(TypedDict):
    No: int
    ProductId: int | None
    Quantity: float | int
    NetValuePLN: float | int
    AspectSplits: list[AspectSplitDetailsJSON]
    Id: int

class AspectSplitDetailsJSON(TypedDict):
    Percent: float | int
    SplitValue: float | int
    Aspects: list[AspectJSON]

class DimensionJSON(TypedDict):
    Name: str
    Code: str
    Value: str | None
    DictionaryValue: str | None
    Type: str

class DimensionClassificationJSON(TypedDict):
    Id: int
    Name: str
    Code: str
    Type: str
    DictionaryId: int | None
    Index: int | None

class PositionDimensionJSON(TypedDict):
    PositionId: int
    Dimensions: list[DimensionJSON]
