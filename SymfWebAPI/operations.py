"""Operation descriptors and shared invocation helpers for controllers."""

from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Any, Callable, Optional, TypeVar, cast, overload

from pydantic import TypeAdapter, ValidationError

from .errors import RequestEncodingError, ResponseDecodingError, ResponseParsingError
from .protocols import SyncInvokerProtocol, SyncRequestProtocol
from .response import ResponseEnvelope

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class OperationSpec:
    """Descriptor of one API endpoint call with response parser."""

    method: str
    path: str
    parser: Callable[[ResponseEnvelope[Any]], ResponseEnvelope[Any]]


def build_typed_operation(method: str, path: str, adapter: TypeAdapter[T]) -> OperationSpec:
    return OperationSpec(
        method=method,
        path=path,
        parser=lambda envelope: parse_with_adapter(envelope, adapter, endpoint=path),
    )


def build_none_operation(method: str, path: str) -> OperationSpec:
    return OperationSpec(
        method=method,
        path=path,
        parser=parse_none,
    )


def build_raw_operation(method: str, path: str) -> OperationSpec:
    return OperationSpec(
        method=method,
        path=path,
        parser=lambda envelope: parse_json_payload(envelope, endpoint=path),
    )


def parse_with_adapter(
    envelope: ResponseEnvelope[Any],
    adapter: TypeAdapter[T],
    *,
    endpoint: str | None = None,
) -> ResponseEnvelope[T]:
    if envelope.model is not None:
        model = cast(T, envelope.model)
    else:
        try:
            model = adapter.validate_json(envelope.raw_text or "null")
        except ValidationError as exc:
            raise ResponseParsingError(
                endpoint=endpoint,
                status_code=envelope.status,
                raw_text=envelope.raw_text,
                validation_error=exc,
            ) from exc
    return ResponseEnvelope(
        model=model,
        status=envelope.status,
        headers=envelope.headers,
        raw_text=envelope.raw_text,
    )


def parse_none(envelope: ResponseEnvelope[Any]) -> ResponseEnvelope[None]:
    return ResponseEnvelope(
        model=None,
        status=envelope.status,
        headers=envelope.headers,
        raw_text=envelope.raw_text,
    )


def parse_json_payload(
    envelope: ResponseEnvelope[Any],
    *,
    endpoint: str | None = None,
) -> ResponseEnvelope[Any]:
    if envelope.model is not None:
        model = envelope.model
    else:
        try:
            model = envelope.json()
        except json.JSONDecodeError as exc:
            raise ResponseDecodingError(
                endpoint=endpoint,
                status_code=envelope.status,
                raw_text=envelope.raw_text,
                decode_error=exc,
            ) from exc

    return ResponseEnvelope(
        model=model,
        status=envelope.status,
        headers=envelope.headers,
        raw_text=envelope.raw_text,
    )


def serialize_request_body(
    value: Any,
    *,
    prefer_model_dump: bool,
    validate: bool,
    body_name: str | None = None,
) -> Any:
    if value is None:
        return None

    if isinstance(value, (str, bytes, bytearray)):
        return value

    dumper = getattr(value, "model_dump_json", None)
    if callable(dumper):
        return dumper(exclude_unset=True)

    if prefer_model_dump and validate:
        raise RequestEncodingError(
            body_name=body_name,
            validate=validate,
            expected_model=True,
            body_value=value,
        )

    try:
        return json.dumps(value)
    except (TypeError, ValueError) as exc:
        raise RequestEncodingError(
            body_name=body_name,
            validate=validate,
            expected_model=prefer_model_dump,
            body_value=value,
            cause=exc,
        ) from exc


@overload
def invoke_operation(
    api: SyncInvokerProtocol,
    operation: OperationSpec,
    *,
    params: Optional[dict] = None,
    data: Any = None,
) -> ResponseEnvelope[Any]: ...


@overload
def invoke_operation(
    api: SyncRequestProtocol,
    operation: OperationSpec,
    *,
    params: Optional[dict] = None,
    data: Any = None,
) -> ResponseEnvelope[Any]: ...


def invoke_operation(
    api: object,
    operation: OperationSpec,
    *,
    params: Optional[dict] = None,
    data: Any = None,
) -> ResponseEnvelope[Any]:
    invoker = getattr(api, "invoke", None)
    if callable(invoker):
        return cast(ResponseEnvelope[Any], invoker(operation, params=params, data=data))

    requester = getattr(api, "request", None)
    if not callable(requester):
        raise TypeError("api must expose either invoke(...) or request(...)")

    envelope = cast(ResponseEnvelope[Any], requester(operation.method, operation.path, params=params, data=data))
    return operation.parser(envelope)
