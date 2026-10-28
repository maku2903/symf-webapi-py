from __future__ import annotations

from datetime import datetime, timedelta, timezone
import logging
import threading
import time

from SymfWebAPI.config import ClientConfig
from SymfWebAPI.session import SessionBackend, SessionManager, SyncSessionManager


class FakeBackend(SessionBackend):
    def __init__(self) -> None:
        self.tokens: list[str] = []
        self.closed_sync: list[str] = []
        self.fail_close_sync = False

    def open_sync(self, device_name: str) -> str:
        token = f"sync-{len(self.tokens)+1}"
        self.tokens.append(token)
        return token

    def close_sync(self, token: str) -> None:
        if self.fail_close_sync:
            raise RuntimeError("close sync failed")
        self.closed_sync.append(token)


class ControlledSyncBackend(SessionBackend):
    def __init__(self) -> None:
        self.open_started = threading.Event()
        self.allow_open_return = threading.Event()
        self.open_calls = 0
        self.closed_sync: list[str] = []

    def open_sync(self, device_name: str) -> str:
        self.open_calls += 1
        self.open_started.set()
        self.allow_open_return.wait(timeout=2)
        return f"sync-race-{self.open_calls}"

    def close_sync(self, token: str) -> None:
        self.closed_sync.append(token)


def _make_config() -> ClientConfig:
    return ClientConfig(
        domain="example",
        application_key="00000000-0000-0000-0000-000000000000",
        device_name="dev-sync",
        max_session_age=timedelta(minutes=1),
    )


def _expire_state(manager: SessionManager) -> None:
    manager.state.opened_at = datetime.now(timezone.utc) - timedelta(minutes=10)


def test_session_manager_sync_cache():
    config = _make_config()
    backend = FakeBackend()
    manager = SessionManager(config, backend)

    state1 = manager.ensure_sync()
    state2 = manager.ensure_sync()

    assert state1.token == state2.token
    assert backend.closed_sync == []


def test_session_manager_sync_refresh_closes_previous():
    config = _make_config()
    backend = FakeBackend()
    manager = SessionManager(config, backend)

    first = manager.ensure_sync()
    _expire_state(manager)
    second = manager.ensure_sync()

    assert first.token != second.token
    assert backend.closed_sync == [first.token]
    assert second.expires_at is not None
    assert second.opened_at is not None
    assert second.expires_at > second.opened_at


def test_sync_session_manager_can_work_standalone():
    config = _make_config()
    backend = FakeBackend()
    manager = SyncSessionManager(config, backend, logger=logging.getLogger(__name__))

    first = manager.ensure_sync()
    second = manager.ensure_sync()

    assert first.token == second.token
    assert first.token and first.token.startswith("sync-")


def test_session_manager_sync_refresh_opens_new_even_if_close_fails():
    config = _make_config()
    backend = FakeBackend()
    manager = SessionManager(config, backend)

    first = manager.ensure_sync()
    _expire_state(manager)
    backend.fail_close_sync = True
    second = manager.ensure_sync()

    assert first.token != second.token
    assert backend.closed_sync == []


def test_close_sync_waits_for_refresh_and_closes_new_token():
    config = _make_config()
    backend = ControlledSyncBackend()
    manager = SessionManager(config, backend)
    closed = threading.Event()

    def ensure_worker() -> None:
        manager.ensure_sync()

    def close_worker() -> None:
        manager.close_sync()
        closed.set()

    ensure_thread = threading.Thread(target=ensure_worker)
    ensure_thread.start()
    backend.open_started.wait(timeout=2)

    close_thread = threading.Thread(target=close_worker)
    close_thread.start()
    time.sleep(0.05)
    assert not closed.is_set()

    backend.allow_open_return.set()
    ensure_thread.join(timeout=2)
    close_thread.join(timeout=2)

    assert closed.is_set()
    assert backend.closed_sync == ["sync-race-1"]


def test_concurrent_ensure_sync_refreshes_once_for_many_waiters():
    config = _make_config()
    backend = ControlledSyncBackend()
    manager = SessionManager(config, backend)
    tokens: list[str] = []
    errors: list[BaseException] = []

    def worker() -> None:
        try:
            tokens.append(manager.ensure_sync().token or "")
        except BaseException as exc:  # pragma: no cover
            errors.append(exc)

    threads = [threading.Thread(target=worker) for _ in range(20)]
    for thread in threads:
        thread.start()
    backend.open_started.wait(timeout=2)
    backend.allow_open_return.set()
    for thread in threads:
        thread.join(timeout=2)

    assert not errors
    assert len(set(tokens)) == 1
    assert backend.open_calls == 1
