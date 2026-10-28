from __future__ import annotations

from typing import Any, List, Optional, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import AdvancePaymentOptions
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleCorrection
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleCorrectionIssue
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocument
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentIssue
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentWZ
from ._common import (
    _prepare_AddNew,
    _prepare_AddNewByCorrectionIssue,
    _prepare_Issue,
    _prepare_IssueByNumber,
    _prepare_IssueAdvancePayment,
    _prepare_IssueAdvancePaymentByDocumentNumberOptions,
    _prepare_IssueWZ,
    _prepare_IssueWZByDocumentNumberInBuffer,
    _prepare_IssueWZCorrection,
    _prepare_IssueWZCorrectionByDocumentNumberIssue,
    _prepare_ChangeDocumentNumber,
    _prepare_IssuePN,
    _prepare_IssuePNByDocumentNumber,
    _prepare_ChangeFiscalStatus,
    _prepare_ChangeFiscalStatusByDocumentNumber,
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
    OP_IssueAdvancePayment,
    OP_IssueAdvancePayment_RAW,
    OP_IssueAdvancePaymentByDocumentNumberOptions,
    OP_IssueAdvancePaymentByDocumentNumberOptions_RAW,
    OP_IssueWZ,
    OP_IssueWZ_RAW,
    OP_IssueWZByDocumentNumberInBuffer,
    OP_IssueWZByDocumentNumberInBuffer_RAW,
    OP_IssueWZCorrection,
    OP_IssueWZCorrection_RAW,
    OP_IssueWZCorrectionByDocumentNumberIssue,
    OP_IssueWZCorrectionByDocumentNumberIssue_RAW,
    OP_ChangeDocumentNumber,
    OP_ChangeDocumentNumber_RAW,
    OP_IssuePN,
    OP_IssuePN_RAW,
    OP_IssuePNByDocumentNumber,
    OP_IssuePNByDocumentNumber_RAW,
    OP_ChangeFiscalStatus,
    OP_ChangeFiscalStatus_RAW,
    OP_ChangeFiscalStatusByDocumentNumber,
    OP_ChangeFiscalStatusByDocumentNumber_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, document: "SaleDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, document: "SaleDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, correction: "SaleCorrectionIssue", *, validate: bool = True) -> ResponseEnvelope[SaleCorrection]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, correction: "SaleCorrectionIssue", *, validate: bool = True) -> ResponseEnvelope[SaleCorrection]: ...
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
def Issue(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def Issue(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def Issue(api: SyncInvokerProtocol, number: str, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def Issue(api: SyncRequestProtocol, number: str, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
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
def IssueAdvancePayment(api: SyncInvokerProtocol, documentId: int, options: "AdvancePaymentOptions", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def IssueAdvancePayment(api: SyncRequestProtocol, documentId: int, options: "AdvancePaymentOptions", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def IssueAdvancePayment(api: SyncInvokerProtocol, documentNumber: str, options: "AdvancePaymentOptions", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def IssueAdvancePayment(api: SyncRequestProtocol, documentNumber: str, options: "AdvancePaymentOptions", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
def IssueAdvancePayment(api: object, documentId: object = _UNSET, options: object = _UNSET, documentNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'options' if options is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId', 'options'}:
        if exact_match_name is not None:
            raise TypeError("IssueAdvancePayment(): ambiguous overload for provided arguments")
        exact_match = 'IssueAdvancePayment'
        exact_match_name = 'IssueAdvancePayment'
    if provided_names == {'documentNumber', 'options'}:
        if exact_match_name is not None:
            raise TypeError("IssueAdvancePayment(): ambiguous overload for provided arguments")
        exact_match = 'IssueAdvancePaymentByDocumentNumberOptions'
        exact_match_name = 'IssueAdvancePaymentByDocumentNumberOptions'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId', 'options'}.issubset(provided_names) and provided_names.issubset({'documentId', 'options'}):
            candidates.append((2, -2, 'IssueAdvancePayment'))
        if {'documentNumber', 'options'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'options'}):
            candidates.append((2, -2, 'IssueAdvancePaymentByDocumentNumberOptions'))
        if not candidates:
            raise TypeError("IssueAdvancePayment(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssueAdvancePayment(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssueAdvancePayment':
        params, data = _prepare_IssueAdvancePayment(validate=validate, documentId=documentId, options=options)
        return invoke_operation(api, OP_IssueAdvancePayment if validate else OP_IssueAdvancePayment_RAW, params=params, data=data)
    if selected == 'IssueAdvancePaymentByDocumentNumberOptions':
        params, data = _prepare_IssueAdvancePaymentByDocumentNumberOptions(validate=validate, documentNumber=documentNumber, options=options)
        return invoke_operation(api, OP_IssueAdvancePaymentByDocumentNumberOptions if validate else OP_IssueAdvancePaymentByDocumentNumberOptions_RAW, params=params, data=data)
    raise TypeError("IssueAdvancePayment(): internal overload dispatch failure")

@overload
def IssueWZ(api: SyncInvokerProtocol, documentId: int, inBuffer: Optional[int] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def IssueWZ(api: SyncRequestProtocol, documentId: int, inBuffer: Optional[int] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def IssueWZ(api: SyncInvokerProtocol, documentNumber: str, inBuffer: Optional[int] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def IssueWZ(api: SyncRequestProtocol, documentNumber: str, inBuffer: Optional[int] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
def IssueWZ(api: object, documentId: object = _UNSET, inBuffer: object = _UNSET, documentNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'inBuffer' if inBuffer is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId', 'inBuffer'}:
        if exact_match_name is not None:
            raise TypeError("IssueWZ(): ambiguous overload for provided arguments")
        exact_match = 'IssueWZ'
        exact_match_name = 'IssueWZ'
    if provided_names == {'documentNumber', 'inBuffer'}:
        if exact_match_name is not None:
            raise TypeError("IssueWZ(): ambiguous overload for provided arguments")
        exact_match = 'IssueWZByDocumentNumberInBuffer'
        exact_match_name = 'IssueWZByDocumentNumberInBuffer'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId', 'inBuffer'}):
            candidates.append((1, -2, 'IssueWZ'))
        if {'documentNumber'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'inBuffer'}):
            candidates.append((1, -2, 'IssueWZByDocumentNumberInBuffer'))
        if not candidates:
            raise TypeError("IssueWZ(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssueWZ(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssueWZ':
        params, data = _prepare_IssueWZ(documentId=documentId, inBuffer=inBuffer)
        return invoke_operation(api, OP_IssueWZ if validate else OP_IssueWZ_RAW, params=params, data=data)
    if selected == 'IssueWZByDocumentNumberInBuffer':
        params, data = _prepare_IssueWZByDocumentNumberInBuffer(documentNumber=documentNumber, inBuffer=inBuffer)
        return invoke_operation(api, OP_IssueWZByDocumentNumberInBuffer if validate else OP_IssueWZByDocumentNumberInBuffer_RAW, params=params, data=data)
    raise TypeError("IssueWZ(): internal overload dispatch failure")

@overload
def IssueWZCorrection(api: SyncInvokerProtocol, documentId: int, issue: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def IssueWZCorrection(api: SyncRequestProtocol, documentId: int, issue: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def IssueWZCorrection(api: SyncInvokerProtocol, documentNumber: str, issue: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def IssueWZCorrection(api: SyncRequestProtocol, documentNumber: str, issue: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
def IssueWZCorrection(api: object, documentId: object = _UNSET, issue: object = _UNSET, documentNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
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
            raise TypeError("IssueWZCorrection(): ambiguous overload for provided arguments")
        exact_match = 'IssueWZCorrection'
        exact_match_name = 'IssueWZCorrection'
    if provided_names == {'documentNumber', 'issue'}:
        if exact_match_name is not None:
            raise TypeError("IssueWZCorrection(): ambiguous overload for provided arguments")
        exact_match = 'IssueWZCorrectionByDocumentNumberIssue'
        exact_match_name = 'IssueWZCorrectionByDocumentNumberIssue'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'issue', 'documentId'}.issubset(provided_names) and provided_names.issubset({'issue', 'documentId'}):
            candidates.append((2, -2, 'IssueWZCorrection'))
        if {'documentNumber', 'issue'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'issue'}):
            candidates.append((2, -2, 'IssueWZCorrectionByDocumentNumberIssue'))
        if not candidates:
            raise TypeError("IssueWZCorrection(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssueWZCorrection(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssueWZCorrection':
        params, data = _prepare_IssueWZCorrection(documentId=documentId, issue=issue)
        return invoke_operation(api, OP_IssueWZCorrection if validate else OP_IssueWZCorrection_RAW, params=params, data=data)
    if selected == 'IssueWZCorrectionByDocumentNumberIssue':
        params, data = _prepare_IssueWZCorrectionByDocumentNumberIssue(documentNumber=documentNumber, issue=issue)
        return invoke_operation(api, OP_IssueWZCorrectionByDocumentNumberIssue if validate else OP_IssueWZCorrectionByDocumentNumberIssue_RAW, params=params, data=data)
    raise TypeError("IssueWZCorrection(): internal overload dispatch failure")

@overload
def ChangeDocumentNumber(api: SyncInvokerProtocol, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def ChangeDocumentNumber(api: SyncRequestProtocol, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def ChangeDocumentNumber(api: object, id: int, number: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_ChangeDocumentNumber(id=id, number=number)
    return invoke_operation(api, OP_ChangeDocumentNumber if validate else OP_ChangeDocumentNumber_RAW, params=params, data=data)

@overload
def IssuePN(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def IssuePN(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def IssuePN(api: SyncInvokerProtocol, documentNumber: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def IssuePN(api: SyncRequestProtocol, documentNumber: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def IssuePN(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId'}:
        if exact_match_name is not None:
            raise TypeError("IssuePN(): ambiguous overload for provided arguments")
        exact_match = 'IssuePN'
        exact_match_name = 'IssuePN'
    if provided_names == {'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("IssuePN(): ambiguous overload for provided arguments")
        exact_match = 'IssuePNByDocumentNumber'
        exact_match_name = 'IssuePNByDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'IssuePN'))
        if {'documentNumber'}.issubset(provided_names) and provided_names.issubset({'documentNumber'}):
            candidates.append((1, -1, 'IssuePNByDocumentNumber'))
        if not candidates:
            raise TypeError("IssuePN(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssuePN(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssuePN':
        params, data = _prepare_IssuePN(documentId=documentId)
        return invoke_operation(api, OP_IssuePN if validate else OP_IssuePN_RAW, params=params, data=data)
    if selected == 'IssuePNByDocumentNumber':
        params, data = _prepare_IssuePNByDocumentNumber(documentNumber=documentNumber)
        return invoke_operation(api, OP_IssuePNByDocumentNumber if validate else OP_IssuePNByDocumentNumber_RAW, params=params, data=data)
    raise TypeError("IssuePN(): internal overload dispatch failure")

@overload
def ChangeFiscalStatus(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def ChangeFiscalStatus(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def ChangeFiscalStatus(api: SyncInvokerProtocol, documentNumber: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def ChangeFiscalStatus(api: SyncRequestProtocol, documentNumber: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def ChangeFiscalStatus(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId'}:
        if exact_match_name is not None:
            raise TypeError("ChangeFiscalStatus(): ambiguous overload for provided arguments")
        exact_match = 'ChangeFiscalStatus'
        exact_match_name = 'ChangeFiscalStatus'
    if provided_names == {'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("ChangeFiscalStatus(): ambiguous overload for provided arguments")
        exact_match = 'ChangeFiscalStatusByDocumentNumber'
        exact_match_name = 'ChangeFiscalStatusByDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'ChangeFiscalStatus'))
        if {'documentNumber'}.issubset(provided_names) and provided_names.issubset({'documentNumber'}):
            candidates.append((1, -1, 'ChangeFiscalStatusByDocumentNumber'))
        if not candidates:
            raise TypeError("ChangeFiscalStatus(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("ChangeFiscalStatus(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'ChangeFiscalStatus':
        params, data = _prepare_ChangeFiscalStatus(documentId=documentId)
        return invoke_operation(api, OP_ChangeFiscalStatus if validate else OP_ChangeFiscalStatus_RAW, params=params, data=data)
    if selected == 'ChangeFiscalStatusByDocumentNumber':
        params, data = _prepare_ChangeFiscalStatusByDocumentNumber(documentNumber=documentNumber)
        return invoke_operation(api, OP_ChangeFiscalStatusByDocumentNumber if validate else OP_ChangeFiscalStatusByDocumentNumber_RAW, params=params, data=data)
    raise TypeError("ChangeFiscalStatus(): internal overload dispatch failure")

__all__ = ["AddNew", "Issue", "IssueAdvancePayment", "IssueWZ", "IssueWZCorrection", "ChangeDocumentNumber", "IssuePN", "ChangeFiscalStatus"]
