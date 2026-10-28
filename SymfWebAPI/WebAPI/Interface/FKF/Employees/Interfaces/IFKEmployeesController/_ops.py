from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Employees.ViewModels import Employee
from SymfWebAPI.WebAPI.Interface.FKF.Employees.ViewModels import EmployeeListElement
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType

_ADAPTER_Get = TypeAdapter(List[EmployeeListElement])
OP_Get = build_typed_operation(method='GET', path='/api/FKEmployees', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/FKEmployees')

_ADAPTER_GetById = TypeAdapter(Employee)
OP_GetById = build_typed_operation(method='GET', path='/api/FKEmployees', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/FKEmployees')

_ADAPTER_GetByPosition = TypeAdapter(Employee)
OP_GetByPosition = build_typed_operation(method='GET', path='/api/FKEmployees', adapter=_ADAPTER_GetByPosition)
OP_GetByPosition_RAW = build_raw_operation(method='GET', path='/api/FKEmployees')

_ADAPTER_GetByCode = TypeAdapter(Employee)
OP_GetByCode = build_typed_operation(method='GET', path='/api/FKEmployees', adapter=_ADAPTER_GetByCode)
OP_GetByCode_RAW = build_raw_operation(method='GET', path='/api/FKEmployees')

_ADAPTER_AddNew = TypeAdapter(Employee)
OP_AddNew = build_typed_operation(method='POST', path='/api/FKEmployees/Create', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/FKEmployees/Create')

OP_Update = build_none_operation(method='PUT', path='/api/FKEmployees/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/FKEmployees/Update')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/FKEmployees/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/FKEmployees/Page')
