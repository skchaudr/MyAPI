#!/usr/bin/env python3
"""Audit vault tags for V4 prefix compliance.

Walks every note's frontmatter, extracts the `tags:` field, classifies
each tag as prefixed (`topic/`, `tool/`, `lang/`, `scope/`) or unprefixed,
and proposes a migration prefix for the unprefixed ones based on
heuristic dictionaries.

Output: a markdown report grouped by suggested prefix, with per-tag
file-count and a sample of files using each tag. Owner uses this as
a Tier 2 worklist for the interactive owner-pass.

Read-only — no vault edits. The owner-pass CLI is the only writer.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

DEFAULT_VAULT = Path("/Users/saboor/Obsidian/SoloDeveloper")
# Triage artifacts live outside both repos. MyAPI is a project repo, not a
# workspace; the vault is for notes, not sync-bloating JSON. Machine-local.
VAULT_TRIAGE_DIR = Path.home() / ".vault-triage-runs"
DEFAULT_REPORT = VAULT_TRIAGE_DIR / "v4-tag-prefix-audit.md"

PREFIXES = ("topic/", "tool/", "lang/", "scope/")

IGNORED_PARTS = {".git", ".obsidian", ".trash", "09 Utilities/Attachments"}

# Heuristic dictionaries — case-insensitive match on the tag's normalized form.
# Add more as the vault evolves; this is a starting set tuned for Saboor's vault.
TOOL_TAGS = {
    "neovim", "vim", "nvim", "obsidian", "ghostty", "iterm", "iterm2", "tmux",
    "zed", "vscode", "vs-code", "antigravity", "claude", "claude-code", "codex",
    "gemini", "copilot", "cursor", "aider", "git", "github", "gh", "fzf",
    "supermaven", "lovable", "supabase", "vercel", "next-forge", "shadcn",
    "templater", "quickadd", "linter", "tasknotes", "dataview", "espanso",
    "raycast", "alfred", "notebooklm", "notebook-lm", "nlm", "openrouter",
    "macos", "darwin", "homebrew", "brew", "node", "npm", "nvm", "python",
    "pip", "poetry", "venv", "rich", "ruff",
}
LANG_TAGS = {
    "ts", "typescript", "js", "javascript", "py", "python", "go", "golang",
    "rust", "java", "c", "cpp", "c++", "csharp", "ruby", "swift", "kotlin",
    "html", "css", "scss", "sql", "bash", "zsh", "shell", "lua",
}
SCOPE_TAGS = {
    "career", "health", "fitness", "ergonomics", "ergonomic", "ops", "finance",
    "finances", "learning", "mindset", "sleep", "family", "relationships",
    "spiritual", "environment", "writing", "communication",
}
# Common topic substrings — used as fallback. Order matters; first match wins.
TOPIC_HINTS = [
    ("ai", "topic/ai"),
    ("ml", "topic/ml"),
    ("llm", "topic/ai"),
    ("agent", "topic/ai"),
    ("agentic", "topic/ai"),
    ("automation", "topic/automation"),
    ("workflow", "topic/workflow"),
    ("web-dev", "topic/web-dev"),
    ("webdev", "topic/web-dev"),
    ("frontend", "topic/web-dev"),
    ("backend", "topic/backend"),
    ("react", "topic/web-dev"),
    ("vite", "topic/web-dev"),
    ("dsa", "topic/dsa"),
    ("interview", "topic/dsa"),
    ("systems", "topic/systems"),
    ("infrastructure", "topic/systems"),
    ("infra", "topic/systems"),
    ("homelab", "topic/systems"),
    ("network", "topic/systems"),
    ("security", "topic/security"),
    ("auth", "topic/security"),
    ("testing", "topic/testing"),
    ("docs", "topic/docs"),
    ("documentation", "topic/docs"),
    ("howto", "topic/howto"),
    ("guide", "topic/howto"),
    ("log", "topic/log"),
    ("workout", "topic/log"),
    ("training", "topic/log"),
    ("meeting", "topic/log"),
    ("incident", "topic/log"),
    ("design", "topic/design"),
    ("ui", "topic/design"),
    ("ux", "topic/design"),
    ("portfolio", "topic/design"),
]
# Tags to drop entirely (legacy structural noise — V4 uses `type:` for these).
DROP_TAGS = {
    "project", "area", "resource", "utility", "task", "log", "concept",
    "event", "periodic",
}


def split_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    raw = text[4:end]
    try:
        parsed = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def normalize_tag(tag: str) -> str:
    """Strip leading #, lowercase, trim whitespace."""
    t = str(tag).strip()
    if t.startswith("#"):
        t = t[1:]
    return t


