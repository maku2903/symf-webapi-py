from __future__ import annotations

from typing import Any, List, Optional, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import CurrencyRate
from ._common import (
    _prepare_Get,
    _prepare_GetByCurrencyIdDate,
    _prepare_GetList,
    _prepare_GetListByCurrency,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByCurrencyIdDate,
    OP_GetByCurrencyIdDate_RAW,
    OP_GetList,
    OP_GetList_RAW,
    OP_GetListByCurrency,
    OP_GetListByCurrency_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[CurrencyRate]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[CurrencyRate]]: ...
@overload
def Get(api: SyncInvokerProtocol, currencyId: int, date: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CurrencyRate]]: ...
@overload
def Get(api: SyncRequestProtocol, currencyId: int, date: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CurrencyRate]]: ...
def Get(api: object, currencyId: object = _UNSET, date: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'currencyId' if currencyId is not _UNSET else None,
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
    if provided_names == {'currencyId', 'date'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByCurrencyIdDate'
        exact_match_name = 'GetByCurrencyIdDate'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'Get'))
        if {'currencyId'}.issubset(provided_names) and provided_names.issubset({'currencyId', 'date'}):
            candidates.append((1, -2, 'GetByCurrencyIdDate'))
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
    if selected == 'GetByCurrencyIdDate':
        params, data = _prepare_GetByCurrencyIdDate(currencyId=currencyId, date=date)
        return invoke_operation(api, OP_GetByCurrencyIdDate if validate else OP_GetByCurrencyIdDate_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetList(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CurrencyRate]]: ...
@overload
def GetList(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CurrencyRate]]: ...
def GetList(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetList(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetList if validate else OP_GetList_RAW, params=params, data=data)

@overload
def GetListByCurrency(api: SyncInvokerProtocol, currencyId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CurrencyRate]]: ...
@overload
def GetListByCurrency(api: SyncRequestProtocol, currencyId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CurrencyRate]]: ...
def GetListByCurrency(api: object, currencyId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetListByCurrency(currencyId=currencyId, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetListByCurrency if validate else OP_GetListByCurrency_RAW, params=params, data=data)

__all__ = ["Get", "GetList", "GetListByCurrency"]
