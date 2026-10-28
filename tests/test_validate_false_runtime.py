from __future__ import annotations

import json

import pytest

from SymfWebAPI import ResponseDecodingError, WebAPI
from SymfWebAPI.response import ResponseEnvelope


class _StubSyncAPI:
    def __init__(self, response_text: str) -> None:
        self.response_text = response_text
        self.calls: list[dict[str, object]] = []

    def request(self, method: str, path: str, *, params=None, data=None):
        self.calls.append({"method": method, "path": path, "params": params, "data": data})
        return ResponseEnvelope(model=None, status=200, headers={"X-Test": "1"}, raw_text=self.response_text)


class _StubSyncInvokerAPI:
    def __init__(self, response_text: str) -> None:
        self.response_text = response_text
        self.calls: list[dict[str, object]] = []

    def invoke(self, operation, *, params=None, data=None):
        self.calls.append({"method": operation.method, "path": operation.path, "params": params, "data": data})
        raw = ResponseEnvelope(model=None, status=200, headers={"X-Test": "1"}, raw_text=self.response_text)
        return operation.parser(raw)


def test_products_get_validate_false_returns_dict_for_sync_request_api() -> None:
    api = _StubSyncAPI(json.dumps({"Id": 1, "Code": "P1", "Name": "Produkt"}))

    result = WebAPI.Interface.Products.Interfaces.IProductsController.Get(api, id=1, validate=False)

    assert result.unwrap()["Code"] == "P1"
    assert result.raw_text is not None
    assert api.calls == [{"method": "GET", "path": "/api/Products", "params": {"id": 1}, "data": None}]


def test_products_get_validate_false_returns_list_for_sync_invoker_api() -> None:
    api = _StubSyncInvokerAPI(json.dumps([{"Id": 1, "Code": "P1", "Name": "Produkt", "Active": True, "Unit": "szt.", "DefaultUnit": "szt.", "VatRate": None, "Type": None, "Barcode": "", "CN": "", "PKWiU": "", "FiscalName": "Produkt"}]))

    result = WebAPI.Interface.Products.Interfaces.IProductsController.Get(api, validate=False)

    first = result.unwrap()[0]
    assert first["Code"] == "P1"
    assert first["VatRate"] is None


def test_products_getpageddocument_validate_false_returns_page_shape() -> None:
    payload = {
        "NextPage": None,
        "PreviousPage": None,
        "PageNumber": 1,
        "LimitPerPage": 20,
        "TotalItems": 1,
        "OrderBy": 0,
        "Data": [
            {
                "Id": 1,
                "Code": "P1",
                "Name": "Produkt",
                "Active": True,
                "Unit": "szt.",
                "DefaultUnit": "szt.",
                "VatRate": None,
                "Type": None,
                "Barcode": "",
                "CN": "",
                "PKWiU": "",
                "FiscalName": "Produkt",
            }
        ],
    }
    api = _StubSyncAPI(json.dumps(payload))

    result = WebAPI.Interface.Products.Interfaces.IProductsController.GetPagedDocument(
        api,
        page=1,
        size=20,
        orderBy=WebAPI.Interface.Enums.enumOrderByType.Asc,
        validate=False,
    )

    page = result.unwrap()
    assert page["PageNumber"] == 1
    assert page["Data"][0]["Code"] == "P1"


def test_products_validate_false_raises_response_decoding_error_on_invalid_json() -> None:
    api = _StubSyncAPI("{invalid")

    with pytest.raises(ResponseDecodingError) as exc_info:
        WebAPI.Interface.Products.Interfaces.IProductsController.Get(api, id=1, validate=False)

    assert exc_info.value.endpoint == "/api/Products"
    assert exc_info.value.status_code == 200
