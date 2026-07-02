"""Small context packet and brief contracts.

These models keep bundle input and brief output reusable across CLI, eval, and
future MCP surfaces without importing Obsidian, ctxpack, or MCP internals.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping


class ContextPacketError(ValueError):
    """Raised when an external packet payload does not match the minimum contract."""


@dataclass(frozen=True)
class ContextPacketItem:
    path: str
    depth: int
    mtime: float | None = None
    chars: int = 0
    content: str = ""
    approx_tokens: int | None = None

    def __post_init__(self) -> None:
        if not self.path:
            raise ContextPacketError("packet item path is required")
        if self.depth < 0:
            raise ContextPacketError(f"packet item depth must be >= 0: {self.path}")
        if self.chars < 0:
            raise ContextPacketError(f"packet item chars must be >= 0: {self.path}")

        computed_chars = len(self.content)
        chars = self.chars or computed_chars
        tokens = self.approx_tokens
        if tokens is None:
            tokens = max(1, chars // 4) if chars else 0
        if tokens < 0:
            raise ContextPacketError(f"packet item approx_tokens must be >= 0: {self.path}")

        object.__setattr__(self, "chars", chars)
        object.__setattr__(self, "approx_tokens", tokens)

    @classmethod
    def from_mapping(cls, payload: Mapping[str, Any]) -> "ContextPacketItem":
        try:
            path = str(payload["path"])
            depth = int(payload.get("depth", 0))
        except (KeyError, TypeError, ValueError) as exc:
            raise ContextPacketError("ctxpack item must include path and numeric depth") from exc

        content = str(payload.get("content", ""))
        chars = _optional_int(payload.get("chars"), default=len(content))
        approx_tokens = _optional_int(payload.get("approx_tokens"), default=None)
        mtime = _optional_float(payload.get("mtime"), default=None)
        return cls(
            path=path,
            depth=depth,
            mtime=mtime,
            chars=chars,
            content=content,
            approx_tokens=approx_tokens,
        )

    def as_evidence_path(self) -> str:
        return self.path

    def as_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "depth": self.depth,
            "mtime": self.mtime,
            "chars": self.chars,
            "approx_tokens": self.approx_tokens,
            "content": self.content,
        }


@dataclass(frozen=True)
class ContextPacket:
    items: tuple[ContextPacketItem, ...]
    source: str = "ctxpack"
    summary: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.items:
            raise ContextPacketError("context packet requires at least one item")

    @property
    def total_chars(self) -> int:
        return sum(item.chars for item in self.items)

    @property
    def approx_tokens(self) -> int:
        return sum(item.approx_tokens or 0 for item in self.items)

    @property
    def evidence_paths(self) -> list[str]:
        return [item.as_evidence_path() for item in self.items]

    @classmethod
    def from_ctxpack_payload(cls, payload: Mapping[str, Any]) -> "ContextPacket":
        raw_items = payload.get("items")
        if not isinstance(raw_items, list):
            raise ContextPacketError("ctxpack payload must include an items list")

        items = tuple(ContextPacketItem.from_mapping(item) for item in raw_items)
        summary = payload.get("summary", {})
        if summary is None:
            summary = {}
        if not isinstance(summary, Mapping):
            raise ContextPacketError("ctxpack summary must be an object when present")

        return cls(items=items, summary=dict(summary))

    def as_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "summary": {
                "item_count": len(self.items),
                "chars": self.total_chars,
                "approx_tokens": self.approx_tokens,
                **self.summary,
            },
            "items": [item.as_dict() for item in self.items],
        }


@dataclass(frozen=True)
class ContextBrief:
    subject: str
    intent: str
    context_type: str
    markdown: str
    evidence_paths: tuple[str, ...] = ()
    open_risks: tuple[str, ...] = ()
    brief_id: str | None = None
    generated_at: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.subject:
            raise ContextPacketError("brief subject is required")
        if not self.intent:
            raise ContextPacketError("brief intent is required")
        if not self.context_type:
            raise ContextPacketError("brief context_type is required")
        if not self.markdown.strip():
            raise ContextPacketError("brief markdown is required")

        if self.brief_id is None:
            safe_subject = self.subject.lower().replace(" ", "-").replace("/", "-")
            object.__setattr__(self, "brief_id", f"{self.intent}:{safe_subject}")
        if self.generated_at is None:
            now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
            object.__setattr__(self, "generated_at", now)

    @classmethod
    def from_packet(
        cls,
        packet: ContextPacket,
        *,
        subject: str,
        intent: str,
        context_type: str,
        short_answer: str,
        why_this_matters: str = "",
        open_risks: tuple[str, ...] | list[str] = (),
    ) -> "ContextBrief":
        risks = tuple(open_risks)
        markdown = render_brief_markdown(
            subject=subject,
            short_answer=short_answer,
            why_this_matters=why_this_matters,
            evidence_paths=packet.evidence_paths,
            open_risks=risks,
        )
        return cls(
            subject=subject,
            intent=intent,
            context_type=context_type,
            markdown=markdown,
            evidence_paths=tuple(packet.evidence_paths),
            open_risks=risks,
            metadata={
                "packet": {
                    "source": packet.source,
                    "item_count": len(packet.items),
                    "chars": packet.total_chars,
                    "approx_tokens": packet.approx_tokens,
                }
            },
        )

    def validate_envelope(self) -> None:
        required_sections = ("## Short Answer", "## Evidence", "## Open Risks / Unknowns")
        missing = [section for section in required_sections if section not in self.markdown]
        if missing:
            raise ContextPacketError(f"brief markdown missing sections: {', '.join(missing)}")
        if not self.evidence_paths:
            raise ContextPacketError("brief requires at least one evidence path")

    def as_envelope(self) -> dict[str, Any]:
        self.validate_envelope()
        return {
            "metadata": {
                "brief_id": self.brief_id,
                "intent": self.intent,
                "context_type": self.context_type,
                "subject": self.subject,
                "generated_at": self.generated_at,
                "evidence_paths": list(self.evidence_paths),
                "open_risks": list(self.open_risks),
                **self.metadata,
            },
            "markdown": self.markdown,
        }


def packet_from_ctxpack(payload: Mapping[str, Any]) -> ContextPacket:
    return ContextPacket.from_ctxpack_payload(payload)


def render_brief_markdown(
    *,
    subject: str,
    short_answer: str,
    why_this_matters: str = "",
    evidence_paths: list[str] | tuple[str, ...] = (),
    open_risks: list[str] | tuple[str, ...] = (),
) -> str:
    evidence = "\n".join(f"- `{path}`" for path in evidence_paths) or "- No evidence paths supplied."
    risks = "\n".join(f"- {risk}" for risk in open_risks) or "- No open risks recorded."
    why = why_this_matters.strip() or "This brief preserves the bounded context a reader needs to act."

    return "\n".join(
        [
            f"# Context Brief: {subject}",
            "",
            "## Short Answer",
            short_answer.strip(),
            "",
            "## Why This Matters",
            why,
            "",
            "## Evidence",
            evidence,
            "",
            "## Open Risks / Unknowns",
            risks,
            "",
        ]
    )


def _optional_int(value: Any, *, default: int | None) -> int | None:
    if value is None:
        return default
    return int(value)


def _optional_float(value: Any, *, default: float | None) -> float | None:
    if value is None:
        return default
    return float(value)
