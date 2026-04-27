#!/usr/bin/env python3
"""Normalizer for Vault Schema V4 metadata migration.

Modes:
  dry-run (default)  — writes reports only, no vault files touched
  --apply            — rewrites YAML frontmatter for high-confidence files
                       (body is never modified, backups written before edits)

Safety contract for --apply:
  1. Only edits files in the selected --subdir.
  2. Requires --confidence high (default when --apply is set).
  3. Writes .bak alongside each edited file before touching it.
  4. Writes a JSON change manifest (--manifest path).
  5. Only rewrites YAML frontmatter — body content is preserved exactly.
  6. Does not move files.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

# Fields the script is allowed to write automatically.
# Meaning-heavy fields (concepts, related, summary) are left for the owner pass.
APPLY_FIELDS = {"type", "status", "area", "project", "tags", "source", "folder_origin", "migration_status"}


VALID_TYPES = {"project", "area", "resource", "concept", "event", "periodic", "log", "utility"}
PROJECT_EVENT_STATUSES = {"active", "incubating", "backlog", "blocked", "done"}
VALID_SOURCES = {"original", "article", "meeting", "transcript", "ai-assisted", "imported"}
TAG_PREFIXES = ("topic/", "tool/", "lang/", "scope/")
MAX_TAGS = 8

DEFAULT_VAULT = Path("/Users/saboor/obsidian/SoloDeveloper")


TOP_LEVEL_MAP = {
    "00 Inbox": ("inbox", "resource"),
    "01 Projects": ("projects", "resource"),
    "02 Areas": ("areas", "resource"),
    "03 Resources": ("resources", "resource"),
    "04 Periodic": ("periodics", "periodic"),
    "05 Archive": ("archive", "resource"),
    "09 Utilities": ("system", "utility"),
    "Templates": ("system", "utility"),
    "TaskNotes": ("projects", "resource"),
    "__ Tasks __": ("projects", "event"),
    "__Tasks__": ("projects", "event"),
    "_tasks": ("projects", "event"),
}

PRIVATE_PATH_PARTS = {"Confidential", "_private", "Relationships", "SMW"}

AREA_BY_PATH = {
    "Career": "Career",
    "Code Problem Solving": "Code Problem Solving",
    "Relationships": "Private",
    "SMW": "Mens Work",
    "Personal": "Personal Growth",
    "Finances": "Finances",
    "Health": "Health",
    "Learning": "Learning",
    "Developer Infrastructure": "Developer Infrastructure",
}

RESOURCE_TOPIC_TAGS = {
    "AI": "topic/ai",
    "API Keys": "topic/security",
    "Google": "tool/google",
    "MacOS": "tool/macos",
    "Mindfulness": "topic/mindfulness",
    "NeoVim": "tool/neovim",
    "Programming": "topic/programming",
    "Workflows": "topic/workflow",
}

RESOURCE_AREA_MAP = {
    "AI": "Developer Infrastructure",
    "API Keys": "Developer Infrastructure",
    "Google": "Developer Infrastructure",
    "MacOS": "Developer Infrastructure",
    "Mindfulness": "Health",
    "NeoVim": "Developer Infrastructure",
    "Programming": "Developer Infrastructure",
    "Workflows": "Developer Infrastructure",
}

PROJECT_NAME_ALIASES = {
    "CxRef": "Context Refinery",
    "GDDP": "GDDP",
    "MyAPI": "MyAPI",
    "SC Automations": "SC Automations",
    "SocialXP": "SocialXP",
    "Solve-Bench": "Solve Bench",
    "Universal Router": "Universal Router",
    "VaultDr": "Vault Doctor",
    "WAS": "Water and Stone",
}


@dataclass
class Suggestion:
    path: str
    destination_folder: str
    confidence: str
    reasons: list[str] = field(default_factory=list)
    review_needed: list[str] = field(default_factory=list)
    current: dict[str, Any] = field(default_factory=dict)
    suggested: dict[str, Any] = field(default_factory=dict)


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    try:
        parsed = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        return {}, body
    if not isinstance(parsed, dict):
        return {}, body
    return parsed, body


def wiki(value: str) -> str:
    return f"[[{value}]]"


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def clean_type(value: Any) -> str | None:
    if not value:
        return None
    normalized = str(value).strip().lower()
    return normalized if normalized in VALID_TYPES else None


def clean_status(value: Any) -> str | None:
    if not value:
        return None
    normalized = str(value).strip().lower()
    return normalized if normalized in PROJECT_EVENT_STATUSES else None


def normalize_tags(existing: Any, inferred: list[str]) -> tuple[list[str], list[str]]:
    review: list[str] = []
    tags: list[str] = []
    for item in as_list(existing):
        tag = str(item).strip()
        if not tag:
            continue
        if tag.startswith("#"):
            tag = tag[1:]
        if tag.startswith(TAG_PREFIXES):
            tags.append(tag)
        else:
            review.append(f"unprefixed tag `{tag}`")
    for tag in inferred:
        if tag not in tags:
            tags.append(tag)
    return tags[:MAX_TAGS], review


def infer_from_path(path: Path, vault_root: Path) -> tuple[str, str, list[str], dict[str, Any]]:
    rel = path.relative_to(vault_root)
    parts = rel.parts
    top = parts[0] if parts else ""

    destination, inferred_type = TOP_LEVEL_MAP.get(top, ("resources", "resource"))
    reasons = [f"top-level folder `{top}` maps to `{destination}/`"]
    inferred: dict[str, Any] = {"type": inferred_type}

    if any(part in PRIVATE_PATH_PARTS for part in parts):
        destination = "_private"
        reasons.append("path contains private/confidential segment")

    if top == "01 Projects" and len(parts) > 1:
        project_name = PROJECT_NAME_ALIASES.get(parts[1], parts[1])
        inferred["project"] = wiki(f"--{project_name}")
        reasons.append(f"project inferred from folder `{parts[1]}`")

    if top == "02 Areas":
        area_name = next((AREA_BY_PATH[p] for p in parts if p in AREA_BY_PATH), None)
        if area_name:
            inferred["area"] = wiki(area_name)
            reasons.append(f"area inferred from folder `{area_name}`")

    if top == "03 Resources" and len(parts) > 1:
        tag = RESOURCE_TOPIC_TAGS.get(parts[1])
        if tag:
            inferred["tags"] = [tag]
            reasons.append(f"tag inferred from resource folder `{parts[1]}`")
        area = RESOURCE_AREA_MAP.get(parts[1])
        if area:
            inferred["area"] = wiki(area)
            reasons.append(f"area inferred from resource folder `{parts[1]}`")

    if top == "04 Periodic":
        inferred["area"] = wiki("Life")
        inferred["tags"] = ["topic/log"]
        reasons.append("periodic note gets life area and log tag")

    if top == "05 Archive":
        reasons.append("archive folder preserves inactive destination")

    if top == "09 Utilities":
        inferred["area"] = wiki("Vault")
        if "_Vault System" in parts:
            inferred["tags"] = ["topic/reference"]
            reasons.append("vault-system utility gets reference tag")
        else:
            reasons.append("utilities note gets vault area")

    name = path.stem.lower()
    if re.search(r"\b(anchor|index|home|homepage)\b", name):
        if top == "01 Projects":
            inferred["type"] = "project"
        elif top == "02 Areas":
            inferred["type"] = "area"
        elif top == "03 Resources":
            inferred["type"] = "resource"
        reasons.append("anchor-like filename adjusted structural type")

    return destination, inferred["type"], reasons, inferred


def suggest_for_file(path: Path, vault_root: Path) -> Suggestion:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, _ = split_frontmatter(text)
    destination, inferred_type, reasons, inferred = infer_from_path(path, vault_root)

    suggested: dict[str, Any] = {}
    review_needed: list[str] = []

    current_type = clean_type(fm.get("type"))
    if current_type:
        suggested["type"] = current_type
        if current_type != inferred_type:
            review_needed.append(f"type conflict: current `{current_type}`, inferred `{inferred_type}`")
    else:
        suggested["type"] = inferred_type

    is_inbox_capture = path.relative_to(vault_root).parts[:1] == ("00 Inbox",)

    if "area" in inferred and not fm.get("area"):
        suggested["area"] = inferred["area"]
    elif fm.get("area"):
        suggested["area"] = fm["area"]
    elif suggested["type"] not in {"concept", "periodic"} and not is_inbox_capture:
        review_needed.append("missing area/project/concept connection")

    if "project" in inferred and not fm.get("project"):
        suggested["project"] = inferred["project"]
    elif fm.get("project"):
        suggested["project"] = fm["project"]

    current_status = clean_status(fm.get("status"))
    if suggested["type"] in {"project", "event"}:
        suggested["status"] = current_status or "active"
    elif fm.get("status"):
        review_needed.append("status exists on non-project/event type")

    inferred_tags = inferred.get("tags", [])
    tags, tag_review = normalize_tags(fm.get("tags"), inferred_tags)
    if tags:
        suggested["tags"] = tags
    review_needed.extend(tag_review)

    if not fm.get("concepts"):
        review_needed.append("concepts need owner assignment")
    else:
        suggested["concepts"] = fm["concepts"]

    # Source field (V4 provenance). Preserve existing valid value or infer a default;
    # apply_suggestion gates whether the inferred default actually gets written.
    current_source = fm.get("source")
    if current_source and str(current_source).strip().lower() in VALID_SOURCES:
        suggested["source"] = str(current_source).strip().lower()
    elif current_source:
        review_needed.append(f"unknown source value `{current_source}`")
        suggested["source"] = current_source
    else:
        rel_top = path.relative_to(vault_root).parts[:1]
        suggested["source"] = "original" if rel_top == ("04 Periodic",) else "imported"

    suggested["folder_origin"] = str(path.relative_to(vault_root).parent)
    suggested["migration_status"] = "v4-dry-run"

    confidence = "high"
    if not review_needed or review_needed == ["concepts need owner assignment"]:
        confidence = "high"
    if len(review_needed) > 2:
        confidence = "medium"
    if any("conflict" in item or "missing area" in item for item in review_needed):
        confidence = "review"

    return Suggestion(
        path=str(path.relative_to(vault_root)),
        destination_folder=destination,
        confidence=confidence,
        reasons=reasons,
        review_needed=review_needed,
        current={k: fm.get(k) for k in ("type", "status", "area", "project", "concepts", "tags") if k in fm},
        suggested=suggested,
    )


def iter_markdown(root: Path) -> list[Path]:
    ignored_parts = {".git", ".obsidian", ".trash", "09 Utilities/Attachments"}
    files: list[Path] = []
    for path in root.rglob("*.md"):
        rel = str(path.relative_to(root))
        if any(rel == ignored or rel.startswith(f"{ignored}/") for ignored in ignored_parts):
            continue
        files.append(path)
    return sorted(files)


def render_markdown(suggestions: list[Suggestion], vault_root: Path) -> str:
    counts: dict[str, int] = {}
    for suggestion in suggestions:
        counts[suggestion.confidence] = counts.get(suggestion.confidence, 0) + 1

    lines = [
        "# Vault Schema V4 Normalization Dry Run",
        "",
        f"Vault root: `{vault_root}`",
        "",
        "## Summary",
        "",
        f"- Total files scanned: {len(suggestions)}",
        f"- High confidence: {counts.get('high', 0)}",
        f"- Medium confidence: {counts.get('medium', 0)}",
        f"- Needs review: {counts.get('review', 0)}",
        "",
        "## Review Queue",
        "",
    ]

    for suggestion in suggestions:
        if suggestion.confidence == "high":
            continue
        lines.extend(
            [
                f"### {suggestion.path}",
                "",
                f"- Confidence: `{suggestion.confidence}`",
                f"- Destination: `{suggestion.destination_folder}/`",
                f"- Reasons: {'; '.join(suggestion.reasons)}",
                f"- Review needed: {'; '.join(suggestion.review_needed)}",
                "- Suggested:",
                "```yaml",
                yaml.safe_dump(suggestion.suggested, sort_keys=False).strip(),
                "```",
                "",
            ]
        )

    lines.extend(["## High-Confidence Sample", ""])
    for suggestion in [s for s in suggestions if s.confidence == "high"][:20]:
        lines.extend(
            [
                f"### {suggestion.path}",
                "",
                f"- Destination: `{suggestion.destination_folder}/`",
                f"- Reasons: {'; '.join(suggestion.reasons)}",
                "```yaml",
                yaml.safe_dump(suggestion.suggested, sort_keys=False).strip(),
                "```",
                "",
            ]
        )
    return "\n".join(lines)


FIELD_ORDER = [
    "type", "status", "area", "project",
    "concepts", "tags", "source",
    "folder_origin", "migration_status",
]


def build_frontmatter(fm: dict[str, Any]) -> str:
    """Serialize frontmatter dict back to YAML, using canonical field order."""
    ordered: dict[str, Any] = {}
    for key in FIELD_ORDER:
        if key in fm:
            ordered[key] = fm[key]
    for key in fm:
        if key not in ordered:
            ordered[key] = fm[key]
    return yaml.dump(ordered, default_flow_style=False, sort_keys=False, allow_unicode=True)


def apply_suggestion(
    suggestion: Suggestion,
    vault_root: Path,
    backup_dir: Path | None,
    *,
    strip_format: bool = True,
    write_source_default: bool = True,
) -> dict[str, Any] | None:
    """Write suggested APPLY_FIELDS into a file's frontmatter.

    Returns a change record dict, or None if nothing changed or an error occurred.
    Writes a .bak file (or backup_dir copy) before touching the original.

    V4 enforcement applied during the apply phase (not just suggested):
      - migration_status flips from `v4-dry-run` to `v4-applied`.
      - `format:` is stripped if strip_format is True.
      - `status:` is removed from non-project/event types (unconditional V4 rule).
      - `source:` default is gated by write_source_default unless file already has source.
    """
    path = vault_root / suggestion.path
    try:
        original_text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"  ERROR reading {suggestion.path}: {exc}")
        return None

    fm, body = split_frontmatter(original_text)

    # Build effective suggestion gated by flags
    effective = dict(suggestion.suggested)

    # Source default is gated by --write-source-default unless file already has source
    if "source" in effective and "source" not in fm and not write_source_default:
        effective.pop("source")

    # In apply mode, migration_status flips to v4-applied
    effective["migration_status"] = "v4-applied"

    # Compute what will actually change from APPLY_FIELDS writes
    changes: dict[str, Any] = {}
    for key in APPLY_FIELDS:
        if key not in effective:
            continue
        new_val = effective[key]
        old_val = fm.get(key)
        if new_val != old_val:
            changes[key] = {"before": old_val, "after": new_val}

    # Format stripping (a removal, not a write — tracked separately)
    will_strip_format = strip_format and "format" in fm
    if will_strip_format:
        changes["format"] = {"before": fm["format"], "after": None}

    # V4 rule: status only on project/event. Strip from others if present.
    final_type = effective.get("type", fm.get("type"))
    will_strip_status = final_type not in {"project", "event"} and "status" in fm
    if will_strip_status:
        changes["status"] = {"before": fm["status"], "after": None}

    if not changes:
        return None

    # Write backup
    if backup_dir:
        backup_path = backup_dir / suggestion.path
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        backup_path.write_text(original_text, encoding="utf-8")
    else:
        path.with_suffix(path.suffix + ".bak").write_text(original_text, encoding="utf-8")

    # Apply changes to frontmatter
    updated_fm = dict(fm)
    for key in APPLY_FIELDS:
        if key in effective:
            updated_fm[key] = effective[key]

    if will_strip_format:
        updated_fm.pop("format", None)
    if will_strip_status:
        updated_fm.pop("status", None)

    new_text = f"---\n{build_frontmatter(updated_fm)}---\n\n{body}"
    path.write_text(new_text, encoding="utf-8")

    return {
        "file": suggestion.path,
        "confidence": suggestion.confidence,
        "changes": changes,
    }


def append_coverage_ledger(
    ledger_path: Path,
    *,
    batch_name: str,
    subdir: str,
    applied: int,
    skipped: int,
    manifest_path: str,
    strip_format: bool,
    write_source_default: bool,
) -> None:
    """Append a run entry to the coverage ledger.

    Solves the "no central ledger" gap from prior batches. Each --apply run
    appends a single entry; the ledger lives at project-docs/coverage-ledger.json
    by default and is the single source of truth for what's been normalized.
    """
    entry = {
        "run_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "batch": batch_name,
        "subdir": subdir,
        "applied": applied,
        "skipped": skipped,
        "manifest": manifest_path,
        "strip_format": strip_format,
        "write_source_default": write_source_default,
    }

    if ledger_path.exists():
        try:
            ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            ledger = {"runs": []}
    else:
        ledger = {"runs": []}

    if not isinstance(ledger, dict) or "runs" not in ledger:
        ledger = {"runs": []}

    ledger["runs"].append(entry)
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    ledger_path.write_text(json.dumps(ledger, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--subdir", default="", help="Path inside the vault to scan (required for --apply)")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--report", type=Path, default=Path("project-docs/vault-schema-v4-normalization-dry-run.md"))
    parser.add_argument("--json", type=Path, default=Path("project-docs/vault-schema-v4-normalization-dry-run.json"))
    parser.add_argument("--apply", action="store_true", help="Write frontmatter changes to vault files")
    parser.add_argument("--confidence", choices=["high", "medium", "review"], default="high",
                        help="Minimum confidence level to apply (default: high)")
    parser.add_argument("--backup-dir", type=Path, default=None,
                        help="Directory for backups before edits (default: .bak alongside each file)")
    parser.add_argument("--manifest", type=Path, default=None,
                        help="Path for JSON change manifest (default: <report>.manifest.json)")
    parser.add_argument("--strip-format", action=argparse.BooleanOptionalAction, default=True,
                        help="Strip the deprecated `format:` field from frontmatter (V4 cleanup). Default: on.")
    parser.add_argument("--write-source-default", action=argparse.BooleanOptionalAction, default=True,
                        help="Backfill `source` (`original` for periodics, `imported` elsewhere) when missing. Default: on.")
    parser.add_argument("--batch", default=None,
                        help="Batch name for the coverage ledger entry (default: derived from --subdir).")
    parser.add_argument("--ledger", type=Path, default=Path("project-docs/coverage-ledger.json"),
                        help="Coverage ledger file path; appended on --apply.")
    args = parser.parse_args()

    if args.apply and not args.subdir:
        print("ERROR: --apply requires --subdir to limit blast radius.")
        return 1

    scan_root = args.root / args.subdir if args.subdir else args.root
    files = iter_markdown(scan_root)
    if args.limit:
        files = files[: args.limit]

    suggestions = [suggest_for_file(path, args.root) for path in files]

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(render_markdown(suggestions, args.root), encoding="utf-8")
    args.json.write_text(
        json.dumps([s.__dict__ for s in suggestions], indent=2),
        encoding="utf-8",
    )
    print(f"WROTE {args.report}")
    print(f"WROTE {args.json}")

    if not args.apply:
        return 0

    # Apply mode — edit vault files
    confidence_rank = {"high": 0, "medium": 1, "review": 2}
    threshold = confidence_rank[args.confidence]
    candidates = [s for s in suggestions if confidence_rank[s.confidence] <= threshold]

    print(f"\nAPPLY MODE  confidence>={args.confidence}  candidates={len(candidates)}")

    if args.backup_dir:
        args.backup_dir.mkdir(parents=True, exist_ok=True)
        print(f"Backups → {args.backup_dir}")
    else:
        print("Backups → .bak alongside each file")

    manifest_path = args.manifest or args.report.with_suffix("").with_suffix(".manifest.json")
    change_records: list[dict[str, Any]] = []
    applied = skipped = errors = 0

    for suggestion in candidates:
        record = apply_suggestion(
            suggestion,
            args.root,
            args.backup_dir,
            strip_format=args.strip_format,
            write_source_default=args.write_source_default,
        )
        if record is None:
            skipped += 1
        else:
            change_records.append(record)
            applied += 1
            print(f"  ✓ {suggestion.path}  ({', '.join(record['changes'])})")

    manifest_path.write_text(
        json.dumps({
            "run_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "subdir": args.subdir,
            "confidence": args.confidence,
            "strip_format": args.strip_format,
            "write_source_default": args.write_source_default,
            "applied": applied,
            "skipped": skipped,
            "changes": change_records,
        }, indent=2),
        encoding="utf-8",
    )
    print(f"\napplied={applied}  skipped={skipped}  errors={errors}")
    print(f"MANIFEST {manifest_path}")

    # Append to the coverage ledger so we have a single source of truth
    # for which batches have been normalized.
    batch_name = args.batch or (args.subdir.replace("/", "-") if args.subdir else "all")
    append_coverage_ledger(
        args.ledger,
        batch_name=batch_name,
        subdir=args.subdir,
        applied=applied,
        skipped=skipped,
        manifest_path=str(manifest_path),
        strip_format=args.strip_format,
        write_source_default=args.write_source_default,
    )
    print(f"LEDGER  {args.ledger}  (batch={batch_name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
