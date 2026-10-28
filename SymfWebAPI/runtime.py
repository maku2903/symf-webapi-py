"""Fabryka synchronicznego klienta opartego na domyślnym transporcie."""

from __future__ import annotations

from typing import Callable, Optional, cast

from .client import SyncAPI
from .config import ClientConfig
from .protocols import SyncTransportProtocol
from .session import SessionManager, SessionState
from .transport import SyncHttpxTransport


def build_sync_client(
    config: ClientConfig,
    *,
    transport: SyncTransportProtocol | None = None,
    manage_transport: bool | None = None,
    on_session_open: Optional[Callable[[SessionState], None]] = None,
    on_session_close: Optional[Callable[[SessionState], None]] = None,
    on_session_invalidate: Optional[Callable[[SessionState], None]] = None,
) -> SyncAPI:
    """Tworzy w pełni skonfigurowanego SyncAPI."""

    own_transport = False
    if transport is None:
        transport = SyncHttpxTransport(config)
        own_transport = True
    if manage_transport is not None:
        own_transport = manage_transport

    session_manager = SessionManager(
        config,
        backend=transport,
        on_open=on_session_open,
        on_close=on_session_close,
        on_invalidate=on_session_invalidate,
    )
    shutdown_hook: Optional[Callable[[], None]] = None
    if own_transport and hasattr(transport, "close"):
        shutdown_hook = cast(Callable[[], None], getattr(transport, "close"))

    return SyncAPI(
        config,
        session_manager=session_manager,
        request_fn=transport.request,
        shutdown_hook=shutdown_hook,
    )
