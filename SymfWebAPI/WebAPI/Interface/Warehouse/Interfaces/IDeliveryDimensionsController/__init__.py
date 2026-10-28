from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DimensionClassification
from ._common import (
    _prepare_Get,
    _prepare_GetClassification,
    _prepare_Update,
    _prepare_UpdateByDeliveryDimensionsDeliveryId,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetClassification,
    OP_GetClassification_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_UpdateByDeliveryDimensionsDeliveryId,
    OP_UpdateByDeliveryDimensionsDeliveryId_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, deliveryId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, deliveryId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def Get(api: object, deliveryId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get(deliveryId=deliveryId)
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetClassification(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def GetClassification(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
def GetClassification(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetClassification()
    return invoke_operation(api, OP_GetClassification if validate else OP_GetClassification_RAW, params=params, data=data)

@overload
def Update(api: SyncInvokerProtocol, deliveryId: int, deliveryDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, deliveryId: int, deliveryDimension: "Dimension", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, deliveryId: int, deliveryDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, deliveryId: int, deliveryDimensions: List["Dimension"], *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, deliveryId: object = _UNSET, deliveryDimension: object = _UNSET, deliveryDimensions: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'deliveryId' if deliveryId is not _UNSET else None,
        'deliveryDimension' if deliveryDimension is not _UNSET else None,
        'deliveryDimensions' if deliveryDimensions is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'deliveryDimension', 'deliveryId'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'Update'
        exact_match_name = 'Update'
    if provided_names == {'deliveryId', 'deliveryDimensions'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByDeliveryDimensionsDeliveryId'
        exact_match_name = 'UpdateByDeliveryDimensionsDeliveryId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'deliveryDimension', 'deliveryId'}.issubset(provided_names) and provided_names.issubset({'deliveryDimension', 'deliveryId'}):
            candidates.append((2, -2, 'Update'))
        if {'deliveryId', 'deliveryDimensions'}.issubset(provided_names) and provided_names.issubset({'deliveryId', 'deliveryDimensions'}):
            candidates.append((2, -2, 'UpdateByDeliveryDimensionsDeliveryId'))
        if not candidates:
            raise TypeError("Update(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Update':
        params, data = _prepare_Update(validate=validate, deliveryId=deliveryId, deliveryDimension=deliveryDimension)
        return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)
    if selected == 'UpdateByDeliveryDimensionsDeliveryId':
        params, data = _prepare_UpdateByDeliveryDimensionsDeliveryId(validate=validate, deliveryId=deliveryId, deliveryDimensions=deliveryDimensions)
        return invoke_operation(api, OP_UpdateByDeliveryDimensionsDeliveryId if validate else OP_UpdateByDeliveryDimensionsDeliveryId_RAW, params=params, data=data)
    raise TypeError("Update(): internal overload dispatch failure")

__all__ = ["Get", "GetClassification", "Update"]
