from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels import CountryProductList

_ADAPTER_Get = TypeAdapter(CountryProductList)
OP_Get = build_typed_operation(method='GET', path='/api/OssProduct', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/OssProduct')

_ADAPTER_GetByCountry = TypeAdapter(CountryProductList)
OP_GetByCountry = build_typed_operation(method='GET', path='/api/OssProduct', adapter=_ADAPTER_GetByCountry)
OP_GetByCountry_RAW = build_raw_operation(method='GET', path='/api/OssProduct')

_ADAPTER_GetByErpProduct = TypeAdapter(CountryProductList)
OP_GetByErpProduct = build_typed_operation(method='GET', path='/api/OssProduct', adapter=_ADAPTER_GetByErpProduct)
OP_GetByErpProduct_RAW = build_raw_operation(method='GET', path='/api/OssProduct')

_ADAPTER_GetByShopProduct = TypeAdapter(CountryProductList)
OP_GetByShopProduct = build_typed_operation(method='GET', path='/api/OssProduct', adapter=_ADAPTER_GetByShopProduct)
OP_GetByShopProduct_RAW = build_raw_operation(method='GET', path='/api/OssProduct')
