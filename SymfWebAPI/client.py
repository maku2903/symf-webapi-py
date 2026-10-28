"""High-level sync client wrapping transport + session manager."""

from __future__ import annotations

from contextlib import AbstractContextManager
from typing import Any, Callable, Optional

from .config import ClientConfig
from .executors import SyncRequestExecutor
from .operations import OperationSpec
from .response import ResponseEnvelope
from .session import SessionManager


class SyncAPI(AbstractContextManager["SyncAPI"]):
    def __init__(
        self,
        config: ClientConfig,
        session_manager: SessionManager,
        request_fn: Callable[..., Any],
        shutdown_hook: Optional[Callable[[], None]] = None,
    ):
        self._session = session_manager
        self._executor = SyncRequestExecutor(config, session_manager, request_fn)
        self._shutdown_hook = shutdown_hook

    def __enter__(self) -> "SyncAPI":
        return self.open()

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def open(self) -> "SyncAPI":
        self._session.ensure_sync()
        return self

    def close(self) -> None:
        try:
            self._session.close_sync()
        finally:
            if self._shutdown_hook:
                self._shutdown_hook()

    def ensure_session(self) -> str:
        return self._executor.ensure_session()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[dict] = None,
        data: Any = None,
    ) -> ResponseEnvelope[Any]:
        return self._executor.request(method, path, params=params, data=data)

    def request_json(
        self,
        method: str,
        path: str,
        *,
        params: Optional[dict] = None,
        data: Any = None,
    ) -> Any:
        envelope = self.request(method, path, params=params, data=data)
        return envelope.json()

    def invalidate_session(self) -> None:
        self._executor.invalidate_session()

    def invoke(
        self,
        operation: OperationSpec,
        *,
        params: Optional[dict] = None,
        data: Any = None,
    ) -> ResponseEnvelope[Any]:
        envelope = self.request(operation.method, operation.path, params=params, data=data)
        return operation.parser(envelope)
