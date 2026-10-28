from __future__ import annotations

import httpx
import pytest

from SymfWebAPI.config import ClientConfig
from SymfWebAPI.errors import TransportError
from SymfWebAPI.transport.httpx_sync import SyncHttpxTransport


def _mock_transport():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/api/Sessions/OpenNewSession":
            assert request.url.params["deviceName"] == "dev-box"
            assert request.headers["Authorization"].startswith("Application ")
            return httpx.Response(200, text='"token-xyz"')
        if request.url.path == "/api/Sessions/CloseSession":
            assert request.headers["Authorization"] == "Session token-xyz"
            return httpx.Response(200, text="")
        if request.url.path == "/api/Ping":
            assert request.headers["Authorization"] == "Session token-xyz"
            return httpx.Response(200, text="pong")
        return httpx.Response(404, text="not found")

    return httpx.Client(base_url="http://example.com", transport=httpx.MockTransport(handler))


def test_sync_httpx_transport_flow():
    config = ClientConfig(
        domain="example.com",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-box",
    )
    client = _mock_transport()
    transport = SyncHttpxTransport(config, client=client)

    token = transport.open_sync(config.device_name)
    assert token == "token-xyz"

    response = transport.request("GET", "/api/Ping", token=token)
    assert response.status_code == 200
    assert response.text == "pong"

    transport.close_sync(token)


def test_sync_httpx_transport_open_maps_http_errors_to_transport_error():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(500, text="boom")

    config = ClientConfig(
        domain="example.com",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-box",
    )
    client = httpx.Client(base_url="http://example.com", transport=httpx.MockTransport(handler))
    transport = SyncHttpxTransport(config, client=client)

    with pytest.raises(TransportError) as exc_info:
        transport.open_sync(config.device_name)

    assert exc_info.value.endpoint == "/api/Sessions/OpenNewSession"


def test_sync_httpx_transport_close_maps_http_errors_to_transport_error():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/api/Sessions/OpenNewSession":
            return httpx.Response(200, text='"token-xyz"')
        if request.url.path == "/api/Sessions/CloseSession":
            return httpx.Response(500, text="boom")
        return httpx.Response(404, text="not found")

    config = ClientConfig(
        domain="example.com",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-box",
    )
    client = httpx.Client(base_url="http://example.com", transport=httpx.MockTransport(handler))
    transport = SyncHttpxTransport(config, client=client)

    token = transport.open_sync(config.device_name)
    with pytest.raises(TransportError) as exc_info:
        transport.close_sync(token)

    assert exc_info.value.endpoint == "/api/Sessions/CloseSession"


def test_sync_httpx_transport_sets_json_content_type_when_body_present():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/api/Payload":
            assert request.headers["Authorization"] == "Session token-xyz"
            assert request.headers["Content-Type"] == "application/json"
            return httpx.Response(200, text="ok")
        return httpx.Response(404, text="not found")

    config = ClientConfig(
        domain="example.com",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-box",
    )
    client = httpx.Client(base_url="http://example.com", transport=httpx.MockTransport(handler))
    transport = SyncHttpxTransport(config, client=client)

    response = transport.request("POST", "/api/Payload", token="token-xyz", data='{"x":1}')
    assert response.status_code == 200


def test_sync_httpx_transport_serializes_dict_payload_as_json():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/api/Payload":
            assert request.headers["Authorization"] == "Session token-xyz"
            assert request.headers["Content-Type"].startswith("application/json")
            assert request.content == b'{"x":1}'
            return httpx.Response(200, text="ok")
        return httpx.Response(404, text="not found")

    config = ClientConfig(
        domain="example.com",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-box",
    )
    client = httpx.Client(base_url="http://example.com", transport=httpx.MockTransport(handler))
    transport = SyncHttpxTransport(config, client=client)

    response = transport.request("POST", "/api/Payload", token="token-xyz", data={"x": 1})
    assert response.status_code == 200
