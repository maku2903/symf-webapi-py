from __future__ import annotations

from typing import Any, Literal, overload
from SymfWebAPI.client import SyncAPI
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.ViewModels import CompanyInfo
from .json_types import CompanyInfoJSON

@overload
def Get(api: SyncAPI, *, validate: Literal[True] = True) -> ResponseEnvelope[CompanyInfo]: ...
@overload
def Get(api: SyncAPI, *, validate: Literal[False]) -> ResponseEnvelope[CompanyInfoJSON]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[CompanyInfo]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: Literal[False]) -> ResponseEnvelope[CompanyInfoJSON]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: Literal[True] = True) -> ResponseEnvelope[CompanyInfo]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: Literal[False]) -> ResponseEnvelope[CompanyInfoJSON]: ...
