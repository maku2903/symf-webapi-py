from __future__ import annotations

from pydantic import BaseModel

import importlib
from typing import TYPE_CHECKING
from typing import List, Optional
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import enumContractorSplitPayment, enumContractorType
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels.CriteriaFilter import (
    IntCriteriaFilter,
    StringCriteriaFilter,
)

class FKF_Contractors_ViewModels_Contractor(BaseModel):
    Id: Optional[int]
    Position: Optional[int]
    Active: bool
    Code: str
    Name: str
    Vies: bool
    VATTaxPayer: bool
    SplitPayment: "enumContractorSplitPayment"
    NIP: Optional[str]
    Regon: str
    Pesel: str
    CreditLimit: bool
    MaxCreditValue: Decimal
    CreditCurrency: str
    Type: "enumContractorType"
    Contact: "ContractorContact"
    Address: "ContractorAddress"
    BankInfo: "ContractorBankInfo"
    Dimensions: List["Dimension"]
Contractor = FKF_Contractors_ViewModels_Contractor

class FKF_Contractors_ViewModels_ContractorAddress(BaseModel):
    Country: str
    City: Optional[str]
    Province: str
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]
ContractorAddress = FKF_Contractors_ViewModels_ContractorAddress

class FKF_Contractors_ViewModels_ContractorBankInfo(BaseModel):
    AccountNumber: Optional[str]
    BankName: Optional[str]
ContractorBankInfo = FKF_Contractors_ViewModels_ContractorBankInfo

class FKF_Contractors_ViewModels_ContractorContact(BaseModel):
    Name: str
    Surname: str
    Phone1: str
    Phone2: str
    Fax: str
    Telex: str
    Email: str
    WWW: str
    Facebook: str
ContractorContact = FKF_Contractors_ViewModels_ContractorContact

class FKF_Contractors_ViewModels_ContractorCriteriaFilter(BaseModel):
    Code: "StringCriteriaFilter"
    Name: "StringCriteriaFilter"
    NIP: Optional["StringCriteriaFilter"]
    City: Optional["StringCriteriaFilter"]
    Province: "StringCriteriaFilter"
    Marker: "IntCriteriaFilter"
    Active: Optional[bool]
    Country: "StringCriteriaFilter"
    EmailDomain: "StringCriteriaFilter"
    KindId: Optional[int]
    CatalogId: Optional[int]
ContractorCriteriaFilter = FKF_Contractors_ViewModels_ContractorCriteriaFilter

class FKF_Contractors_ViewModels_ContractorListElement(BaseModel):
    Id: int
    Position: int
    Code: str
    Name: str
    Type: Optional["enumContractorType"]
    NIP: Optional[str]
    Active: bool
    Place: str
    PostCode: Optional[str]
ContractorListElement = FKF_Contractors_ViewModels_ContractorListElement

_VERSIONED_CHILDREN = ['V2026_1']

_VERSIONED_EXPORTS = {
}

def __getattr__(name: str):
    if name in _VERSIONED_CHILDREN:
        value = importlib.import_module(f".{name}", __name__)
        globals()[name] = value
        return value
    child_name = _VERSIONED_EXPORTS.get(name)
    if child_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = importlib.import_module(f".{child_name}", __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value

def __dir__():
    return sorted(set(_VERSIONED_CHILDREN) | set(_VERSIONED_EXPORTS) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import V2026_1
