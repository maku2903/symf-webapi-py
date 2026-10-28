from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocument
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentEdit
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentIssue
from ._common import (
    _prepare_AddNew,
    _prepare_Edit,
    _prepare_Issue,
    _prepare_IssueByNumber,
    _prepare_IssueMMPlus,
    _prepare_IssueMMPlusByDocumentNumber,
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
    OP_IssueMMPlus,
    OP_IssueMMPlus_RAW,
    OP_IssueMMPlusByDocumentNumber,
    OP_IssueMMPlusByDocumentNumber_RAW,
    OP_ChangeDocumentNumber,
    OP_ChangeDocumentNumber_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, document: "WarehouseDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, document: "WarehouseDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
def AddNew(api: object, issue: bool, document: "WarehouseDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, issue=issue, document=document)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Edit(api: SyncInvokerProtocol, document: "WarehouseDocumentEdit", *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
@overload
def Edit(api: SyncRequestProtocol, document: "WarehouseDocumentEdit", *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
def Edit(api: object, document: "WarehouseDocumentEdit", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Edit(validate=validate, document=document)
    return invoke_operation(api, OP_Edit if validate else OP_Edit_RAW, params=params, data=data)

@overload
def Issue(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
@overload
def Issue(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
@overload
def Issue(api: SyncInvokerProtocol, number: str, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
@overload
def Issue(api: SyncRequestProtocol, number: str, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
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
def IssueMMPlus(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def IssueMMPlus(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def IssueMMPlus(api: SyncInvokerProtocol, documentNumber: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def IssueMMPlus(api: SyncRequestProtocol, documentNumber: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def IssueMMPlus(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId'}:
        if exact_match_name is not None:
            raise TypeError("IssueMMPlus(): ambiguous overload for provided arguments")
        exact_match = 'IssueMMPlus'
        exact_match_name = 'IssueMMPlus'
    if provided_names == {'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("IssueMMPlus(): ambiguous overload for provided arguments")
        exact_match = 'IssueMMPlusByDocumentNumber'
        exact_match_name = 'IssueMMPlusByDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'IssueMMPlus'))
        if {'documentNumber'}.issubset(provided_names) and provided_names.issubset({'documentNumber'}):
            candidates.append((1, -1, 'IssueMMPlusByDocumentNumber'))
        if not candidates:
            raise TypeError("IssueMMPlus(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssueMMPlus(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssueMMPlus':
        params, data = _prepare_IssueMMPlus(documentId=documentId)
        return invoke_operation(api, OP_IssueMMPlus if validate else OP_IssueMMPlus_RAW, params=params, data=data)
    if selected == 'IssueMMPlusByDocumentNumber':
        params, data = _prepare_IssueMMPlusByDocumentNumber(documentNumber=documentNumber)
        return invoke_operation(api, OP_IssueMMPlusByDocumentNumber if validate else OP_IssueMMPlusByDocumentNumber_RAW, params=params, data=data)
    raise TypeError("IssueMMPlus(): internal overload dispatch failure")

@overload
def ChangeDocumentNumber(api: SyncInvokerProtocol, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def ChangeDocumentNumber(api: SyncRequestProtocol, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def ChangeDocumentNumber(api: object, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_ChangeDocumentNumber(id=id, number=number)
    return invoke_operation(api, OP_ChangeDocumentNumber if validate else OP_ChangeDocumentNumber_RAW, params=params, data=data)

__all__ = ["AddNew", "Edit", "Issue", "IssueMMPlus", "ChangeDocumentNumber"]
