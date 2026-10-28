"""Konfiguracja klienta Symfonia WebAPI."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import timedelta
import re
from typing import Final

from .errors import ConfigurationError

_GUID_RE: Final[re.Pattern[str]] = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)


def _validate_guid(label: str, value: str) -> None:
    if not _GUID_RE.fullmatch(value or ""):
        raise ConfigurationError(f"{label} must be a GUID (got: {value!r})")


def _validate_non_empty(label: str, value: str) -> None:
    if not value or not value.strip():
        raise ConfigurationError(f"{label} must be a non-empty string")


def _validate_domain(domain: str) -> None:
    if "://" in domain:
        raise ConfigurationError("domain must not include URL scheme (use https flag instead)")


@dataclass(slots=True)
class ClientConfig:
    """Podstawowe parametry wymagane do połączenia z WebAPI."""

    domain: str
    application_key: str
    device_name: str
    https: bool = False
    request_timeout: float = 30.0
    sanitize_nul_chars_in_responses: bool = False
    max_session_age: timedelta | None = field(default_factory=lambda: timedelta(minutes=25))

    def __post_init__(self) -> None:
        _validate_non_empty("domain", self.domain)
        _validate_non_empty("device_name", self.device_name)
        _validate_domain(self.domain)
        _validate_guid("application_key", self.application_key)
        if self.request_timeout <= 0:
            raise ConfigurationError("request_timeout must be positive")
        if self.max_session_age is not None and self.max_session_age.total_seconds() <= 0:
            raise ConfigurationError("max_session_age must be positive when set")

    @property
    def base_url(self) -> str:
        scheme = "https" if self.https else "http"
        return f"{scheme}://{self.domain}"
