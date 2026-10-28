from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import Order
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderFV
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderWZ
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels.Orders import OssOrder
from ._common import (
    _prepare_AddNew,
    _prepare_IssueFV,
    _prepare_IssueWZ,
)
from ._ops import (
    OP_AddNew,
    OP_AddNew_RAW,
    OP_IssueFV,
    OP_IssueFV_RAW,
    OP_IssueWZ,
    OP_IssueWZ_RAW,
)

_UNSET = object()

@overload
def AddNew(api: SyncInvokerProtocol, issue: bool, order: "OssOrder", *, validate: bool = True) -> ResponseEnvelope[Order]: ...
@overload
def AddNew(api: SyncRequestProtocol, issue: bool, order: "OssOrder", *, validate: bool = True) -> ResponseEnvelope[Order]: ...
def AddNew(api: object, issue: bool, order: "OssOrder", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, issue=issue, order=order)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def IssueFV(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
@overload
def IssueFV(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
def IssueFV(api: object, orderId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IssueFV(orderId=orderId)
    return invoke_operation(api, OP_IssueFV if validate else OP_IssueFV_RAW, params=params, data=data)

@overload
def IssueWZ(api: SyncInvokerProtocol, orderId: int, inBuffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
@overload
def IssueWZ(api: SyncRequestProtocol, orderId: int, inBuffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
def IssueWZ(api: object, orderId: int, inBuffer: bool, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IssueWZ(orderId=orderId, inBuffer=inBuffer)
    return invoke_operation(api, OP_IssueWZ if validate else OP_IssueWZ_RAW, params=params, data=data)

__all__ = ["AddNew", "IssueFV", "IssueWZ"]
