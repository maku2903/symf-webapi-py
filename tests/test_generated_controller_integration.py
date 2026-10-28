from __future__ import annotations

import json

import pytest

from SymfWebAPI import RequestEncodingError, ResponseParsingError, WebAPI
from SymfWebAPI.response import ResponseEnvelope


class _StubSyncAPI:
    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []
        self.response_model: object | None = None
        self.response_text = "[]"

    def request(self, method: str, path: str, *, params=None, data=None):
        self.calls.append(
            {
                "method": method,
                "path": path,
                "params": params,
                "data": data,
            }
        )
        return ResponseEnvelope(
            model=self.response_model,
            status=200,
            headers={"X-Test": "1"},
            raw_text=self.response_text,
        )


class _BodyStub:
    def __init__(self, payload: dict[str, object]) -> None:
        self.payload = payload
        self.dump_calls: list[bool] = []

    def model_dump_json(self, *, exclude_unset: bool) -> str:
        self.dump_calls.append(exclude_unset)
        return json.dumps(self.payload)


class _StubSyncInvokerAPI:
    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    def invoke(self, operation, *, params=None, data=None):
        self.calls.append(
            {
                "method": operation.method,
                "path": operation.path,
                "params": params,
                "data": data,
            }
        )
        raw = ResponseEnvelope(model=None, status=200, headers={"X-Test": "1"}, raw_text="[]")
        return operation.parser(raw)


def test_generated_controller_parses_response_and_uses_contract():
    api = _StubSyncAPI()
    controller = WebAPI.Interface.Products.Interfaces.IProductsController

    result = controller.Get(api, salePrices=False)

    assert isinstance(result.model, list)
    assert result.model == []
    assert result.status == 200
    assert api.calls == [
        {
            "method": "GET",
            "path": "/api/Products",
            "params": {"salePrices": False},
            "data": None,
        }
    ]


def test_generated_controller_raises_response_parsing_error_on_invalid_json():
    class _InvalidJsonAPI(_StubSyncAPI):
        def request(self, method: str, path: str, *, params=None, data=None):
            self.calls.append(
                {
                    "method": method,
                    "path": path,
                    "params": params,
                    "data": data,
                }
            )
            return ResponseEnvelope(model=None, status=200, headers={"X-Test": "1"}, raw_text="{invalid")

    api = _InvalidJsonAPI()
    controller = WebAPI.Interface.Products.Interfaces.IProductsController

    with pytest.raises(ResponseParsingError) as exc_info:
        controller.Get(api, salePrices=False)
    assert exc_info.value.endpoint == "/api/Products"
    assert exc_info.value.status_code == 200
    assert exc_info.value.__cause__ is not None


def test_generated_sync_update_serializes_body_with_model_dump_json():
    api = _StubSyncAPI()
    controller = WebAPI.Interface.Products.Interfaces.IProductsController
    body = _BodyStub({"Id": 1, "Code": "P1"})

    result = controller.Update(api, product=body)

    assert result.status == 200
    assert body.dump_calls == [True]
    assert api.calls == [
        {
            "method": "PUT",
            "path": "/api/Products/Update",
            "params": None,
            "data": '{"Id": 1, "Code": "P1"}',
        }
    ]


def test_generated_sync_addnew_validate_false_serializes_raw_dict_body_and_returns_raw_json():
    api = _StubSyncAPI()
    api.response_text = json.dumps({"Id": 1, "Code": "P1", "Name": "Produkt"})
    controller = WebAPI.Interface.Products.Interfaces.IProductsController

    result = controller.AddNew(
        api,
        product={"Id": 1, "Code": "P1", "Name": "Produkt"},
        validate=False,
    )

    assert result.unwrap()["Code"] == "P1"
    assert api.calls == [
        {
            "method": "POST",
            "path": "/api/Products/Create",
            "params": None,
            "data": '{"Id": 1, "Code": "P1", "Name": "Produkt"}',
        }
    ]


def test_generated_sync_addnew_validate_true_rejects_raw_dict_for_model_body():
    api = _StubSyncAPI()
    controller = WebAPI.Interface.Products.Interfaces.IProductsController

    with pytest.raises(RequestEncodingError) as exc_info:
        controller.AddNew(api, product={"Id": 1, "Code": "P1"})

    assert exc_info.value.body_name == "product"
    assert exc_info.value.validate is True


def test_generated_sync_get_paged_document_uses_enum_value_in_query():
    api = _StubSyncAPI()
    api.response_model = object()
    controller = WebAPI.Interface.Products.Interfaces.IProductsController
    order_by = WebAPI.Interface.Enums.enumOrderByType.Asc

    result = controller.GetPagedDocument(api, page=1, size=20, orderBy=order_by)

    assert result.model is api.response_model
    assert api.calls == [
        {
            "method": "GET",
            "path": "/api/Products/Page",
            "params": {"page": 1, "size": 20, "orderBy": order_by.value},
            "data": None,
        }
    ]


def test_generated_controller_uses_invoke_path_for_sync_invoker_api():
    api = _StubSyncInvokerAPI()
    controller = WebAPI.Interface.Products.Interfaces.IProductsController

    result = controller.Get(api, salePrices=False)

    assert result.model == []
    assert api.calls == [
        {
            "method": "GET",
            "path": "/api/Products",
            "params": {"salePrices": False},
            "data": None,
        }
    ]
