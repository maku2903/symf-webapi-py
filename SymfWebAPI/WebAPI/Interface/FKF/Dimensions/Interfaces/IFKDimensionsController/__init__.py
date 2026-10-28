from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import DimensionClassification
from SymfWebAPI.WebAPI.Interface.FKF.Dimensions.ViewModels import Document
from ._common import (
    _prepare_GetAccountChartByIdAndYear,
    _prepare_GetDocumentByIdAndYear,
    _prepare_GetClassification,
)
from ._ops import (
    OP_GetAccountChartByIdAndYear,
    OP_GetAccountChartByIdAndYear_RAW,
    OP_GetDocumentByIdAndYear,
    OP_GetDocumentByIdAndYear_RAW,
    OP_GetClassification,
    OP_GetClassification_RAW,
)

_UNSET = object()

@overload
def GetAccountChartByIdAndYear(api: SyncInvokerProtocol, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def GetAccountChartByIdAndYear(api: SyncRequestProtocol, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def GetAccountChartByIdAndYear(api: object, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetAccountChartByIdAndYear(id=id, yearId=yearId)
    return invoke_operation(api, OP_GetAccountChartByIdAndYear if validate else OP_GetAccountChartByIdAndYear_RAW, params=params, data=data)

@overload
def GetDocumentByIdAndYear(api: SyncInvokerProtocol, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[Document]: ...
@overload
def GetDocumentByIdAndYear(api: SyncRequestProtocol, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[Document]: ...
def GetDocumentByIdAndYear(api: object, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentByIdAndYear(id=id, yearId=yearId)
    return invoke_operation(api, OP_GetDocumentByIdAndYear if validate else OP_GetDocumentByIdAndYear_RAW, params=params, data=data)

@overload
def GetClassification(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def GetClassification(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
def GetClassification(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetClassification()
    return invoke_operation(api, OP_GetClassification if validate else OP_GetClassification_RAW, params=params, data=data)

__all__ = ["GetAccountChartByIdAndYear", "GetDocumentByIdAndYear", "GetClassification"]
