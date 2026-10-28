from __future__ import annotations

from typing import Any, List, Literal, overload
from SymfWebAPI.client import SyncAPI
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentSeries
from .json_types import DocumentSeriesJSON

@overload
def Get(api: SyncAPI, documentTypeId: int, *, validate: Literal[True] = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
@overload
def Get(api: SyncAPI, documentTypeId: int, *, validate: Literal[False]) -> ResponseEnvelope[list[DocumentSeriesJSON]]: ...
@overload
def Get(api: SyncInvokerProtocol, documentTypeId: int, *, validate: Literal[True] = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
@overload
def Get(api: SyncInvokerProtocol, documentTypeId: int, *, validate: Literal[False]) -> ResponseEnvelope[list[DocumentSeriesJSON]]: ...
@overload
def Get(api: SyncRequestProtocol, documentTypeId: int, *, validate: Literal[True] = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
@overload
def Get(api: SyncRequestProtocol, documentTypeId: int, *, validate: Literal[False]) -> ResponseEnvelope[list[DocumentSeriesJSON]]: ...
