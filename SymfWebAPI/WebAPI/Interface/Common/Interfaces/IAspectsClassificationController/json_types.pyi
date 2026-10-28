from __future__ import annotations

from typing import Any, TypedDict

class DimensionClassificationJSON(TypedDict):
    Id: int
    Name: str
    Code: str
    Type: str
    DictionaryId: int | None
    Index: int | None
