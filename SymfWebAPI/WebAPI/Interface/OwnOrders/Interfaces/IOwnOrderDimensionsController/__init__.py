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
    _prepare_GetByBufferOrderNumber,
    _prepare_GetPositionsByOrderId,
    _prepare_GetPositionsByOrderNumber,
    _prepare_GetPosition,
    _prepare_GetClassification,
    _prepare_GetPositionClassification,
    _prepare_Update,
    _prepare_UpdateByBufferOrderDimensionOrderNumber,
    _prepare_UpdateByOrderDimensionsOrderId,
    _prepare_UpdateByBufferOrderDimensionsOrderNumber,
    _prepare_UpdatePosition,
    _prepare_UpdatePositionByPositionDimensionsPositionId,
    _prepare_UpdatePositionByPositionDimension,
    _prepare_GetAspects,
    _prepare_GetAspectsByBufferOrderNumber,
    _prepare_UpdateAspect,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByBufferOrderNumber,
    OP_GetByBufferOrderNumber_RAW,
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
    OP_UpdateByBufferOrderDimensionOrderNumber,
    OP_UpdateByBufferOrderDimensionOrderNumber_RAW,
    OP_UpdateByOrderDimensionsOrderId,
    OP_UpdateByOrderDimensionsOrderId_RAW,
    OP_UpdateByBufferOrderDimensionsOrderNumber,
    OP_UpdateByBufferOrderDimensionsOrderNumber_RAW,
    OP_UpdatePosition,
    OP_UpdatePosition_RAW,
    OP_UpdatePositionByPositionDimensionsPositionId,
    OP_UpdatePositionByPositionDimensionsPositionId_RAW,
    OP_UpdatePositionByPositionDimension,
    OP_UpdatePositionByPositionDimension_RAW,
    OP_GetAspects,
    OP_GetAspects_RAW,
    OP_GetAspectsByBufferOrderNumber,
    OP_GetAspectsByBufferOrderNumber_RAW,
    OP_UpdateAspect,
    OP_UpdateAspect_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def Get(api: object, orderId: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'buffer', 'orderNumber'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByBufferOrderNumber'
        exact_match_name = 'GetByBufferOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId'}.issubset(provided_names) and provided_names.issubset({'orderId'}):
            candidates.append((1, -1, 'Get'))
        if {'buffer', 'orderNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderNumber'}):
            candidates.append((2, -2, 'GetByBufferOrderNumber'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(orderId=orderId)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByBufferOrderNumber':
        params, data = _prepare_GetByBufferOrderNumber(orderNumber=orderNumber, buffer=buffer)
        return invoke_operation(api, OP_GetByBufferOrderNumber if validate else OP_GetByBufferOrderNumber_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetPositionsByOrderId(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
@overload
def GetPositionsByOrderId(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
def GetPositionsByOrderId(api: object, orderId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionsByOrderId(orderId=orderId)
    return invoke_operation(api, OP_GetPositionsByOrderId if validate else OP_GetPositionsByOrderId_RAW, params=params, data=data)

@overload
def GetPositionsByOrderNumber(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
@overload
def GetPositionsByOrderNumber(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PositionDimension]]: ...
def GetPositionsByOrderNumber(api: object, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionsByOrderNumber(orderNumber=orderNumber, buffer=buffer)
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
def Update(api: SyncInvokerProtocol, orderId: int, orderDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, orderId: int, orderDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, orderDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, orderNumber: str, buffer: bool, orderDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, orderId: int, orderDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, orderId: int, orderDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, orderDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, orderNumber: str, buffer: bool, orderDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, orderId: object = _UNSET, orderDimension: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, orderDimensions: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'orderDimension' if orderDimension is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
        'orderDimensions' if orderDimensions is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderDimension', 'orderId'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'Update'
        exact_match_name = 'Update'
    if provided_names == {'buffer', 'orderDimension', 'orderNumber'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByBufferOrderDimensionOrderNumber'
        exact_match_name = 'UpdateByBufferOrderDimensionOrderNumber'
    if provided_names == {'orderDimensions', 'orderId'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByOrderDimensionsOrderId'
        exact_match_name = 'UpdateByOrderDimensionsOrderId'
    if provided_names == {'buffer', 'orderDimensions', 'orderNumber'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByBufferOrderDimensionsOrderNumber'
        exact_match_name = 'UpdateByBufferOrderDimensionsOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderDimension', 'orderId'}.issubset(provided_names) and provided_names.issubset({'orderDimension', 'orderId'}):
            candidates.append((2, -2, 'Update'))
        if {'buffer', 'orderDimension', 'orderNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderDimension', 'orderNumber'}):
            candidates.append((3, -3, 'UpdateByBufferOrderDimensionOrderNumber'))
        if {'orderDimensions', 'orderId'}.issubset(provided_names) and provided_names.issubset({'orderDimensions', 'orderId'}):
            candidates.append((2, -2, 'UpdateByOrderDimensionsOrderId'))
        if {'buffer', 'orderDimensions', 'orderNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderDimensions', 'orderNumber'}):
            candidates.append((3, -3, 'UpdateByBufferOrderDimensionsOrderNumber'))
        if not candidates:
            raise TypeError("Update(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Update':
        params, data = _prepare_Update(validate=validate, orderId=orderId, orderDimension=orderDimension)
        return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)
    if selected == 'UpdateByBufferOrderDimensionOrderNumber':
        params, data = _prepare_UpdateByBufferOrderDimensionOrderNumber(validate=validate, orderNumber=orderNumber, buffer=buffer, orderDimension=orderDimension)
        return invoke_operation(api, OP_UpdateByBufferOrderDimensionOrderNumber if validate else OP_UpdateByBufferOrderDimensionOrderNumber_RAW, params=params, data=data)
    if selected == 'UpdateByOrderDimensionsOrderId':
        params, data = _prepare_UpdateByOrderDimensionsOrderId(validate=validate, orderId=orderId, orderDimensions=orderDimensions)
        return invoke_operation(api, OP_UpdateByOrderDimensionsOrderId if validate else OP_UpdateByOrderDimensionsOrderId_RAW, params=params, data=data)
    if selected == 'UpdateByBufferOrderDimensionsOrderNumber':
        params, data = _prepare_UpdateByBufferOrderDimensionsOrderNumber(validate=validate, orderNumber=orderNumber, buffer=buffer, orderDimensions=orderDimensions)
        return invoke_operation(api, OP_UpdateByBufferOrderDimensionsOrderNumber if validate else OP_UpdateByBufferOrderDimensionsOrderNumber_RAW, params=params, data=data)
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
def GetAspects(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[AspectDocument]: ...
@overload
def GetAspects(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[AspectDocument]: ...
@overload
def GetAspects(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[AspectDocument]: ...
@overload
def GetAspects(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[AspectDocument]: ...
def GetAspects(api: object, orderId: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId'}:
        if exact_match_name is not None:
            raise TypeError("GetAspects(): ambiguous overload for provided arguments")
        exact_match = 'GetAspects'
        exact_match_name = 'GetAspects'
    if provided_names == {'buffer', 'orderNumber'}:
        if exact_match_name is not None:
            raise TypeError("GetAspects(): ambiguous overload for provided arguments")
        exact_match = 'GetAspectsByBufferOrderNumber'
        exact_match_name = 'GetAspectsByBufferOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId'}.issubset(provided_names) and provided_names.issubset({'orderId'}):
            candidates.append((1, -1, 'GetAspects'))
        if {'buffer', 'orderNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderNumber'}):
            candidates.append((2, -2, 'GetAspectsByBufferOrderNumber'))
        if not candidates:
            raise TypeError("GetAspects(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetAspects(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetAspects':
        params, data = _prepare_GetAspects(orderId=orderId)
        return invoke_operation(api, OP_GetAspects if validate else OP_GetAspects_RAW, params=params, data=data)
    if selected == 'GetAspectsByBufferOrderNumber':
        params, data = _prepare_GetAspectsByBufferOrderNumber(orderNumber=orderNumber, buffer=buffer)
        return invoke_operation(api, OP_GetAspectsByBufferOrderNumber if validate else OP_GetAspectsByBufferOrderNumber_RAW, params=params, data=data)
    raise TypeError("GetAspects(): internal overload dispatch failure")

@overload
def UpdateAspect(api: SyncInvokerProtocol, aspectPosition: "AspectPositionEdit", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateAspect(api: SyncRequestProtocol, aspectPosition: "AspectPositionEdit", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def UpdateAspect(api: object, aspectPosition: "AspectPositionEdit", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_UpdateAspect(validate=validate, aspectPosition=aspectPosition)
    return invoke_operation(api, OP_UpdateAspect if validate else OP_UpdateAspect_RAW, params=params, data=data)

__all__ = ["Get", "GetPositionsByOrderId", "GetPositionsByOrderNumber", "GetPosition", "GetClassification", "GetPositionClassification", "Update", "UpdatePosition", "GetAspects", "UpdateAspect"]
