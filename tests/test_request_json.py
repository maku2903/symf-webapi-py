from __future__ import annotations

import json
from typing import Any

from SymfWebAPI.client import SyncAPI
from SymfWebAPI.config import ClientConfig
from SymfWebAPI.session import SessionBackend, SessionManager


class StubResponse:
    def __init__(self, status_code: int, text: str = ""):
        self.status_code = status_code
        self.text = text
        self.headers = {"X-Test": "1"}


class FakeBackend(SessionBackend):
    def __init__(self) -> None:
        self.counter = 0

    def open_sync(self, device_name: str) -> str:
        self.counter += 1
        return f"token-{self.counter}"

    def close_sync(self, token: str) -> None:
        return None


def _config() -> ClientConfig:
    return ClientConfig(
        domain="example",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-client-sync",
    )


def test_sync_api_request_json_returns_decoded_payload() -> None:
    backend = FakeBackend()
    manager = SessionManager(_config(), backend)

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        return StubResponse(200, text=json.dumps({"items": [1, 2, 3], "ok": True}))

    api = SyncAPI(_config(), manager, request_fn)

    payload = api.request_json("GET", "/api/test")

    assert payload == {"items": [1, 2, 3], "ok": True}
