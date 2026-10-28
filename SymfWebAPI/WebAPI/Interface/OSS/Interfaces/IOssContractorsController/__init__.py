from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import Contractor
from ._common import (
    _prepare_Get,
    _prepare_AddNew,
    _prepare_Update,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_AddNew,
    OP_AddNew_RAW,
    OP_Update,
    OP_Update_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
def Get(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get(id=id)
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def AddNew(api: SyncInvokerProtocol, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def AddNew(api: SyncRequestProtocol, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
def AddNew(api: object, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, syncFk=syncFk, contractor=contractor)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Update(api: SyncInvokerProtocol, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Update(validate=validate, syncFk=syncFk, contractor=contractor)
    return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)

__all__ = ["Get", "AddNew", "Update"]
