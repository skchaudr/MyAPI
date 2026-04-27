#!/usr/bin/env python3
"""Suggest concept links for each note based on body-keyword matching.

For each Phase 4 batch dryrun JSON, scan every note's body for keyword
patterns matching the 21 seeded concept stubs. Emit a per-batch markdown
"cheat sheet" — note path → suggested concepts → hit count. The owner
uses this to fly through the interactive owner-pass: most rows become
one-keystroke confirmations instead of fresh judgment calls.

Output: one .md per batch + an index linking them.

Cheat-sheet rows are read-only suggestions. Nothing is written to the
vault. Owner pass remains the only path that mutates `concepts:`.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DEFAULT_VAULT = Path("/Users/saboor/Obsidian/SoloDeveloper")
# Triage artifacts live outside both repos. MyAPI is a project repo, not a
# workspace; the vault is for notes, not sync-bloating JSON. Machine-local.
VAULT_TRIAGE_DIR = Path.home() / ".vault-triage-runs"
DEFAULT_REPORTS_DIR = VAULT_TRIAGE_DIR
DEFAULT_BATCH_GLOB = "v4-batch-*-dryrun.json"

# Each concept maps to keyword patterns that suggest the body talks about it.
# Patterns are case-insensitive substring or word-boundary regexes.
# Designed for *suggestion*, not classification — false positives are tolerable
# because the human still confirms each one in the owner-pass.
CONCEPT_PATTERNS: dict[str, list[str]] = {
    "Infrastructure": [r"\binfra(structure)?\b", r"\bvm\b", r"\bserver\b", r"\bnetwork(ing)?\b", r"\bhomelab\b"],
    "Developer Workflow": [r"\bworkflow\b", r"\bci[\s/-]*cd\b", r"\bdeploy(ment)?\b", r"\bbuild(s|ing)?\b", r"\bpipeline\b"],
    "Programming": [r"\b(python|javascript|typescript|go(lang)?|rust|java)\b", r"\bsyntax\b", r"\bfunction\b", r"\bclass(es)?\b"],
    "AI Tooling": [r"\b(claude|gpt|gemini|copilot|cursor|aider)\b", r"\bllm\b", r"\bai (assistant|coding|tool)\b", r"\bopenrouter\b"],
    "Code Problem Solving": [r"\bleetcode\b", r"\b(dsa|algorithm|data structure)\b", r"\binterview prep\b", r"\b(solve|practice) problem"],
    "Multi-Device Git Workflow": [r"\bgit\b", r"\b(rebase|merge|branch|fetch|push|pull|stash|cherry-pick)\b", r"\bremote (origin|repo)\b"],
    "CLI Workflow": [r"\b(terminal|shell|bash|zsh|tmux|fzf)\b", r"\bcommand line\b", r"\b(pipe|piped|grep|awk|sed)\b", r"\balias(es)?\b"],
    "Knowledge Management": [r"\b(obsidian|vault|notes?)\b", r"\bcapture\b", r"\b(triage|normaliz)", r"\bknowledge\b"],
    "Keybindings": [r"\b(keybind(ing)?s?|shortcut|hotkey|leader key)\b", r"\b(home row|thumb cluster|chord)\b", r"\blayer\b"],
    "IDE": [r"\b(neovim|nvim|vscode|vs code|zed|antigravity|cursor)\b", r"\beditor\b", r"\b(plugin|extension)s?\b"],
    "OpenClaw": [r"\bopenclaw\b", r"\bclaw\b"],
    "Raspberry Pi": [r"\b(raspberry|raspi|pi(s)?)\b", r"\bheadless\b", r"\bssh\b"],
    "Dygma Raise": [r"\bdygma\b", r"\b(thumb cluster|keyboard layer|raise)\b"],
    "Automation": [r"\b(automation|automate|automat\w+)\b", r"\bhook(s)?\b", r"\b(cron|crontab|launchd)\b", r"\b(trigger|schedul)"],
    "Vault Normalization": [r"\b(schema|normaliz|frontmatter|v4)\b", r"\b(migration|migrate)\b", r"\bbatch normaliz"],
    "Agentic AI": [r"\bagent(ic|s)?\b", r"\bautonomous\b", r"\b(tool use|tool call)\b", r"\b(plan(ner|ning)?|orchestrat)"],
    "Client Work": [r"\b(client|freelance|beiley)\b", r"\b(scope|deliverable|invoice|kickoff)\b"],
    "Documentation": [r"\b(documentation|docs?|readme|runbook|handoff|adr)\b"],
    "Portfolio Design": [r"\bportfolio\b", r"\b(landing page|hero section|design system)\b"],
    "Benchmarking": [r"\b(benchmark|bench|solve-bench)\b", r"\b(eval|evaluation)\b", r"\b(retrieval|rerank)\b"],
    "Hand Therapy": [r"\b(hand therapy|nerve glide|ergonomic|nerve pain)\b", r"\b(rsi|carpal|tunnel)\b"],
}

COMPILED = {c: [re.compile(p, re.I) for p in patterns] for c, patterns in CONCEPT_PATTERNS.items()}


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_block, body_text). Empty frontmatter if none."""
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---", 4)
    if end == -1:
        return "", text
    return text[4:end], text[end + 4:]


