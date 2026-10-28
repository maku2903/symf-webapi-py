from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductPhoto
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductPhotoListElement
from SymfWebAPI.WebAPI.Interface.Enums import enumPhotoQuality
from ._common import (
    _prepare_Get,
    _prepare_GetByProductCode,
    _prepare_GetByPhotoIdQuality,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByProductCode,
    OP_GetByProductCode_RAW,
    OP_GetByPhotoIdQuality,
    OP_GetByPhotoIdQuality_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductPhotoListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductPhotoListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ProductPhotoListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ProductPhotoListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, photoId: int, quality: "enumPhotoQuality", *, validate: bool = True) -> ResponseEnvelope[ProductPhoto]: ...
@overload
def Get(api: SyncRequestProtocol, photoId: int, quality: "enumPhotoQuality", *, validate: bool = True) -> ResponseEnvelope[ProductPhoto]: ...
def Get(api: object, productId: object = _UNSET, productCode: object = _UNSET, photoId: object = _UNSET, quality: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
        'photoId' if photoId is not _UNSET else None,
        'quality' if quality is not _UNSET else None,
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
    if provided_names == {'photoId', 'quality'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByPhotoIdQuality'
        exact_match_name = 'GetByPhotoIdQuality'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId'}.issubset(provided_names) and provided_names.issubset({'productId'}):
            candidates.append((1, -1, 'Get'))
        if {'productCode'}.issubset(provided_names) and provided_names.issubset({'productCode'}):
            candidates.append((1, -1, 'GetByProductCode'))
        if {'photoId', 'quality'}.issubset(provided_names) and provided_names.issubset({'photoId', 'quality'}):
            candidates.append((2, -2, 'GetByPhotoIdQuality'))
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
    if selected == 'GetByPhotoIdQuality':
        params, data = _prepare_GetByPhotoIdQuality(photoId=photoId, quality=quality)
        return invoke_operation(api, OP_GetByPhotoIdQuality if validate else OP_GetByPhotoIdQuality_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

__all__ = ["Get"]
