from __future__ import annotations

from typing import Any, List
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import IncrementalSyncListElement
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.PriceLists import PriceList
from SymfWebAPI.WebAPI.Interface.Products.ViewModels.PriceLists import PriceListListElement

_ADAPTER_Get = TypeAdapter(PriceList)
OP_Get = build_typed_operation(method='GET', path='/api/PriceLists', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/PriceLists')

_ADAPTER_GetByCode = TypeAdapter(PriceList)
OP_GetByCode = build_typed_operation(method='GET', path='/api/PriceLists', adapter=_ADAPTER_GetByCode)
OP_GetByCode_RAW = build_raw_operation(method='GET', path='/api/PriceLists')

_ADAPTER_GetGet = TypeAdapter(List[PriceListListElement])
OP_GetGet = build_typed_operation(method='GET', path='/api/PriceLists', adapter=_ADAPTER_GetGet)
OP_GetGet_RAW = build_raw_operation(method='GET', path='/api/PriceLists')

_ADAPTER_IncrementalSync = TypeAdapter(List[IncrementalSyncListElement])
OP_IncrementalSync = build_typed_operation(method='GET', path='/api/PriceLists/IncrementalSync', adapter=_ADAPTER_IncrementalSync)
OP_IncrementalSync_RAW = build_raw_operation(method='GET', path='/api/PriceLists/IncrementalSync')
