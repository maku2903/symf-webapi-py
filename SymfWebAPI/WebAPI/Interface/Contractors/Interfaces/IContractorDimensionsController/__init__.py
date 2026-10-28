from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DimensionClassification
from ._common import (
    _prepare_Get,
    _prepare_GetByContractorCode,
    _prepare_Update,
    _prepare_UpdateByContractorCodeContractorDimension,
    _prepare_UpdateByContractorDimensionsContractorId,
    _prepare_UpdateByContractorCodeContractorDimensions,
    _prepare_GetClassification,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByContractorCode,
    OP_GetByContractorCode_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_UpdateByContractorCodeContractorDimension,
    OP_UpdateByContractorCodeContractorDimension_RAW,
    OP_UpdateByContractorDimensionsContractorId,
    OP_UpdateByContractorDimensionsContractorId_RAW,
    OP_UpdateByContractorCodeContractorDimensions,
    OP_UpdateByContractorCodeContractorDimensions_RAW,
    OP_GetClassification,
    OP_GetClassification_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncInvokerProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def Get(api: object, contractorId: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorId'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'contractorCode'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByContractorCode'
        exact_match_name = 'GetByContractorCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorId'}):
            candidates.append((1, -1, 'Get'))
        if {'contractorCode'}.issubset(provided_names) and provided_names.issubset({'contractorCode'}):
            candidates.append((1, -1, 'GetByContractorCode'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(contractorId=contractorId)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByContractorCode':
        params, data = _prepare_GetByContractorCode(contractorCode=contractorCode)
        return invoke_operation(api, OP_GetByContractorCode if validate else OP_GetByContractorCode_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def Update(api: SyncInvokerProtocol, contractorId: int, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, contractorId: int, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, contractorCode: str, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, contractorCode: str, contractorDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, contractorId: int, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, contractorId: int, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, contractorCode: str, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, contractorCode: str, contractorDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, contractorId: object = _UNSET, contractorDimension: object = _UNSET, contractorCode: object = _UNSET, contractorDimensions: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'contractorDimension' if contractorDimension is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
        'contractorDimensions' if contractorDimensions is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorId', 'contractorDimension'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'Update'
        exact_match_name = 'Update'
    if provided_names == {'contractorCode', 'contractorDimension'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByContractorCodeContractorDimension'
        exact_match_name = 'UpdateByContractorCodeContractorDimension'
    if provided_names == {'contractorId', 'contractorDimensions'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByContractorDimensionsContractorId'
        exact_match_name = 'UpdateByContractorDimensionsContractorId'
    if provided_names == {'contractorCode', 'contractorDimensions'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByContractorCodeContractorDimensions'
        exact_match_name = 'UpdateByContractorCodeContractorDimensions'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorId', 'contractorDimension'}.issubset(provided_names) and provided_names.issubset({'contractorId', 'contractorDimension'}):
            candidates.append((2, -2, 'Update'))
        if {'contractorCode', 'contractorDimension'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'contractorDimension'}):
            candidates.append((2, -2, 'UpdateByContractorCodeContractorDimension'))
        if {'contractorId', 'contractorDimensions'}.issubset(provided_names) and provided_names.issubset({'contractorId', 'contractorDimensions'}):
            candidates.append((2, -2, 'UpdateByContractorDimensionsContractorId'))
        if {'contractorCode', 'contractorDimensions'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'contractorDimensions'}):
            candidates.append((2, -2, 'UpdateByContractorCodeContractorDimensions'))
        if not candidates:
            raise TypeError("Update(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Update':
        params, data = _prepare_Update(validate=validate, contractorId=contractorId, contractorDimension=contractorDimension)
        return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)
    if selected == 'UpdateByContractorCodeContractorDimension':
        params, data = _prepare_UpdateByContractorCodeContractorDimension(validate=validate, contractorCode=contractorCode, contractorDimension=contractorDimension)
        return invoke_operation(api, OP_UpdateByContractorCodeContractorDimension if validate else OP_UpdateByContractorCodeContractorDimension_RAW, params=params, data=data)
    if selected == 'UpdateByContractorDimensionsContractorId':
        params, data = _prepare_UpdateByContractorDimensionsContractorId(validate=validate, contractorId=contractorId, contractorDimensions=contractorDimensions)
        return invoke_operation(api, OP_UpdateByContractorDimensionsContractorId if validate else OP_UpdateByContractorDimensionsContractorId_RAW, params=params, data=data)
    if selected == 'UpdateByContractorCodeContractorDimensions':
        params, data = _prepare_UpdateByContractorCodeContractorDimensions(validate=validate, contractorCode=contractorCode, contractorDimensions=contractorDimensions)
        return invoke_operation(api, OP_UpdateByContractorCodeContractorDimensions if validate else OP_UpdateByContractorCodeContractorDimensions_RAW, params=params, data=data)
    raise TypeError("Update(): internal overload dispatch failure")

@overload
def GetClassification(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def GetClassification(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
def GetClassification(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetClassification()
    return invoke_operation(api, OP_GetClassification if validate else OP_GetClassification_RAW, params=params, data=data)

__all__ = ["Get", "Update", "GetClassification"]
