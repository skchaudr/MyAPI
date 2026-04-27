#!/usr/bin/env python3
"""Harvest candidate V4 concepts from existing vault wiki links.

For every `[[wiki link]]` in the vault (frontmatter + body), count
occurrences. Anything appearing in 3+ distinct notes is a concept
candidate. Emit a markdown report grouped by frequency tier.

The owner reviews the report and decides which candidates become
real `type: concept` stub notes in 03 Resources/Concepts/.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_VAULT = Path("/Users/saboor/Obsidian/SoloDeveloper")
# Triage artifacts live outside both repos. MyAPI is a project repo, not a
# workspace; the vault is for notes, not sync-bloating JSON. Machine-local.
VAULT_TRIAGE_DIR = Path.home() / ".vault-triage-runs"
DEFAULT_REPORT = VAULT_TRIAGE_DIR / "v4-concept-harvest.md"

# Match [[anything]] but not embeds ![[...]] and not internal anchors with |alias —
# we keep the raw link text before any pipe.
WIKI_LINK_RE = re.compile(r"(?<!!)\[\[([^\[\]]+?)\]\]")

# Folders to skip — attachments, system internals, archive (we want active concepts).
IGNORED_PARTS = {".git", ".obsidian", ".trash", "09 Utilities/Attachments"}


def link_canonical(raw: str) -> str:
    """Normalize a wiki link target: strip alias, strip subpath, strip .md, trim."""
    # Drop alias (text after |)
    target = raw.split("|", 1)[0]
    # Drop fragment (text after #)
    target = target.split("#", 1)[0]
    # Drop folder path — keep only the basename
    target = target.rsplit("/", 1)[-1]
    # Drop .md extension if present
    if target.endswith(".md"):
        target = target[:-3]
    return target.strip()


def is_concept_note(path: Path) -> bool:
    """Cheap check: a file is a concept note if its frontmatter has type: concept."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    if not text.startswith("---\n"):
        return False
    end = text.find("\n---", 4)
    if end == -1:
        return False
    fm = text[4:end]
    return bool(re.search(r"^type:\s*concept\s*$", fm, re.M))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--min-occurrences", type=int, default=3,
                        help="Minimum distinct files to qualify as a candidate. Default: 3.")
    args = parser.parse_args()

    # Per-target: count how many distinct files reference it
    file_counts: dict[str, set[str]] = defaultdict(set)
    # Track which targets already have an actual concept stub note
    existing_concepts: set[str] = set()

    for path in args.root.rglob("*.md"):
        rel = str(path.relative_to(args.root))
        if any(rel.startswith(i + "/") or rel == i for i in IGNORED_PARTS):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        # Track if this file is itself a concept stub
        if is_concept_note(path):
            existing_concepts.add(path.stem)

        for raw in WIKI_LINK_RE.findall(text):
            target = link_canonical(raw)
            if not target:
                continue
            file_counts[target].add(rel)

    # Build candidate list: distinct-file count >= threshold, AND no concept stub yet
    candidates: list[tuple[str, int]] = []
    already_seeded: list[tuple[str, int]] = []
    for target, files in file_counts.items():
        cnt = len(files)
        if cnt < args.min_occurrences:
            continue
        if target in existing_concepts:
            already_seeded.append((target, cnt))
        else:
            candidates.append((target, cnt))

    candidates.sort(key=lambda x: (-x[1], x[0].lower()))
    already_seeded.sort(key=lambda x: (-x[1], x[0].lower()))

    # Tiered presentation by frequency
    def tier(cnt: int) -> str:
        if cnt >= 25: return "Tier A — workhorse links (25+ files)"
        if cnt >= 10: return "Tier B — recurring themes (10–24 files)"
        if cnt >= 5: return "Tier C — emerging patterns (5–9 files)"
        return "Tier D — borderline (3–4 files)"

    by_tier: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for t, c in candidates:
        by_tier[tier(c)].append((t, c))

    lines = [
        "---",
        "type: utility",
        "title: V4 Concept Harvest",
        "area: \"[[Vault]]\"",
        "source: original",
        "---",
        "",
        "# V4 Concept Harvest",
        "",
        f"Vault root: `{args.root}`",
        f"Threshold: links appearing in **{args.min_occurrences}+ distinct files**.",
        "",
        f"- Distinct wiki-link targets: **{len(file_counts)}**",
        f"- Above threshold: **{len(candidates) + len(already_seeded)}**",
        f"- Already concept-stubbed: **{len(already_seeded)}**",
        f"- New candidates (need review): **{len(candidates)}**",
        "",
        "Each candidate is a `[[link]]` that already appears across multiple notes — meaning",
        "your past self has been gesturing at this idea for a while. Promoting to a concept",
        "stub in `03 Resources/Concepts/` makes it part of the V4 graph backbone.",
        "",
        "Decide per row: **keep** (promote to concept stub), **drop** (not really a concept),",
        "or **rename** (canonical form differs from the link text).",
        "",
    ]

    for tier_name in ["Tier A — workhorse links (25+ files)",
                      "Tier B — recurring themes (10–24 files)",
                      "Tier C — emerging patterns (5–9 files)",
                      "Tier D — borderline (3–4 files)"]:
        if tier_name not in by_tier:
            continue
        lines.append(f"## {tier_name}")
        lines.append("")
        lines.append("| Count | Candidate | Decision |")
        lines.append("| ----- | --------- | -------- |")
        for target, cnt in by_tier[tier_name]:
            lines.append(f"| {cnt} | `[[{target}]]` |  |")
        lines.append("")

    if already_seeded:
        lines.append("## Already concept-stubbed (informational)")
        lines.append("")
        lines.append("| Count | Concept |")
        lines.append("| ----- | ------- |")
        for target, cnt in already_seeded:
            lines.append(f"| {cnt} | `[[{target}]]` |")
        lines.append("")

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines), encoding="utf-8")
    print(f"WROTE {args.report}")
    print(f"distinct targets: {len(file_counts)}")
    print(f"candidates (>= {args.min_occurrences} files, not yet stubbed): {len(candidates)}")
    print(f"already stubbed: {len(already_seeded)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
