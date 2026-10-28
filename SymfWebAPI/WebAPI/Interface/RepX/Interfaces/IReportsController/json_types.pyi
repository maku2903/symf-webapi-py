from __future__ import annotations

from typing import Any, TypedDict

class PDFJSON(TypedDict):
    Hash_SHA1: str
    ContentFile_Base64: str
    CreateDate: str

class ReportDefinitionJSON(TypedDict):
    Id: int
    IsActive: bool
    Name: str
    Location: Any
