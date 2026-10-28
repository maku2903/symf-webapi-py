from __future__ import annotations

from pydantic import BaseModel

import importlib
from typing import TYPE_CHECKING
from typing import List, Optional
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import (
    Catalog,
    Dimension,
    FilterDimensionCriteria,
    Kind,
    PaymentFormBase,
    PaymentRegistryBase,
)
from SymfWebAPI.WebAPI.Interface.Common.ViewModels.CriteriaFilter import (
    IntCriteriaFilter,
    StringCriteriaFilter,
)
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumContractorSplitPayment,
    enumContractorType,
    enumFilterCriteriaMode,
    enumPriceKind,
    enumSalePriceType,
)

class ContractorCorrespondenceAddress(BaseModel):
    Country: str
    City: Optional[str]
    Province: str
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]
    FullAddress: str

class ContractorDefaultAddress(BaseModel):
    Country: str
    City: Optional[str]
    Province: str
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]
    FullAddress: str

class ContractorDeliveryAddress(BaseModel):
    Id: Optional[int]
    Code: str
    Country: str
    City: Optional[str]
    Province: str
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]
    FullAddress: str

class ContractorFK(BaseModel):
    IdFK: str
    IdFKSync: Optional[int]
    IdentFK: str
    ParameterFK: str

class ContractorFilterCriteria(BaseModel):
    Code_From: str
    Code_To: str
    Code_Mode: Optional["enumFilterCriteriaMode"]
    Name_From: str
    Name_To: str
    Name_Mode: Optional["enumFilterCriteriaMode"]
    NIP_From: str
    NIP_To: str
    NIP_Mode: Optional["enumFilterCriteriaMode"]
    City_From: str
    City_To: str
    City_Mode: Optional["enumFilterCriteriaMode"]
    Province_From: str
    Province_To: str
    Province_Mode: Optional["enumFilterCriteriaMode"]
    Marker_From: int
    Marker_To: int
    Marker_Mode: Optional["enumFilterCriteriaMode"]
    Active: Optional[bool]
    Country: str
    Dimensions: List["FilterDimensionCriteria"]

class ContractorListElementWithDimensions(BaseModel):
    Dimensions: List["Dimension"]
    Id: int
    Code: str
    Name: str
    Type: Optional["enumContractorType"]
    NIP: Optional[str]
    Pesel: str
    Active: bool
    PriceType: Optional["enumSalePriceType"]
    PriceKind: Optional["enumPriceKind"]
    PaymentFormOid: int
    PaymentRegistryOid: int
    Place: str
    PostCode: Optional[str]

class Contractors_ViewModels_Contractor(BaseModel):
    Id: Optional[int]
    Active: bool
    Code: str
    Name: str
    Vies: bool
    VATTaxPayer: bool
    NIP: Optional[str]
    Pesel: str
    Regon: str
    CreditLimit: bool
    MaxCreditValue: Decimal
    CreditCurrency: str
    PriceNegotiation: bool
    DefaultDiscountPercent: Decimal
    PriceType: "enumSalePriceType"
    PriceKind: "enumPriceKind"
    Type: "enumContractorType"
    SplitPayment: "enumContractorSplitPayment"
    Note: Optional[str]
    Marker: int
    Due: Decimal
    Obligation: Decimal
    PaymentRegistry: "PaymentRegistryBase"
    PaymentForm: "PaymentFormBase"
    Contact: "ContractorContact"
    DefaultAddress: "ContractorDefaultAddress"
    CorrespondenceAddress: "ContractorCorrespondenceAddress"
    BankInfo: "ContractorBankInfo"
    FK: "ContractorFK"
    Catalog: "Catalog"
    Kind: "Kind"
    Dimensions: List["Dimension"]
    DeliveryAddresses: List["ContractorDeliveryAddress"]
    RtfNote: Optional[str]
Contractor = Contractors_ViewModels_Contractor

class Contractors_ViewModels_ContractorAddress(BaseModel):
    Country: str
    City: Optional[str]
    Province: str
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    PostCode: Optional[str]
    FullAddress: str
ContractorAddress = Contractors_ViewModels_ContractorAddress

class Contractors_ViewModels_ContractorBankInfo(BaseModel):
    AccountNumber: Optional[str]
    AccountNumer: str
    BankName: Optional[str]
    SWIFT_BIC: str
ContractorBankInfo = Contractors_ViewModels_ContractorBankInfo

class Contractors_ViewModels_ContractorContact(BaseModel):
    Name: str
    Surname: str
    Phone1: str
    Phone2: str
    Fax: str
    Email: str
    WWW: str
    Facebook: str
ContractorContact = Contractors_ViewModels_ContractorContact

class Contractors_ViewModels_ContractorCriteriaFilter(BaseModel):
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
ContractorCriteriaFilter = Contractors_ViewModels_ContractorCriteriaFilter

class Contractors_ViewModels_ContractorListElement(BaseModel):
    Id: int
    Code: str
    Name: str
    Type: Optional["enumContractorType"]
    NIP: Optional[str]
    Pesel: str
    Active: bool
    PriceType: Optional["enumSalePriceType"]
    PriceKind: Optional["enumPriceKind"]
    PaymentFormOid: int
    PaymentRegistryOid: int
    Place: str
    PostCode: Optional[str]
ContractorListElement = Contractors_ViewModels_ContractorListElement

_VERSIONED_CHILDREN = ['V2026_1', 'V2026_2']

_VERSIONED_EXPORTS = {
    'ContractorV2026_1': 'V2026_1',
    'ContractorV2026_2': 'V2026_2',
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
    from . import V2026_2
    from .V2026_1 import ContractorV2026_1
    from .V2026_2 import ContractorV2026_2
