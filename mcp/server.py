"""Fixture-backed MyMCP foundation.

The future MCP server wrapper should call these two functions directly and keep
transport concerns outside this module.
"""

from __future__ import annotations

from pathlib import Path

from scripts.source_manifest import Source, summarize_source

REPO_ROOT = Path(__file__).resolve().parents[1]
GOLDEN_BRIEFS_DIR = REPO_ROOT / "evals" / "golden_briefs"


def get_project_context(project: str) -> dict[str, object]:
    """Return a project context envelope backed by a golden brief fixture."""
    fixture_path = GOLDEN_BRIEFS_DIR / f"get_project_context_{_slug(project)}.md"
    return _context_envelope(
        tool_name="get_project_context",
        selector_key="project",
        selector_value=project,
        fixture_path=fixture_path,
    )


def get_person_context(subject: str = "Sab") -> dict[str, object]:
    """Return a person context envelope backed by a golden brief fixture."""
    fixture_path = GOLDEN_BRIEFS_DIR / f"get_person_context_{_slug(subject)}.md"
    return _context_envelope(
        tool_name="get_person_context",
        selector_key="subject",
        selector_value=subject,
        fixture_path=fixture_path,
    )


def _context_envelope(
    *,
    tool_name: str,
    selector_key: str,
    selector_value: str,
    fixture_path: Path,
) -> dict[str, object]:
    if not fixture_path.exists():
        raise FileNotFoundError(
            f"No golden brief fixture for {tool_name}({selector_value!r}): {fixture_path}"
        )

    return {
        "tool_name": tool_name,
        selector_key: selector_value,
        "markdown": fixture_path.read_text(encoding="utf-8"),
        "evidence_paths": [str(fixture_path)],
        "source_manifest_summary": summarize_source(
            Source("golden_briefs", GOLDEN_BRIEFS_DIR, True, (".md",))
        ),
    }


def _slug(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")
