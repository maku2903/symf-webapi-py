from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import (
    Catalog,
    Dimension,
    FilterDimensionCriteria,
    Kind,
    VatRateBase,
)
from SymfWebAPI.WebAPI.Interface.Common.ViewModels.CriteriaFilter import (
    IntCriteriaFilter,
    StringCriteriaFilter,
)
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumDefaultUnitOfMeasurementKind,
    enumFilterCriteriaMode,
    enumJPK_V7ProductGroup,
    enumPhotoQuality,
    enumPriceParameter,
    enumPriceRecalculateType,
    enumPriceRounding,
    enumProductType,
    enumSettlementMethod,
)
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import (
    ProductBasePrice,
    ProductListElementSalePrice,
    ProductPrice,
    ProductSalePrice,
)

class Product(BaseModel):
    Id: Optional[int]
    Active: bool
    Code: str
    Name: str
    Type: "enumProductType"
    Barcode: str
    PKWiU: str
    CNFull: str
    CN: str
    DeliveryScheme: str
    FiscalName: str
    AgriculturalPromotionFund: str
    PriceNegotiation: bool
    PriceRounding: Optional["enumPriceRounding"]
    PriceRecalculateType: Optional["enumPriceRecalculateType"]
    SettlementMethod: Optional["enumSettlementMethod"]
    PriceParameter: Optional["enumPriceParameter"]
    VAT50Minus: bool
    ReverseCharge: bool
    SplitPayment: bool
    JPK_V7ProductGroup: Optional["enumJPK_V7ProductGroup"]
    StaticSet: bool
    PriceSetMode: bool
    CollationSetMode: bool
    SalePriceRecalculate: bool
    CurrencyMode: bool
    CurrencyRateWithoutConversion: Decimal
    CurrencyRate: Decimal
    CurrencyConversion: int
    CurrencyRateDate: datetime
    MinState: Decimal
    MaxState: Decimal
    Note: Optional[str]
    Marker: int
    FK: "ProductFK"
    Intrastat: "ProductIntrastat"
    UnitsOfMeasurement: "ProductUnitsOfMeasurement"
    BasePrice: "ProductBasePrice"
    PurchasePrice: "ProductPrice"
    PurchasePriceInCurrency: "ProductPrice"
    SalePrices: List["ProductSalePrice"]
    CalcOther: "ProductPrice"
    CalcExcise: "ProductPrice"
    CalcDuty: "ProductPrice"
    Kind: "Kind"
    Catalog: "Catalog"
    VatRate: Optional["VatRateBase"]
    SetElements: Optional[List["ProductSetElement"]]
    Dimensions: List["Dimension"]
    Barcodes: List["ProductBarcode"]
    LogisticFields: List["ProductLogisticField"]
    RtfNote: Optional[str]

class ProductBarcode(BaseModel):
    Barcode: Optional[str]
    UnitName: str
    UnitOfMeasurement: str
    UnitOfMeasurementGuid: Optional[str]
    SendToKSeF: Optional[bool]

class ProductBarcodes(BaseModel):
    Id: int
    Code: str
    Barcodes: List["ProductBarcode"]

class ProductCriteriaFilter(BaseModel):
    Active: Optional[bool]
    Marker: "IntCriteriaFilter"
    FiscalName: "StringCriteriaFilter"
    CN: "StringCriteriaFilter"
    Barcode: "StringCriteriaFilter"
    Name: "StringCriteriaFilter"
    Code: "StringCriteriaFilter"
    Type: Optional["enumProductType"]
    KindId: Optional[int]
    CatalogId: Optional[int]

class ProductFK(BaseModel):
    IdFK: str
    ParameterFK: str

class ProductFilterCriteria(BaseModel):
    Code_From: str
    Code_To: str
    Code_Mode: Optional["enumFilterCriteriaMode"]
    Name_From: str
    Name_To: str
    Name_Mode: Optional["enumFilterCriteriaMode"]
    Barcode_From: str
    Barcode_To: str
    Barcode_Mode: Optional["enumFilterCriteriaMode"]
    CN_From: int
    CN_To: int
    CN_Mode: Optional["enumFilterCriteriaMode"]
    FiscalName_From: str
    FiscalName_To: str
    FiscalName_Mode: Optional["enumFilterCriteriaMode"]
    Marker_From: int
    Marker_To: int
    Marker_Mode: Optional["enumFilterCriteriaMode"]
    Active: Optional[bool]
    Dimensions: List["FilterDimensionCriteria"]

class ProductIntrastat(BaseModel):
    RatioOfWeight: Decimal
    RatioOfComplementaryUM: Decimal
    ComplementaryUM: str
    UseComplementaryUM: bool

class ProductListElement(BaseModel):
    Id: int
    Code: str
    Name: str
    Active: bool
    Unit: Optional[str]
    DefaultUnit: Optional[str]
    VatRate: Optional[str]
    Type: Optional["enumProductType"]
    Barcode: str
    CN: str
    PKWiU: str
    FiscalName: str

class ProductListElementWithDimensions(BaseModel):
    Dimensions: List["Dimension"]
    Id: int
    Code: str
    Name: str
    Active: bool
    Unit: Optional[str]
    DefaultUnit: Optional[str]
    VatRate: Optional[str]
    Type: Optional["enumProductType"]
    Barcode: str
    CN: str
    PKWiU: str
    FiscalName: str

class ProductListElementWithSalePrices(BaseModel):
    SalePrices: List["ProductListElementSalePrice"]
    Id: int
    Code: str
    Name: str
    Active: bool
    Unit: Optional[str]
    DefaultUnit: Optional[str]
    VatRate: Optional[str]
    Type: Optional["enumProductType"]
    Barcode: str
    CN: str
    PKWiU: str
    FiscalName: str

class ProductLogisticField(BaseModel):
    UnitTypeName: str
    Name: str
    Value: Optional[Decimal]
    Unit: str

class ProductPhoto(BaseModel):
    Id: int
    Name: str
    Description: str
    CreateDate: datetime
    ContentFile_Base64: str
    PhotoQuality: "enumPhotoQuality"

class ProductPhotoListElement(BaseModel):
    Id: int
    Name: str
    Description: str
    CreateDate: datetime

class ProductSetElement(BaseModel):
    Id: int
    Code: str
    Name: str
    Quantity: Decimal
    DisplayQuantity: Decimal
    DisplayUM: str

class ProductUnitsOfMeasurement(BaseModel):
    RecordUM: str
    AdditionalUM1: str
    AdditionalUM2: str
    DefaultUM: str
    DisplayUM: str
    DefaultUMKind: "enumDefaultUnitOfMeasurementKind"
    RatioOfAdditionalUM1: Decimal
    RatioOfAdditionalUM2: Decimal
    RatioOfDefaultUM: Decimal
