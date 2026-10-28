from __future__ import annotations

from typing import Any, TypedDict

class BusinessDictionaryJSON(TypedDict):
    Id: Any
    Code: str
    Name: str
    Elements: list[BusinessDictionaryElementJSON]

class BusinessDictionaryElementJSON(TypedDict):
    Id: int | None
    Code: str
    Position: str
    Type: Any
    DimensionValue: str

class ContractorPositionJSON(TypedDict):
    Id: int
    Position: int

class DictionaryJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Active: bool
    DefaultElementId: int | None
    SuggestedElementId: int | None
    NonSetElementId: int | None
    Elements: list[DictionaryElementJSON]

class DictionaryElementJSON(TypedDict):
    Id: int | None
    Position: int | None
    Active: bool
    Code: str
    Name: str
    Description: str
    Attributes: list[DictionaryElementAttributeJSON]

class DictionaryElementAttributeJSON(TypedDict):
    Id: int
    Inherited: bool
    Name: str
    Value: str
    Type: str

class DictionaryListElementJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Active: bool | None
