from __future__ import annotations

from datetime import timedelta

import pytest

from SymfWebAPI.config import ClientConfig
from SymfWebAPI.errors import ConfigurationError


def test_client_config_valid_builds_base_url():
    cfg = ClientConfig(
        domain="example.com",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-box",
        https=True,
    )
    assert cfg.base_url == "https://example.com"


@pytest.mark.parametrize(
    ("kwargs", "expected_fragment"),
    [
        (
            {
                "domain": "",
                "application_key": "00000000-0000-0000-0000-000000000000",
                "device_name": "dev",
            },
            "domain must be a non-empty string",
        ),
        (
            {
                "domain": "example.com",
                "application_key": "not-guid",
                "device_name": "dev",
            },
            "application_key must be a GUID",
        ),
        (
            {
                "domain": "https://example.com",
                "application_key": "00000000-0000-0000-0000-000000000000",
                "device_name": "dev",
            },
            "domain must not include URL scheme",
        ),
        (
            {
                "domain": "example.com",
                "application_key": "00000000-0000-0000-0000-000000000000",
                "device_name": "dev",
                "request_timeout": 0,
            },
            "request_timeout must be positive",
        ),
        (
            {
                "domain": "example.com",
                "application_key": "00000000-0000-0000-0000-000000000000",
                "device_name": "dev",
                "max_session_age": timedelta(seconds=0),
            },
            "max_session_age must be positive when set",
        ),
    ],
)
def test_client_config_raises_configuration_error(kwargs: dict, expected_fragment: str):
    with pytest.raises(ConfigurationError, match=expected_fragment):
        ClientConfig(**kwargs)

