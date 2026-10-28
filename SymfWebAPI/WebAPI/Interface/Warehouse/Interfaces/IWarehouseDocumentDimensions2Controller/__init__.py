from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PositionDimension
from ._common import (
    _prepare_Get,
    _prepare_GetByBufferDocumentNumber,
    _prepare_GetPositionsByOrderId,
    _prepare_GetPositionsByOrderNumber,
    _prepare_GetPosition,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByBufferDocumentNumber,
    OP_GetByBufferDocumentNumber_RAW,
    OP_GetPositionsByOrderId,
    OP_GetPositionsByOrderId_RAW,
    OP_GetPositionsByOrderNumber,
    OP_GetPositionsByOrderNumber_RAW,
    OP_GetPosition,
    OP_GetPosition_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def Get(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'documentNumber', 'buffer'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByBufferDocumentNumber'
        exact_match_name = 'GetByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'Get'))
        if {'documentNumber', 'buffer'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'buffer'}):
            candidates.append((2, -2, 'GetByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(documentId=documentId)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByBufferDocumentNumber':
        params, data = _prepare_GetByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetByBufferDocumentNumber if validate else OP_GetByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetPositionsByOrderId(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
@overload
def GetPositionsByOrderId(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
def GetPositionsByOrderId(api: object, documentId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionsByOrderId(documentId=documentId)
    return invoke_operation(api, OP_GetPositionsByOrderId if validate else OP_GetPositionsByOrderId_RAW, params=params, data=data)

@overload
def GetPositionsByOrderNumber(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
@overload
def GetPositionsByOrderNumber(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
def GetPositionsByOrderNumber(api: object, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionsByOrderNumber(documentNumber=documentNumber, buffer=buffer)
    return invoke_operation(api, OP_GetPositionsByOrderNumber if validate else OP_GetPositionsByOrderNumber_RAW, params=params, data=data)

@overload
def GetPosition(api: SyncInvokerProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def GetPosition(api: SyncRequestProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def GetPosition(api: object, positionId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPosition(positionId=positionId)
    return invoke_operation(api, OP_GetPosition if validate else OP_GetPosition_RAW, params=params, data=data)

__all__ = ["Get", "GetPositionsByOrderId", "GetPositionsByOrderNumber", "GetPosition"]
