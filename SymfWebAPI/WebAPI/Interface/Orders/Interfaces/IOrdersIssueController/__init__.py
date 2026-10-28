from __future__ import annotations

from typing import Any, List, Optional, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import Order
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderEdit
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderFV
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderIssue
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderWZ
from ._common import (
    _prepare_AddNew,
    _prepare_Edit,
    _prepare_Issue,
    _prepare_IssueByNumber,
    _prepare_IssueWZ,
    _prepare_IssueWZByInBufferOrderNumber,
    _prepare_IssueFV,
    _prepare_IssueFVByOrderNumber,
    _prepare_Delete,
    _prepare_DeleteByBufferNumber,
    _prepare_ChangeDocumentNumber,
)
from ._ops import (
    OP_AddNew,
    OP_AddNew_RAW,
    OP_Edit,
    OP_Edit_RAW,
    OP_Issue,
    OP_Issue_RAW,
    OP_IssueByNumber,
    OP_IssueByNumber_RAW,
    OP_IssueWZ,
    OP_IssueWZ_RAW,
    OP_IssueWZByInBufferOrderNumber,
    OP_IssueWZByInBufferOrderNumber_RAW,
    OP_IssueFV,
    OP_IssueFV_RAW,
    OP_IssueFVByOrderNumber,
    OP_IssueFVByOrderNumber_RAW,
    OP_Delete,
    OP_Delete_RAW,
    OP_DeleteByBufferNumber,
    OP_DeleteByBufferNumber_RAW,
    OP_ChangeDocumentNumber,
    OP_ChangeDocumentNumber_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, order: "OrderIssue", *, validate: bool = True) -> ResponseEnvelope[Order]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, order: "OrderIssue", *, validate: bool = True) -> ResponseEnvelope[Order]: ...
