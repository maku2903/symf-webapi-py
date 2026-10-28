from __future__ import annotations

from typing import Any, List, Literal, overload
from SymfWebAPI.client import SyncAPI
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Country
from .json_types import CountryJSON

@overload
def Get(api: SyncAPI, *, validate: Literal[True] = True) -> ResponseEnvelope[List[Country]]: ...
@overload
def Get(api: SyncAPI, *, validate: Literal[False]) -> ResponseEnvelope[list[CountryJSON]]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[List[Country]]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: Literal[False]) -> ResponseEnvelope[list[CountryJSON]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[List[Country]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: Literal[False]) -> ResponseEnvelope[list[CountryJSON]]: ...
