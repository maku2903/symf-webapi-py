from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import BusinessDictionary
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import BusinessDictionaryElement
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import ContractorPosition
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import Dictionary
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import DictionaryElement
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import DictionaryListElement
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_AddNew,
    _prepare_Update,
    _prepare_SetElementPosition,
    _prepare_SetElementPositionByIdPosition,
    _prepare_SetContractorPosition,
    _prepare_SetContractorPositionByIdPosition,
    _prepare_GetBusiness,
    _prepare_AddNewBusiness,
    _prepare_UpdateBusiness,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetById,
    OP_GetById_RAW,
    OP_AddNew,
    OP_AddNew_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_SetElementPosition,
    OP_SetElementPosition_RAW,
    OP_SetElementPositionByIdPosition,
    OP_SetElementPositionByIdPosition_RAW,
    OP_SetContractorPosition,
    OP_SetContractorPosition_RAW,
    OP_SetContractorPositionByIdPosition,
    OP_SetContractorPositionByIdPosition_RAW,
    OP_GetBusiness,
    OP_GetBusiness_RAW,
    OP_AddNewBusiness,
    OP_AddNewBusiness_RAW,
    OP_UpdateBusiness,
    OP_UpdateBusiness_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DictionaryListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DictionaryListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Dictionary]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Dictionary]: ...
def Get(api: object, id: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetById'
        exact_match_name = 'GetById'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'Get'))
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'GetById'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get()
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetById':
        params, data = _prepare_GetById(id=id)
        return invoke_operation(api, OP_GetById if validate else OP_GetById_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def AddNew(api: SyncInvokerProtocol, dictionaryId: int, element: "DictionaryElement", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def AddNew(api: SyncRequestProtocol, dictionaryId: int, element: "DictionaryElement", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def AddNew(api: object, dictionaryId: int, element: "DictionaryElement", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, dictionaryId=dictionaryId, element=element)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Update(api: SyncInvokerProtocol, dictionaryId: int, element: "DictionaryElement", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, dictionaryId: int, element: "DictionaryElement", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, dictionaryId: int, element: "DictionaryElement", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Update(validate=validate, dictionaryId=dictionaryId, element=element)
    return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)

@overload
def SetElementPosition(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def SetElementPosition(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def SetElementPosition(api: SyncInvokerProtocol, id: int, position: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def SetElementPosition(api: SyncRequestProtocol, id: int, position: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def SetElementPosition(api: object, id: object = _UNSET, position: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'position' if position is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("SetElementPosition(): ambiguous overload for provided arguments")
        exact_match = 'SetElementPosition'
        exact_match_name = 'SetElementPosition'
    if provided_names == {'position', 'id'}:
        if exact_match_name is not None:
            raise TypeError("SetElementPosition(): ambiguous overload for provided arguments")
        exact_match = 'SetElementPositionByIdPosition'
        exact_match_name = 'SetElementPositionByIdPosition'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'SetElementPosition'))
        if {'position', 'id'}.issubset(provided_names) and provided_names.issubset({'position', 'id'}):
            candidates.append((2, -2, 'SetElementPositionByIdPosition'))
        if not candidates:
            raise TypeError("SetElementPosition(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("SetElementPosition(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'SetElementPosition':
        params, data = _prepare_SetElementPosition(id=id)
        return invoke_operation(api, OP_SetElementPosition if validate else OP_SetElementPosition_RAW, params=params, data=data)
    if selected == 'SetElementPositionByIdPosition':
        params, data = _prepare_SetElementPositionByIdPosition(id=id, position=position)
        return invoke_operation(api, OP_SetElementPositionByIdPosition if validate else OP_SetElementPositionByIdPosition_RAW, params=params, data=data)
    raise TypeError("SetElementPosition(): internal overload dispatch failure")

@overload
def SetContractorPosition(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[ContractorPosition]: ...
@overload
def SetContractorPosition(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[ContractorPosition]: ...
@overload
def SetContractorPosition(api: SyncInvokerProtocol, id: int, position: int, *, validate: bool = True) -> ResponseEnvelope[ContractorPosition]: ...
@overload
def SetContractorPosition(api: SyncRequestProtocol, id: int, position: int, *, validate: bool = True) -> ResponseEnvelope[ContractorPosition]: ...
def SetContractorPosition(api: object, id: object = _UNSET, position: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'position' if position is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("SetContractorPosition(): ambiguous overload for provided arguments")
        exact_match = 'SetContractorPosition'
        exact_match_name = 'SetContractorPosition'
    if provided_names == {'position', 'id'}:
        if exact_match_name is not None:
            raise TypeError("SetContractorPosition(): ambiguous overload for provided arguments")
        exact_match = 'SetContractorPositionByIdPosition'
        exact_match_name = 'SetContractorPositionByIdPosition'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'SetContractorPosition'))
        if {'position', 'id'}.issubset(provided_names) and provided_names.issubset({'position', 'id'}):
            candidates.append((2, -2, 'SetContractorPositionByIdPosition'))
        if not candidates:
            raise TypeError("SetContractorPosition(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("SetContractorPosition(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'SetContractorPosition':
        params, data = _prepare_SetContractorPosition(id=id)
        return invoke_operation(api, OP_SetContractorPosition if validate else OP_SetContractorPosition_RAW, params=params, data=data)
    if selected == 'SetContractorPositionByIdPosition':
        params, data = _prepare_SetContractorPositionByIdPosition(id=id, position=position)
        return invoke_operation(api, OP_SetContractorPositionByIdPosition if validate else OP_SetContractorPositionByIdPosition_RAW, params=params, data=data)
    raise TypeError("SetContractorPosition(): internal overload dispatch failure")

@overload
def GetBusiness(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[BusinessDictionary]: ...
@overload
def GetBusiness(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[BusinessDictionary]: ...
def GetBusiness(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetBusiness(id=id)
    return invoke_operation(api, OP_GetBusiness if validate else OP_GetBusiness_RAW, params=params, data=data)

@overload
def AddNewBusiness(api: SyncInvokerProtocol, dictionaryId: int, element: "BusinessDictionaryElement", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def AddNewBusiness(api: SyncRequestProtocol, dictionaryId: int, element: "BusinessDictionaryElement", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def AddNewBusiness(api: object, dictionaryId: int, element: "BusinessDictionaryElement", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNewBusiness(validate=validate, dictionaryId=dictionaryId, element=element)
    return invoke_operation(api, OP_AddNewBusiness if validate else OP_AddNewBusiness_RAW, params=params, data=data)

@overload
def UpdateBusiness(api: SyncInvokerProtocol, dictionaryId: int, element: "BusinessDictionaryElement", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateBusiness(api: SyncRequestProtocol, dictionaryId: int, element: "BusinessDictionaryElement", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def UpdateBusiness(api: object, dictionaryId: int, element: "BusinessDictionaryElement", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_UpdateBusiness(validate=validate, dictionaryId=dictionaryId, element=element)
    return invoke_operation(api, OP_UpdateBusiness if validate else OP_UpdateBusiness_RAW, params=params, data=data)

__all__ = ["Get", "AddNew", "Update", "SetElementPosition", "SetContractorPosition", "GetBusiness", "AddNewBusiness", "UpdateBusiness"]
