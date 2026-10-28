from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
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
from ._common import (
    _prepare_Update,
    _prepare_UpdateByPricesProductCode,
    _prepare_Recalculate,
    _prepare_RecalculateByProductCode,
    _prepare_GetSalePricesByProduct,
    _prepare_GetSalePricesByProductByProductCode,
    _prepare_GetSalePricesByProductKind,
    _prepare_GetSalePrices,
    _prepare_GetQuantitativeDiscountsByProduct,
    _prepare_GetQuantitativeDiscountsByProductByProductCode,
    _prepare_GetQuantitativeDiscountsByProductKind,
    _prepare_GetQuantitativeDiscounts,
    _prepare_GetIndividualDiscountsByContractor,
    _prepare_GetIndividualDiscountsByContractorByContractorCode,
    _prepare_GetIndividualDiscountsByContractorKind,
    _prepare_GetIndividualDiscounts,
    _prepare_GetPriceFactors,
    _prepare_CalculatePrices,
    _prepare_OrderPrices,
)
from ._ops import (
    OP_Update,
    OP_Update_RAW,
    OP_UpdateByPricesProductCode,
    OP_UpdateByPricesProductCode_RAW,
    OP_Recalculate,
    OP_Recalculate_RAW,
    OP_RecalculateByProductCode,
    OP_RecalculateByProductCode_RAW,
    OP_GetSalePricesByProduct,
    OP_GetSalePricesByProduct_RAW,
    OP_GetSalePricesByProductByProductCode,
    OP_GetSalePricesByProductByProductCode_RAW,
    OP_GetSalePricesByProductKind,
    OP_GetSalePricesByProductKind_RAW,
    OP_GetSalePrices,
    OP_GetSalePrices_RAW,
    OP_GetQuantitativeDiscountsByProduct,
    OP_GetQuantitativeDiscountsByProduct_RAW,
    OP_GetQuantitativeDiscountsByProductByProductCode,
    OP_GetQuantitativeDiscountsByProductByProductCode_RAW,
    OP_GetQuantitativeDiscountsByProductKind,
    OP_GetQuantitativeDiscountsByProductKind_RAW,
    OP_GetQuantitativeDiscounts,
    OP_GetQuantitativeDiscounts_RAW,
    OP_GetIndividualDiscountsByContractor,
    OP_GetIndividualDiscountsByContractor_RAW,
    OP_GetIndividualDiscountsByContractorByContractorCode,
    OP_GetIndividualDiscountsByContractorByContractorCode_RAW,
    OP_GetIndividualDiscountsByContractorKind,
    OP_GetIndividualDiscountsByContractorKind_RAW,
    OP_GetIndividualDiscounts,
    OP_GetIndividualDiscounts_RAW,
    OP_GetPriceFactors,
    OP_GetPriceFactors_RAW,
    OP_CalculatePrices,
    OP_CalculatePrices_RAW,
    OP_OrderPrices,
    OP_OrderPrices_RAW,
)

_UNSET = object()

