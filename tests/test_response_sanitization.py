from __future__ import annotations

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


def test_sync_api_can_strip_nul_chars_from_response_text() -> None:
    config = ClientConfig(
        domain="example",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-client-sync",
        sanitize_nul_chars_in_responses=True,
    )
    backend = FakeBackend()
    manager = SessionManager(config, backend)

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        return StubResponse(200, text='{"name":"abc\\u0000def"}')

    api = SyncAPI(config, manager, request_fn)

    payload = api.request_json("GET", "/api/test")

    assert payload == {"name": "abcdef"}
