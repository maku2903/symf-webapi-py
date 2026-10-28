from __future__ import annotations

from pydantic import BaseModel

from typing import Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumVatRegisterKind,
    enumVatRegisterType,
    enumYearClosingStatus,
)

class Account(BaseModel):
    Synthetic: int
    Analytic1: int
    Analytic2: int
    Analytic3: int
    Analytic4: int
    Analytic5: int

class CurrencyTable(BaseModel):
    Id: int
    Date: datetime
    CurrencyId: int
    Table: str
    Description: str
    SaleCurrencyRate: Decimal
    PurchaseCurrencyRate: Decimal

class FKF_Common_ViewModels_Country(BaseModel):
    Id: int
    Name: str
    Code: str
    Active: bool
Country = FKF_Common_ViewModels_Country

class FKF_Common_ViewModels_Currency(BaseModel):
    Id: int
    Shortcut: str
    Name: str
    Active: bool
Currency = FKF_Common_ViewModels_Currency

class FKF_Common_ViewModels_Dimension(BaseModel):
    Name: str
    Code: str
    Value: Optional[str]
    DictionaryValue: Optional[str]
    Type: str
Dimension = FKF_Common_ViewModels_Dimension

class FKF_Common_ViewModels_DimensionClassification(BaseModel):
    Id: int
    Name: str
    Code: str
    Type: str
    DictionaryId: Optional[int]
    Index: Optional[int]
DimensionClassification = FKF_Common_ViewModels_DimensionClassification

class FKF_Common_ViewModels_Marker(BaseModel):
    Subtype: int
    Name: str
    Active: bool
Marker = FKF_Common_ViewModels_Marker

class FKF_Common_ViewModels_Region(BaseModel):
    Id: int
    Name: str
    Description: str
    Active: bool
Region = FKF_Common_ViewModels_Region

class FKF_Common_ViewModels_VatRate(BaseModel):
    Id: int
    Code: str
    Rate: str
    IsActive: bool
    DateFrom: Optional[datetime]
    DateTo: Optional[datetime]
VatRate = FKF_Common_ViewModels_VatRate

class FilterCriteria(BaseModel):
    Code: str
    Value: str

class TaxOffice(BaseModel):
    Id: int
    Position: int
    Code: str
    Name: str
    City: Optional[str]
    IsActive: bool

class VatRegister(BaseModel):
    Id: int
    Name: str
    Type: "enumVatRegisterType"
    Kind: "enumVatRegisterKind"
    Active: bool
    Correction: bool
    Period: Optional[int]

class VatRegisterMarker(BaseModel):
    Id: int
    Code: str
    IsActive: bool

class Year(BaseModel):
    Id: int
    Code: str
    Closed: "enumYearClosingStatus"
    Archived: bool
    StartDate: datetime
    EndDate: datetime
    Length: int