@overload
def Update(api: SyncInvokerProtocol, productId: int, prices: "ProductPricesEdit", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, productId: int, prices: "ProductPricesEdit", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, productCode: str, prices: "ProductPricesEdit", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, productCode: str, prices: "ProductPricesEdit", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, productId: object = _UNSET, prices: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'prices' if prices is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'prices', 'productId'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'Update'
        exact_match_name = 'Update'
    if provided_names == {'prices', 'productCode'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByPricesProductCode'
        exact_match_name = 'UpdateByPricesProductCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'prices', 'productId'}.issubset(provided_names) and provided_names.issubset({'prices', 'productId'}):
            candidates.append((2, -2, 'Update'))
        if {'prices', 'productCode'}.issubset(provided_names) and provided_names.issubset({'prices', 'productCode'}):
            candidates.append((2, -2, 'UpdateByPricesProductCode'))
        if not candidates:
            raise TypeError("Update(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Update':
        params, data = _prepare_Update(validate=validate, productId=productId, prices=prices)
        return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)
    if selected == 'UpdateByPricesProductCode':
        params, data = _prepare_UpdateByPricesProductCode(validate=validate, productCode=productCode, prices=prices)
        return invoke_operation(api, OP_UpdateByPricesProductCode if validate else OP_UpdateByPricesProductCode_RAW, params=params, data=data)
    raise TypeError("Update(): internal overload dispatch failure")

@overload
def Recalculate(api: SyncInvokerProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Recalculate(api: SyncRequestProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Recalculate(api: SyncInvokerProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Recalculate(api: SyncRequestProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Recalculate(api: object, productId: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productId'}:
        if exact_match_name is not None:
            raise TypeError("Recalculate(): ambiguous overload for provided arguments")
        exact_match = 'Recalculate'
        exact_match_name = 'Recalculate'
    if provided_names == {'productCode'}:
        if exact_match_name is not None:
            raise TypeError("Recalculate(): ambiguous overload for provided arguments")
        exact_match = 'RecalculateByProductCode'
        exact_match_name = 'RecalculateByProductCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId'}.issubset(provided_names) and provided_names.issubset({'productId'}):
            candidates.append((1, -1, 'Recalculate'))
        if {'productCode'}.issubset(provided_names) and provided_names.issubset({'productCode'}):
            candidates.append((1, -1, 'RecalculateByProductCode'))
        if not candidates:
            raise TypeError("Recalculate(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Recalculate(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Recalculate':
        params, data = _prepare_Recalculate(productId=productId)
        return invoke_operation(api, OP_Recalculate if validate else OP_Recalculate_RAW, params=params, data=data)
    if selected == 'RecalculateByProductCode':
        params, data = _prepare_RecalculateByProductCode(productCode=productCode)
        return invoke_operation(api, OP_RecalculateByProductCode if validate else OP_RecalculateByProductCode_RAW, params=params, data=data)
    raise TypeError("Recalculate(): internal overload dispatch failure")

@overload
def GetSalePricesByProduct(api: SyncInvokerProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductSalePriceBase]]: ...
@overload
def GetSalePricesByProduct(api: SyncRequestProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductSalePriceBase]]: ...
@overload
def GetSalePricesByProduct(api: SyncInvokerProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ProductSalePriceBase]]: ...
@overload
def GetSalePricesByProduct(api: SyncRequestProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ProductSalePriceBase]]: ...
def GetSalePricesByProduct(api: object, productId: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productId'}:
        if exact_match_name is not None:
            raise TypeError("GetSalePricesByProduct(): ambiguous overload for provided arguments")
        exact_match = 'GetSalePricesByProduct'
        exact_match_name = 'GetSalePricesByProduct'
    if provided_names == {'productCode'}:
        if exact_match_name is not None:
            raise TypeError("GetSalePricesByProduct(): ambiguous overload for provided arguments")
        exact_match = 'GetSalePricesByProductByProductCode'
        exact_match_name = 'GetSalePricesByProductByProductCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId'}.issubset(provided_names) and provided_names.issubset({'productId'}):
            candidates.append((1, -1, 'GetSalePricesByProduct'))
        if {'productCode'}.issubset(provided_names) and provided_names.issubset({'productCode'}):
            candidates.append((1, -1, 'GetSalePricesByProductByProductCode'))
        if not candidates:
            raise TypeError("GetSalePricesByProduct(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetSalePricesByProduct(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetSalePricesByProduct':
        params, data = _prepare_GetSalePricesByProduct(productId=productId)
        return invoke_operation(api, OP_GetSalePricesByProduct if validate else OP_GetSalePricesByProduct_RAW, params=params, data=data)
    if selected == 'GetSalePricesByProductByProductCode':
        params, data = _prepare_GetSalePricesByProductByProductCode(productCode=productCode)
        return invoke_operation(api, OP_GetSalePricesByProductByProductCode if validate else OP_GetSalePricesByProductByProductCode_RAW, params=params, data=data)
    raise TypeError("GetSalePricesByProduct(): internal overload dispatch failure")

@overload
def GetSalePricesByProductKind(api: SyncInvokerProtocol, productKindId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductPriceListElement]]: ...
@overload
def GetSalePricesByProductKind(api: SyncRequestProtocol, productKindId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductPriceListElement]]: ...
def GetSalePricesByProductKind(api: object, productKindId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSalePricesByProductKind(productKindId=productKindId)
    return invoke_operation(api, OP_GetSalePricesByProductKind if validate else OP_GetSalePricesByProductKind_RAW, params=params, data=data)

@overload
def GetSalePrices(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductPriceListElement]]: ...
@overload
def GetSalePrices(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductPriceListElement]]: ...
def GetSalePrices(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSalePrices()
    return invoke_operation(api, OP_GetSalePrices if validate else OP_GetSalePrices_RAW, params=params, data=data)

@overload
def GetQuantitativeDiscountsByProduct(api: SyncInvokerProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[QuantitativeDiscount]]: ...
@overload
def GetQuantitativeDiscountsByProduct(api: SyncRequestProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[QuantitativeDiscount]]: ...
@overload
def GetQuantitativeDiscountsByProduct(api: SyncInvokerProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[QuantitativeDiscount]]: ...
@overload
def GetQuantitativeDiscountsByProduct(api: SyncRequestProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[QuantitativeDiscount]]: ...
def GetQuantitativeDiscountsByProduct(api: object, productId: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productId'}:
        if exact_match_name is not None:
            raise TypeError("GetQuantitativeDiscountsByProduct(): ambiguous overload for provided arguments")
        exact_match = 'GetQuantitativeDiscountsByProduct'
        exact_match_name = 'GetQuantitativeDiscountsByProduct'
    if provided_names == {'productCode'}:
        if exact_match_name is not None:
            raise TypeError("GetQuantitativeDiscountsByProduct(): ambiguous overload for provided arguments")
        exact_match = 'GetQuantitativeDiscountsByProductByProductCode'
        exact_match_name = 'GetQuantitativeDiscountsByProductByProductCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId'}.issubset(provided_names) and provided_names.issubset({'productId'}):
            candidates.append((1, -1, 'GetQuantitativeDiscountsByProduct'))
        if {'productCode'}.issubset(provided_names) and provided_names.issubset({'productCode'}):
            candidates.append((1, -1, 'GetQuantitativeDiscountsByProductByProductCode'))
        if not candidates:
            raise TypeError("GetQuantitativeDiscountsByProduct(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetQuantitativeDiscountsByProduct(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetQuantitativeDiscountsByProduct':
        params, data = _prepare_GetQuantitativeDiscountsByProduct(productId=productId)
        return invoke_operation(api, OP_GetQuantitativeDiscountsByProduct if validate else OP_GetQuantitativeDiscountsByProduct_RAW, params=params, data=data)
    if selected == 'GetQuantitativeDiscountsByProductByProductCode':
        params, data = _prepare_GetQuantitativeDiscountsByProductByProductCode(productCode=productCode)
        return invoke_operation(api, OP_GetQuantitativeDiscountsByProductByProductCode if validate else OP_GetQuantitativeDiscountsByProductByProductCode_RAW, params=params, data=data)
    raise TypeError("GetQuantitativeDiscountsByProduct(): internal overload dispatch failure")

@overload
def GetQuantitativeDiscountsByProductKind(api: SyncInvokerProtocol, productKindId: int, *, validate: bool = True) -> ResponseEnvelope[List[QuantitativeDiscountListElement]]: ...
@overload
def GetQuantitativeDiscountsByProductKind(api: SyncRequestProtocol, productKindId: int, *, validate: bool = True) -> ResponseEnvelope[List[QuantitativeDiscountListElement]]: ...
def GetQuantitativeDiscountsByProductKind(api: object, productKindId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetQuantitativeDiscountsByProductKind(productKindId=productKindId)
    return invoke_operation(api, OP_GetQuantitativeDiscountsByProductKind if validate else OP_GetQuantitativeDiscountsByProductKind_RAW, params=params, data=data)

@overload
def GetQuantitativeDiscounts(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[QuantitativeDiscountListElement]]: ...
@overload
def GetQuantitativeDiscounts(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[QuantitativeDiscountListElement]]: ...
def GetQuantitativeDiscounts(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetQuantitativeDiscounts()
    return invoke_operation(api, OP_GetQuantitativeDiscounts if validate else OP_GetQuantitativeDiscounts_RAW, params=params, data=data)

@overload
def GetIndividualDiscountsByContractor(api: SyncInvokerProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[IndividualDiscount]]: ...
@overload
def GetIndividualDiscountsByContractor(api: SyncRequestProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[IndividualDiscount]]: ...
@overload
def GetIndividualDiscountsByContractor(api: SyncInvokerProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[IndividualDiscount]]: ...
@overload
def GetIndividualDiscountsByContractor(api: SyncRequestProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[IndividualDiscount]]: ...
def GetIndividualDiscountsByContractor(api: object, contractorId: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorId'}:
        if exact_match_name is not None:
            raise TypeError("GetIndividualDiscountsByContractor(): ambiguous overload for provided arguments")
        exact_match = 'GetIndividualDiscountsByContractor'
        exact_match_name = 'GetIndividualDiscountsByContractor'
    if provided_names == {'contractorCode'}:
        if exact_match_name is not None:
            raise TypeError("GetIndividualDiscountsByContractor(): ambiguous overload for provided arguments")
        exact_match = 'GetIndividualDiscountsByContractorByContractorCode'
        exact_match_name = 'GetIndividualDiscountsByContractorByContractorCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorId'}):
            candidates.append((1, -1, 'GetIndividualDiscountsByContractor'))
        if {'contractorCode'}.issubset(provided_names) and provided_names.issubset({'contractorCode'}):
            candidates.append((1, -1, 'GetIndividualDiscountsByContractorByContractorCode'))
        if not candidates:
            raise TypeError("GetIndividualDiscountsByContractor(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetIndividualDiscountsByContractor(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetIndividualDiscountsByContractor':
        params, data = _prepare_GetIndividualDiscountsByContractor(contractorId=contractorId)
        return invoke_operation(api, OP_GetIndividualDiscountsByContractor if validate else OP_GetIndividualDiscountsByContractor_RAW, params=params, data=data)
    if selected == 'GetIndividualDiscountsByContractorByContractorCode':
        params, data = _prepare_GetIndividualDiscountsByContractorByContractorCode(contractorCode=contractorCode)
        return invoke_operation(api, OP_GetIndividualDiscountsByContractorByContractorCode if validate else OP_GetIndividualDiscountsByContractorByContractorCode_RAW, params=params, data=data)
    raise TypeError("GetIndividualDiscountsByContractor(): internal overload dispatch failure")

@overload
def GetIndividualDiscountsByContractorKind(api: SyncInvokerProtocol, contractorKindId: int, *, validate: bool = True) -> ResponseEnvelope[List[IndividualDiscount]]: ...
@overload
def GetIndividualDiscountsByContractorKind(api: SyncRequestProtocol, contractorKindId: int, *, validate: bool = True) -> ResponseEnvelope[List[IndividualDiscount]]: ...
def GetIndividualDiscountsByContractorKind(api: object, contractorKindId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetIndividualDiscountsByContractorKind(contractorKindId=contractorKindId)
    return invoke_operation(api, OP_GetIndividualDiscountsByContractorKind if validate else OP_GetIndividualDiscountsByContractorKind_RAW, params=params, data=data)

@overload
def GetIndividualDiscounts(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[IndividualDiscountListElement]]: ...
@overload
def GetIndividualDiscounts(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[IndividualDiscountListElement]]: ...
def GetIndividualDiscounts(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetIndividualDiscounts()
    return invoke_operation(api, OP_GetIndividualDiscounts if validate else OP_GetIndividualDiscounts_RAW, params=params, data=data)

@overload
def GetPriceFactors(api: SyncInvokerProtocol, criteria: "PriceFactorCriteria", *, validate: bool = True) -> ResponseEnvelope[List[PriceFactor]]: ...
@overload
def GetPriceFactors(api: SyncRequestProtocol, criteria: "PriceFactorCriteria", *, validate: bool = True) -> ResponseEnvelope[List[PriceFactor]]: ...
def GetPriceFactors(api: object, criteria: "PriceFactorCriteria", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPriceFactors(criteria=criteria)
    return invoke_operation(api, OP_GetPriceFactors if validate else OP_GetPriceFactors_RAW, params=params, data=data)

@overload
def CalculatePrices(api: SyncInvokerProtocol, criteria: "PriceCalculationCriteria", *, validate: bool = True) -> ResponseEnvelope[PriceCalculationResult]: ...
@overload
def CalculatePrices(api: SyncRequestProtocol, criteria: "PriceCalculationCriteria", *, validate: bool = True) -> ResponseEnvelope[PriceCalculationResult]: ...
def CalculatePrices(api: object, criteria: "PriceCalculationCriteria", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_CalculatePrices(validate=validate, criteria=criteria)
    return invoke_operation(api, OP_CalculatePrices if validate else OP_CalculatePrices_RAW, params=params, data=data)

@overload
def OrderPrices(api: SyncInvokerProtocol, criteria: "PriceOrderCriteria", *, validate: bool = True) -> ResponseEnvelope[PriceOrderResult]: ...
@overload
def OrderPrices(api: SyncRequestProtocol, criteria: "PriceOrderCriteria", *, validate: bool = True) -> ResponseEnvelope[PriceOrderResult]: ...
def OrderPrices(api: object, criteria: "PriceOrderCriteria", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_OrderPrices(validate=validate, criteria=criteria)
    return invoke_operation(api, OP_OrderPrices if validate else OP_OrderPrices_RAW, params=params, data=data)

__all__ = ["Update", "Recalculate", "GetSalePricesByProduct", "GetSalePricesByProductKind", "GetSalePrices", "GetQuantitativeDiscountsByProduct", "GetQuantitativeDiscountsByProductKind", "GetQuantitativeDiscounts", "GetIndividualDiscountsByContractor", "GetIndividualDiscountsByContractorKind", "GetIndividualDiscounts", "GetPriceFactors", "CalculatePrices", "OrderPrices"]
