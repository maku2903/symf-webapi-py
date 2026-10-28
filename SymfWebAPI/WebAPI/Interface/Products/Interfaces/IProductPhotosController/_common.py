from __future__ import annotations

from typing import Any

def _prepare_Get(*, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_GetByProductCode(*, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = None
    return params or None, data

def _prepare_GetByPhotoIdQuality(*, photoId, quality) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["photoId"] = photoId
    params["quality"] = quality.value
    data = None
    return params or None, data
