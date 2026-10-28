from __future__ import annotations

from typing import Any

def _prepare_CloseSession() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_OpenNewSession(*, deviceName) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["deviceName"] = deviceName
    data = None
    return params or None, data

def _prepare_SessionInformationAsync(*, cancellationToken) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["cancellationToken"] = cancellationToken
    data = None
    return params or None, data
