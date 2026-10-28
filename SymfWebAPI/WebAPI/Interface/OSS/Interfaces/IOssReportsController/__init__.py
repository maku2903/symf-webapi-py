from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from ._common import (
    _prepare_GetOrderPDF,
    _prepare_GetSaleDocumentPDF,
    _prepare_GetWarehouseDocumentPDF,
)
from ._ops import (
    OP_GetOrderPDF,
    OP_GetOrderPDF_RAW,
    OP_GetSaleDocumentPDF,
    OP_GetSaleDocumentPDF_RAW,
    OP_GetWarehouseDocumentPDF,
    OP_GetWarehouseDocumentPDF_RAW,
)

_UNSET = object()

@overload
def GetOrderPDF(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetOrderPDF(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
def GetOrderPDF(api: object, orderId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetOrderPDF(orderId=orderId)
    return invoke_operation(api, OP_GetOrderPDF if validate else OP_GetOrderPDF_RAW, params=params, data=data)

@overload
def GetSaleDocumentPDF(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetSaleDocumentPDF(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
def GetSaleDocumentPDF(api: object, documentId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSaleDocumentPDF(documentId=documentId)
    return invoke_operation(api, OP_GetSaleDocumentPDF if validate else OP_GetSaleDocumentPDF_RAW, params=params, data=data)

@overload
def GetWarehouseDocumentPDF(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetWarehouseDocumentPDF(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
def GetWarehouseDocumentPDF(api: object, documentId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWarehouseDocumentPDF(documentId=documentId)
    return invoke_operation(api, OP_GetWarehouseDocumentPDF if validate else OP_GetWarehouseDocumentPDF_RAW, params=params, data=data)

__all__ = ["GetOrderPDF", "GetSaleDocumentPDF", "GetWarehouseDocumentPDF"]
