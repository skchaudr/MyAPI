#!/usr/bin/env python3
"""Generate a note-refinement queue from a retrieval benchmark report."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


TABLE_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|(.*)\|\s*$")


@dataclass(frozen=True)
class BenchmarkRow:
    number: int
    query: str
    intent: str
    after_filter: str
    from_khoj: str
    top_results: list[str]


@dataclass(frozen=True)
class RefinementTarget:
    desired_anchor: str
    problem: str
    owner_action: str
    benchmark_goal: str


TARGETS: dict[int, RefinementTarget] = {
    1: RefinementTarget(
        desired_anchor="my-devinfra-system-anchor.md",
        problem="Project identity still depends on a mix of one useful Obsidian note and raw Claude evidence.",
        owner_action="Create or strengthen the canonical My_DevInfra identity note with current scope, components, and source evidence.",
        benchmark_goal="The My_DevInfra anchor should appear in the top 3 and raw dumps should sit below it.",
    ),
    7: RefinementTarget(
        desired_anchor="retrieval-rag-learning-anchor.md",
        problem="Retrieval-learning queries surface plausible ChatGPT notes, but no synthesized learning anchor clearly wins.",
        owner_action="Create a concise retrieval/RAG learning anchor that names embeddings, indexing, RAG, reranking, and benchmark lessons.",
        benchmark_goal="The retrieval/RAG anchor should appear in the top 3 for retrieval-learning questions.",
    ),
    8: RefinementTarget(
        desired_anchor="obsidian-vault-schema-anchor.md",
        problem="Vault-schema decisions are scattered across ChatGPT and Obsidian notes.",
        owner_action="Create a vault schema decision anchor with folder logic, frontmatter rules, note kinds, and current tradeoffs.",
        benchmark_goal="The schema anchor should appear in the top 3 for vault-schema decision queries.",
    ),
    10: RefinementTarget(
        desired_anchor="khoj-deployment-indexing-anchor.md",
        problem="Khoj deployment/indexing queries are still won by raw operational logs.",
        owner_action="Create a Khoj deployment/indexing anchor with VM, data disk, service, reindex, and verification state.",
        benchmark_goal="The Khoj anchor should appear above Claude/Codex raw logs for operational indexing queries.",
    ),
    12: RefinementTarget(
        desired_anchor="api-deployment-status-anchor.md",
        problem="API deployment status is partly answered by system-status briefing, but raw logs still dominate.",
        owner_action="Create or refine the current API deployment status anchor with service paths, health checks, and known failure modes.",
        benchmark_goal="The API status anchor should appear in the top 3 and answer the status question directly.",
    ),
    16: RefinementTarget(
        desired_anchor="vm-tailscale-ssh-access-anchor.md",
        problem="VM/Tailscale/SSH access queries surface raw command sessions instead of an access runbook.",
        owner_action="Create a VM access anchor with Tailscale IPs, gcloud SSH syntax, service checks, disk layout, and recovery notes.",
        benchmark_goal="The VM access anchor should appear above raw command logs for Tailscale, SSH, and VM access queries.",
    ),
    18: RefinementTarget(
        desired_anchor="current-system-end-to-end-anchor.md",
        problem="End-to-end system understanding lacks one canonical overview result.",
        owner_action="Create a system overview anchor that connects MyAPI, Context Refinery, Khoj, Obsidian corpus, benchmark loop, and VM runtime.",
        benchmark_goal="The system overview anchor should appear in the top 3 for end-to-end docs queries.",
    ),
}


def split_markdown_row(line: str) -> list[str]:
    """Split a simple markdown table row while preserving escaped pipes."""
    cells: list[str] = []
    current: list[str] = []
    escaped = False

    for char in line.strip():
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\":
            escaped = True
            current.append(char)
            continue
        if char == "|":
            cells.append("".join(current).strip())
            current = []
            continue
        current.append(char)

    cells.append("".join(current).strip())
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def parse_benchmark(path: Path) -> list[BenchmarkRow]:
    rows: list[BenchmarkRow] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = TABLE_ROW_RE.match(line)
        if not match:
            continue
        cells = split_markdown_row(line)
        if len(cells) < 6 or not cells[0].isdigit():
            continue
        top_results = [item.strip() for item in cells[5].split("<br>") if item.strip()]
        rows.append(
            BenchmarkRow(
                number=int(cells[0]),
                query=cells[1],
                intent=cells[2],
                after_filter=cells[3],
                from_khoj=cells[4],
                top_results=top_results,
            )
        )
    return rows


def render_queue(rows: list[BenchmarkRow], benchmark_path: Path) -> str:
    lines = [
        "# Benchmark-Driven Refinement Queue",
        "",
        f"Source benchmark: `{benchmark_path}`",
        "",
        "Purpose: convert retrieval benchmark misses into a small owner-pass queue for source-of-truth anchor notes.",
        "",
        "Operating loop:",
        "",
        "1. Normalize deterministic metadata.",
        "2. Owner/refiner writes or strengthens the target anchor.",
        "3. Reindex Khoj.",
        "4. Rerun the same benchmark.",
        "5. Compare whether the anchor now wins.",
        "",
        "## Anchor Targets",
        "",
    ]

    by_number = {row.number: row for row in rows}
    for number in sorted(TARGETS):
        row = by_number.get(number)
        target = TARGETS[number]
        if row is None:
            continue
        lines.extend(
            [
                f"### Q{row.number}: {row.query}",
                "",
                f"- Intent: `{row.intent}`",
                f"- Desired anchor: `{target.desired_anchor}`",
                f"- Problem: {target.problem}",
                f"- Owner action: {target.owner_action}",
                f"- Benchmark goal: {target.benchmark_goal}",
                f"- Current top results: {', '.join(row.top_results[:5])}",
                "",
                "Owner-pass notes:",
                "",
                "- ",
                "",
            ]
        )

    lines.extend(
        [
            "## Batch Normalizer Scope",
            "",
            "Safe deterministic fields:",
            "",
            "- `title`",
            "- `aliases`",
            "- `source`",
            "- `document_kind`",
            "- `type`",
            "- `status`",
            "- `projects`",
            "- `tags`",
            "- `created`",
            "- `modified`",
            "- `benchmark_targets`",
            "",
            "Owner-controlled fields:",
            "",
            "- `summary`",
            "- `decisions`",
            "- `failure_modes`",
            "- `source_evidence`",
            "- `related`",
            "",
            "## First Pilot Batch",
            "",
            "- `my-devinfra-system-anchor.md`",
            "- `khoj-deployment-indexing-anchor.md`",
            "- `vm-tailscale-ssh-access-anchor.md`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("benchmark", type=Path, help="Path to benchmark markdown report")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Path to write refinement queue markdown")
    args = parser.parse_args()

    rows = parse_benchmark(args.benchmark)
    if not rows:
        raise SystemExit(f"No benchmark rows found in {args.benchmark}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_queue(rows, args.benchmark), encoding="utf-8")
    print(f"WROTE {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
