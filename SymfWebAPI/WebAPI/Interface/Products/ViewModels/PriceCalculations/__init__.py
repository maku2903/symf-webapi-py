from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import enumPriceCalculationMethod, enumSalePriceType

class PriceCalculation(BaseModel):
    DepartmentId: int
    ContractorId: int
    Date: datetime
    PriceType: "enumSalePriceType"
    Currency: str

class PriceCalculationCriteria(BaseModel):
    CalculationMethod: "enumPriceCalculationMethod"
    Products: List["PriceCalculationProductCriteria"]
    DepartmentId: int
    ContractorId: int
    Date: datetime
    PriceType: "enumSalePriceType"
    Currency: str

class PriceCalculationProduct(BaseModel):
    Id: int
    Quantity: Decimal

class PriceCalculationProductCriteria(BaseModel):
    Id: int
    Quantity: Decimal

class PriceCalculationProductResult(BaseModel):
    Price: Decimal
    Id: int
    Quantity: Decimal

class PriceCalculationResult(BaseModel):
    Products: List["PriceCalculationProductResult"]
    DepartmentId: int
    ContractorId: int
    Date: datetime
    PriceType: "enumSalePriceType"
    Currency: str

class PriceOrder(BaseModel):
    Department: str
    Date: datetime
    SalePriceType: "enumSalePriceType"
    Currency: str

class PriceOrderContractor(BaseModel):
    Id: Optional[int]
    Code: str

class PriceOrderContractorCriteria(BaseModel):
    Id: Optional[int]
    Code: str

class PriceOrderCriteria(BaseModel):
    Contractor: "PriceOrderContractorCriteria"
    TypeCode: str
    Series: str
    Products: List["PriceOrderProductCriteria"]
    Department: str
    Date: datetime
    SalePriceType: "enumSalePriceType"
    Currency: str

class PriceOrderProduct(BaseModel):
    Code: str
    Quantity: Decimal

class PriceOrderProductCriteria(BaseModel):
    Code: str
    Quantity: Decimal

class PriceOrderProductResult(BaseModel):
    Id: int
    Price: Decimal
    Code: str
    Quantity: Decimal

class PriceOrderResult(BaseModel):
    Contractor: "PriceOrderContractor"
    Products: List["PriceOrderProductResult"]
    Department: str
    Date: datetime
    SalePriceType: "enumSalePriceType"
    Currency: str
