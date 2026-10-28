from __future__ import annotations

from typing import Any, TypedDict

class ProductPhotoJSON(TypedDict):
    Id: int
    Name: str
    Description: str
    CreateDate: str
    ContentFile_Base64: str
    PhotoQuality: Any

class ProductPhotoListElementJSON(TypedDict):
    Id: int
    Name: str
    Description: str
    CreateDate: str
