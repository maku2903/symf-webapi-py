from __future__ import annotations

from typing import Any, List, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Year
from ._common import (
    _prepare_Get,
    _prepare_GetByDate,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByDate,
    OP_GetByDate_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Year]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Year]]: ...
@overload
def Get(api: SyncInvokerProtocol, date: datetime, *, validate: bool = True) -> ResponseEnvelope[Year]: ...
@overload
def Get(api: SyncRequestProtocol, date: datetime, *, validate: bool = True) -> ResponseEnvelope[Year]: ...
def Get(api: object, date: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'date' if date is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'date'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByDate'
        exact_match_name = 'GetByDate'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'Get'))
        if {'date'}.issubset(provided_names) and provided_names.issubset({'date'}):
            candidates.append((1, -1, 'GetByDate'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get()
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByDate':
        params, data = _prepare_GetByDate(date=date)
        return invoke_operation(api, OP_GetByDate if validate else OP_GetByDate_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

__all__ = ["Get"]
