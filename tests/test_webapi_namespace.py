import pytest
import importlib

from SymfWebAPI import WebAPI
from SymfWebAPI.errors import SessionManagementBypassWarning
from SymfWebAPI.response import ResponseEnvelope


def test_session_controller_namespaces_available():
    interfaces = WebAPI.Interface.Interfaces
    assert hasattr(interfaces, "ISessionController")
    controller = interfaces.ISessionController
    assert hasattr(controller, "OpenNewSession")
    assert not hasattr(controller, "Sync")
    assert not hasattr(controller, "Async")


def test_manual_session_controller_emits_warning():
    class _StubApi:
        def request(self, method: str, path: str, *, params=None, data=None):
            return ResponseEnvelope(model=None, status=200, headers={}, raw_text=None)

    with pytest.warns(SessionManagementBypassWarning):
        WebAPI.Interface.Interfaces.ISessionController.OpenNewSession(_StubApi(), deviceName="dev")


def test_viewmodels_versioned_packages_reexport_to_parent_namespace():
    fkf_documents = WebAPI.Interface.FKF.Documents.ViewModels
    assert hasattr(fkf_documents, "Document")
    assert hasattr(fkf_documents, "V2026_1")

    sales_correction_issue = importlib.import_module(
        "SymfWebAPI.WebAPI.Interface.Sales.ViewModels.CorrectionIssue"
    )
    assert hasattr(sales_correction_issue, "SaleCorrectionIssue")
    assert hasattr(sales_correction_issue, "V2026_1")