def AddNew(api: object, issue: bool, order: "OrderIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, issue=issue, order=order)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Edit(api: SyncInvokerProtocol, order: "OrderEdit", *, validate: bool = True) -> ResponseEnvelope[Order]: ...
@overload
def Edit(api: SyncRequestProtocol, order: "OrderEdit", *, validate: bool = True) -> ResponseEnvelope[Order]: ...
def Edit(api: object, order: "OrderEdit", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Edit(validate=validate, order=order)
    return invoke_operation(api, OP_Edit if validate else OP_Edit_RAW, params=params, data=data)

@overload
def Issue(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Order]: ...
@overload
def Issue(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Order]: ...
@overload
def Issue(api: SyncInvokerProtocol, number: str, *, validate: bool = True) -> ResponseEnvelope[Order]: ...
@overload
def Issue(api: SyncRequestProtocol, number: str, *, validate: bool = True) -> ResponseEnvelope[Order]: ...
def Issue(api: object, id: object = _UNSET, number: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'number' if number is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("Issue(): ambiguous overload for provided arguments")
        exact_match = 'Issue'
        exact_match_name = 'Issue'
    if provided_names == {'number'}:
        if exact_match_name is not None:
            raise TypeError("Issue(): ambiguous overload for provided arguments")
        exact_match = 'IssueByNumber'
        exact_match_name = 'IssueByNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'Issue'))
        if {'number'}.issubset(provided_names) and provided_names.issubset({'number'}):
            candidates.append((1, -1, 'IssueByNumber'))
        if not candidates:
            raise TypeError("Issue(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Issue(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Issue':
        params, data = _prepare_Issue(id=id)
        return invoke_operation(api, OP_Issue if validate else OP_Issue_RAW, params=params, data=data)
    if selected == 'IssueByNumber':
        params, data = _prepare_IssueByNumber(number=number)
        return invoke_operation(api, OP_IssueByNumber if validate else OP_IssueByNumber_RAW, params=params, data=data)
    raise TypeError("Issue(): internal overload dispatch failure")

@overload
def IssueWZ(api: SyncInvokerProtocol, orderId: int, inBuffer: Optional[int] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
@overload
def IssueWZ(api: SyncRequestProtocol, orderId: int, inBuffer: Optional[int] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
@overload
def IssueWZ(api: SyncInvokerProtocol, orderNumber: str, inBuffer: Optional[int] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
@overload
def IssueWZ(api: SyncRequestProtocol, orderNumber: str, inBuffer: Optional[int] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
def IssueWZ(api: object, orderId: object = _UNSET, inBuffer: object = _UNSET, orderNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'inBuffer' if inBuffer is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId', 'inBuffer'}:
        if exact_match_name is not None:
            raise TypeError("IssueWZ(): ambiguous overload for provided arguments")
        exact_match = 'IssueWZ'
        exact_match_name = 'IssueWZ'
    if provided_names == {'orderNumber', 'inBuffer'}:
        if exact_match_name is not None:
            raise TypeError("IssueWZ(): ambiguous overload for provided arguments")
        exact_match = 'IssueWZByInBufferOrderNumber'
        exact_match_name = 'IssueWZByInBufferOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId'}.issubset(provided_names) and provided_names.issubset({'orderId', 'inBuffer'}):
            candidates.append((1, -2, 'IssueWZ'))
        if {'orderNumber'}.issubset(provided_names) and provided_names.issubset({'orderNumber', 'inBuffer'}):
            candidates.append((1, -2, 'IssueWZByInBufferOrderNumber'))
        if not candidates:
            raise TypeError("IssueWZ(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssueWZ(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssueWZ':
        params, data = _prepare_IssueWZ(orderId=orderId, inBuffer=inBuffer)
        return invoke_operation(api, OP_IssueWZ if validate else OP_IssueWZ_RAW, params=params, data=data)
    if selected == 'IssueWZByInBufferOrderNumber':
        params, data = _prepare_IssueWZByInBufferOrderNumber(orderNumber=orderNumber, inBuffer=inBuffer)
        return invoke_operation(api, OP_IssueWZByInBufferOrderNumber if validate else OP_IssueWZByInBufferOrderNumber_RAW, params=params, data=data)
    raise TypeError("IssueWZ(): internal overload dispatch failure")

@overload
def IssueFV(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
@overload
def IssueFV(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
@overload
def IssueFV(api: SyncInvokerProtocol, orderNumber: str, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
@overload
def IssueFV(api: SyncRequestProtocol, orderNumber: str, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
def IssueFV(api: object, orderId: object = _UNSET, orderNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId'}:
        if exact_match_name is not None:
            raise TypeError("IssueFV(): ambiguous overload for provided arguments")
        exact_match = 'IssueFV'
        exact_match_name = 'IssueFV'
    if provided_names == {'orderNumber'}:
        if exact_match_name is not None:
            raise TypeError("IssueFV(): ambiguous overload for provided arguments")
        exact_match = 'IssueFVByOrderNumber'
        exact_match_name = 'IssueFVByOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId'}.issubset(provided_names) and provided_names.issubset({'orderId'}):
            candidates.append((1, -1, 'IssueFV'))
        if {'orderNumber'}.issubset(provided_names) and provided_names.issubset({'orderNumber'}):
            candidates.append((1, -1, 'IssueFVByOrderNumber'))
        if not candidates:
            raise TypeError("IssueFV(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssueFV(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssueFV':
        params, data = _prepare_IssueFV(orderId=orderId)
        return invoke_operation(api, OP_IssueFV if validate else OP_IssueFV_RAW, params=params, data=data)
    if selected == 'IssueFVByOrderNumber':
        params, data = _prepare_IssueFVByOrderNumber(orderNumber=orderNumber)
        return invoke_operation(api, OP_IssueFVByOrderNumber if validate else OP_IssueFVByOrderNumber_RAW, params=params, data=data)
    raise TypeError("IssueFV(): internal overload dispatch failure")

@overload
def Delete(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Delete(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Delete(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Delete(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Delete(api: object, id: object = _UNSET, number: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'number' if number is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("Delete(): ambiguous overload for provided arguments")
        exact_match = 'Delete'
        exact_match_name = 'Delete'
    if provided_names == {'buffer', 'number'}:
        if exact_match_name is not None:
            raise TypeError("Delete(): ambiguous overload for provided arguments")
        exact_match = 'DeleteByBufferNumber'
        exact_match_name = 'DeleteByBufferNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'Delete'))
        if {'buffer', 'number'}.issubset(provided_names) and provided_names.issubset({'buffer', 'number'}):
            candidates.append((2, -2, 'DeleteByBufferNumber'))
        if not candidates:
            raise TypeError("Delete(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Delete(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Delete':
        params, data = _prepare_Delete(id=id)
        return invoke_operation(api, OP_Delete if validate else OP_Delete_RAW, params=params, data=data)
    if selected == 'DeleteByBufferNumber':
        params, data = _prepare_DeleteByBufferNumber(number=number, buffer=buffer)
        return invoke_operation(api, OP_DeleteByBufferNumber if validate else OP_DeleteByBufferNumber_RAW, params=params, data=data)
    raise TypeError("Delete(): internal overload dispatch failure")

@overload
def ChangeDocumentNumber(api: SyncInvokerProtocol, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def ChangeDocumentNumber(api: SyncRequestProtocol, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def ChangeDocumentNumber(api: object, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_ChangeDocumentNumber(id=id, number=number)
    return invoke_operation(api, OP_ChangeDocumentNumber if validate else OP_ChangeDocumentNumber_RAW, params=params, data=data)

__all__ = ["AddNew", "Edit", "Issue", "IssueWZ", "IssueFV", "Delete", "ChangeDocumentNumber"]
