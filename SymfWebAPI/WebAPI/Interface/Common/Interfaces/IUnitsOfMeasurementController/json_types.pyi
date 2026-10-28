from __future__ import annotations

from typing import Any, TypedDict

class UnitOfMeasurementJSON(TypedDict):
    Id: int
    Name: str
    Description: str
    Active: bool

class UnitOfMeasurementDefinitionJSON(TypedDict):
    Guid: str
    Name: str
    No: int
