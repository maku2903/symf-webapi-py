from __future__ import annotations

import pytest
from pydantic import TypeAdapter

from SymfWebAPI import WebAPI
from SymfWebAPI.WebAPI.Interface.Enums import enumDocumentCharacter


@pytest.mark.parametrize("model_name", [
    "ProductListElement", "ProductListElementWithDimensions", "ProductListElementWithSalePrices",
])
@pytest.mark.parametrize("field_name", ["Unit", "DefaultUnit"])
def test_product_list_units_accept_none(model_name, field_name):
    model = getattr(WebAPI.Interface.Products.ViewModels, model_name)
    assert TypeAdapter(model.model_fields[field_name].annotation).validate_python(None) is None


@pytest.mark.parametrize("model_name", ["ContractorListElement", "ContractorListElementWithDimensions"])
@pytest.mark.parametrize("field_name", ["Pesel", "Place"])
def test_contractor_list_fields_accept_none(model_name, field_name):
    model = getattr(WebAPI.Interface.Contractors.ViewModels, model_name)
    assert TypeAdapter(model.model_fields[field_name].annotation).validate_python(None) is None


@pytest.mark.parametrize("field_name", ["Reservations", "Deliveries"])
def test_warehouse_position_collections_accept_none_and_empty_list(field_name):
    model = WebAPI.Interface.Warehouse.ViewModels.WarehouseDocumentPosition
    model.model_rebuild()
    adapter = TypeAdapter(model.model_fields[field_name].annotation)
    assert adapter.validate_python(None) is None
    assert adapter.validate_python([]) == []


def test_product_vat_rate_accepts_none() -> None:
    product_model = WebAPI.Interface.Products.ViewModels.Product
    field = product_model.model_fields["VatRate"]

    assert TypeAdapter(field.annotation).validate_python(None) is None


def test_product_rtf_note_accepts_none() -> None:
    product_model = WebAPI.Interface.Products.ViewModels.Product
    field = product_model.model_fields["RtfNote"]

    assert TypeAdapter(field.annotation).validate_python(None) is None


def test_contractor_rtf_note_accepts_none() -> None:
    contractor_model = WebAPI.Interface.Contractors.ViewModels.Contractor
    field = contractor_model.model_fields["RtfNote"]

    assert TypeAdapter(field.annotation).validate_python(None) is None


def test_page_previous_page_accepts_none() -> None:
    page_model = WebAPI.Interface.ViewModels.Page
    field = page_model.model_fields["PreviousPage"]

    assert TypeAdapter(field.annotation).validate_python(None) is None


def test_page_next_page_accepts_none() -> None:
    page_model = WebAPI.Interface.ViewModels.Page
    field = page_model.model_fields["NextPage"]

    assert TypeAdapter(field.annotation).validate_python(None) is None


def test_dimension_value_accepts_none() -> None:
    dimension_model = WebAPI.Interface.FKF.Common.ViewModels.Dimension
    field = dimension_model.model_fields["Value"]

    assert TypeAdapter(field.annotation).validate_python(None) is None


def test_common_dimension_fields_accept_none() -> None:
    dimension_model = WebAPI.Interface.Common.ViewModels.Dimension

    assert TypeAdapter(dimension_model.model_fields["Value"].annotation).validate_python(None) is None
    assert TypeAdapter(dimension_model.model_fields["DictionaryValue"].annotation).validate_python(None) is None


def test_payment_registry_base_account_number_accepts_none() -> None:
    registry_model = WebAPI.Interface.Common.ViewModels.PaymentRegistryBase
    field = registry_model.model_fields["AccountNumber"]

    assert TypeAdapter(field.annotation).validate_python(None) is None


def test_payment_registry_fields_accept_none() -> None:
    registry_model = WebAPI.Interface.Common.ViewModels.PaymentRegistry

    assert TypeAdapter(registry_model.model_fields["BankName"].annotation).validate_python(None) is None
    assert TypeAdapter(registry_model.model_fields["AccountNumber"].annotation).validate_python(None) is None


def test_document_address_fields_accept_none() -> None:
    address_model = WebAPI.Interface.Common.ViewModels.DocumentAddress

    for field_name in ("Name", "NIP", "City", "PostCode", "Street", "HouseNo", "ApartmentNo"):
        assert TypeAdapter(address_model.model_fields[field_name].annotation).validate_python(None) is None


def test_character_relation_hash_sets_are_rendered_as_lists() -> None:
    relation_model = WebAPI.Interface.Common.ViewModels.CharacterRelation
    characters = list(enumDocumentCharacter)
    assert len(characters) >= 2

    corrections = TypeAdapter(relation_model.model_fields["Corrections"].annotation).validate_python(
        [characters[0]]
    )
    related = TypeAdapter(relation_model.model_fields["Related"].annotation).validate_python(
        [characters[1]]
    )

    assert corrections == [characters[0]]
    assert related == [characters[1]]


def test_sale_document_fields_accept_none() -> None:
    sale_document_model = WebAPI.Interface.Sales.ViewModels.SaleDocument

    assert TypeAdapter(sale_document_model.model_fields["Note"].annotation).validate_python(None) is None
    assert TypeAdapter(sale_document_model.model_fields["NumberKSeF"].annotation).validate_python(None) is None
    assert TypeAdapter(sale_document_model.model_fields["Id2External"].annotation).validate_python(None) is None


def test_sale_document_list_element_id2external_accepts_none() -> None:
    sale_document_list_model = WebAPI.Interface.Sales.ViewModels.SaleDocumentListElement

    assert TypeAdapter(sale_document_list_model.model_fields["Id2External"].annotation).validate_python(None) is None
