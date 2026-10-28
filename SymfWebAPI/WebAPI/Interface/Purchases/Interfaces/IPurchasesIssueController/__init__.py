from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseCorrection
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseCorrectionIssue
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocument
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentIssue
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentPZ
from ._common import (
    _prepare_AddNew,
    _prepare_AddNewByCorrectionIssue,
    _prepare_Issue,
    _prepare_IssueByNumber,
    _prepare_IssuePZ,
    _prepare_IssuePZByDocumentNumber,
    _prepare_IssuePZCorrection,
    _prepare_IssuePZCorrectionByDocumentNumberIssue,
    _prepare_ChangeDocumentNumber,
)
from ._ops import (
    OP_AddNew,
    OP_AddNew_RAW,
    OP_AddNewByCorrectionIssue,
    OP_AddNewByCorrectionIssue_RAW,
    OP_Issue,
    OP_Issue_RAW,
    OP_IssueByNumber,
    OP_IssueByNumber_RAW,
    OP_IssuePZ,
    OP_IssuePZ_RAW,
    OP_IssuePZByDocumentNumber,
    OP_IssuePZByDocumentNumber_RAW,
    OP_IssuePZCorrection,
    OP_IssuePZCorrection_RAW,
    OP_IssuePZCorrectionByDocumentNumberIssue,
    OP_IssuePZCorrectionByDocumentNumberIssue_RAW,
    OP_ChangeDocumentNumber,
    OP_ChangeDocumentNumber_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, document: "PurchaseDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, document: "PurchaseDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, correction: "PurchaseCorrectionIssue", *, validate: bool = True) -> ResponseEnvelope[PurchaseCorrection]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, correction: "PurchaseCorrectionIssue", *, validate: bool = True) -> ResponseEnvelope[PurchaseCorrection]: ...
