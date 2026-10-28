from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels import ProductMap
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels import ProductMapCreate
from ._common import (
    _prepare_Create,
    _prepare_Delete,
    _prepare_Get,
    _prepare_GetByCountry,
    _prepare_GetByErpProduct,
    _prepare_GetByShopProduct,
)
from ._ops import (
    OP_Create,
    OP_Create_RAW,
    OP_Delete,
    OP_Delete_RAW,
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
def Create(api: SyncInvokerProtocol, map: "ProductMapCreate", *, validate: bool = True) -> ResponseEnvelope[ProductMap]: ...
@overload
def Create(api: SyncRequestProtocol, map: "ProductMapCreate", *, validate: bool = True) -> ResponseEnvelope[ProductMap]: ...
def Create(api: object, map: "ProductMapCreate", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Create(validate=validate, map=map)
    return invoke_operation(api, OP_Create if validate else OP_Create_RAW, params=params, data=data)

@overload
def Delete(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Delete(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Delete(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Delete(id=id)
    return invoke_operation(api, OP_Delete if validate else OP_Delete_RAW, params=params, data=data)

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductMap]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductMap]]: ...
def Get(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get()
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetByCountry(api: SyncInvokerProtocol, countryId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductMap]]: ...
@overload
def GetByCountry(api: SyncRequestProtocol, countryId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductMap]]: ...
def GetByCountry(api: object, countryId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByCountry(countryId=countryId)
    return invoke_operation(api, OP_GetByCountry if validate else OP_GetByCountry_RAW, params=params, data=data)

@overload
def GetByErpProduct(api: SyncInvokerProtocol, erpProductId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductMap]]: ...
@overload
def GetByErpProduct(api: SyncRequestProtocol, erpProductId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductMap]]: ...
def GetByErpProduct(api: object, erpProductId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByErpProduct(erpProductId=erpProductId)
    return invoke_operation(api, OP_GetByErpProduct if validate else OP_GetByErpProduct_RAW, params=params, data=data)

@overload
def GetByShopProduct(api: SyncInvokerProtocol, shopProductId: str, *, validate: bool = True) -> ResponseEnvelope[List[ProductMap]]: ...
@overload
def GetByShopProduct(api: SyncRequestProtocol, shopProductId: str, *, validate: bool = True) -> ResponseEnvelope[List[ProductMap]]: ...
def GetByShopProduct(api: object, shopProductId: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByShopProduct(shopProductId=shopProductId)
    return invoke_operation(api, OP_GetByShopProduct if validate else OP_GetByShopProduct_RAW, params=params, data=data)

__all__ = ["Create", "Delete", "Get", "GetByCountry", "GetByErpProduct", "GetByShopProduct"]
