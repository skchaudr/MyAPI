"""Privacy-first Sentry setup for the Context Refinery API.

Sentry is enabled only when SENTRY_DSN is present. The scrubber intentionally
removes request bodies, headers, paths, query text, retrieved content, and raw
exception messages because this service can touch personal knowledge data.
"""

from __future__ import annotations

import os
from typing import Any

SENSITIVE_KEYS = {
    "authorization",
    "api_key",
    "body",
    "content",
    "contents",
    "cookie",
    "cookies",
    "data",
    "description",
    "document",
    "documents",
    "evidence",
    "file",
    "file_path",
    "headers",
    "html",
    "markdown",
    "message",
    "path",
    "paths",
    "prompt",
    "query",
    "request",
    "response",
    "result",
    "results",
    "secret",
    "source",
    "sources",
    "text",
    "token",
    "transcript",
    "url",
}

SAFE_CONTEXT_KEYS = {
    "endpoint",
    "environment",
    "model",
    "retrieval_lane",
    "route",
    "service",
    "status",
}


def _sample_rate() -> float:
    try:
        return float(os.getenv("SENTRY_TRACES_SAMPLE_RATE", "0.1"))
    except ValueError:
        return 0.1


def _scrub_value(value: Any, key: str | None = None, depth: int = 0) -> Any:
    if depth > 6:
        return "[Filtered]"

    normalized_key = key.lower() if isinstance(key, str) else ""
    if normalized_key in SENSITIVE_KEYS:
        return "[Filtered]"

    if isinstance(value, dict):
        return {
            item_key: _scrub_value(item_value, str(item_key), depth + 1)
            for item_key, item_value in value.items()
        }

    if isinstance(value, list):
        return [_scrub_value(item, key, depth + 1) for item in value[:20]]

    if isinstance(value, tuple):
        return tuple(_scrub_value(item, key, depth + 1) for item in value[:20])

    if isinstance(value, str) and len(value) > 120:
        return "[Filtered]"

    return value


def scrub_sentry_event(event: dict[str, Any], hint: dict[str, Any]) -> dict[str, Any] | None:
    event["request"] = _scrub_value(event.get("request"), "request")
    event["extra"] = _scrub_value(event.get("extra", {}), "extra")
    event["contexts"] = {
        key: _scrub_value(value, key)
        for key, value in event.get("contexts", {}).items()
        if key in SAFE_CONTEXT_KEYS
    }

    for breadcrumb in event.get("breadcrumbs", {}).get("values", []):
        breadcrumb["message"] = "[Filtered]" if breadcrumb.get("message") else breadcrumb.get("message")
        breadcrumb["data"] = _scrub_value(breadcrumb.get("data", {}), "data")

    for exception in event.get("exception", {}).get("values", []):
        if "value" in exception:
            exception["value"] = "[Filtered]"

    event.setdefault("tags", {})["service"] = "myapi-context-refinery"
    return event


def init_sentry() -> None:
    dsn = os.getenv("SENTRY_DSN")
    if not dsn:
        return

    try:
        import sentry_sdk
        from sentry_sdk.integrations.fastapi import FastApiIntegration
    except Exception:
        return

    sentry_sdk.init(
        dsn=dsn,
        integrations=[FastApiIntegration()],
        environment=os.getenv("SENTRY_ENVIRONMENT", os.getenv("ENVIRONMENT", "development")),
        release=os.getenv("SENTRY_RELEASE"),
        traces_sample_rate=_sample_rate(),
        send_default_pii=False,
        before_send=scrub_sentry_event,
    )
