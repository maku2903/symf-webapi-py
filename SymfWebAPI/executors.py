"""Sync request executor implementing one shared request flow policy."""

from __future__ import annotations

from typing import Any, Callable, Optional

from .config import ClientConfig
from .errors import SessionExpiredError
from .request_engine import bind_path_params, normalize_query_params, should_retry_auth, to_envelope_or_raise
from .response import ResponseEnvelope
from .session import SessionManager


class SyncRequestExecutor:
    def __init__(
        self,
        config: ClientConfig,
        session_manager: SessionManager,
        request_fn: Callable[..., Any],
    ) -> None:
        self._config = config
        self._session = session_manager
        self._request = request_fn

    def ensure_session(self) -> str:
        state = self._session.ensure_sync()
        if not state.token:
            raise SessionExpiredError("Session not established")
        return state.token

    def invalidate_session(self) -> None:
        self._session.invalidate()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[dict] = None,
        data: Any = None,
    ) -> ResponseEnvelope[Any]:
        normalized_params = normalize_query_params(params)
        bound_path, normalized_params = bind_path_params(path, normalized_params)
        token = self.ensure_session()
        response = self._request(method, bound_path, token=token, params=normalized_params, data=data)
        if should_retry_auth(response.status_code):
            self.invalidate_session()
            token = self.ensure_session()
            response = self._request(method, bound_path, token=token, params=normalized_params, data=data)
        return to_envelope_or_raise(
            response,
            path=bound_path,
            strip_nul_chars=self._config.sanitize_nul_chars_in_responses,
        )
