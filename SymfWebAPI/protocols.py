"""Structural protocols used by controllers and runtime builders."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Protocol, TypeVar

from .response import ResponseEnvelope
from .session import SessionBackend

if TYPE_CHECKING:
    from .operations import OperationSpec

T = TypeVar("T")


class SyncRequestProtocol(Protocol):
    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[dict] = None,
        data: Any = None,
    ) -> ResponseEnvelope[Any]:
        ...


class SyncInvokerProtocol(Protocol):
    def invoke(
        self,
        operation: "OperationSpec[T]",
        *,
        params: Optional[dict] = None,
        data: Any = None,
    ) -> ResponseEnvelope[T]:
        ...


class SyncTransportProtocol(SessionBackend, Protocol):
    def request(
        self,
        method: str,
        path: str,
        *,
        token: str,
        params: Optional[dict] = None,
        data: Any = None,
    ) -> Any:
        ...
