from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

_VERSIONED_CHILDREN = ['V2026_1', 'V2026_2']

_VERSIONED_EXPORTS = {
    'SaleDocumentIssue': 'V2026_1',
    'SaleDocumentIssuePositionElementV2026_2': 'V2026_2',
    'SaleDocumentIssueRequestV2026_2': 'V2026_2',
}

def __getattr__(name: str):
    if name in _VERSIONED_CHILDREN:
        value = importlib.import_module(f".{name}", __name__)
        globals()[name] = value
        return value
    child_name = _VERSIONED_EXPORTS.get(name)
    if child_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = importlib.import_module(f".{child_name}", __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value

def __dir__():
    return sorted(set(_VERSIONED_CHILDREN) | set(_VERSIONED_EXPORTS) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import V2026_1
    from . import V2026_2
    from .V2026_1 import SaleDocumentIssue
    from .V2026_2 import SaleDocumentIssuePositionElementV2026_2, SaleDocumentIssueRequestV2026_2
