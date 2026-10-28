from __future__ import annotations

from typing import Any

def _prepare_BalanceAndTurnoverAsync(*, options) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["options"] = options
    data = None
    return params or None, data
