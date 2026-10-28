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

class ProductJSON(TypedDict):
    Id: int | None
    Active: bool
    Code: str
    Name: str
    Type: Any
    Barcode: str
    PKWiU: str
    CNFull: str
    CN: str
    DeliveryScheme: str
    FiscalName: str
    AgriculturalPromotionFund: str
    PriceNegotiation: bool
    PriceRounding: Any | None
    PriceRecalculateType: Any | None
    SettlementMethod: Any | None
    PriceParameter: Any | None
    VAT50Minus: bool
    ReverseCharge: bool
    SplitPayment: bool
    JPK_V7ProductGroup: Any | None
    StaticSet: bool
    PriceSetMode: bool
    CollationSetMode: bool
    SalePriceRecalculate: bool
    CurrencyMode: bool
    CurrencyRateWithoutConversion: float | int
    CurrencyRate: float | int
    CurrencyConversion: int
    CurrencyRateDate: str
    MinState: float | int
    MaxState: float | int
    Note: str | None
    Marker: int
    FK: ProductFKJSON
    Intrastat: ProductIntrastatJSON
    UnitsOfMeasurement: ProductUnitsOfMeasurementJSON
    BasePrice: ProductBasePriceJSON
    PurchasePrice: ProductPriceJSON
    PurchasePriceInCurrency: ProductPriceJSON
    SalePrices: list[ProductSalePriceJSON]
    CalcOther: ProductPriceJSON
    CalcExcise: ProductPriceJSON
    CalcDuty: ProductPriceJSON
    Kind: KindJSON
    Catalog: CatalogJSON
    VatRate: VatRateBaseJSON | None
    SetElements: list[ProductSetElementJSON] | None
    Dimensions: list[DimensionJSON]
    Barcodes: list[ProductBarcodeJSON]
    LogisticFields: list[ProductLogisticFieldJSON]
    RtfNote: str | None

class ProductBarcodeJSON(TypedDict):
    Barcode: str | None
    UnitName: str
    UnitOfMeasurement: str
    UnitOfMeasurementGuid: str | None
    SendToKSeF: bool | None

class ProductBarcodesJSON(TypedDict):
    Id: int
    Code: str
    Barcodes: list[ProductBarcodeJSON]

class ProductBasePriceJSON(TypedDict):
    Date: str
    Value: float | int
    Currency: str

class ProductFKJSON(TypedDict):
    IdFK: str
    ParameterFK: str

class ProductIntrastatJSON(TypedDict):
    RatioOfWeight: float | int
    RatioOfComplementaryUM: float | int
    ComplementaryUM: str
    UseComplementaryUM: bool

class ProductListElementJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Active: bool
    Unit: str | None
    DefaultUnit: str | None
    VatRate: str | None
    Type: Any | None
    Barcode: str
    CN: str
    PKWiU: str
    FiscalName: str

class ProductListElementSalePriceJSON(TypedDict):
    Type: Any
    Kind: Any
    Value: float | int
    Currency: str

class ProductListElementWithDimensionsJSON(TypedDict):
    Dimensions: list[DimensionJSON]
    Id: int
    Code: str
    Name: str
    Active: bool
    Unit: str | None
    DefaultUnit: str | None
    VatRate: str | None
    Type: Any | None
    Barcode: str
    CN: str
    PKWiU: str
    FiscalName: str

class ProductListElementWithSalePricesJSON(TypedDict):
    SalePrices: list[ProductListElementSalePriceJSON]
    Id: int
    Code: str
    Name: str
    Active: bool
    Unit: str | None
    DefaultUnit: str | None
    VatRate: str | None
    Type: Any | None
    Barcode: str
    CN: str
    PKWiU: str
    FiscalName: str

class ProductLogisticFieldJSON(TypedDict):
    UnitTypeName: str
    Name: str
    Value: float | int | None
    Unit: str

class ProductPriceJSON(TypedDict):
    Value: float | int
    Currency: str

class ProductSalePriceJSON(TypedDict):
    AutomaticValue: bool
    Type: Any
    ProfitPercent: float | int
    MarkupPercent: float | int
    LinkedWithBasePrice: bool
    Kind: Any
    PriceParameter: Any
    Value: float | int
    Currency: str

class ProductSetElementJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Quantity: float | int
    DisplayQuantity: float | int
    DisplayUM: str

class ProductUnitsOfMeasurementJSON(TypedDict):
    RecordUM: str
    AdditionalUM1: str
    AdditionalUM2: str
    DefaultUM: str
    DisplayUM: str
    DefaultUMKind: Any
    RatioOfAdditionalUM1: float | int
    RatioOfAdditionalUM2: float | int
    RatioOfDefaultUM: float | int

class VatRateBaseJSON(TypedDict):
    Id: int | None
    Code: str

class GetPagedDocumentJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[ProductListElementJSON]

class GetPageWithSalePricesJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[ProductListElementWithSalePricesJSON]

class GetPageWithDimensionsJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[ProductListElementWithDimensionsJSON]
