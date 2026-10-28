from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import (
    Catalog,
    Dimension,
    Kind,
    PaymentFormBase,
    PaymentRegistryBase,
)
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import (
    ContractorBankInfo,
    ContractorContact,
    ContractorCorrespondenceAddress,
    ContractorDefaultAddress,
    ContractorDeliveryAddress,
    ContractorFK,
)
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumContractorSplitPayment,
    enumContractorType,
    enumPriceKind,
    enumSalePriceType,
)

class ContractorV2026_2(BaseModel):
    Jst: Optional[bool]
    VatGroup: Optional[bool]
    LinkedUnit: bool
    Id: Optional[int]
    Active: bool
    Code: str
    Name: str
    Vies: bool
    VATTaxPayer: bool
    NIP: str
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
    Note: str
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
    RtfNote: str
