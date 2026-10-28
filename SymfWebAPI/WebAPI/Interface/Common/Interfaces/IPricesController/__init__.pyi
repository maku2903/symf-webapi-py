from __future__ import annotations

from typing import Any, List, Literal, overload
from SymfWebAPI.client import SyncAPI
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PriceType
from .json_types import PriceTypeJSON

@overload
def GetSalePriceTypes(api: SyncAPI, *, validate: Literal[True] = True) -> ResponseEnvelope[List[PriceType]]: ...
@overload
def GetSalePriceTypes(api: SyncAPI, *, validate: Literal[False]) -> ResponseEnvelope[list[PriceTypeJSON]]: ...
@overload
def GetSalePriceTypes(api: SyncInvokerProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[List[PriceType]]: ...
@overload
def GetSalePriceTypes(api: SyncInvokerProtocol, *, validate: Literal[False]) -> ResponseEnvelope[list[PriceTypeJSON]]: ...
@overload
def GetSalePriceTypes(api: SyncRequestProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[List[PriceType]]: ...
@overload
def GetSalePriceTypes(api: SyncRequestProtocol, *, validate: Literal[False]) -> ResponseEnvelope[list[PriceTypeJSON]]: ...
