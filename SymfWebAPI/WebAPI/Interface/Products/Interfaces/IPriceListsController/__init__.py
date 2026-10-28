from __future__ import annotations

from typing import Any, List, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import IncrementalSyncListElement
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.PriceLists import PriceList
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.PriceLists import PriceListListElement
from ._common import (
    _prepare_Get,
    _prepare_GetByCode,
    _prepare_GetGet,
    _prepare_IncrementalSync,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByCode,
    OP_GetByCode_RAW,
    OP_GetGet,
    OP_GetGet_RAW,
    OP_IncrementalSync,
    OP_IncrementalSync_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[PriceList]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[PriceList]: ...
@overload
def Get(api: SyncInvokerProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[PriceList]: ...
@overload
def Get(api: SyncRequestProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[PriceList]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PriceListListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PriceListListElement]]: ...
def Get(api: object, id: object = _UNSET, code: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'code' if code is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'code'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByCode'
        exact_match_name = 'GetByCode'
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetGet'
        exact_match_name = 'GetGet'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'Get'))
        if {'code'}.issubset(provided_names) and provided_names.issubset({'code'}):
            candidates.append((1, -1, 'GetByCode'))
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'GetGet'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(id=id)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByCode':
        params, data = _prepare_GetByCode(code=code)
        return invoke_operation(api, OP_GetByCode if validate else OP_GetByCode_RAW, params=params, data=data)
    if selected == 'GetGet':
        params, data = _prepare_GetGet()
        return invoke_operation(api, OP_GetGet if validate else OP_GetGet_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def IncrementalSync(api: SyncInvokerProtocol, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[List[IncrementalSyncListElement]]: ...
@overload
def IncrementalSync(api: SyncRequestProtocol, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[List[IncrementalSyncListElement]]: ...
def IncrementalSync(api: object, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IncrementalSync(dateFrom=dateFrom)
    return invoke_operation(api, OP_IncrementalSync if validate else OP_IncrementalSync_RAW, params=params, data=data)

__all__ = ["Get", "IncrementalSync"]
