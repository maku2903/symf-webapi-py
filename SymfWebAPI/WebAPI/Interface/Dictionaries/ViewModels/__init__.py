from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from SymfWebAPI.WebAPI.Interface.Enums import DictionaryElementType, DictionaryType

class BusinessDictionary(BaseModel):
    Id: "DictionaryType"
    Code: str
    Name: str
    Elements: List["BusinessDictionaryElement"]

class BusinessDictionaryElement(BaseModel):
    Id: Optional[int]
    Code: str
    Position: str
    Type: "DictionaryElementType"
    DimensionValue: str

class ContractorPosition(BaseModel):
    Id: int
    Position: int

class Dictionary(BaseModel):
    Id: int
    Code: str
    Name: str
    Active: bool
    DefaultElementId: Optional[int]
    SuggestedElementId: Optional[int]
    NonSetElementId: Optional[int]
    Elements: List["DictionaryElement"]

class DictionaryElement(BaseModel):
    Id: Optional[int]
    Position: Optional[int]
    Active: bool
    Code: str
    Name: str
    Description: str
    Attributes: List["DictionaryElementAttribute"]

class DictionaryElementAttribute(BaseModel):
    Id: int
    Inherited: bool
    Name: str
    Value: str
    Type: str

class DictionaryListElement(BaseModel):
    Id: int
    Code: str
    Name: str
    Active: Optional[bool]
