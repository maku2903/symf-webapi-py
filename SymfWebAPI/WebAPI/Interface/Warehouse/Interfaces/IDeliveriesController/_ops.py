from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import DeliveryListElement

_ADAPTER_GetInWarehouse = TypeAdapter(List[DeliveryListElement])
OP_GetInWarehouse = build_typed_operation(method='GET', path='/api/Deliveries/InWarehouse', adapter=_ADAPTER_GetInWarehouse)
OP_GetInWarehouse_RAW = build_raw_operation(method='GET', path='/api/Deliveries/InWarehouse')

_ADAPTER_GetInWarehouseByProductCodeWarehouseCode = TypeAdapter(List[DeliveryListElement])
OP_GetInWarehouseByProductCodeWarehouseCode = build_typed_operation(method='GET', path='/api/Deliveries/InWarehouse', adapter=_ADAPTER_GetInWarehouseByProductCodeWarehouseCode)
OP_GetInWarehouseByProductCodeWarehouseCode_RAW = build_raw_operation(method='GET', path='/api/Deliveries/InWarehouse')
