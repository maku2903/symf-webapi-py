"""Zarządzanie sesją WebAPI (handshake, odświeżanie, zamykanie)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import logging
import threading
from typing import Callable, Optional, Protocol

from .config import ClientConfig


class SessionBackend(Protocol):
    """Minimalny interfejs backendu wykonującego żądania sesyjne."""

    def open_sync(self, device_name: str) -> str:
        """Zwraca nowy token sesyjny."""

    def close_sync(self, token: str) -> None:
        """Zamyka wskazaną sesję."""


@dataclass(slots=True)
class SessionState:
    token: Optional[str] = None
    opened_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None

    def is_expired(self, *, max_age: Optional[timedelta], now: Optional[datetime] = None) -> bool:
        if not self.token:
            return True
        now = now or datetime.now(timezone.utc)
        if self.expires_at and now >= self.expires_at:
            return True
        if max_age and self.opened_at:
            return now - self.opened_at >= max_age
        return False


class _SharedSessionState:
    """Thread-safe shared state used by the sync session manager."""

    def __init__(self, config: ClientConfig) -> None:
        self._config = config
        self.state = SessionState()
        self.lock = threading.RLock()
        self.condition = threading.Condition(self.lock)
        self.refreshing = False

    def is_fresh(self) -> bool:
        return not self.state.is_expired(max_age=self._config.max_session_age)

    def wait_for_refresh_locked(self) -> None:
        while self.refreshing:
            self.condition.wait()

    def fail_refresh(self) -> None:
        with self.lock:
            self.refreshing = False
            self.condition.notify_all()

    def commit_refresh(self, token: str) -> SessionState:
        now = datetime.now(timezone.utc)
        expires_at = now + self._config.max_session_age if self._config.max_session_age else None
        new_state = SessionState(token=token, opened_at=now, expires_at=expires_at)
        with self.lock:
            self.state = new_state
            self.refreshing = False
            self.condition.notify_all()
            return self.state


class SyncSessionManager:
    """Synchronous session lifecycle coordinator."""

    def __init__(
        self,
        config: ClientConfig,
        backend: SessionBackend,
        shared_state: Optional[_SharedSessionState] = None,
        *,
        logger: logging.Logger,
        on_open: Optional[Callable[[SessionState], None]] = None,
        on_close: Optional[Callable[[SessionState], None]] = None,
        on_invalidate: Optional[Callable[[SessionState], None]] = None,
    ) -> None:
        self._config = config
        self._backend = backend
        self._shared = shared_state or _SharedSessionState(config)
        self._logger = logger
        self._on_open = on_open
        self._on_close = on_close
        self._on_invalidate = on_invalidate

    @property
    def state(self) -> SessionState:
        return self._shared.state

    def _close_previous_sync(self, previous_state: SessionState) -> None:
        token = previous_state.token
        if not token:
            return
        try:
            self._backend.close_sync(token)
            self._logger.info("Closed previous sync session for device=%s", self._config.device_name)
            if self._on_close:
                self._on_close(previous_state)
        except Exception:
            self._logger.warning(
                "Failed to close previous sync session for device=%s",
                self._config.device_name,
                exc_info=True,
            )

    def ensure_sync(self) -> SessionState:
        while True:
            with self._shared.lock:
                if self._shared.is_fresh():
                    return self._shared.state
                if self._shared.refreshing:
                    self._shared.wait_for_refresh_locked()
                    continue
                self._shared.refreshing = True
                previous_state = self._shared.state

            try:
                self._close_previous_sync(previous_state)
                token = self._backend.open_sync(self._config.device_name)
            except Exception:
                self._shared.fail_refresh()
                raise

            new_state = self._shared.commit_refresh(token)
            self._logger.info("Opened sync session for device=%s", self._config.device_name)
            if self._on_open:
                self._on_open(new_state)
            return new_state

    def close_sync(self) -> None:
        with self._shared.lock:
            self._shared.wait_for_refresh_locked()
            if not self._shared.state.token:
                return
            token = self._shared.state.token
            prev_state = self._shared.state
            self._shared.state = SessionState()
            self._shared.condition.notify_all()

        try:
            self._backend.close_sync(token)
            self._logger.info("Closed sync session for device=%s", self._config.device_name)
        finally:
            if self._on_close:
                self._on_close(prev_state)

    def invalidate(self) -> None:
        with self._shared.lock:
            self._shared.wait_for_refresh_locked()
            if self._shared.state.token:
                self._logger.info("Invalidated session for device=%s", self._config.device_name)
                if self._on_invalidate:
                    self._on_invalidate(self._shared.state)
            self._shared.state = SessionState()
            self._shared.condition.notify_all()


class SessionManager(SyncSessionManager):
    """Backward-compatible sync session manager facade."""

    def __init__(
        self,
        config: ClientConfig,
        backend: SessionBackend,
        *,
        on_open: Optional[Callable[[SessionState], None]] = None,
        on_close: Optional[Callable[[SessionState], None]] = None,
        on_invalidate: Optional[Callable[[SessionState], None]] = None,
    ):
        super().__init__(
            config,
            backend,
            logger=logging.getLogger(__name__),
            on_open=on_open,
            on_close=on_close,
            on_invalidate=on_invalidate,
        )
