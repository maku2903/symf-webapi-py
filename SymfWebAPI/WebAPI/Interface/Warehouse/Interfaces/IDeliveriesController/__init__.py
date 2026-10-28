from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import DeliveryListElement
from ._common import (
    _prepare_GetInWarehouse,
    _prepare_GetInWarehouseByProductCodeWarehouseCode,
)
from ._ops import (
    OP_GetInWarehouse,
    OP_GetInWarehouse_RAW,
    OP_GetInWarehouseByProductCodeWarehouseCode,
    OP_GetInWarehouseByProductCodeWarehouseCode_RAW,
)

_UNSET = object()

@overload
def GetInWarehouse(api: SyncInvokerProtocol, warehouseId: int, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[DeliveryListElement]]: ...
@overload
def GetInWarehouse(api: SyncRequestProtocol, warehouseId: int, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[DeliveryListElement]]: ...
@overload
def GetInWarehouse(api: SyncInvokerProtocol, warehouseCode: str, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[DeliveryListElement]]: ...
@overload
def GetInWarehouse(api: SyncRequestProtocol, warehouseCode: str, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[DeliveryListElement]]: ...
def GetInWarehouse(api: object, warehouseId: object = _UNSET, productId: object = _UNSET, warehouseCode: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'warehouseId' if warehouseId is not _UNSET else None,
        'productId' if productId is not _UNSET else None,
        'warehouseCode' if warehouseCode is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productId', 'warehouseId'}:
        if exact_match_name is not None:
            raise TypeError("GetInWarehouse(): ambiguous overload for provided arguments")
        exact_match = 'GetInWarehouse'
        exact_match_name = 'GetInWarehouse'
    if provided_names == {'productCode', 'warehouseCode'}:
        if exact_match_name is not None:
            raise TypeError("GetInWarehouse(): ambiguous overload for provided arguments")
        exact_match = 'GetInWarehouseByProductCodeWarehouseCode'
        exact_match_name = 'GetInWarehouseByProductCodeWarehouseCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId', 'warehouseId'}.issubset(provided_names) and provided_names.issubset({'productId', 'warehouseId'}):
            candidates.append((2, -2, 'GetInWarehouse'))
        if {'productCode', 'warehouseCode'}.issubset(provided_names) and provided_names.issubset({'productCode', 'warehouseCode'}):
            candidates.append((2, -2, 'GetInWarehouseByProductCodeWarehouseCode'))
        if not candidates:
            raise TypeError("GetInWarehouse(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetInWarehouse(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetInWarehouse':
        params, data = _prepare_GetInWarehouse(warehouseId=warehouseId, productId=productId)
        return invoke_operation(api, OP_GetInWarehouse if validate else OP_GetInWarehouse_RAW, params=params, data=data)
    if selected == 'GetInWarehouseByProductCodeWarehouseCode':
        params, data = _prepare_GetInWarehouseByProductCodeWarehouseCode(warehouseCode=warehouseCode, productCode=productCode)
        return invoke_operation(api, OP_GetInWarehouseByProductCodeWarehouseCode if validate else OP_GetInWarehouseByProductCodeWarehouseCode_RAW, params=params, data=data)
    raise TypeError("GetInWarehouse(): internal overload dispatch failure")

__all__ = ["GetInWarehouse"]
