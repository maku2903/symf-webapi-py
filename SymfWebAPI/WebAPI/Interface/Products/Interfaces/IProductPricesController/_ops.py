from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import IndividualDiscount
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import IndividualDiscountListElement
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.PriceCalculations import PriceCalculationCriteria
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.PriceCalculations import PriceCalculationResult
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import PriceFactor
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import PriceFactorCriteria
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.PriceCalculations import PriceOrderCriteria
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.PriceCalculations import PriceOrderResult
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import ProductPriceListElement
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import ProductPricesEdit
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import ProductSalePriceBase
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import QuantitativeDiscount
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.Prices import QuantitativeDiscountListElement

OP_Update = build_none_operation(method='PUT', path='/api/ProductPrices/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/ProductPrices/Update')

OP_UpdateByPricesProductCode = build_none_operation(method='PUT', path='/api/ProductPrices/Update')
OP_UpdateByPricesProductCode_RAW = build_raw_operation(method='PUT', path='/api/ProductPrices/Update')

OP_Recalculate = build_none_operation(method='PATCH', path='/api/ProductPrices/Recalculate')
OP_Recalculate_RAW = build_raw_operation(method='PATCH', path='/api/ProductPrices/Recalculate')

OP_RecalculateByProductCode = build_none_operation(method='PATCH', path='/api/ProductPrices/Recalculate')
OP_RecalculateByProductCode_RAW = build_raw_operation(method='PATCH', path='/api/ProductPrices/Recalculate')

_ADAPTER_GetSalePricesByProduct = TypeAdapter(List[ProductSalePriceBase])
OP_GetSalePricesByProduct = build_typed_operation(method='GET', path='/api/ProductPrices/SalePrices', adapter=_ADAPTER_GetSalePricesByProduct)
OP_GetSalePricesByProduct_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/SalePrices')

_ADAPTER_GetSalePricesByProductByProductCode = TypeAdapter(List[ProductSalePriceBase])
OP_GetSalePricesByProductByProductCode = build_typed_operation(method='GET', path='/api/ProductPrices/SalePrices', adapter=_ADAPTER_GetSalePricesByProductByProductCode)
OP_GetSalePricesByProductByProductCode_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/SalePrices')

_ADAPTER_GetSalePricesByProductKind = TypeAdapter(List[ProductPriceListElement])
OP_GetSalePricesByProductKind = build_typed_operation(method='GET', path='/api/ProductPrices/SalePrices', adapter=_ADAPTER_GetSalePricesByProductKind)
OP_GetSalePricesByProductKind_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/SalePrices')

_ADAPTER_GetSalePrices = TypeAdapter(List[ProductPriceListElement])
OP_GetSalePrices = build_typed_operation(method='GET', path='/api/ProductPrices/SalePrices', adapter=_ADAPTER_GetSalePrices)
OP_GetSalePrices_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/SalePrices')

_ADAPTER_GetQuantitativeDiscountsByProduct = TypeAdapter(List[QuantitativeDiscount])
OP_GetQuantitativeDiscountsByProduct = build_typed_operation(method='GET', path='/api/ProductPrices/QuantitativeDiscounts', adapter=_ADAPTER_GetQuantitativeDiscountsByProduct)
OP_GetQuantitativeDiscountsByProduct_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/QuantitativeDiscounts')

_ADAPTER_GetQuantitativeDiscountsByProductByProductCode = TypeAdapter(List[QuantitativeDiscount])
OP_GetQuantitativeDiscountsByProductByProductCode = build_typed_operation(method='GET', path='/api/ProductPrices/QuantitativeDiscounts', adapter=_ADAPTER_GetQuantitativeDiscountsByProductByProductCode)
OP_GetQuantitativeDiscountsByProductByProductCode_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/QuantitativeDiscounts')

_ADAPTER_GetQuantitativeDiscountsByProductKind = TypeAdapter(List[QuantitativeDiscountListElement])
OP_GetQuantitativeDiscountsByProductKind = build_typed_operation(method='GET', path='/api/ProductPrices/QuantitativeDiscounts', adapter=_ADAPTER_GetQuantitativeDiscountsByProductKind)
OP_GetQuantitativeDiscountsByProductKind_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/QuantitativeDiscounts')

_ADAPTER_GetQuantitativeDiscounts = TypeAdapter(List[QuantitativeDiscountListElement])
OP_GetQuantitativeDiscounts = build_typed_operation(method='GET', path='/api/ProductPrices/QuantitativeDiscounts', adapter=_ADAPTER_GetQuantitativeDiscounts)
OP_GetQuantitativeDiscounts_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/QuantitativeDiscounts')

_ADAPTER_GetIndividualDiscountsByContractor = TypeAdapter(List[IndividualDiscount])
OP_GetIndividualDiscountsByContractor = build_typed_operation(method='GET', path='/api/ProductPrices/IndividualDiscounts', adapter=_ADAPTER_GetIndividualDiscountsByContractor)
OP_GetIndividualDiscountsByContractor_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/IndividualDiscounts')

_ADAPTER_GetIndividualDiscountsByContractorByContractorCode = TypeAdapter(List[IndividualDiscount])
OP_GetIndividualDiscountsByContractorByContractorCode = build_typed_operation(method='GET', path='/api/ProductPrices/IndividualDiscounts', adapter=_ADAPTER_GetIndividualDiscountsByContractorByContractorCode)
OP_GetIndividualDiscountsByContractorByContractorCode_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/IndividualDiscounts')

_ADAPTER_GetIndividualDiscountsByContractorKind = TypeAdapter(List[IndividualDiscount])
OP_GetIndividualDiscountsByContractorKind = build_typed_operation(method='GET', path='/api/ProductPrices/IndividualDiscounts', adapter=_ADAPTER_GetIndividualDiscountsByContractorKind)
OP_GetIndividualDiscountsByContractorKind_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/IndividualDiscounts')

_ADAPTER_GetIndividualDiscounts = TypeAdapter(List[IndividualDiscountListElement])
OP_GetIndividualDiscounts = build_typed_operation(method='GET', path='/api/ProductPrices/IndividualDiscounts', adapter=_ADAPTER_GetIndividualDiscounts)
OP_GetIndividualDiscounts_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/IndividualDiscounts')

_ADAPTER_GetPriceFactors = TypeAdapter(List[PriceFactor])
OP_GetPriceFactors = build_typed_operation(method='GET', path='/api/ProductPrices/PriceFactors', adapter=_ADAPTER_GetPriceFactors)
OP_GetPriceFactors_RAW = build_raw_operation(method='GET', path='/api/ProductPrices/PriceFactors')

_ADAPTER_CalculatePrices = TypeAdapter(PriceCalculationResult)
OP_CalculatePrices = build_typed_operation(method='PATCH', path='/api/ProductPrices/CalculatePrices', adapter=_ADAPTER_CalculatePrices)
OP_CalculatePrices_RAW = build_raw_operation(method='PATCH', path='/api/ProductPrices/CalculatePrices')

_ADAPTER_OrderPrices = TypeAdapter(PriceOrderResult)
OP_OrderPrices = build_typed_operation(method='PATCH', path='/api/ProductPrices/OrderPrices', adapter=_ADAPTER_OrderPrices)
OP_OrderPrices_RAW = build_raw_operation(method='PATCH', path='/api/ProductPrices/OrderPrices')
