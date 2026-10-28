"""Synchronous HTTP transport oparty o httpx.Client."""

from __future__ import annotations

from typing import Any, Dict, Optional

import httpx

from ..config import ClientConfig
from ..errors import TransportError
from ..session import SessionBackend


class SyncHttpxTransport(SessionBackend):
    """Backend dla SyncAPI bazujący na httpx.Client."""

    def __init__(self, config: ClientConfig, *, client: httpx.Client | None = None) -> None:
        self._config = config
        self._client = client or httpx.Client(
            base_url=config.base_url,
            timeout=config.request_timeout,
        )

    def open_sync(self, device_name: str) -> str:
        path = "/api/Sessions/OpenNewSession"
        try:
            response = self._client.get(
                path,
                params={"deviceName": device_name},
                headers={"Authorization": f"Application {self._config.application_key}"},
            )
            response.raise_for_status()
            return response.text.strip('"')
        except httpx.HTTPError as exc:
            raise TransportError(f"open session failed: {exc}", endpoint=path) from exc

    def close_sync(self, token: str) -> None:
        path = "/api/Sessions/CloseSession"
        try:
            response = self._client.get(
                path,
                headers={"Authorization": f"Session {token}"},
            )
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise TransportError(f"close session failed: {exc}", endpoint=path) from exc

    def request(
        self,
        method: str,
        path: str,
        *,
        token: str,
        params: Optional[Dict[str, Any]] = None,
        data: Any = None,
    ) -> httpx.Response:
        headers = {"Authorization": f"Session {token}"}
        request_kwargs: Dict[str, Any] = {"params": params, "headers": headers}
        if data is not None:
            if isinstance(data, (str, bytes, bytearray, memoryview)):
                request_kwargs["content"] = data
                if isinstance(data, str):
                    headers["Content-Type"] = "application/json"
            else:
                request_kwargs["json"] = data
        try:
            return self._client.request(method, path, **request_kwargs)
        except httpx.HTTPError as exc:
            raise TransportError(f"request failed: {exc}", endpoint=path) from exc

    def close(self) -> None:
        self._client.close()
