"""Response container shared by generated sync controllers."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class ResponseEnvelope(Generic[T]):
    model: Optional[T]
    status: int
    headers: dict
    raw_text: Optional[str] = None

    def unwrap(self) -> T:
        if self.model is None:
            raise ValueError("Response has no model")
        return self.model

    def json(self) -> Any:
        if self.raw_text is None or not self.raw_text.strip():
            return None
        return json.loads(self.raw_text)
