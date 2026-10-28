"""Forward-compatible enum primitives used by generated models."""

from __future__ import annotations

from enum import Enum
import re
from typing import Any

_UNRECOGNIZED_NAME_SANITIZE_RE = re.compile(r"[^0-9A-Za-z_]")


class ForwardCompatibleEnum(Enum):
    """Enum that preserves unknown values returned by the server."""

    @property
    def is_unrecognized(self) -> bool:
        return bool(getattr(self, "_unrecognized_", False))

    @property
    def raw_value(self) -> Any:
        return self.value

    @classmethod
    def _missing_(cls, value: object):
        cached = cls._value2member_map_.get(value)
        if cached is not None:
            return cached

        pseudo_member = object.__new__(cls)
        value_repr = str(value)
        safe_value = _UNRECOGNIZED_NAME_SANITIZE_RE.sub("_", value_repr).strip("_") or "VALUE"
        pseudo_member._name_ = f"UNRECOGNIZED_{safe_value}"
        pseudo_member._value_ = value
        pseudo_member._unrecognized_ = True
        cls._value2member_map_[value] = pseudo_member
        return pseudo_member
