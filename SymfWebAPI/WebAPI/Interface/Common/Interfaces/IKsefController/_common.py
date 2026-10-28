from __future__ import annotations

from typing import Any

def _prepare_AddSendToKsefEventAsync(*, cancellationToken, docId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["cancellationToken"] = cancellationToken
    params["docId"] = docId
    data = None
    return params or None, data

def _prepare_ChangeKsefStatusAsync(*, id, ksefStatus, cancellationToken) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    params["ksefStatus"] = ksefStatus
    params["cancellationToken"] = cancellationToken
    data = None
    return params or None, data
