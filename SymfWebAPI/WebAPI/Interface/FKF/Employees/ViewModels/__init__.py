from __future__ import annotations

from pydantic import BaseModel

from typing import Optional

class Employee(BaseModel):
    Id: Optional[int]
    Position: Optional[int]
    Active: bool
    Code: str
    Name: str
    SecondName: str
    Surname: str
    NIP: Optional[str]
    Pesel: str
    Phone: str
    Address: "EmployeeAddress"
    BankInfo: "EmployeeBankInfo"

class EmployeeAddress(BaseModel):
    City: Optional[str]
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]

class EmployeeBankInfo(BaseModel):
    AccountNumber: Optional[str]
    BankName: Optional[str]

class EmployeeListElement(BaseModel):
    Id: int
    Position: int
    Code: str
    Name: str
    Surname: str
    NIP: Optional[str]
    Pesel: str
    Active: bool
    Place: str
