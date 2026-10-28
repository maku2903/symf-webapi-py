from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Rdf import RdfDocumentLink
from ._common import (
    _prepare_AddNew,
    _prepare_Update,
)
from ._ops import (
    OP_AddNew,
    OP_AddNew_RAW,
    OP_Update,
    OP_Update_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, documentId: int, yearId: int, newDocumentLink: "RdfDocumentLink", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def AddNew(api: SyncRequestProtocol, documentId: int, yearId: int, newDocumentLink: "RdfDocumentLink", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def AddNew(api: object, documentId: int, yearId: int, newDocumentLink: "RdfDocumentLink", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, documentId=documentId, yearId=yearId, newDocumentLink=newDocumentLink)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Update(api: SyncInvokerProtocol, documentId: int, yearId: int, newDocumentLink: "RdfDocumentLink", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, documentId: int, yearId: int, newDocumentLink: "RdfDocumentLink", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, documentId: int, yearId: int, newDocumentLink: "RdfDocumentLink", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Update(validate=validate, documentId=documentId, yearId=yearId, newDocumentLink=newDocumentLink)
    return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)

__all__ = ["AddNew", "Update"]
