from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.HMF.Develogic.ViewModels import DevelogicAdvancePayment
from SymfWebAPI.WebAPI.Interface.HMF.Develogic.ViewModels import DevelogicContractInvoiceIssue
from SymfWebAPI.WebAPI.Interface.HMF.Develogic.ViewModels import DevelogicDocumentIssue
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocument
from ._common import (
    _prepare_AddNew,
    _prepare_IssueAdvancePayment,
    _prepare_IssueContractInvoice,
)
from ._ops import (
    OP_AddNew,
    OP_AddNew_RAW,
    OP_IssueAdvancePayment,
    OP_IssueAdvancePayment_RAW,
    OP_IssueContractInvoice,
    OP_IssueContractInvoice_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, invoiceKind: "IssueInvoiceKind", document: "DevelogicDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, invoiceKind: "IssueInvoiceKind", document: "DevelogicDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
def AddNew(api: object, issue: bool, invoiceKind: "IssueInvoiceKind", document: "DevelogicDocumentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, issue=issue, invoiceKind=invoiceKind, document=document)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def IssueAdvancePayment(api: SyncInvokerProtocol, contractId: "DevelogicAdvancePayment", invoiceKind: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def IssueAdvancePayment(api: SyncRequestProtocol, contractId: "DevelogicAdvancePayment", invoiceKind: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
def IssueAdvancePayment(api: object, contractId: "DevelogicAdvancePayment", invoiceKind: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IssueAdvancePayment(contractId=contractId, invoiceKind=invoiceKind)
    return invoke_operation(api, OP_IssueAdvancePayment if validate else OP_IssueAdvancePayment_RAW, params=params, data=data)

@overload
def IssueContractInvoice(api: SyncInvokerProtocol, contractId: "DevelogicContractInvoiceIssue", invoiceKind: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def IssueContractInvoice(api: SyncRequestProtocol, contractId: "DevelogicContractInvoiceIssue", invoiceKind: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
def IssueContractInvoice(api: object, contractId: "DevelogicContractInvoiceIssue", invoiceKind: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IssueContractInvoice(contractId=contractId, invoiceKind=invoiceKind)
    return invoke_operation(api, OP_IssueContractInvoice if validate else OP_IssueContractInvoice_RAW, params=params, data=data)

__all__ = ["AddNew", "IssueAdvancePayment", "IssueContractInvoice"]
