from __future__ import annotations

from typing import Any

def _prepare_Get(*, documentTypeId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentTypeId"] = documentTypeId
    data = None
    return params or None, data
