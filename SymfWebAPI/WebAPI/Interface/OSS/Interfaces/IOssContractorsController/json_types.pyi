from __future__ import annotations

from typing import Any, TypedDict

class CatalogJSON(TypedDict):
    Id: int
    ParentId: int
    Name: str
    FullPath: str

class DimensionJSON(TypedDict):
    Name: str
    Code: str
    Value: str | None
    DictionaryValue: str | None
    Type: str

class ContractorCorrespondenceAddressJSON(TypedDict):
    Country: str
    City: str | None
    Province: str
    Street: str | None
    HouseNo: str | None
    ApartmentNo: str | None
    PostCode: str | None
    FullAddress: str

class ContractorDefaultAddressJSON(TypedDict):
    Country: str
    City: str | None
    Province: str
    Street: str | None
    HouseNo: str | None
    ApartmentNo: str | None
    PostCode: str | None
    FullAddress: str

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

class ContractorFKJSON(TypedDict):
    IdFK: str
    IdFKSync: int | None
    IdentFK: str
    ParameterFK: str

class ContractorJSON(TypedDict):
    Id: int | None
    Active: bool
    Code: str
    Name: str
    Vies: bool
    VATTaxPayer: bool
    NIP: str | None
    Pesel: str
    Regon: str
    CreditLimit: bool
    MaxCreditValue: float | int
    CreditCurrency: str
    PriceNegotiation: bool
    DefaultDiscountPercent: float | int
    PriceType: Any
    PriceKind: Any
    Type: Any
    SplitPayment: Any
    Note: str | None
    Marker: int
    Due: float | int
    Obligation: float | int
    PaymentRegistry: PaymentRegistryBaseJSON
    PaymentForm: PaymentFormBaseJSON
    Contact: ContractorContactJSON
    DefaultAddress: ContractorDefaultAddressJSON
    CorrespondenceAddress: ContractorCorrespondenceAddressJSON
    BankInfo: ContractorBankInfoJSON
    FK: ContractorFKJSON
    Catalog: CatalogJSON
    Kind: KindJSON
    Dimensions: list[DimensionJSON]
    DeliveryAddresses: list[ContractorDeliveryAddressJSON]
    RtfNote: str | None

class ContractorBankInfoJSON(TypedDict):
    AccountNumber: str | None
    AccountNumer: str
    BankName: str | None
    SWIFT_BIC: str

class ContractorContactJSON(TypedDict):
    Name: str
    Surname: str
    Phone1: str
    Phone2: str
    Fax: str
    Email: str
    WWW: str
    Facebook: str

class KindJSON(TypedDict):
    Id: int | None
    Code: str
    Active: bool

class PaymentFormBaseJSON(TypedDict):
    Id: int | None
    Client: int

class PaymentRegistryBaseJSON(TypedDict):
    Id: int | None
    Code: str
    AccountNumber: str | None
