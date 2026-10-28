from __future__ import annotations

from typing import Any, TypedDict

class DimensionJSON(TypedDict):
    Name: str
    Code: str
    Value: str | None
    DictionaryValue: str | None
    Type: str

class ContractorJSON(TypedDict):
    Id: int | None
    Position: int | None
    Active: bool
    Code: str
    Name: str
    Vies: bool
    VATTaxPayer: bool
    SplitPayment: Any
    NIP: str | None
    Regon: str
    Pesel: str
    CreditLimit: bool
    MaxCreditValue: float | int
    CreditCurrency: str
    Type: Any
    Contact: ContractorContactJSON
    Address: ContractorAddressJSON
    BankInfo: ContractorBankInfoJSON
    Dimensions: list[DimensionJSON]

class ContractorAddressJSON(TypedDict):
    Country: str
    City: str | None
    Province: str
    Street: str | None
    HouseNo: str | None
    ApartmentNo: str | None
    PostCode: str | None

class ContractorBankInfoJSON(TypedDict):
    AccountNumber: str | None
    BankName: str | None

class ContractorContactJSON(TypedDict):
    Name: str
    Surname: str
    Phone1: str
    Phone2: str
    Fax: str
    Telex: str
    Email: str
    WWW: str
    Facebook: str

class ContractorListElementJSON(TypedDict):
    Id: int
    Position: int
    Code: str
    Name: str
    Type: Any | None
    NIP: str | None
    Active: bool
    Place: str
    PostCode: str | None

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
    Data: list[ContractorListElementJSON]
