from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTROLLER_STUB = (
    ROOT
    / "SymfWebAPI"
    / "WebAPI"
    / "Interface"
    / "Products"
    / "Interfaces"
    / "IProductsController"
    / "__init__.pyi"
)
JSON_TYPES_STUB = (
    ROOT
    / "SymfWebAPI"
    / "WebAPI"
    / "Interface"
    / "Products"
    / "Interfaces"
    / "IProductsController"
    / "json_types.pyi"
)


def test_products_controller_stub_exposes_validate_false_overload_for_sync_api() -> None:
    content = CONTROLLER_STUB.read_text(encoding="utf-8")

    assert "from SymfWebAPI.client import SyncAPI" in content
    assert (
        'def GetPagedDocument(api: SyncAPI, page: int, size: int, orderBy: "enumOrderByType", *, validate: Literal[False])'
        in content
    )
    assert "ResponseEnvelope[GetPagedDocumentJSON]" in content


def test_products_json_types_stub_infers_page_item_shape() -> None:
    content = JSON_TYPES_STUB.read_text(encoding="utf-8")

    assert "class GetPagedDocumentJSON(TypedDict):" in content
    assert "NextPage: str | None" in content
    assert "PreviousPage: str | None" in content
    assert "Data: list[ProductListElementJSON]" in content


def test_products_controller_stub_allows_raw_request_body_for_validate_false() -> None:
    content = CONTROLLER_STUB.read_text(encoding="utf-8")

    assert 'def AddNew(api: SyncAPI, product: Any, *, validate: Literal[False])' in content
    assert 'def Update(api: SyncAPI, product: Any, *, validate: Literal[False])' in content
