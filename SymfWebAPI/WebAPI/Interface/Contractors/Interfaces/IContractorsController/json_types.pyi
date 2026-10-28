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

class MarkerJSON(TypedDict):
    Subtype: int
    Name: str
    Active: bool

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

class ContractorListElementWithDimensionsJSON(TypedDict):
    Dimensions: list[DimensionJSON]
    Id: int
    Code: str
    Name: str
    Type: Any | None
    NIP: str | None
    Pesel: str | None
    Active: bool
    PriceType: Any | None
    PriceKind: Any | None
    PaymentFormOid: int
    PaymentRegistryOid: int
    Place: str | None
    PostCode: str | None

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

class ContractorListElementJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Type: Any | None
    NIP: str | None
    Pesel: str | None
    Active: bool
    PriceType: Any | None
    PriceKind: Any | None
    PaymentFormOid: int
    PaymentRegistryOid: int
    Place: str | None
    PostCode: str | None

class IncrementalSyncListElementJSON(TypedDict):
    Id: int
    ModifyType: Any
    ModifiedAt: str
    Object: Any

class KindJSON(TypedDict):
    Id: int | None
    Code: str
    Active: bool

class PageJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[Any]

class PaymentFormBaseJSON(TypedDict):
    Id: int | None
    Client: int

class PaymentRegistryBaseJSON(TypedDict):
    Id: int | None
    Code: str
    AccountNumber: str | None

class GetPagedDocumentJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[ContractorListElementJSON]

class GetPagedDocumentWithDimensionsJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[Any]
