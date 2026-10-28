from __future__ import annotations

from typing import Any, TypedDict

class SessionInformationJSON(TypedDict):
    Token: str
    DeviceName: str
    RegisterTime: str
    ExpireTime: str
    TotalSessionsCount: int
