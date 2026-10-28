from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumIndividualDiscountSubjectType,
    enumPriceFactorType,
    enumPriceKind,
    enumPriceListConnectionType,
    enumPriceParameter,
    enumPriceRecalculateType,
    enumPriceType,
    enumSalePriceType,
)

class IndividualDiscount(BaseModel):
    Id: int
    Code: str
    Name: str
    Active: bool
    Value: Decimal
    Currency: str
    Type: "enumPriceFactorType"
    SubjectType: "enumIndividualDiscountSubjectType"

class IndividualDiscountListElement(BaseModel):
    Id: int
    Code: str
    Name: str
    Active: bool
    SubjectType: "enumIndividualDiscountSubjectType"
    IndividualDiscounts: List["IndividualDiscount"]

class PriceFactor(BaseModel):
    Code: str
    PriceType: "enumPriceType"
    Value: Decimal
    Currency: str
    Type: "enumPriceFactorType"
    PriceListId: Optional[int]
    ProductId: Optional[int]
    ProductKindId: Optional[int]
    ContractorId: Optional[int]
    ContractorKindId: Optional[int]
    DepartmentId: Optional[int]
    Priority: int
    MinimalPriority: int
    ConnectionType: "enumPriceListConnectionType"
    TimeLimited: bool

class PriceFactorCriteria(BaseModel):
    PriceType: "enumSalePriceType"
    Quantity: Decimal
    PeriodPricing: bool
    DatePrice: Optional[datetime]
    ProductKindId: Optional[int]
    ProductId: Optional[int]
    ContractorKindId: Optional[int]
    ContractorId: Optional[int]
    DepartmentId: Optional[int]

class ProductBasePrice(BaseModel):
    Date: datetime
    Value: Decimal
    Currency: str

class ProductListElementSalePrice(BaseModel):
    Type: "enumSalePriceType"
    Kind: "enumPriceKind"
    Value: Decimal
    Currency: str

class ProductPrice(BaseModel):
    Value: Decimal
    Currency: str

class ProductPriceListElement(BaseModel):
    Id: int
    Code: str
    Name: str
    Active: bool
    SalePrices: List["ProductSalePriceBase"]

class ProductPricesEdit(BaseModel):
    SalePriceRecalculate: bool
    CurrencyMode: bool
    CurrencyRateWithoutConversion: Decimal
    CurrencyRate: Decimal
    CurrencyRateDate: datetime
    PriceParameter: Optional["enumPriceParameter"]
    PriceRecalculateType: Optional["enumPriceRecalculateType"]
    BasePrice: "ProductBasePrice"
    PurchasePrice: "ProductPrice"
    PurchasePriceInCurrency: "ProductPrice"
    CalcExcise: "ProductPrice"
    CalcDuty: "ProductPrice"
    CalcOther: "ProductPrice"
    SalePrices: List["ProductSalePrice"]

class ProductSalePrice(BaseModel):
    AutomaticValue: bool
    Type: "enumSalePriceType"
    ProfitPercent: Decimal
    MarkupPercent: Decimal
    LinkedWithBasePrice: bool
    Kind: "enumPriceKind"
    PriceParameter: "enumPriceParameter"
    Value: Decimal
    Currency: str

class ProductSalePriceBase(BaseModel):
    Type: "enumSalePriceType"
    ProfitPercent: Decimal
    MarkupPercent: Decimal
    LinkedWithBasePrice: bool
    Kind: "enumPriceKind"
    PriceParameter: "enumPriceParameter"
    Value: Decimal
    Currency: str

class QuantitativeDiscount(BaseModel):
    QuantityFrom: Decimal
    QuantityTo: Optional[Decimal]
    Value: Decimal
    Currency: str
    Type: "enumPriceFactorType"

class QuantitativeDiscountListElement(BaseModel):
    Id: int
    Code: str
    Name: str
    Active: bool
    Discounts: List["QuantitativeDiscount"]
