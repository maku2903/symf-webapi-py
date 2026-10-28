from __future__ import annotations

from pydantic import BaseModel

from SymfWebAPI import WebAPI


def test_known_enum_member_is_recognized():
    member = WebAPI.Interface.Enums.enumOrderByType.Asc
    assert member.value == 1
    assert member.is_unrecognized is False


def test_unknown_enum_value_creates_forward_compatible_member():
    member = WebAPI.Interface.Enums.enumOrderByType(999)
    assert member.value == 999
    assert member.is_unrecognized is True
    assert member.name.startswith("UNRECOGNIZED_")


def test_unknown_enum_value_is_cached():
    first = WebAPI.Interface.Enums.enumOrderByType(999)
    second = WebAPI.Interface.Enums.enumOrderByType(999)
    assert first is second


def test_pydantic_model_accepts_unknown_enum_and_roundtrips_value():
    class Payload(BaseModel):
        order_by: WebAPI.Interface.Enums.enumOrderByType

    payload = Payload.model_validate({"order_by": 777})
    assert payload.order_by.value == 777
    assert payload.order_by.is_unrecognized is True
    assert payload.model_dump(mode="json")["order_by"] == 777
