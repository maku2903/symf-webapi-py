from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Employees.ViewModels import Employee
from SymfWebAPI.WebAPI.Interface.FKF.Employees.ViewModels import EmployeeListElement
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetByPosition,
    _prepare_GetByCode,
    _prepare_AddNew,
    _prepare_Update,
    _prepare_GetPagedDocument,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetById,
    OP_GetById_RAW,
    OP_GetByPosition,
    OP_GetByPosition_RAW,
    OP_GetByCode,
    OP_GetByCode_RAW,
    OP_AddNew,
    OP_AddNew_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[EmployeeListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[EmployeeListElement]]: ...
def Get(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get()
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetById(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Employee]: ...
@overload
def GetById(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Employee]: ...
def GetById(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetById(id=id)
    return invoke_operation(api, OP_GetById if validate else OP_GetById_RAW, params=params, data=data)

@overload
def GetByPosition(api: SyncInvokerProtocol, position: int, *, validate: bool = True) -> ResponseEnvelope[Employee]: ...
@overload
def GetByPosition(api: SyncRequestProtocol, position: int, *, validate: bool = True) -> ResponseEnvelope[Employee]: ...
def GetByPosition(api: object, position: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByPosition(position=position)
    return invoke_operation(api, OP_GetByPosition if validate else OP_GetByPosition_RAW, params=params, data=data)

@overload
def GetByCode(api: SyncInvokerProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[Employee]: ...
@overload
def GetByCode(api: SyncRequestProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[Employee]: ...
def GetByCode(api: object, code: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByCode(code=code)
    return invoke_operation(api, OP_GetByCode if validate else OP_GetByCode_RAW, params=params, data=data)

@overload
def AddNew(api: SyncInvokerProtocol, employee: "Employee", *, validate: bool = True) -> ResponseEnvelope[Employee]: ...
@overload
def AddNew(api: SyncRequestProtocol, employee: "Employee", *, validate: bool = True) -> ResponseEnvelope[Employee]: ...
def AddNew(api: object, employee: "Employee", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, employee=employee)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Update(api: SyncInvokerProtocol, employee: "Employee", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, employee: "Employee", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, employee: "Employee", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Update(validate=validate, employee=employee)
    return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)

@overload
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

__all__ = ["Get", "GetById", "GetByPosition", "GetByCode", "AddNew", "Update", "GetPagedDocument"]
