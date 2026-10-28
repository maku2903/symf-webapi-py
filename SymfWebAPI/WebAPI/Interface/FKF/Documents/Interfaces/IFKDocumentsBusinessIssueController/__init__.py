from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Issue.Business import BusinessDocumentIssue
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import Document
from ._common import (
    _prepare_NewPurchaseInvoice,
    _prepare_NewPurchaseInvoiceCorrection,
    _prepare_NewSaleInvoice,
    _prepare_NewSaleInvoiceCorrection,
)
from ._ops import (
    OP_NewPurchaseInvoice,
    OP_NewPurchaseInvoice_RAW,
    OP_NewPurchaseInvoiceCorrection,
    OP_NewPurchaseInvoiceCorrection_RAW,
    OP_NewSaleInvoice,
    OP_NewSaleInvoice_RAW,
    OP_NewSaleInvoiceCorrection,
    OP_NewSaleInvoiceCorrection_RAW,
)

_UNSET = object()

@overload
def NewPurchaseInvoice(api: SyncInvokerProtocol, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
@overload
def NewPurchaseInvoice(api: SyncRequestProtocol, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
def NewPurchaseInvoice(api: object, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_NewPurchaseInvoice(validate=validate, documentIssue=documentIssue)
    return invoke_operation(api, OP_NewPurchaseInvoice if validate else OP_NewPurchaseInvoice_RAW, params=params, data=data)

@overload
def NewPurchaseInvoiceCorrection(api: SyncInvokerProtocol, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
@overload
def NewPurchaseInvoiceCorrection(api: SyncRequestProtocol, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
def NewPurchaseInvoiceCorrection(api: object, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_NewPurchaseInvoiceCorrection(validate=validate, documentIssue=documentIssue)
    return invoke_operation(api, OP_NewPurchaseInvoiceCorrection if validate else OP_NewPurchaseInvoiceCorrection_RAW, params=params, data=data)

@overload
def NewSaleInvoice(api: SyncInvokerProtocol, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
@overload
def NewSaleInvoice(api: SyncRequestProtocol, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
def NewSaleInvoice(api: object, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_NewSaleInvoice(validate=validate, documentIssue=documentIssue)
    return invoke_operation(api, OP_NewSaleInvoice if validate else OP_NewSaleInvoice_RAW, params=params, data=data)

@overload
def NewSaleInvoiceCorrection(api: SyncInvokerProtocol, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
@overload
def NewSaleInvoiceCorrection(api: SyncRequestProtocol, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Document]: ...
def NewSaleInvoiceCorrection(api: object, documentIssue: "BusinessDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_NewSaleInvoiceCorrection(validate=validate, documentIssue=documentIssue)
    return invoke_operation(api, OP_NewSaleInvoiceCorrection if validate else OP_NewSaleInvoiceCorrection_RAW, params=params, data=data)

__all__ = ["NewPurchaseInvoice", "NewPurchaseInvoiceCorrection", "NewSaleInvoice", "NewSaleInvoiceCorrection"]
