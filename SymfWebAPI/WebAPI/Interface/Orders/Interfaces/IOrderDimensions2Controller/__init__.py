from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PositionDimension
from ._common import (
    _prepare_Get,
    _prepare_GetByBufferOrderNumber,
    _prepare_GetPositionsByOrderId,
    _prepare_GetPositionsByOrderNumber,
    _prepare_GetPosition,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByBufferOrderNumber,
    OP_GetByBufferOrderNumber_RAW,
    OP_GetPositionsByOrderId,
    OP_GetPositionsByOrderId_RAW,
    OP_GetPositionsByOrderNumber,
    OP_GetPositionsByOrderNumber_RAW,
    OP_GetPosition,
    OP_GetPosition_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def Get(api: object, orderId: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'buffer', 'orderNumber'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByBufferOrderNumber'
        exact_match_name = 'GetByBufferOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId'}.issubset(provided_names) and provided_names.issubset({'orderId'}):
            candidates.append((1, -1, 'Get'))
        if {'buffer', 'orderNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderNumber'}):
            candidates.append((2, -2, 'GetByBufferOrderNumber'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(orderId=orderId)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByBufferOrderNumber':
        params, data = _prepare_GetByBufferOrderNumber(orderNumber=orderNumber, buffer=buffer)
        return invoke_operation(api, OP_GetByBufferOrderNumber if validate else OP_GetByBufferOrderNumber_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetPositionsByOrderId(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
@overload
def GetPositionsByOrderId(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
def GetPositionsByOrderId(api: object, orderId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionsByOrderId(orderId=orderId)
    return invoke_operation(api, OP_GetPositionsByOrderId if validate else OP_GetPositionsByOrderId_RAW, params=params, data=data)

@overload
def GetPositionsByOrderNumber(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
@overload
def GetPositionsByOrderNumber(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
def GetPositionsByOrderNumber(api: object, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionsByOrderNumber(orderNumber=orderNumber, buffer=buffer)
    return invoke_operation(api, OP_GetPositionsByOrderNumber if validate else OP_GetPositionsByOrderNumber_RAW, params=params, data=data)

@overload
def GetPosition(api: SyncInvokerProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def GetPosition(api: SyncRequestProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def GetPosition(api: object, positionId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPosition(positionId=positionId)
    return invoke_operation(api, OP_GetPosition if validate else OP_GetPosition_RAW, params=params, data=data)

__all__ = ["Get", "GetPositionsByOrderId", "GetPositionsByOrderNumber", "GetPosition"]
