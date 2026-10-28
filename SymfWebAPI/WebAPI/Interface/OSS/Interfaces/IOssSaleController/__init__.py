from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels.Sales import OssDomesticSaleDocument
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels.Sales import OssSaleDocument
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocument
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentWZ
from ._common import (
    _prepare_AddNew,
    _prepare_AddNewReceipt,
    _prepare_IssueWZ,
)
from ._ops import (
    OP_AddNew,
    OP_AddNew_RAW,
    OP_AddNewReceipt,
    OP_AddNewReceipt_RAW,
    OP_IssueWZ,
    OP_IssueWZ_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, invoiceKind: "IssueInvoiceKind", saleDocument: "OssSaleDocument", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, invoiceKind: "IssueInvoiceKind", saleDocument: "OssSaleDocument", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
def AddNew(api: object, issue: bool, invoiceKind: "IssueInvoiceKind", saleDocument: "OssSaleDocument", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, issue=issue, invoiceKind=invoiceKind, saleDocument=saleDocument)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def AddNewReceipt(api: SyncInvokerProtocol, issue: bool, invoiceKind: "IssueInvoiceKind", receipt: "OssDomesticSaleDocument", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def AddNewReceipt(api: SyncRequestProtocol, issue: bool, invoiceKind: "IssueInvoiceKind", receipt: "OssDomesticSaleDocument", *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
def AddNewReceipt(api: object, issue: bool, invoiceKind: "IssueInvoiceKind", receipt: "OssDomesticSaleDocument", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNewReceipt(validate=validate, issue=issue, invoiceKind=invoiceKind, receipt=receipt)
    return invoke_operation(api, OP_AddNewReceipt if validate else OP_AddNewReceipt_RAW, params=params, data=data)

@overload
def IssueWZ(api: SyncInvokerProtocol, documentId: int, inBuffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def IssueWZ(api: SyncRequestProtocol, documentId: int, inBuffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
def IssueWZ(api: object, documentId: int, inBuffer: bool, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IssueWZ(documentId=documentId, inBuffer=inBuffer)
    return invoke_operation(api, OP_IssueWZ if validate else OP_IssueWZ_RAW, params=params, data=data)

__all__ = ["AddNew", "AddNewReceipt", "IssueWZ"]
