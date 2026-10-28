from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Dimension
from ._common import (
    _prepare_GetById,
    _prepare_GetByPosition,
    _prepare_GetByCode,
)
from ._ops import (
    OP_GetById,
    OP_GetById_RAW,
    OP_GetByPosition,
    OP_GetByPosition_RAW,
    OP_GetByCode,
    OP_GetByCode_RAW,
)

_UNSET = object()

@overload
def GetById(api: SyncInvokerProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def GetById(api: SyncRequestProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def GetById(api: object, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetById(contractorId=contractorId)
    return invoke_operation(api, OP_GetById if validate else OP_GetById_RAW, params=params, data=data)

@overload
def GetByPosition(api: SyncInvokerProtocol, contractorPosition: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def GetByPosition(api: SyncRequestProtocol, contractorPosition: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def GetByPosition(api: object, contractorPosition: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByPosition(contractorPosition=contractorPosition)
    return invoke_operation(api, OP_GetByPosition if validate else OP_GetByPosition_RAW, params=params, data=data)

@overload
def GetByCode(api: SyncInvokerProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def GetByCode(api: SyncRequestProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def GetByCode(api: object, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByCode(contractorCode=contractorCode)
    return invoke_operation(api, OP_GetByCode if validate else OP_GetByCode_RAW, params=params, data=data)

__all__ = ["GetById", "GetByPosition", "GetByCode"]
