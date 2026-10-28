from __future__ import annotations

from typing import Any, TypedDict

class DimensionJSON(TypedDict):
    Name: str
    Code: str
    Value: str | None
    DictionaryValue: str | None
    Type: str
