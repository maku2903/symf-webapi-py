from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from ._common import (
    _prepare_Get,
    _prepare_GetByProductCode,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByProductCode,
    OP_GetByProductCode_RAW,
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

__all__ = ["Get"]
