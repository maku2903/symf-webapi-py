from __future__ import annotations

from typing import Any, TypedDict

class ContractorDeliveryAddressJSON(TypedDict):
    Id: int | None
    Code: str
    Country: str
    City: str | None
    Province: str
    Street: str | None
    HouseNo: str | None
    ApartmentNo: str | None
    PostCode: str | None
    FullAddress: str
