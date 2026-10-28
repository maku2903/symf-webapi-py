from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocument
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentIssue
from ._common import (
    _prepare_AddNew,
)
from ._ops import (
    OP_AddNew,
    OP_AddNew_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, document: "PurchaseDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, document: "PurchaseDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
def AddNew(api: object, issue: bool, document: "PurchaseDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, issue=issue, document=document)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

__all__ = ["AddNew"]
