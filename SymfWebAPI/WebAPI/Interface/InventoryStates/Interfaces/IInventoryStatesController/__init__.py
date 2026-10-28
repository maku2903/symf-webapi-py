from __future__ import annotations

from typing import Any, List, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.InventoryStates.ViewModels import InventoryState
from ._common import (
    _prepare_Get,
    _prepare_GetByProductId,
    _prepare_GetByProductCode,
    _prepare_GetByWarehouseId,
    _prepare_GetByWarehouseCode,
    _prepare_GetByProductIdAndWarehouseId,
    _prepare_GetChanges,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByProductId,
    OP_GetByProductId_RAW,
    OP_GetByProductCode,
    OP_GetByProductCode_RAW,
    OP_GetByWarehouseId,
    OP_GetByWarehouseId_RAW,
    OP_GetByWarehouseCode,
    OP_GetByWarehouseCode_RAW,
    OP_GetByProductIdAndWarehouseId,
    OP_GetByProductIdAndWarehouseId_RAW,
    OP_GetChanges,
    OP_GetChanges_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
def Get(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get()
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetByProductId(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
@overload
def GetByProductId(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
def GetByProductId(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByProductId(id=id)
    return invoke_operation(api, OP_GetByProductId if validate else OP_GetByProductId_RAW, params=params, data=data)

@overload
def GetByProductCode(api: SyncInvokerProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
@overload
def GetByProductCode(api: SyncRequestProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
def GetByProductCode(api: object, code: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByProductCode(code=code)
    return invoke_operation(api, OP_GetByProductCode if validate else OP_GetByProductCode_RAW, params=params, data=data)

@overload
def GetByWarehouseId(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
@overload
def GetByWarehouseId(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
def GetByWarehouseId(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByWarehouseId(id=id)
    return invoke_operation(api, OP_GetByWarehouseId if validate else OP_GetByWarehouseId_RAW, params=params, data=data)

@overload
def GetByWarehouseCode(api: SyncInvokerProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
@overload
def GetByWarehouseCode(api: SyncRequestProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
def GetByWarehouseCode(api: object, code: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByWarehouseCode(code=code)
    return invoke_operation(api, OP_GetByWarehouseCode if validate else OP_GetByWarehouseCode_RAW, params=params, data=data)

@overload
def GetByProductIdAndWarehouseId(api: SyncInvokerProtocol, productId: int, warehouseId: int, *, validate: bool = True) -> ResponseEnvelope[InventoryState]: ...
@overload
def GetByProductIdAndWarehouseId(api: SyncRequestProtocol, productId: int, warehouseId: int, *, validate: bool = True) -> ResponseEnvelope[InventoryState]: ...
def GetByProductIdAndWarehouseId(api: object, productId: int, warehouseId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByProductIdAndWarehouseId(productId=productId, warehouseId=warehouseId)
    return invoke_operation(api, OP_GetByProductIdAndWarehouseId if validate else OP_GetByProductIdAndWarehouseId_RAW, params=params, data=data)

@overload
def GetChanges(api: SyncInvokerProtocol, date: datetime, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
@overload
def GetChanges(api: SyncRequestProtocol, date: datetime, *, validate: bool = True) -> ResponseEnvelope[List[InventoryState]]: ...
def GetChanges(api: object, date: datetime, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetChanges(date=date)
    return invoke_operation(api, OP_GetChanges if validate else OP_GetChanges_RAW, params=params, data=data)

__all__ = ["Get", "GetByProductId", "GetByProductCode", "GetByWarehouseId", "GetByWarehouseCode", "GetByProductIdAndWarehouseId", "GetChanges"]
