"""Error hierarchy for Symfonia WebAPI client runtime."""

from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Optional

from pydantic import ValidationError


class SymfoniaError(RuntimeError):
    """Base exception for all runtime errors."""


class ConfigurationError(SymfoniaError):
    """Raised when client configuration is invalid."""


class TransportError(SymfoniaError):
    """Wrapping lower-level HTTP/IO errors."""

    def __init__(self, message: str, *, endpoint: Optional[str] = None) -> None:
        super().__init__(message)
        self.endpoint = endpoint


class SessionError(SymfoniaError):
    """Base class for session-specific issues."""


class SessionExpiredError(SessionError):
    """Raised when session token is no longer valid."""

    def __init__(self, message: str, *, endpoint: Optional[str] = None) -> None:
        super().__init__(message)
        self.endpoint = endpoint


@dataclass(slots=True)
class WebAPIHttpError(SymfoniaError):
    """Raised for non-success HTTP responses."""

    status_code: int
    endpoint: str
    response_text: str


class SessionManagementBypassWarning(UserWarning):
    """Warning emitted when manual session endpoints are called directly."""


class ResponseParsingError(SymfoniaError):
    """Raised when response JSON cannot be parsed into the expected model."""

    def __init__(
        self,
        *,
        endpoint: str | None,
        status_code: int,
        raw_text: str | None,
        validation_error: ValidationError,
    ) -> None:
        self.endpoint = endpoint
        self.status_code = status_code
        self.raw_text = raw_text
        self.validation_error = validation_error

        details = validation_error.errors(include_url=False)
        first = details[0] if details else {}
        self.error_details = details
        self.location = tuple(first.get("loc", ()))
        self.error_type = first.get("type")
        self.input_value = first.get("input")

        message = f"Failed to parse response for endpoint {endpoint or '<unknown>'} (HTTP {status_code})"
        if self.location:
            message += f"; field={'.'.join(str(part) for part in self.location)}"
        if self.error_type:
            message += f"; error_type={self.error_type}"
        if "input" in first:
            message += f"; value={first['input']!r}"

        preview = (raw_text or "").replace("\r", "\\r").replace("\n", "\\n")
        if preview:
            if len(preview) > 240:
                preview = preview[:237] + "..."
            message += f"; payload={preview!r}"

        super().__init__(message)


class ResponseDecodingError(SymfoniaError):
    """Raised when response body is not valid JSON for raw-response mode."""

    def __init__(
        self,
        *,
        endpoint: str | None,
        status_code: int,
        raw_text: str | None,
        decode_error: json.JSONDecodeError,
    ) -> None:
        self.endpoint = endpoint
        self.status_code = status_code
        self.raw_text = raw_text
        self.decode_error = decode_error

        message = f"Failed to decode JSON response for endpoint {endpoint or '<unknown>'} (HTTP {status_code})"
        message += f"; error={decode_error.msg!r}"
        message += f"; position={decode_error.pos}"

        preview = (raw_text or "").replace("\r", "\\r").replace("\n", "\\n")
        if preview:
            if len(preview) > 240:
                preview = preview[:237] + "..."
            message += f"; payload={preview!r}"

        super().__init__(message)


class RequestEncodingError(SymfoniaError):
    """Raised when request body cannot be serialized for the selected mode."""

    def __init__(
        self,
        *,
        body_name: str | None,
        validate: bool,
        expected_model: bool,
        body_value: object,
        cause: Exception | None = None,
    ) -> None:
        self.body_name = body_name
        self.validate = validate
        self.expected_model = expected_model
        self.body_value = body_value
        self.cause = cause

        label = body_name or "<body>"
        if expected_model and validate:
            message = (
                f"Failed to encode request body {label}: validate=True expects a Pydantic model "
                "or object exposing model_dump_json(...); use validate=False for raw JSON bodies"
            )
        else:
            message = f"Failed to encode request body {label} as JSON"

        if cause is not None:
            message += f"; error={cause!r}"

        super().__init__(message)
