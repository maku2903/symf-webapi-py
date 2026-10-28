from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels.Aspects import AspectDocument
from SymfWebAPI.WebAPI.Interface.Common.ViewModels.Aspects import AspectPositionEdit
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DimensionClassification
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PositionDimension
from ._common import (
    _prepare_Get,
    _prepare_GetByBufferDocumentNumber,
    _prepare_GetPositionsByOrderId,
    _prepare_GetPositionsByOrderNumber,
    _prepare_GetPosition,
    _prepare_GetClassification,
    _prepare_GetPositionClassification,
    _prepare_Update,
    _prepare_UpdateByBufferDocumentDimensionDocumentNumber,
    _prepare_UpdateByDocumentDimensionsDocumentId,
    _prepare_UpdateByBufferDocumentDimensionsDocumentNumber,
    _prepare_UpdatePosition,
    _prepare_UpdatePositionByPositionDimensionsPositionId,
    _prepare_UpdatePositionByPositionDimension,
    _prepare_GetAspects,
    _prepare_GetAspectsByBufferDocumentNumber,
    _prepare_UpdateAspect,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByBufferDocumentNumber,
    OP_GetByBufferDocumentNumber_RAW,
    OP_GetPositionsByOrderId,
    OP_GetPositionsByOrderId_RAW,
    OP_GetPositionsByOrderNumber,
    OP_GetPositionsByOrderNumber_RAW,
    OP_GetPosition,
    OP_GetPosition_RAW,
    OP_GetClassification,
    OP_GetClassification_RAW,
    OP_GetPositionClassification,
    OP_GetPositionClassification_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_UpdateByBufferDocumentDimensionDocumentNumber,
    OP_UpdateByBufferDocumentDimensionDocumentNumber_RAW,
    OP_UpdateByDocumentDimensionsDocumentId,
    OP_UpdateByDocumentDimensionsDocumentId_RAW,
    OP_UpdateByBufferDocumentDimensionsDocumentNumber,
    OP_UpdateByBufferDocumentDimensionsDocumentNumber_RAW,
    OP_UpdatePosition,
    OP_UpdatePosition_RAW,
    OP_UpdatePositionByPositionDimensionsPositionId,
    OP_UpdatePositionByPositionDimensionsPositionId_RAW,
    OP_UpdatePositionByPositionDimension,
    OP_UpdatePositionByPositionDimension_RAW,
    OP_GetAspects,
    OP_GetAspects_RAW,
    OP_GetAspectsByBufferDocumentNumber,
    OP_GetAspectsByBufferDocumentNumber_RAW,
    OP_UpdateAspect,
    OP_UpdateAspect_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def Get(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'buffer', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByBufferDocumentNumber'
        exact_match_name = 'GetByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'Get'))
        if {'buffer', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber'}):
            candidates.append((2, -2, 'GetByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(documentId=documentId)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByBufferDocumentNumber':
        params, data = _prepare_GetByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetByBufferDocumentNumber if validate else OP_GetByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetPositionsByOrderId(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
@overload
def GetPositionsByOrderId(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
def GetPositionsByOrderId(api: object, documentId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionsByOrderId(documentId=documentId)
    return invoke_operation(api, OP_GetPositionsByOrderId if validate else OP_GetPositionsByOrderId_RAW, params=params, data=data)

@overload
def GetPositionsByOrderNumber(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
@overload
def GetPositionsByOrderNumber(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
def GetPositionsByOrderNumber(api: object, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionsByOrderNumber(documentNumber=documentNumber, buffer=buffer)
    return invoke_operation(api, OP_GetPositionsByOrderNumber if validate else OP_GetPositionsByOrderNumber_RAW, params=params, data=data)

@overload
def GetPosition(api: SyncInvokerProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def GetPosition(api: SyncRequestProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def GetPosition(api: object, positionId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPosition(positionId=positionId)
    return invoke_operation(api, OP_GetPosition if validate else OP_GetPosition_RAW, params=params, data=data)

@overload
def GetClassification(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def GetClassification(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
def GetClassification(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetClassification()
    return invoke_operation(api, OP_GetClassification if validate else OP_GetClassification_RAW, params=params, data=data)

@overload
def GetPositionClassification(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def GetPositionClassification(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
def GetPositionClassification(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionClassification()
    return invoke_operation(api, OP_GetPositionClassification if validate else OP_GetPositionClassification_RAW, params=params, data=data)

@overload
def Update(api: SyncInvokerProtocol, documentId: int, documentDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, documentId: int, documentDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, documentDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, documentNumber: str, buffer: bool, documentDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, documentId: int, documentDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, documentId: int, documentDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, documentDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, documentNumber: str, buffer: bool, documentDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, documentId: object = _UNSET, documentDimension: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, documentDimensions: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'documentDimension' if documentDimension is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
        'documentDimensions' if documentDimensions is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentDimension', 'documentId'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'Update'
        exact_match_name = 'Update'
    if provided_names == {'buffer', 'documentDimension', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByBufferDocumentDimensionDocumentNumber'
        exact_match_name = 'UpdateByBufferDocumentDimensionDocumentNumber'
    if provided_names == {'documentDimensions', 'documentId'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByDocumentDimensionsDocumentId'
        exact_match_name = 'UpdateByDocumentDimensionsDocumentId'
    if provided_names == {'buffer', 'documentDimensions', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByBufferDocumentDimensionsDocumentNumber'
        exact_match_name = 'UpdateByBufferDocumentDimensionsDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentDimension', 'documentId'}.issubset(provided_names) and provided_names.issubset({'documentDimension', 'documentId'}):
            candidates.append((2, -2, 'Update'))
        if {'buffer', 'documentDimension', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentDimension', 'documentNumber'}):
            candidates.append((3, -3, 'UpdateByBufferDocumentDimensionDocumentNumber'))
        if {'documentDimensions', 'documentId'}.issubset(provided_names) and provided_names.issubset({'documentDimensions', 'documentId'}):
            candidates.append((2, -2, 'UpdateByDocumentDimensionsDocumentId'))
        if {'buffer', 'documentDimensions', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentDimensions', 'documentNumber'}):
            candidates.append((3, -3, 'UpdateByBufferDocumentDimensionsDocumentNumber'))
        if not candidates:
            raise TypeError("Update(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Update':
        params, data = _prepare_Update(validate=validate, documentId=documentId, documentDimension=documentDimension)
        return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)
    if selected == 'UpdateByBufferDocumentDimensionDocumentNumber':
        params, data = _prepare_UpdateByBufferDocumentDimensionDocumentNumber(validate=validate, documentNumber=documentNumber, buffer=buffer, documentDimension=documentDimension)
        return invoke_operation(api, OP_UpdateByBufferDocumentDimensionDocumentNumber if validate else OP_UpdateByBufferDocumentDimensionDocumentNumber_RAW, params=params, data=data)
    if selected == 'UpdateByDocumentDimensionsDocumentId':
        params, data = _prepare_UpdateByDocumentDimensionsDocumentId(validate=validate, documentId=documentId, documentDimensions=documentDimensions)
        return invoke_operation(api, OP_UpdateByDocumentDimensionsDocumentId if validate else OP_UpdateByDocumentDimensionsDocumentId_RAW, params=params, data=data)
    if selected == 'UpdateByBufferDocumentDimensionsDocumentNumber':
        params, data = _prepare_UpdateByBufferDocumentDimensionsDocumentNumber(validate=validate, documentNumber=documentNumber, buffer=buffer, documentDimensions=documentDimensions)
        return invoke_operation(api, OP_UpdateByBufferDocumentDimensionsDocumentNumber if validate else OP_UpdateByBufferDocumentDimensionsDocumentNumber_RAW, params=params, data=data)
    raise TypeError("Update(): internal overload dispatch failure")

@overload
def UpdatePosition(api: SyncInvokerProtocol, positionId: int, positionDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdatePosition(api: SyncRequestProtocol, positionId: int, positionDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdatePosition(api: SyncInvokerProtocol, positionId: int, positionDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdatePosition(api: SyncRequestProtocol, positionId: int, positionDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdatePosition(api: SyncInvokerProtocol, positionDimension: List["PositionDimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdatePosition(api: SyncRequestProtocol, positionDimension: List["PositionDimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
def UpdatePosition(api: object, positionId: object = _UNSET, positionDimension: object = _UNSET, positionDimensions: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'positionId' if positionId is not _UNSET else None,
        'positionDimension' if positionDimension is not _UNSET else None,
        'positionDimensions' if positionDimensions is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'positionDimension', 'positionId'}:
        if exact_match_name is not None:
            raise TypeError("UpdatePosition(): ambiguous overload for provided arguments")
        exact_match = 'UpdatePosition'
        exact_match_name = 'UpdatePosition'
    if provided_names == {'positionDimensions', 'positionId'}:
        if exact_match_name is not None:
            raise TypeError("UpdatePosition(): ambiguous overload for provided arguments")
        exact_match = 'UpdatePositionByPositionDimensionsPositionId'
        exact_match_name = 'UpdatePositionByPositionDimensionsPositionId'
    if provided_names == {'positionDimension'}:
        if exact_match_name is not None:
            raise TypeError("UpdatePosition(): ambiguous overload for provided arguments")
        exact_match = 'UpdatePositionByPositionDimension'
        exact_match_name = 'UpdatePositionByPositionDimension'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'positionDimension', 'positionId'}.issubset(provided_names) and provided_names.issubset({'positionDimension', 'positionId'}):
            candidates.append((2, -2, 'UpdatePosition'))
        if {'positionDimensions', 'positionId'}.issubset(provided_names) and provided_names.issubset({'positionDimensions', 'positionId'}):
            candidates.append((2, -2, 'UpdatePositionByPositionDimensionsPositionId'))
        if {'positionDimension'}.issubset(provided_names) and provided_names.issubset({'positionDimension'}):
            candidates.append((1, -1, 'UpdatePositionByPositionDimension'))
        if not candidates:
            raise TypeError("UpdatePosition(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("UpdatePosition(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'UpdatePosition':
        params, data = _prepare_UpdatePosition(validate=validate, positionId=positionId, positionDimension=positionDimension)
        return invoke_operation(api, OP_UpdatePosition if validate else OP_UpdatePosition_RAW, params=params, data=data)
    if selected == 'UpdatePositionByPositionDimensionsPositionId':
        params, data = _prepare_UpdatePositionByPositionDimensionsPositionId(validate=validate, positionId=positionId, positionDimensions=positionDimensions)
        return invoke_operation(api, OP_UpdatePositionByPositionDimensionsPositionId if validate else OP_UpdatePositionByPositionDimensionsPositionId_RAW, params=params, data=data)
    if selected == 'UpdatePositionByPositionDimension':
        params, data = _prepare_UpdatePositionByPositionDimension(validate=validate, positionDimension=positionDimension)
        return invoke_operation(api, OP_UpdatePositionByPositionDimension if validate else OP_UpdatePositionByPositionDimension_RAW, params=params, data=data)
    raise TypeError("UpdatePosition(): internal overload dispatch failure")

@overload
def GetAspects(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[AspectDocument]: ...
@overload
def GetAspects(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[AspectDocument]: ...
@overload
def GetAspects(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[AspectDocument]: ...
@overload
def GetAspects(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[AspectDocument]: ...
def GetAspects(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId'}:
        if exact_match_name is not None:
            raise TypeError("GetAspects(): ambiguous overload for provided arguments")
        exact_match = 'GetAspects'
        exact_match_name = 'GetAspects'
    if provided_names == {'buffer', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("GetAspects(): ambiguous overload for provided arguments")
        exact_match = 'GetAspectsByBufferDocumentNumber'
        exact_match_name = 'GetAspectsByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'GetAspects'))
        if {'buffer', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber'}):
            candidates.append((2, -2, 'GetAspectsByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("GetAspects(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetAspects(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetAspects':
        params, data = _prepare_GetAspects(documentId=documentId)
        return invoke_operation(api, OP_GetAspects if validate else OP_GetAspects_RAW, params=params, data=data)
    if selected == 'GetAspectsByBufferDocumentNumber':
        params, data = _prepare_GetAspectsByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetAspectsByBufferDocumentNumber if validate else OP_GetAspectsByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("GetAspects(): internal overload dispatch failure")

@overload
def UpdateAspect(api: SyncInvokerProtocol, aspectPosition: "AspectPositionEdit", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateAspect(api: SyncRequestProtocol, aspectPosition: "AspectPositionEdit", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def UpdateAspect(api: object, aspectPosition: "AspectPositionEdit", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_UpdateAspect(validate=validate, aspectPosition=aspectPosition)
    return invoke_operation(api, OP_UpdateAspect if validate else OP_UpdateAspect_RAW, params=params, data=data)

__all__ = ["Get", "GetPositionsByOrderId", "GetPositionsByOrderNumber", "GetPosition", "GetClassification", "GetPositionClassification", "Update", "UpdatePosition", "GetAspects", "UpdateAspect"]