def suggest_for_body(body: str) -> list[tuple[str, int]]:
    """Return [(concept, total_hits), ...] sorted by hits desc."""
    hits: dict[str, int] = {}
    for concept, patterns in COMPILED.items():
        n = sum(len(p.findall(body)) for p in patterns)
        if n > 0:
            hits[concept] = n
    return sorted(hits.items(), key=lambda x: (-x[1], x[0]))


def render_batch_report(batch_name: str, dryrun_data: list[dict], vault_root: Path) -> tuple[str, int]:
    """Build the per-batch cheat-sheet markdown. Returns (md_text, suggested_count)."""
    rows = []
    suggested_total = 0

    for item in dryrun_data:
        rel = item.get("path")
        if not rel:
            continue
        path = vault_root / rel
        if not path.exists():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        _, body = split_frontmatter(text)
        suggestions = suggest_for_body(body)
        if not suggestions:
            continue
        suggested_total += 1
        # Top 3 concepts max — owner-pass will probably accept top 1-2
        top = suggestions[:3]
        concept_links = ", ".join(f"`[[{c}]]`" for c, _ in top)
        hit_summary = " ".join(f"{c}:{n}" for c, n in top)
        rows.append((rel, item.get("confidence", "?"), concept_links, hit_summary))

    # Sort: review > medium > high; within same confidence, alphabetical
    confidence_rank = {"review": 0, "medium": 1, "high": 2}
    rows.sort(key=lambda r: (confidence_rank.get(r[1], 9), r[0].lower()))

    lines = [
        f"# Concept Suggestions — {batch_name}",
        "",
        f"For owner-pass on this batch. Each note's body was scanned for keyword patterns",
        f"matching the 21 seeded concept stubs. **Suggestions only — confirm each in the CLI.**",
        "",
        f"- Notes in batch: {len(dryrun_data)}",
        f"- Notes with 1+ concept suggestion: {suggested_total}",
        "",
        "| Note | Conf | Suggested Concepts | Hits |",
        "| ---- | ---- | ------------------ | ---- |",
    ]
    for rel, conf, concept_links, hit_summary in rows:
        # Escape pipes in note paths for the markdown table
        safe_rel = rel.replace("|", "\\|")
        lines.append(f"| `{safe_rel}` | {conf} | {concept_links} | {hit_summary} |")
    lines.append("")
    return "\n".join(lines), suggested_total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault-root", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--reports-dir", type=Path, default=DEFAULT_REPORTS_DIR)
    parser.add_argument("--batch-glob", default=DEFAULT_BATCH_GLOB)
    args = parser.parse_args()

    batches = sorted(args.reports_dir.glob(args.batch_glob))
    if not batches:
        print(f"No batches matching {args.batch_glob} in {args.reports_dir}")
        return 1

    index_lines = [
        "# V4 Concept Suggestion Index",
        "",
        "Per-batch concept-suggestion cheat sheets. Each file is a worklist for the",
        "interactive owner-pass at `python3 -m context_refinery.triage`.",
        "",
        "**Workflow:**",
        "1. Open the cheat sheet for the batch you're about to triage.",
        "2. Run the owner-pass on that batch's queue JSON.",
        "3. For each note, glance at the cheat sheet row and accept the suggested concepts (or override).",
        "",
        "| Batch | Cheat Sheet | Notes Suggested |",
        "| ----- | ----------- | --------------- |",
    ]

    grand_total = 0
    for batch_path in batches:
        batch_name = batch_path.stem.replace("-dryrun", "")
        try:
            data = json.loads(batch_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"  SKIP {batch_path.name} (invalid JSON)")
            continue
        md, count = render_batch_report(batch_name, data, args.vault_root)
        out_path = args.reports_dir / f"{batch_name}-concept-suggestions.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"WROTE {out_path}  ({count} notes with suggestions)")
        index_lines.append(f"| `{batch_name}` | [{out_path.name}]({out_path.name}) | {count} |")
        grand_total += count

    index_lines.append("")
    index_lines.append(f"**Total notes with at least one suggested concept: {grand_total}**")
    index_path = args.reports_dir / "v4-concept-suggestions-INDEX.md"
    index_path.write_text("\n".join(index_lines), encoding="utf-8")
    print(f"WROTE {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
