from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import pytest

from SymfWebAPI.client import SyncAPI
from SymfWebAPI.config import ClientConfig
from SymfWebAPI.errors import WebAPIHttpError
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


def _make_config() -> ClientConfig:
    return ClientConfig(
        domain="example",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-client-sync",
    )


def test_sync_api_request_ok_uses_token_and_returns_envelope():
    backend = FakeBackend()
    manager = SessionManager(_make_config(), backend)

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        assert token == "token-1"
        assert method == "GET"
        assert path == "/api/test"
        assert params == {"q": 1}
        assert data == "payload"
        return StubResponse(200, text="ok")

    api = SyncAPI(_make_config(), manager, request_fn)
    resp = api.request("GET", "/api/test", params={"q": 1}, data="payload")
    assert resp.status == 200
    assert resp.raw_text == "ok"
    assert resp.headers["X-Test"] == "1"


def test_sync_api_http_error_maps_to_webapi_http_error():
    backend = FakeBackend()
    manager = SessionManager(_make_config(), backend)

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        return StubResponse(500, text="boom")

    api = SyncAPI(_make_config(), manager, request_fn)
    with pytest.raises(WebAPIHttpError) as exc_info:
        api.request("GET", "/api/fail")
    assert exc_info.value.status_code == 500
    assert exc_info.value.endpoint == "/api/fail"
    assert exc_info.value.response_text == "boom"


def test_sync_api_open_ensure_invalidate_reopens_session():
    backend = FakeBackend()
    manager = SessionManager(_make_config(), backend)

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        return StubResponse(200, text=token)

    api = SyncAPI(_make_config(), manager, request_fn)
    api.open()
    first = api.ensure_session()
    assert first == "token-1"

    api.invalidate_session()
    second = api.ensure_session()
    assert second == "token-2"
    assert second != first


def test_sync_api_close_calls_shutdown_hook_even_when_session_close_fails():
    class FailingCloseBackend(FakeBackend):
        def close_sync(self, token: str) -> None:
            raise RuntimeError("close failed")

    backend = FailingCloseBackend()
    manager = SessionManager(_make_config(), backend)
    shutdown_calls: list[str] = []

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        return StubResponse(200, text="ok")

    def shutdown_hook() -> None:
        shutdown_calls.append("done")

    api = SyncAPI(_make_config(), manager, request_fn, shutdown_hook=shutdown_hook)
    api.open()
    with pytest.raises(RuntimeError, match="close failed"):
        api.close()
    assert shutdown_calls == ["done"]


def test_sync_api_close_is_safe_without_open():
    backend = FakeBackend()
    manager = SessionManager(_make_config(), backend)

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        return StubResponse(200, text="ok")

    api = SyncAPI(_make_config(), manager, request_fn)
    api.close()
    api.open()
    assert api.ensure_session() == "token-1"


def test_sync_api_401_retries_once_with_fresh_session():
    backend = FakeBackend()
    manager = SessionManager(_make_config(), backend)
    calls: list[tuple[str, str, str]] = []
    responses = [StubResponse(401, text="auth-error"), StubResponse(200, text="ok")]

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        calls.append((method, path, token))
        return responses.pop(0)

    api = SyncAPI(_make_config(), manager, request_fn)
    response = api.request("GET", "/api/secured")

    assert response.status == 200
    assert calls == [
        ("GET", "/api/secured", "token-1"),
        ("GET", "/api/secured", "token-2"),
    ]
    assert api.ensure_session() == "token-2"


def test_sync_api_403_does_not_retry_or_invalidate_session():
    backend = FakeBackend()
    manager = SessionManager(_make_config(), backend)
    calls: list[tuple[str, str, str]] = []

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        calls.append((method, path, token))
        return StubResponse(403, text="forbidden")

    api = SyncAPI(_make_config(), manager, request_fn)
    with pytest.raises(WebAPIHttpError) as exc_info:
        api.request("GET", "/api/secured")

    assert exc_info.value.status_code == 403
    assert calls == [("GET", "/api/secured", "token-1")]
    assert api.ensure_session() == "token-1"


def test_sync_api_request_serializes_datetime_query_params():
    backend = FakeBackend()
    manager = SessionManager(_make_config(), backend)
    dt = datetime(2026, 2, 25, 13, 14, 15, tzinfo=timezone.utc)

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        assert params == {"from": "2026-02-25T13:14:15+00:00"}
        return StubResponse(200, text="ok")

    api = SyncAPI(_make_config(), manager, request_fn)
    api.request("GET", "/api/test", params={"from": dt})


def test_sync_api_request_serializes_nested_datetime_query_params():
    backend = FakeBackend()
    manager = SessionManager(_make_config(), backend)
    dt = datetime(2026, 2, 25, 13, 14, 15, tzinfo=timezone.utc)

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        assert params == {
            "filter": {
                "from": "2026-02-25T13:14:15+00:00",
                "items": ["2026-02-25T13:14:15+00:00"],
            }
        }
        return StubResponse(200, text="ok")

    api = SyncAPI(_make_config(), manager, request_fn)
    api.request("GET", "/api/test", params={"filter": {"from": dt, "items": [dt]}})


def test_sync_api_request_binds_path_params_and_removes_them_from_query():
    backend = FakeBackend()
    manager = SessionManager(_make_config(), backend)

    def request_fn(method: str, path: str, *, token: str, params: dict | None, data: Any):
        assert path == "/api/v2026.2/Sales/Status/Refresh/123"
        assert params == {"verbose": True}
        return StubResponse(200, text="ok")

    api = SyncAPI(_make_config(), manager, request_fn)
    api.request("GET", "/api/v2026.2/Sales/Status/Refresh/{id:int}", params={"id": 123, "verbose": True})
