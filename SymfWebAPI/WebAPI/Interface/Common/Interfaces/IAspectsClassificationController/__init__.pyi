from __future__ import annotations

from typing import Any, List, Literal, overload
from SymfWebAPI.client import SyncAPI
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DimensionClassification
from .json_types import DimensionClassificationJSON

@overload
def Get(api: SyncAPI, *, validate: Literal[True] = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def Get(api: SyncAPI, *, validate: Literal[False]) -> ResponseEnvelope[list[DimensionClassificationJSON]]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: Literal[False]) -> ResponseEnvelope[list[DimensionClassificationJSON]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[List[DimensionClassification]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: Literal[False]) -> ResponseEnvelope[list[DimensionClassificationJSON]]: ...
