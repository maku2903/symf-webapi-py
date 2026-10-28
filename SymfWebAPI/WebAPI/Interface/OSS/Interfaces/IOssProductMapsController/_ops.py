from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels import ProductMap
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels import ProductMapCreate

_ADAPTER_Create = TypeAdapter(ProductMap)
OP_Create = build_typed_operation(method='POST', path='/api/OssProductMap/Create', adapter=_ADAPTER_Create)
OP_Create_RAW = build_raw_operation(method='POST', path='/api/OssProductMap/Create')

OP_Delete = build_none_operation(method='DELETE', path='/api/OssProductMap/Delete')
OP_Delete_RAW = build_raw_operation(method='DELETE', path='/api/OssProductMap/Delete')

_ADAPTER_Get = TypeAdapter(List[ProductMap])
OP_Get = build_typed_operation(method='GET', path='/api/OssProductMap', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/OssProductMap')

_ADAPTER_GetByCountry = TypeAdapter(List[ProductMap])
OP_GetByCountry = build_typed_operation(method='GET', path='/api/OssProductMap', adapter=_ADAPTER_GetByCountry)
OP_GetByCountry_RAW = build_raw_operation(method='GET', path='/api/OssProductMap')

_ADAPTER_GetByErpProduct = TypeAdapter(List[ProductMap])
OP_GetByErpProduct = build_typed_operation(method='GET', path='/api/OssProductMap', adapter=_ADAPTER_GetByErpProduct)
OP_GetByErpProduct_RAW = build_raw_operation(method='GET', path='/api/OssProductMap')

_ADAPTER_GetByShopProduct = TypeAdapter(List[ProductMap])
OP_GetByShopProduct = build_typed_operation(method='GET', path='/api/OssProductMap', adapter=_ADAPTER_GetByShopProduct)
OP_GetByShopProduct_RAW = build_raw_operation(method='GET', path='/api/OssProductMap')
