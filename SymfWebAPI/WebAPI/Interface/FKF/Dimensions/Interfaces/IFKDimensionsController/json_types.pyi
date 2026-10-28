from __future__ import annotations

from typing import Any, TypedDict

class DocumentRecordDimensionJSON(TypedDict):
    Index: int
    Value: str | None

class DocumentRecordDimensionSplitJSON(TypedDict):
    SplitValue: float | int
    Percent: float | int
    Dimensions: list[DocumentRecordDimensionJSON]

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

class DocumentJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Source: Any
    YearId: int
    DocumentDate: str
    ContractorPosition: int
    Records: list[DocumentRecordJSON]

class DocumentRecordJSON(TypedDict):
    Id: int
    No: int
    SplitNo: int
    Side: Any
    Account: str
    Value: float | int
    ValuePLN: float | int
    Currency: str
    DimensionSplits: list[DocumentRecordDimensionSplitJSON]
