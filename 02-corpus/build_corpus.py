#!/usr/bin/env python3
"""Build the deterministic Part 1 decision corpus using only the Python stdlib."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
from typing import Any, Iterable, Mapping


ROOM = Path(__file__).resolve().parent
DEFAULT_INPUT = ROOM.parent / "01-decisions" / "output" / "decisions-canonical.jsonl"
DEFAULT_OUTPUT = ROOM / "output" / "corpus"
SOURCE_LABEL = "01-decisions/output/decisions-canonical.jsonl"
REQUIRED_FIELDS = (
    "id",
    "schema_version",
    "project",
    "title",
    "summary",
    "statement",
    "status",
    "rationale",
    "decided_on",
    "sources",
)
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate one Markdown document per canonical decision plus an index."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="canonical JSONL input")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="generated corpus directory")
    return parser.parse_args()


def load_decisions(path: Path) -> tuple[list[dict[str, Any]], str]:
    raw = path.read_bytes()
    decisions: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    for line_number, raw_line in enumerate(raw.splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            decision = json.loads(raw_line)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
        if not isinstance(decision, dict):
            raise ValueError(f"{path}:{line_number}: each JSONL record must be an object")

        missing = [field for field in REQUIRED_FIELDS if field not in decision]
        if missing:
            raise ValueError(f"{path}:{line_number}: missing required fields: {', '.join(missing)}")

        decision_id = decision["id"]
        if not isinstance(decision_id, str) or not SAFE_ID.fullmatch(decision_id):
            raise ValueError(f"{path}:{line_number}: unsafe decision id {decision_id!r}")
        if decision_id.lower() == "index":
            raise ValueError(f"{path}:{line_number}: decision id conflicts with index.md")
        if decision_id in seen_ids:
            raise ValueError(f"{path}:{line_number}: duplicate decision id {decision_id!r}")

        project = decision["project"]
        if not isinstance(project, str) or not project or any(home == "" for home in project.split("/")):
            raise ValueError(f"{path}:{line_number}: project must contain non-empty slash-separated homes")
        if not isinstance(decision["sources"], list) or not decision["sources"]:
            raise ValueError(f"{path}:{line_number}: sources must be a non-empty list")

        for field in ("schema_version", "title", "summary", "statement", "status", "rationale", "decided_on"):
            if not isinstance(decision[field], str) or not decision[field]:
                raise ValueError(f"{path}:{line_number}: {field} must be a non-empty string")

        seen_ids.add(decision_id)
        decisions.append(decision)

    if not decisions:
        raise ValueError(f"{path}: canonical decision set is empty")

    decisions.sort(key=lambda item: item["id"])
    return decisions, hashlib.sha256(raw).hexdigest()


def yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    raise TypeError(f"unsupported YAML scalar type: {type(value).__name__}")


def yaml_lines(value: Any, indent: int = 0) -> list[str]:
    pad = " " * indent
    if isinstance(value, Mapping):
        if not value:
            return [pad + "{}"]
        lines: list[str] = []
        for key, child in value.items():
            if not isinstance(key, str):
                raise TypeError("YAML mapping keys must be strings")
            if isinstance(child, Mapping) or isinstance(child, list):
                if not child:
                    lines.append(f"{pad}{key}: {'{}' if isinstance(child, Mapping) else '[]'}")
                else:
                    lines.append(f"{pad}{key}:")
                    lines.extend(yaml_lines(child, indent + 2))
            else:
                lines.append(f"{pad}{key}: {yaml_scalar(child)}")
        return lines
    if isinstance(value, list):
        if not value:
            return [pad + "[]"]
        lines = []
        for child in value:
            if isinstance(child, Mapping) or isinstance(child, list):
                lines.append(pad + "-")
                lines.extend(yaml_lines(child, indent + 2))
            else:
                lines.append(f"{pad}- {yaml_scalar(child)}")
        return lines
    return [pad + yaml_scalar(value)]


def frontmatter(data: Mapping[str, Any]) -> str:
    return "---\n" + "\n".join(yaml_lines(data)) + "\n---\n"


def optional_list_section(title: str, values: Any) -> list[str]:
    if not isinstance(values, list) or not values:
        return []
    lines = [f"## {title}", ""]
    lines.extend(f"- {value}" for value in values)
    lines.append("")
    return lines


def render_decision(decision: Mapping[str, Any]) -> str:
    lines = [
        frontmatter(decision).rstrip(),
        "",
        f"# {decision['id']} — {decision['title']}",
        "",
        f"> {decision['summary']}",
        "",
        "## Decision",
        "",
        str(decision["statement"]),
        "",
        "## Rationale",
        "",
        str(decision["rationale"]),
        "",
        "## Record",
        "",
        f"- **Project:** `{decision['project']}`",
        f"- **Status:** `{decision['status']}`",
        f"- **Decided on:** `{decision['decided_on']}`",
    ]
    if decision.get("decided_by"):
        lines.append(f"- **Decided by:** {decision['decided_by']}")
    lines.append("")

    lines.extend(optional_list_section("Alternatives considered", decision.get("alternatives_considered")))
    if decision.get("consequences"):
        lines.extend(["## Consequences", "", str(decision["consequences"]), ""])

    replaces = decision.get("replaces")
    replaced_by = decision.get("replaced_by")
    relations = decision.get("related_decisions")
    if replaces or replaced_by or relations:
        lines.extend(["## Decision links", ""])
        for target in replaces or []:
            lines.append(f"- Replaces [{target}]({target}.md)")
        if replaced_by:
            lines.append(f"- Replaced by [{replaced_by}]({replaced_by}.md)")
        for relation in relations or []:
            note = f" — {relation['note']}" if relation.get("note") else ""
            lines.append(
                f"- `{relation['rel']}` [{relation['target_id']}]({relation['target_id']}.md){note}"
            )
        lines.append("")

    lines.extend(["## Sources", ""])
    for source in decision["sources"]:
        note = f" — {source['note']}" if source.get("note") else ""
        lines.append(f"- `{source['kind']}` `{source['ref']}`{note}")
    lines.append("")
    return "\n".join(lines)


def project_homes(decisions: Iterable[Mapping[str, Any]]) -> dict[str, list[Mapping[str, Any]]]:
    grouped: dict[str, list[Mapping[str, Any]]] = {}
    for decision in decisions:
        # Taxonomy rule: project is preserved verbatim; homes come only from split("/").
        for home in decision["project"].split("/"):
            grouped.setdefault(home, []).append(decision)
    return grouped


def decision_link(decision: Mapping[str, Any]) -> str:
    return f"- [{decision['id']} — {decision['title']}]({decision['id']}.md) — `{decision['project']}`"


def render_index(decisions: list[Mapping[str, Any]], source_sha256: str) -> str:
    homes = project_homes(decisions)
    metadata = {
        "type": "decision-corpus-index",
        "schema_version": "1.0",
        "source": SOURCE_LABEL,
        "source_sha256": source_sha256,
        "decision_count": len(decisions),
        "project_homes": sorted(homes),
    }
    lines = [
        frontmatter(metadata).rstrip(),
        "",
        "# Canonical decision corpus",
        "",
        f"Generated deterministically from `{SOURCE_LABEL}` ({len(decisions)} decisions).",
        "",
        "Project values remain verbatim in each decision's YAML frontmatter. Index homes are derived exclusively with `project.split(\"/\")`; a multi-home decision is listed under every resulting home.",
        "",
        "## Project homes",
        "",
    ]
    for home in sorted(homes):
        lines.extend([f"### {home}", ""])
        lines.extend(decision_link(decision) for decision in homes[home])
        lines.append("")

    lines.extend(["## All decisions", ""])
    lines.extend(decision_link(decision) for decision in decisions)
    lines.append("")
    return "\n".join(lines)


def write_utf8(path: Path, content: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


def write_snapshot(destination: Path, decisions: list[dict[str, Any]], source_sha256: str) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    write_utf8(destination / "index.md", render_index(decisions, source_sha256))
    for decision in decisions:
        write_utf8(destination / f"{decision['id']}.md", render_decision(decision))


def replace_output(output: Path, decisions: list[dict[str, Any]], source_sha256: str) -> None:
    output = output.expanduser()
    if output.is_symlink():
        raise ValueError(f"refusing to replace symlink output: {output}")
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    staging = Path(tempfile.mkdtemp(prefix=f".{output.name}.build-", dir=output.parent))
    backup: Path | None = None
    try:
        write_snapshot(staging, decisions, source_sha256)
        if output.exists():
            backup = Path(tempfile.mkdtemp(prefix=f".{output.name}.backup-", dir=output.parent))
            backup.rmdir()
            os.replace(output, backup)
        os.replace(staging, output)
        if backup is not None:
            shutil.rmtree(backup)
    except Exception:
        if backup is not None and backup.exists() and not output.exists():
            os.replace(backup, output)
        raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)


def main() -> int:
    args = parse_args()
    try:
        decisions, source_sha256 = load_decisions(args.input.resolve())
        replace_output(args.output, decisions, source_sha256)
    except (OSError, TypeError, ValueError) as exc:
        raise SystemExit(f"error: {exc}") from exc

    print(f"built {len(decisions)} decisions + index in {args.output}")
    print(f"source sha256: {source_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
