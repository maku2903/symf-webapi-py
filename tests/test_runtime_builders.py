from __future__ import annotations

from dataclasses import dataclass

from SymfWebAPI import ClientConfig
from SymfWebAPI.runtime import build_sync_client
from SymfWebAPI.session import SessionBackend


@dataclass
class _StubResponse:
    status_code: int = 200
    text: str = "ok"
    headers: dict = None

    def __post_init__(self):
        self.headers = self.headers or {}


class _StubSyncTransport(SessionBackend):
    def __init__(self) -> None:
        self.open_calls = 0
        self.close_calls = 0
        self.closed = False

    def open_sync(self, device_name: str) -> str:
        self.open_calls += 1
        return "stub-token"

    def close_sync(self, token: str) -> None:
        self.close_calls += 1

    def request(self, method: str, path: str, *, token: str, params=None, data=None):
        assert token == "stub-token"
        return _StubResponse()

    def close(self) -> None:
        self.closed = True


def test_build_sync_client_with_custom_transport():
    config = ClientConfig(
        domain="example.com",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-runtime",
    )
    transport = _StubSyncTransport()
    events: list[str] = []
    api = build_sync_client(
        config,
        transport=transport,
        manage_transport=True,
        on_session_open=lambda state: events.append("open"),
        on_session_close=lambda state: events.append("close"),
        on_session_invalidate=lambda state: events.append("invalidate"),
    )

    with api:
        resp = api.request("GET", "/api/test")
        assert resp.status == 200
        assert transport.open_calls == 1
    assert transport.close_calls == 1
    assert transport.closed


def test_sync_client_manual_open_invalidate_close():
    config = ClientConfig(
        domain="example.com",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-runtime",
    )
    transport = _StubSyncTransport()
    events: list[str] = []
    api = build_sync_client(
        config,
        transport=transport,
        manage_transport=True,
        on_session_open=lambda state: events.append("open"),
        on_session_close=lambda state: events.append("close"),
        on_session_invalidate=lambda state: events.append("invalidate"),
    )

    api.open()
    assert transport.open_calls == 1
    api.invalidate_session()
    api.open()
    assert transport.open_calls == 2
    api.close()
    assert transport.close_calls == 1
    assert events == ["open", "invalidate", "open", "close"]
