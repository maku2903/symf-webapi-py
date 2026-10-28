from __future__ import annotations

from typing import Any, TypedDict

class IndividualDiscountJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Active: bool
    Value: float | int
    Currency: str
    Type: Any
    SubjectType: Any

class IndividualDiscountListElementJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Active: bool
    SubjectType: Any
    IndividualDiscounts: list[IndividualDiscountJSON]

class PriceCalculationProductResultJSON(TypedDict):
    Price: float | int
    Id: int
    Quantity: float | int

class PriceCalculationResultJSON(TypedDict):
    Products: list[PriceCalculationProductResultJSON]
    DepartmentId: int
    ContractorId: int
    Date: str
    PriceType: Any
    Currency: str

class PriceFactorJSON(TypedDict):
    Code: str
    PriceType: Any
    Value: float | int
    Currency: str
    Type: Any
    PriceListId: int | None
    ProductId: int | None
    ProductKindId: int | None
    ContractorId: int | None
    ContractorKindId: int | None
    DepartmentId: int | None
    Priority: int
    MinimalPriority: int
    ConnectionType: Any
    TimeLimited: bool

class PriceOrderContractorJSON(TypedDict):
    Id: int | None
    Code: str

class PriceOrderProductResultJSON(TypedDict):
    Id: int
    Price: float | int
    Code: str
    Quantity: float | int

class PriceOrderResultJSON(TypedDict):
    Contractor: PriceOrderContractorJSON
    Products: list[PriceOrderProductResultJSON]
    Department: str
    Date: str
    SalePriceType: Any
    Currency: str

class ProductPriceListElementJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Active: bool
    SalePrices: list[ProductSalePriceBaseJSON]

class ProductSalePriceBaseJSON(TypedDict):
    Type: Any
    ProfitPercent: float | int
    MarkupPercent: float | int
    LinkedWithBasePrice: bool
    Kind: Any
    PriceParameter: Any
    Value: float | int
    Currency: str

class QuantitativeDiscountJSON(TypedDict):
    QuantityFrom: float | int
    QuantityTo: float | int | None
    Value: float | int
    Currency: str
    Type: Any

class QuantitativeDiscountListElementJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Active: bool
    Discounts: list[QuantitativeDiscountJSON]
