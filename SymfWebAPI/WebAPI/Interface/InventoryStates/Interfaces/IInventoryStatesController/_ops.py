from __future__ import annotations

from typing import Any, List
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.InventoryStates.ViewModels import InventoryState

_ADAPTER_Get = TypeAdapter(List[InventoryState])
OP_Get = build_typed_operation(method='GET', path='/api/InventoryStates', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/InventoryStates')

_ADAPTER_GetByProductId = TypeAdapter(List[InventoryState])
OP_GetByProductId = build_typed_operation(method='GET', path='/api/InventoryStates/ByProduct', adapter=_ADAPTER_GetByProductId)
OP_GetByProductId_RAW = build_raw_operation(method='GET', path='/api/InventoryStates/ByProduct')

_ADAPTER_GetByProductCode = TypeAdapter(List[InventoryState])
OP_GetByProductCode = build_typed_operation(method='GET', path='/api/InventoryStates/ByProduct', adapter=_ADAPTER_GetByProductCode)
OP_GetByProductCode_RAW = build_raw_operation(method='GET', path='/api/InventoryStates/ByProduct')

_ADAPTER_GetByWarehouseId = TypeAdapter(List[InventoryState])
OP_GetByWarehouseId = build_typed_operation(method='GET', path='/api/InventoryStates/ByWarehouse', adapter=_ADAPTER_GetByWarehouseId)
OP_GetByWarehouseId_RAW = build_raw_operation(method='GET', path='/api/InventoryStates/ByWarehouse')

_ADAPTER_GetByWarehouseCode = TypeAdapter(List[InventoryState])
OP_GetByWarehouseCode = build_typed_operation(method='GET', path='/api/InventoryStates/ByWarehouse', adapter=_ADAPTER_GetByWarehouseCode)
OP_GetByWarehouseCode_RAW = build_raw_operation(method='GET', path='/api/InventoryStates/ByWarehouse')

_ADAPTER_GetByProductIdAndWarehouseId = TypeAdapter(InventoryState)
OP_GetByProductIdAndWarehouseId = build_typed_operation(method='GET', path='/api/InventoryStates/ByProductAndWarehouse', adapter=_ADAPTER_GetByProductIdAndWarehouseId)
OP_GetByProductIdAndWarehouseId_RAW = build_raw_operation(method='GET', path='/api/InventoryStates/ByProductAndWarehouse')

_ADAPTER_GetChanges = TypeAdapter(List[InventoryState])
OP_GetChanges = build_typed_operation(method='GET', path='/api/InventoryStates/Changes', adapter=_ADAPTER_GetChanges)
OP_GetChanges_RAW = build_raw_operation(method='GET', path='/api/InventoryStates/Changes')
