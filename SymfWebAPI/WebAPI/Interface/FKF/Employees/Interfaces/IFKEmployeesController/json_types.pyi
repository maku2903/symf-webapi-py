from __future__ import annotations

from typing import Any, TypedDict

class EmployeeJSON(TypedDict):
    Id: int | None
    Position: int | None
    Active: bool
    Code: str
    Name: str
    SecondName: str
    Surname: str
    NIP: str | None
    Pesel: str
    Phone: str
    Address: EmployeeAddressJSON
    BankInfo: EmployeeBankInfoJSON

class EmployeeAddressJSON(TypedDict):
    City: str | None
    Street: str | None
    HouseNo: str | None
    ApartmentNo: str | None
    PostCode: str | None

class EmployeeBankInfoJSON(TypedDict):
    AccountNumber: str | None
    BankName: str | None

class EmployeeListElementJSON(TypedDict):
    Id: int
    Position: int
    Code: str
    Name: str
    Surname: str
    NIP: str | None
    Pesel: str
    Active: bool
    Place: str

class PageJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[Any]

class GetPagedDocumentJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[EmployeeListElementJSON]
