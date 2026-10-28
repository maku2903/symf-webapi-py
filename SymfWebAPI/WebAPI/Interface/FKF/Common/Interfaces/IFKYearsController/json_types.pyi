from __future__ import annotations

from typing import Any, TypedDict

class YearJSON(TypedDict):
    Id: int
    Code: str
    Closed: Any
    Archived: bool
    StartDate: str
    EndDate: str
    Length: int