def AddNew(api: object, issue: object = _UNSET, document: object = _UNSET, correction: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'issue' if issue is not _UNSET else None,
        'document' if document is not _UNSET else None,
        'correction' if correction is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'issue', 'document'}:
        if exact_match_name is not None:
            raise TypeError("AddNew(): ambiguous overload for provided arguments")
        exact_match = 'AddNew'
        exact_match_name = 'AddNew'
    if provided_names == {'issue', 'correction'}:
        if exact_match_name is not None:
            raise TypeError("AddNew(): ambiguous overload for provided arguments")
        exact_match = 'AddNewByCorrectionIssue'
        exact_match_name = 'AddNewByCorrectionIssue'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'issue', 'document'}.issubset(provided_names) and provided_names.issubset({'issue', 'document'}):
            candidates.append((2, -2, 'AddNew'))
        if {'issue', 'correction'}.issubset(provided_names) and provided_names.issubset({'issue', 'correction'}):
            candidates.append((2, -2, 'AddNewByCorrectionIssue'))
        if not candidates:
            raise TypeError("AddNew(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("AddNew(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'AddNew':
        params, data = _prepare_AddNew(validate=validate, issue=issue, document=document)
        return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)
    if selected == 'AddNewByCorrectionIssue':
        params, data = _prepare_AddNewByCorrectionIssue(validate=validate, issue=issue, correction=correction)
        return invoke_operation(api, OP_AddNewByCorrectionIssue if validate else OP_AddNewByCorrectionIssue_RAW, params=params, data=data)
    raise TypeError("AddNew(): internal overload dispatch failure")

@overload
def Issue(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def Issue(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def Issue(api: SyncInvokerProtocol, number: str, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def Issue(api: SyncRequestProtocol, number: str, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
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
def IssuePZ(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def IssuePZ(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def IssuePZ(api: SyncInvokerProtocol, documentNumber: str, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def IssuePZ(api: SyncRequestProtocol, documentNumber: str, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
def IssuePZ(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId'}:
        if exact_match_name is not None:
            raise TypeError("IssuePZ(): ambiguous overload for provided arguments")
        exact_match = 'IssuePZ'
        exact_match_name = 'IssuePZ'
    if provided_names == {'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("IssuePZ(): ambiguous overload for provided arguments")
        exact_match = 'IssuePZByDocumentNumber'
        exact_match_name = 'IssuePZByDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'IssuePZ'))
        if {'documentNumber'}.issubset(provided_names) and provided_names.issubset({'documentNumber'}):
            candidates.append((1, -1, 'IssuePZByDocumentNumber'))
        if not candidates:
            raise TypeError("IssuePZ(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssuePZ(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssuePZ':
        params, data = _prepare_IssuePZ(documentId=documentId)
        return invoke_operation(api, OP_IssuePZ if validate else OP_IssuePZ_RAW, params=params, data=data)
    if selected == 'IssuePZByDocumentNumber':
        params, data = _prepare_IssuePZByDocumentNumber(documentNumber=documentNumber)
        return invoke_operation(api, OP_IssuePZByDocumentNumber if validate else OP_IssuePZByDocumentNumber_RAW, params=params, data=data)
    raise TypeError("IssuePZ(): internal overload dispatch failure")

@overload
def IssuePZCorrection(api: SyncInvokerProtocol, documentId: int, issue: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def IssuePZCorrection(api: SyncRequestProtocol, documentId: int, issue: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def IssuePZCorrection(api: SyncInvokerProtocol, documentNumber: str, issue: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def IssuePZCorrection(api: SyncRequestProtocol, documentNumber: str, issue: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
def IssuePZCorrection(api: object, documentId: object = _UNSET, issue: object = _UNSET, documentNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'issue' if issue is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'issue', 'documentId'}:
        if exact_match_name is not None:
            raise TypeError("IssuePZCorrection(): ambiguous overload for provided arguments")
        exact_match = 'IssuePZCorrection'
        exact_match_name = 'IssuePZCorrection'
    if provided_names == {'documentNumber', 'issue'}:
        if exact_match_name is not None:
            raise TypeError("IssuePZCorrection(): ambiguous overload for provided arguments")
        exact_match = 'IssuePZCorrectionByDocumentNumberIssue'
        exact_match_name = 'IssuePZCorrectionByDocumentNumberIssue'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'issue', 'documentId'}.issubset(provided_names) and provided_names.issubset({'issue', 'documentId'}):
            candidates.append((2, -2, 'IssuePZCorrection'))
        if {'documentNumber', 'issue'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'issue'}):
            candidates.append((2, -2, 'IssuePZCorrectionByDocumentNumberIssue'))
        if not candidates:
            raise TypeError("IssuePZCorrection(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssuePZCorrection(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssuePZCorrection':
        params, data = _prepare_IssuePZCorrection(documentId=documentId, issue=issue)
        return invoke_operation(api, OP_IssuePZCorrection if validate else OP_IssuePZCorrection_RAW, params=params, data=data)
    if selected == 'IssuePZCorrectionByDocumentNumberIssue':
        params, data = _prepare_IssuePZCorrectionByDocumentNumberIssue(documentNumber=documentNumber, issue=issue)
        return invoke_operation(api, OP_IssuePZCorrectionByDocumentNumberIssue if validate else OP_IssuePZCorrectionByDocumentNumberIssue_RAW, params=params, data=data)
    raise TypeError("IssuePZCorrection(): internal overload dispatch failure")

@overload
def ChangeDocumentNumber(api: SyncInvokerProtocol, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def ChangeDocumentNumber(api: SyncRequestProtocol, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def ChangeDocumentNumber(api: object, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_ChangeDocumentNumber(id=id, number=number)
    return invoke_operation(api, OP_ChangeDocumentNumber if validate else OP_ChangeDocumentNumber_RAW, params=params, data=data)

__all__ = ["AddNew", "Issue", "IssuePZ", "IssuePZCorrection", "ChangeDocumentNumber"]
