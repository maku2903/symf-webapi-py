from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import Document
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Issue.Custom import DocumentIssue
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import DocumentMessage
from ._common import (
    _prepare_AddNew,
    _prepare_Validate,
)
from ._ops import (
    OP_AddNew,
    OP_AddNew_RAW,
    OP_Validate,
    OP_Validate_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, documentIssue: "DocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
@overload
def AddNew(api: SyncRequestProtocol, documentIssue: "DocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
def AddNew(api: object, documentIssue: "DocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, documentIssue=documentIssue)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Validate(api: SyncInvokerProtocol, documentIssue: "DocumentIssue", *, validate: bool = True) -> ResponseEnvelope[List[DocumentMessage]]: ...
@overload
def Validate(api: SyncRequestProtocol, documentIssue: "DocumentIssue", *, validate: bool = True) -> ResponseEnvelope[List[DocumentMessage]]: ...
def Validate(api: object, documentIssue: "DocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Validate(validate=validate, documentIssue=documentIssue)
    return invoke_operation(api, OP_Validate if validate else OP_Validate_RAW, params=params, data=data)

__all__ = ["AddNew", "Validate"]
