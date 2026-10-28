from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Contractors.ViewModels import Contractor
from SymfWebAPI.WebAPI.Interface.FKF.Contractors.ViewModels import ContractorCriteriaFilter
from SymfWebAPI.WebAPI.Interface.FKF.Contractors.ViewModels import ContractorListElement
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import FilterCriteria
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetByPosition,
    _prepare_GetByCode,
    _prepare_GetByNIP,
    _prepare_GetByPesel,
    _prepare_Filter,
    _prepare_AddNew,
    _prepare_Update,
    _prepare_GetPagedDocument,
    _prepare_FilterSql,
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
    OP_GetByNIP,
    OP_GetByNIP_RAW,
    OP_GetByPesel,
    OP_GetByPesel_RAW,
    OP_Filter,
    OP_Filter_RAW,
    OP_AddNew,
    OP_AddNew_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
    OP_FilterSql,
    OP_FilterSql_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
def Get(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get()
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetById(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def GetById(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
def GetById(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetById(id=id)
    return invoke_operation(api, OP_GetById if validate else OP_GetById_RAW, params=params, data=data)

@overload
def GetByPosition(api: SyncInvokerProtocol, position: int, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def GetByPosition(api: SyncRequestProtocol, position: int, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
def GetByPosition(api: object, position: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByPosition(position=position)
    return invoke_operation(api, OP_GetByPosition if validate else OP_GetByPosition_RAW, params=params, data=data)

@overload
def GetByCode(api: SyncInvokerProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def GetByCode(api: SyncRequestProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
def GetByCode(api: object, code: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByCode(code=code)
    return invoke_operation(api, OP_GetByCode if validate else OP_GetByCode_RAW, params=params, data=data)

@overload
def GetByNIP(api: SyncInvokerProtocol, nip: str, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
@overload
def GetByNIP(api: SyncRequestProtocol, nip: str, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
def GetByNIP(api: object, nip: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByNIP(nip=nip)
    return invoke_operation(api, OP_GetByNIP if validate else OP_GetByNIP_RAW, params=params, data=data)

@overload
def GetByPesel(api: SyncInvokerProtocol, pesel: str, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
@overload
def GetByPesel(api: SyncRequestProtocol, pesel: str, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
def GetByPesel(api: object, pesel: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByPesel(pesel=pesel)
    return invoke_operation(api, OP_GetByPesel if validate else OP_GetByPesel_RAW, params=params, data=data)

@overload
def Filter(api: SyncInvokerProtocol, criteria: List["FilterCriteria"], *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
@overload
def Filter(api: SyncRequestProtocol, criteria: List["FilterCriteria"], *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
def Filter(api: object, criteria: List["FilterCriteria"], *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Filter(validate=validate, criteria=criteria)
    return invoke_operation(api, OP_Filter if validate else OP_Filter_RAW, params=params, data=data)

@overload
def AddNew(api: SyncInvokerProtocol, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def AddNew(api: SyncRequestProtocol, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
def AddNew(api: object, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, contractor=contractor)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Update(api: SyncInvokerProtocol, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Update(validate=validate, contractor=contractor)
    return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)

@overload
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

@overload
def FilterSql(api: SyncInvokerProtocol, criteriaFilter: "ContractorCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
@overload
def FilterSql(api: SyncRequestProtocol, criteriaFilter: "ContractorCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
def FilterSql(api: object, criteriaFilter: "ContractorCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_FilterSql(validate=validate, criteriaFilter=criteriaFilter)
    return invoke_operation(api, OP_FilterSql if validate else OP_FilterSql_RAW, params=params, data=data)

__all__ = ["Get", "GetById", "GetByPosition", "GetByCode", "GetByNIP", "GetByPesel", "Filter", "AddNew", "Update", "GetPagedDocument", "FilterSql"]
