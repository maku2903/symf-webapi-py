"""Shared request policy and response mapping for sync/async clients."""

from __future__ import annotations

from datetime import date, datetime
import re
from typing import Any, Optional
from urllib.parse import quote

from .errors import WebAPIHttpError
from .response import ResponseEnvelope

_PATH_PARAM_RE = re.compile(r"\{(?P<name>[^}:]+)(?::[^}]+)?\}")


def normalize_query_value(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize_query_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalize_query_value(item) for item in value]
    return value


def normalize_query_params(params: Optional[dict]) -> Optional[dict]:
    if params is None:
        return None
    return {key: normalize_query_value(value) for key, value in params.items()}


def bind_path_params(path: str, params: Optional[dict]) -> tuple[str, Optional[dict]]:
    if params is None or "{" not in path:
        return path, params

    remaining = dict(params)

    def _replace(match: re.Match[str]) -> str:
        name = match.group("name")
        if name not in remaining:
            return match.group(0)

        value = remaining.pop(name)
        if value is None:
            return match.group(0)

        return quote(str(value), safe="")

    bound_path = _PATH_PARAM_RE.sub(_replace, path)
    return bound_path, remaining or None


def should_retry_auth(status_code: int) -> bool:
    return status_code == 401


def sanitize_response_text(text: str, *, strip_nul_chars: bool) -> str:
    if strip_nul_chars:
        return text.replace("\x00", "").replace("\\u0000", "").replace("\\U0000", "")
    return text


def to_envelope_or_raise(
    response: Any,
    *,
    path: str,
    strip_nul_chars: bool = False,
) -> ResponseEnvelope[Any]:
    if 200 <= response.status_code < 300:
        text = sanitize_response_text(response.text, strip_nul_chars=strip_nul_chars)
        return ResponseEnvelope(
            model=None,
            status=response.status_code,
            headers=dict(response.headers),
            raw_text=text,
        )
    raise WebAPIHttpError(response.status_code, endpoint=path, response_text=response.text)
