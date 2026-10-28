from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import enumContractorSplitPayment, enumContractorType
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.FKF.Contractors.ViewModels import (
    ContractorAddress,
    ContractorBankInfo,
    ContractorContact,
)

class FKF_Contractors_ViewModels_V2026_1_Contractor(BaseModel):
    LinkedUnit: Optional[bool]
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
Contractor = FKF_Contractors_ViewModels_V2026_1_Contractor
