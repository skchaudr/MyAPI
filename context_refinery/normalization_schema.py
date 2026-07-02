"""Corpus v1 normalization schema.

Defines the reusable metadata vocabulary for v1-stamped corpus items and
deterministic path-based inference helpers. The shape is intentionally narrow:
stamping is path-driven where possible so common sources normalize without
content inspection or changes to adapter parser behavior.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from typing import Optional


# --- Vocabulary -------------------------------------------------------------

SOURCE_TYPES = frozenset({
    "anchor",
    "project_doc",
    "handoff",
    "daily_note",
    "conversation",
    "cli_session",
    "code",
    "test",
    "config",
    "reference",
    "note",
})

WORK_TYPES = frozenset({
    "project_work",
    "configuration",
    "experiment",
    "reflection",
    "creative",
    "research",
})

TEMPORAL_MODES = frozenset({"episodic", "meta", "hybrid"})

THREAD_TYPES = frozenset({
    "execution", "configuration", "exploration",
    "reflection", "research", "support",
})

OUTCOMES = frozenset({
    "decision", "code_change", "diagnosis",
    "plan", "insight", "no_artifact",
})

SIGNAL_STRENGTHS = frozenset({"high", "medium", "low"})
RAW_THREAD_WEIGHTS = frozenset({"normal", "downweighted", "excluded"})
REVIEW_STATUSES = frozenset({"inferred", "needs_review", "approved"})


# --- Path-based inference ---------------------------------------------------

# Path segments -> source_type. Checked in order; first match wins.
# Uses substring matches against the POSIX-style path.
_PATH_TO_SOURCE_TYPE: tuple[tuple[str, str], ...] = (
    ("source-of-truth-anchors/", "anchor"),
    (".handoffs/", "handoff"),
    ("handoffs/", "handoff"),
    ("/.codex/sessions/", "cli_session"),
    ("/.codex/command-logs/", "cli_session"),
    ("/Daily/", "daily_note"),
    ("04 Periodic/", "daily_note"),
    ("project-docs/", "project_doc"),
    ("docs/", "project_doc"),
    ("01 Projects/", "project_doc"),
    ("02 Areas/", "project_doc"),
    ("03 Resources/", "reference"),
    ("05 Archive/", "note"),
    ("00 Inbox/", "note"),
    ("Templates/", "config"),
    ("_routines/", "config"),
)

# Conversation/CLI-session sources are keyed by adapter when available.
_ADAPTER_TO_SOURCE_TYPE: dict[str, Optional[str]] = {
    "chatgpt": "conversation",
    "claude_web": "conversation",
    "claude_code": "cli_session",
    "codex": "cli_session",
    "obsidian": None,  # path-based; resolved by infer_source_type
}

# Daily-note filename pattern: e.g. "4.18.26.daily.project.md" or "2026-04-18.md".
_DAILY_NOTE_RE = re.compile(
    r"^(?:\d{4}-\d{2}-\d{2}|\d{1,2}\.\d{1,2}\.\d{2,4}\.daily)",
)


def infer_source_type(path: str, adapter: Optional[str] = None) -> str:
    """Return the v1 source_type for a corpus item."""
    if adapter and adapter in _ADAPTER_TO_SOURCE_TYPE:
        mapped = _ADAPTER_TO_SOURCE_TYPE[adapter]
        if mapped is not None:
            return mapped

    posix = path.replace(os.sep, "/")

    base = posix.rsplit("/", 1)[-1]
    if _DAILY_NOTE_RE.match(base):
        return "daily_note"

    for needle, source_type in _PATH_TO_SOURCE_TYPE:
        if needle in posix:
            return source_type

    return "note"


def infer_temporal_mode(source_type: str) -> str:
    """Default temporal_mode from source_type."""
    if source_type in {"conversation", "cli_session", "daily_note"}:
        return "episodic"
    if source_type in {"anchor", "project_doc", "handoff", "reference", "config"}:
        return "meta"
    return "meta"


def infer_primary_project(path: str, title: Optional[str] = None) -> str:
    """Best-effort project label from path segments."""
    haystacks = [path.lower().replace(os.sep, "/")]
    if title:
        haystacks.append(title.lower())
    blob = " ".join(haystacks)

    rules: tuple[tuple[str, str], ...] = (
        ("myapi", "myapi"),
        ("context_refinery", "myapi"),
        ("context-refinery", "myapi"),
        ("/gdd", "gddp"),
        ("graph-driven", "gddp"),
        ("openclaw", "openclaw"),
        ("opclaw", "openclaw"),
        ("devinfra", "devinfra"),
        ("dev-infra", "devinfra"),
        ("tailscale", "devinfra"),
        ("vault", "vault"),
        ("obsidian", "vault"),
    )
    for needle, label in rules:
        if needle in blob:
            return label
    return "unknown"


# --- Frontmatter merge helper ----------------------------------------------

# Fields we own at the v1 layer. Existing values are preserved when present.
V1_FIELDS: tuple[str, ...] = (
    "source_type",
    "work_type",
    "temporal_mode",
    "primary_project",
    "review_status",
    "thread_type",
    "outcome",
    "signal_strength",
    "raw_thread_weight",
    "artifact_summary",
)


@dataclass
class V1Stamp:
    """The v1 metadata block to merge into a doc's frontmatter."""

    source_type: str
    temporal_mode: str
    primary_project: str = "unknown"
    work_type: list[str] = field(default_factory=list)
    review_status: str = "inferred"

    # Conversation-only fields; left None for non-conversation items.
    thread_type: Optional[str] = None
    outcome: Optional[str] = None
    signal_strength: Optional[str] = None
    raw_thread_weight: Optional[str] = None
    artifact_summary: Optional[str] = None

    def as_dict(self) -> dict:
        out: dict = {
            "source_type": self.source_type,
            "temporal_mode": self.temporal_mode,
            "primary_project": self.primary_project,
            "review_status": self.review_status,
        }
        if self.work_type:
            out["work_type"] = list(self.work_type)
        for key in (
            "thread_type",
            "outcome",
            "signal_strength",
            "raw_thread_weight",
            "artifact_summary",
        ):
            value = getattr(self, key)
            if value is not None:
                out[key] = value
        return out


def merge_v1_into_frontmatter(existing: dict, stamp: V1Stamp) -> dict:
    """Merge v1 fields into an existing frontmatter dict.

    Existing values win over inferred ones to preserve operator-curated
    metadata. Unknown keys in existing pass through untouched.
    """
    merged = dict(existing) if existing else {}
    for key, value in stamp.as_dict().items():
        if key not in merged or merged[key] in (None, "", []):
            merged[key] = value
    return merged


def stamp_from_path(
    path: str,
    *,
    adapter: Optional[str] = None,
    title: Optional[str] = None,
) -> V1Stamp:
    """Build a V1Stamp for an item using path and adapter hints."""
    source_type = infer_source_type(path, adapter=adapter)
    return V1Stamp(
        source_type=source_type,
        temporal_mode=infer_temporal_mode(source_type),
        primary_project=infer_primary_project(path, title=title),
    )
