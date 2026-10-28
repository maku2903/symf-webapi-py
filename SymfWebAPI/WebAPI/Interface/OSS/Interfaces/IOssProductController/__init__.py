from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels import CountryProductList
from ._common import (
    _prepare_Get,
    _prepare_GetByCountry,
    _prepare_GetByErpProduct,
    _prepare_GetByShopProduct,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByCountry,
    OP_GetByCountry_RAW,
    OP_GetByErpProduct,
    OP_GetByErpProduct_RAW,
    OP_GetByShopProduct,
    OP_GetByShopProduct_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[CountryProductList]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[CountryProductList]: ...
def Get(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get()
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetByCountry(api: SyncInvokerProtocol, countryId: int, *, validate: bool = True) -> ResponseEnvelope[CountryProductList]: ...
@overload
def GetByCountry(api: SyncRequestProtocol, countryId: int, *, validate: bool = True) -> ResponseEnvelope[CountryProductList]: ...
def GetByCountry(api: object, countryId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByCountry(countryId=countryId)
    return invoke_operation(api, OP_GetByCountry if validate else OP_GetByCountry_RAW, params=params, data=data)

@overload
def GetByErpProduct(api: SyncInvokerProtocol, erpProductId: int, *, validate: bool = True) -> ResponseEnvelope[CountryProductList]: ...
@overload
def GetByErpProduct(api: SyncRequestProtocol, erpProductId: int, *, validate: bool = True) -> ResponseEnvelope[CountryProductList]: ...
def GetByErpProduct(api: object, erpProductId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByErpProduct(erpProductId=erpProductId)
    return invoke_operation(api, OP_GetByErpProduct if validate else OP_GetByErpProduct_RAW, params=params, data=data)

@overload
def GetByShopProduct(api: SyncInvokerProtocol, shopProductId: str, *, validate: bool = True) -> ResponseEnvelope[CountryProductList]: ...
@overload
def GetByShopProduct(api: SyncRequestProtocol, shopProductId: str, *, validate: bool = True) -> ResponseEnvelope[CountryProductList]: ...
def GetByShopProduct(api: object, shopProductId: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByShopProduct(shopProductId=shopProductId)
    return invoke_operation(api, OP_GetByShopProduct if validate else OP_GetByShopProduct_RAW, params=params, data=data)

__all__ = ["Get", "GetByCountry", "GetByErpProduct", "GetByShopProduct"]
