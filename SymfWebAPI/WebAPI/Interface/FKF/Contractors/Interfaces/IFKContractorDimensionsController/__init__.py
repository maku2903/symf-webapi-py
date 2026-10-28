from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import DimensionClassification
from ._common import (
    _prepare_GetById,
    _prepare_GetByPosition,
    _prepare_GetByCode,
    _prepare_UpdateById,
    _prepare_UpdateByPosition,
    _prepare_UpdateByCode,
    _prepare_UpdateByIdByContractorDimensionsContractorId,
    _prepare_UpdateByPositionByContractorDimensionsContractorPosition,
    _prepare_UpdateByCodeByContractorCodeContractorDimensions,
    _prepare_GetClassification,
)
from ._ops import (
    OP_GetById,
    OP_GetById_RAW,
    OP_GetByPosition,
    OP_GetByPosition_RAW,
    OP_GetByCode,
    OP_GetByCode_RAW,
    OP_UpdateById,
    OP_UpdateById_RAW,
    OP_UpdateByPosition,
    OP_UpdateByPosition_RAW,
    OP_UpdateByCode,
    OP_UpdateByCode_RAW,
    OP_UpdateByIdByContractorDimensionsContractorId,
    OP_UpdateByIdByContractorDimensionsContractorId_RAW,
    OP_UpdateByPositionByContractorDimensionsContractorPosition,
    OP_UpdateByPositionByContractorDimensionsContractorPosition_RAW,
    OP_UpdateByCodeByContractorCodeContractorDimensions,
    OP_UpdateByCodeByContractorCodeContractorDimensions_RAW,
    OP_GetClassification,
    OP_GetClassification_RAW,
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

@overload
def UpdateById(api: SyncInvokerProtocol, contractorId: int, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateById(api: SyncRequestProtocol, contractorId: int, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateById(api: SyncInvokerProtocol, contractorId: int, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateById(api: SyncRequestProtocol, contractorId: int, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
def UpdateById(api: object, contractorId: object = _UNSET, contractorDimension: object = _UNSET, contractorDimensions: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'contractorDimension' if contractorDimension is not _UNSET else None,
        'contractorDimensions' if contractorDimensions is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorDimension', 'contractorId'}:
        if exact_match_name is not None:
            raise TypeError("UpdateById(): ambiguous overload for provided arguments")
        exact_match = 'UpdateById'
        exact_match_name = 'UpdateById'
    if provided_names == {'contractorDimensions', 'contractorId'}:
        if exact_match_name is not None:
            raise TypeError("UpdateById(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByIdByContractorDimensionsContractorId'
        exact_match_name = 'UpdateByIdByContractorDimensionsContractorId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorDimension', 'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorDimension', 'contractorId'}):
            candidates.append((2, -2, 'UpdateById'))
        if {'contractorDimensions', 'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorDimensions', 'contractorId'}):
            candidates.append((2, -2, 'UpdateByIdByContractorDimensionsContractorId'))
        if not candidates:
            raise TypeError("UpdateById(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("UpdateById(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'UpdateById':
        params, data = _prepare_UpdateById(validate=validate, contractorId=contractorId, contractorDimension=contractorDimension)
        return invoke_operation(api, OP_UpdateById if validate else OP_UpdateById_RAW, params=params, data=data)
    if selected == 'UpdateByIdByContractorDimensionsContractorId':
        params, data = _prepare_UpdateByIdByContractorDimensionsContractorId(validate=validate, contractorId=contractorId, contractorDimensions=contractorDimensions)
        return invoke_operation(api, OP_UpdateByIdByContractorDimensionsContractorId if validate else OP_UpdateByIdByContractorDimensionsContractorId_RAW, params=params, data=data)
    raise TypeError("UpdateById(): internal overload dispatch failure")

@overload
def UpdateByPosition(api: SyncInvokerProtocol, contractorPosition: int, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateByPosition(api: SyncRequestProtocol, contractorPosition: int, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateByPosition(api: SyncInvokerProtocol, contractorPosition: int, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateByPosition(api: SyncRequestProtocol, contractorPosition: int, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
def UpdateByPosition(api: object, contractorPosition: object = _UNSET, contractorDimension: object = _UNSET, contractorDimensions: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorPosition' if contractorPosition is not _UNSET else None,
        'contractorDimension' if contractorDimension is not _UNSET else None,
        'contractorDimensions' if contractorDimensions is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorDimension', 'contractorPosition'}:
        if exact_match_name is not None:
            raise TypeError("UpdateByPosition(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByPosition'
        exact_match_name = 'UpdateByPosition'
    if provided_names == {'contractorDimensions', 'contractorPosition'}:
        if exact_match_name is not None:
            raise TypeError("UpdateByPosition(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByPositionByContractorDimensionsContractorPosition'
        exact_match_name = 'UpdateByPositionByContractorDimensionsContractorPosition'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorDimension', 'contractorPosition'}.issubset(provided_names) and provided_names.issubset({'contractorDimension', 'contractorPosition'}):
            candidates.append((2, -2, 'UpdateByPosition'))
        if {'contractorDimensions', 'contractorPosition'}.issubset(provided_names) and provided_names.issubset({'contractorDimensions', 'contractorPosition'}):
            candidates.append((2, -2, 'UpdateByPositionByContractorDimensionsContractorPosition'))
        if not candidates:
            raise TypeError("UpdateByPosition(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("UpdateByPosition(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'UpdateByPosition':
        params, data = _prepare_UpdateByPosition(validate=validate, contractorPosition=contractorPosition, contractorDimension=contractorDimension)
        return invoke_operation(api, OP_UpdateByPosition if validate else OP_UpdateByPosition_RAW, params=params, data=data)
    if selected == 'UpdateByPositionByContractorDimensionsContractorPosition':
        params, data = _prepare_UpdateByPositionByContractorDimensionsContractorPosition(validate=validate, contractorPosition=contractorPosition, contractorDimensions=contractorDimensions)
        return invoke_operation(api, OP_UpdateByPositionByContractorDimensionsContractorPosition if validate else OP_UpdateByPositionByContractorDimensionsContractorPosition_RAW, params=params, data=data)
    raise TypeError("UpdateByPosition(): internal overload dispatch failure")

@overload
def UpdateByCode(api: SyncInvokerProtocol, contractorCode: str, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateByCode(api: SyncRequestProtocol, contractorCode: str, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateByCode(api: SyncInvokerProtocol, contractorCode: str, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateByCode(api: SyncRequestProtocol, contractorCode: str, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
def UpdateByCode(api: object, contractorCode: object = _UNSET, contractorDimension: object = _UNSET, contractorDimensions: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorCode' if contractorCode is not _UNSET else None,
        'contractorDimension' if contractorDimension is not _UNSET else None,
        'contractorDimensions' if contractorDimensions is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorCode', 'contractorDimension'}:
        if exact_match_name is not None:
            raise TypeError("UpdateByCode(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByCode'
        exact_match_name = 'UpdateByCode'
    if provided_names == {'contractorCode', 'contractorDimensions'}:
        if exact_match_name is not None:
            raise TypeError("UpdateByCode(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByCodeByContractorCodeContractorDimensions'
        exact_match_name = 'UpdateByCodeByContractorCodeContractorDimensions'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorCode', 'contractorDimension'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'contractorDimension'}):
            candidates.append((2, -2, 'UpdateByCode'))
        if {'contractorCode', 'contractorDimensions'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'contractorDimensions'}):
            candidates.append((2, -2, 'UpdateByCodeByContractorCodeContractorDimensions'))
        if not candidates:
            raise TypeError("UpdateByCode(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("UpdateByCode(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'UpdateByCode':
        params, data = _prepare_UpdateByCode(validate=validate, contractorCode=contractorCode, contractorDimension=contractorDimension)
        return invoke_operation(api, OP_UpdateByCode if validate else OP_UpdateByCode_RAW, params=params, data=data)
    if selected == 'UpdateByCodeByContractorCodeContractorDimensions':
        params, data = _prepare_UpdateByCodeByContractorCodeContractorDimensions(validate=validate, contractorCode=contractorCode, contractorDimensions=contractorDimensions)
        return invoke_operation(api, OP_UpdateByCodeByContractorCodeContractorDimensions if validate else OP_UpdateByCodeByContractorCodeContractorDimensions_RAW, params=params, data=data)
    raise TypeError("UpdateByCode(): internal overload dispatch failure")

@overload
def GetClassification(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def GetClassification(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
def GetClassification(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetClassification()
    return invoke_operation(api, OP_GetClassification if validate else OP_GetClassification_RAW, params=params, data=data)

__all__ = ["GetById", "GetByPosition", "GetByCode", "UpdateById", "UpdateByPosition", "UpdateByCode", "GetClassification"]
