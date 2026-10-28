from __future__ import annotations

from typing import Any, List, Literal, overload
from SymfWebAPI.client import SyncAPI
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Region
from .json_types import RegionJSON

@overload
def Get(api: SyncAPI, *, validate: Literal[True] = True) -> ResponseEnvelope[List[Region]]: ...
@overload
def Get(api: SyncAPI, *, validate: Literal[False]) -> ResponseEnvelope[list[RegionJSON]]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[List[Region]]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: Literal[False]) -> ResponseEnvelope[list[RegionJSON]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[List[Region]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: Literal[False]) -> ResponseEnvelope[list[RegionJSON]]: ...