def classify(tag: str) -> str | None:
    """Return suggested prefix for an unprefixed tag, or None to drop."""
    norm = tag.lower().replace("_", "-")
    if norm in DROP_TAGS:
        return None  # drop entirely
    if norm in TOOL_TAGS:
        return f"tool/{norm}"
    if norm in LANG_TAGS:
        # Map verbose forms to canonical short codes
        canonical = {"typescript": "ts", "javascript": "js", "python": "py", "golang": "go"}
        return f"lang/{canonical.get(norm, norm)}"
    if norm in SCOPE_TAGS:
        return f"scope/{norm}"
    for hint, suggestion in TOPIC_HINTS:
        if hint in norm:
            return suggestion
    # Fallback: topic/<slug>
    slug = re.sub(r"[^a-z0-9-]+", "-", norm).strip("-")
    return f"topic/{slug}" if slug else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault-root", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    # Per unprefixed tag → list of file paths using it
    unprefixed_uses: dict[str, list[str]] = defaultdict(list)
    # Per prefixed tag → file count (for sanity)
    prefixed_counts: Counter = Counter()
    # Total notes, notes with tags, notes with at least one unprefixed tag
    total_notes = 0
    notes_with_tags = 0
    notes_with_unprefixed = 0

    for path in args.vault_root.rglob("*.md"):
        rel = str(path.relative_to(args.vault_root))
        if any(rel.startswith(i + "/") or rel == i for i in IGNORED_PARTS):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        total_notes += 1
        fm = split_frontmatter(text)
        tags = fm.get("tags")
        if tags is None:
            continue
        if isinstance(tags, str):
            tags = [tags]
        if not isinstance(tags, list):
            continue
        notes_with_tags += 1
        had_unprefixed = False
        for raw in tags:
            t = normalize_tag(raw)
            if not t:
                continue
            if t.startswith(PREFIXES):
                prefixed_counts[t] += 1
            else:
                unprefixed_uses[t].append(rel)
                had_unprefixed = True
        if had_unprefixed:
            notes_with_unprefixed += 1

    # Group unprefixed tags by suggested migration target
    by_suggestion: dict[str, list[tuple[str, int, list[str]]]] = defaultdict(list)
    drop_list: list[tuple[str, int, list[str]]] = []
    for tag, files in sorted(unprefixed_uses.items(), key=lambda x: (-len(x[1]), x[0].lower())):
        suggestion = classify(tag)
        entry = (tag, len(files), files[:5])  # sample 5 files per tag
        if suggestion is None:
            drop_list.append(entry)
        else:
            by_suggestion[suggestion].append(entry)

    # Render report
    lines = [
        "---",
        "type: utility",
        "title: V4 Tag Prefix Audit",
        "area: '[[Vault]]'",
        "source: original",
        "---",
        "",
        "# V4 Tag Prefix Audit",
        "",
        f"Vault root: `{args.vault_root}`",
        "",
        "## Summary",
        "",
        f"- Total notes scanned: **{total_notes}**",
        f"- Notes with `tags:` field: **{notes_with_tags}**",
        f"- Notes with at least one unprefixed tag: **{notes_with_unprefixed}**",
        f"- Distinct unprefixed tag values: **{len(unprefixed_uses)}**",
        f"- Distinct prefixed tag values (already V4-clean): **{len(prefixed_counts)}**",
        "",
        "## Tier 2 Worklist — Unprefixed → Suggested Prefix",
        "",
        "Each row is one tag value to migrate via the owner-pass CLI. The suggested prefix",
        "is a heuristic; override during owner-pass when the meaning is wrong.",
        "",
    ]

    if drop_list:
        lines.append("### Suggested DROP — structural noise (V4 uses `type:` for these)")
        lines.append("")
        lines.append("| Tag | Files | Sample |")
        lines.append("| --- | ----- | ------ |")
        for tag, count, sample in drop_list:
            sample_str = ", ".join(f"`{s}`" for s in sample)
            lines.append(f"| `{tag}` | {count} | {sample_str} |")
        lines.append("")

    for suggestion in sorted(by_suggestion.keys()):
        lines.append(f"### → `{suggestion}`")
        lines.append("")
        lines.append("| Tag | Files | Sample (up to 5) |")
        lines.append("| --- | ----- | ---------------- |")
        for tag, count, sample in by_suggestion[suggestion]:
            sample_str = ", ".join(f"`{s}`" for s in sample)
            lines.append(f"| `{tag}` | {count} | {sample_str} |")
        lines.append("")

    lines.append("## Existing Prefixed Tags (V4-clean — informational)")
    lines.append("")
    lines.append("| Tag | Files |")
    lines.append("| --- | ----- |")
    for tag, count in prefixed_counts.most_common():
        lines.append(f"| `{tag}` | {count} |")
    lines.append("")

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines), encoding="utf-8")
    print(f"WROTE {args.report}")
    print(f"unprefixed: {len(unprefixed_uses)} distinct tags across {notes_with_unprefixed} notes")
    print(f"to drop: {len(drop_list)}")
    print(f"prefixed: {len(prefixed_counts)} distinct tags")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
