from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DimensionClassification
from ._common import (
    _prepare_Get,
    _prepare_GetByProductCode,
    _prepare_Update,
    _prepare_UpdateByProductCodeProductDimension,
    _prepare_UpdateByProductDimensionsProductId,
    _prepare_UpdateByProductCodeProductDimensions,
    _prepare_GetClassification,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByProductCode,
    OP_GetByProductCode_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_UpdateByProductCodeProductDimension,
    OP_UpdateByProductCodeProductDimension_RAW,
    OP_UpdateByProductDimensionsProductId,
    OP_UpdateByProductDimensionsProductId_RAW,
    OP_UpdateByProductCodeProductDimensions,
    OP_UpdateByProductCodeProductDimensions_RAW,
    OP_GetClassification,
    OP_GetClassification_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncInvokerProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def Get(api: object, productId: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productId'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'productCode'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByProductCode'
        exact_match_name = 'GetByProductCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId'}.issubset(provided_names) and provided_names.issubset({'productId'}):
            candidates.append((1, -1, 'Get'))
        if {'productCode'}.issubset(provided_names) and provided_names.issubset({'productCode'}):
            candidates.append((1, -1, 'GetByProductCode'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(productId=productId)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByProductCode':
        params, data = _prepare_GetByProductCode(productCode=productCode)
        return invoke_operation(api, OP_GetByProductCode if validate else OP_GetByProductCode_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def Update(api: SyncInvokerProtocol, productId: int, productDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, productId: int, productDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, productCode: str, productDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, productCode: str, productDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, productId: int, productDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, productId: int, productDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, productCode: str, productDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, productCode: str, productDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, productId: object = _UNSET, productDimension: object = _UNSET, productCode: object = _UNSET, productDimensions: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productDimension' if productDimension is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
        'productDimensions' if productDimensions is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productDimension', 'productId'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'Update'
        exact_match_name = 'Update'
    if provided_names == {'productCode', 'productDimension'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByProductCodeProductDimension'
        exact_match_name = 'UpdateByProductCodeProductDimension'
    if provided_names == {'productDimensions', 'productId'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByProductDimensionsProductId'
        exact_match_name = 'UpdateByProductDimensionsProductId'
    if provided_names == {'productCode', 'productDimensions'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByProductCodeProductDimensions'
        exact_match_name = 'UpdateByProductCodeProductDimensions'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productDimension', 'productId'}.issubset(provided_names) and provided_names.issubset({'productDimension', 'productId'}):
            candidates.append((2, -2, 'Update'))
        if {'productCode', 'productDimension'}.issubset(provided_names) and provided_names.issubset({'productCode', 'productDimension'}):
            candidates.append((2, -2, 'UpdateByProductCodeProductDimension'))
        if {'productDimensions', 'productId'}.issubset(provided_names) and provided_names.issubset({'productDimensions', 'productId'}):
            candidates.append((2, -2, 'UpdateByProductDimensionsProductId'))
        if {'productCode', 'productDimensions'}.issubset(provided_names) and provided_names.issubset({'productCode', 'productDimensions'}):
            candidates.append((2, -2, 'UpdateByProductCodeProductDimensions'))
        if not candidates:
            raise TypeError("Update(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Update':
        params, data = _prepare_Update(validate=validate, productId=productId, productDimension=productDimension)
        return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)
    if selected == 'UpdateByProductCodeProductDimension':
        params, data = _prepare_UpdateByProductCodeProductDimension(validate=validate, productCode=productCode, productDimension=productDimension)
        return invoke_operation(api, OP_UpdateByProductCodeProductDimension if validate else OP_UpdateByProductCodeProductDimension_RAW, params=params, data=data)
    if selected == 'UpdateByProductDimensionsProductId':
        params, data = _prepare_UpdateByProductDimensionsProductId(validate=validate, productId=productId, productDimensions=productDimensions)
        return invoke_operation(api, OP_UpdateByProductDimensionsProductId if validate else OP_UpdateByProductDimensionsProductId_RAW, params=params, data=data)
    if selected == 'UpdateByProductCodeProductDimensions':
        params, data = _prepare_UpdateByProductCodeProductDimensions(validate=validate, productCode=productCode, productDimensions=productDimensions)
        return invoke_operation(api, OP_UpdateByProductCodeProductDimensions if validate else OP_UpdateByProductCodeProductDimensions_RAW, params=params, data=data)
    raise TypeError("Update(): internal overload dispatch failure")

@overload
def GetClassification(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def GetClassification(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
def GetClassification(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetClassification()
    return invoke_operation(api, OP_GetClassification if validate else OP_GetClassification_RAW, params=params, data=data)

__all__ = ["Get", "Update", "GetClassification"]
