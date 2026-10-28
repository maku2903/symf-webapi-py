from __future__ import annotations

from typing import Any, Literal, overload
from SymfWebAPI.client import SyncAPI
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocument
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentIssue
from .json_types import PurchaseDocumentJSON

@overload
def AddNew(api: SyncAPI, issue: bool, document: "PurchaseDocumentIssue", *, validate: Literal[True] = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def AddNew(api: SyncAPI, issue: bool, document: Any, *, validate: Literal[False]) -> ResponseEnvelope[PurchaseDocumentJSON]: ...
@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, document: "PurchaseDocumentIssue", *, validate: Literal[True] = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, document: Any, *, validate: Literal[False]) -> ResponseEnvelope[PurchaseDocumentJSON]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, document: "PurchaseDocumentIssue", *, validate: Literal[True] = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, document: Any, *, validate: Literal[False]) -> ResponseEnvelope[PurchaseDocumentJSON]: ...
