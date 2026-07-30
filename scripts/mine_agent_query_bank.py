#!/usr/bin/env python3
"""Mine real agent-attempted questions from Pi/Codex session stores.

Read-only extractor. Produces a versioned question-bank manifest plus an
aggregate receipt. No raw transcript text is written to the repo; only
per-question fingerprints and provenance.

Two stores are scanned per host:

  - codex_sessions: ~/.codex/sessions/**/*.jsonl (Codex rollout format)
  - pi_agent_sessions: ~/.pi/agent/sessions/**/*.jsonl (Pi message log)

User-role messages are extracted, normalized, deduplicated, and categorized
into:

  - knowledge: free-form information question
  - graphify_invocation: calls the graphify CLI (extract / show / etc.)
  - graphify_meta: asks about graphify itself without invoking it

Provenance is preserved per question: host, store, session file path, the
timestamp from the source message, and the line/message index inside the
file. Each unique question is recorded once with an `occurrences` list
pointing at every place it appeared.

Outputs:

  - <out_dir>/question-bank-manifest.json (full bank, no raw text)
  - <out_dir>/benchmark-receipt.md      (human-readable summary)
  - <out_dir>/_scratch/                 (intermediates; gitignored)
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "1.0"
BANK_VERSION = "1.0.0"
SCRATCH_DIR: Path = REPO_ROOT / "evals" / "question-bank" / "_scratch"

# ---- normalization ----------------------------------------------------------

_WS_RE = re.compile(r"\s+")
_CONTROL_RE = re.compile(r"[\x00-\x08\x0b-\x0c\x0e-\x1f]")


def normalize_text(text: str) -> str:
    """Return a stable, deduplication-friendly form of a question.

    Strips AGENTS.md-style instruction blocks, normalises whitespace, drops
    leading/trailing punctuation noise, and folds case. This is intentionally
    aggressive: near-duplicates should collide here so the bank reflects what
    an agent actually needed, not the surface wording of every variant.
    """
    if not text:
        return ""
    # Remove AGENTS.md / INSTRUCTIONS / system-prompt blocks common in
    # Codex user payloads so the underlying question is what gets hashed.
    text = re.sub(r"<INSTRUCTIONS>.*?</INSTRUCTIONS>", " ", text, flags=re.DOTALL)
    text = re.sub(r"<permissions instructions>.*?</permissions instructions>", " ", text, flags=re.DOTALL)
    text = re.sub(r"^# AGENTS\.md instructions for .+?$", " ", text, flags=re.MULTILINE)
    text = _CONTROL_RE.sub(" ", text)
    text = unicodedata.normalize("NFKC", text)
    text = text.strip().lower()
    text = _WS_RE.sub(" ", text)
    text = text.strip(" \t\n\r,.;:!?\"'`*_~#-")
    return text


def text_fingerprint(text: str) -> str:
    """Stable hash for the original text (for cross-store dedup)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def norm_key(text: str) -> str:
    return hashlib.sha256(normalize_text(text).encode("utf-8")).hexdigest()[:16]


def first_tokens(text: str, n: int = 8) -> list[str]:
    toks = re.findall(r"[A-Za-z0-9_./-]+", text.lower())[:n]
    return toks


# ---- question-shape filter --------------------------------------------------

_INTERROGATIVE_RE = re.compile(
    r"^(?:what|why|how|when|where|who|which|is|are|was|were|do|does|did|can|could|would|should|"
    r"will|shall|have|has|had|may|might|must|am|i|you|we|they|he|she|it|there)\b",
    re.IGNORECASE,
)
_IMPERATIVE_QUESTION_RE = re.compile(r"\b(find|show|list|compare|contrast|explain|describe|tell|summari[sz]e|recall|remember|recap|re-?explain|list out|walk me through|what about|how about)\b", re.IGNORECASE)
_QUESTION_MARK_RE = re.compile(r"\?")
_GRAPHIFY_SUBCOMMAND_RE = re.compile(r"\bgraphify\s+(extract|show|merge|diff|export|init|validate)\b", re.IGNORECASE)
_GRAPHIFY_PATH_RE = re.compile(r"graphify[\-/][\w./-]+\.(?:json|md)", re.IGNORECASE)

# Setup / system-prompt shape: starts with a `# ` markdown header and a `<` style
# block, or begins with `task:`, `you are`, or `# AGENTS.md`. These are
# first-turn preambles, not user questions.
_SETUP_HEADER_RE = re.compile(
    r"^\s*(?:#\s*AGENTS\.md|<INSTRUCTIONS>|<permissions instructions>|task\s*[:：]|"
    r"you are\s+(?:a|an|the|pi|codex|a coding assistant)|"
    r"system prompt|##\s*system|context:)",
    re.IGNORECASE,
)
_VERY_SHORT_RE = re.compile(r"^\s*(yes|no|ok|okay|sure|yeah|yep|nope|continue|go|do it|proceed|stop|wait|k thanks|thanks|ty|thx|please|go ahead|alright|alrighty)\s*[.!]?\s*$", re.IGNORECASE)

# Pasted content detection. Many Codex user turns are 1k+ char pastes of
# web pages, transcripts, or directory dumps. These are not questions the
# agent had in their head; they are raw material the agent is reacting to.
# We cap length per category and look for paste-shaped structure.
_PASTE_HEADER_RE = re.compile(r"^(?:#\s+\S|\*\*[A-Z]|\s*```|<!DOCTYPE|<\?xml|---|={3,}|#{20,})", re.MULTILINE)
_LONG_PASTE_LINE_RE = re.compile(r"^.{500,}$", re.MULTILINE)
_MAX_KNOWLEDGE_CHARS = 1800
_MAX_GRAPHIFY_INVOCATION_CHARS = 4000
_MAX_GRAPHIFY_META_CHARS = 1500

# Reactive conversational openers. These are real questions, but they are
# reactions to a prior turn and depend on context the bank cannot carry.
# We keep them in the bank (they are real agent questions) but tag them as
# `conversational` so the benchmark subset can filter them out.
_REACTIVE_OPENER_RE = re.compile(
    r"^\s*(?:"
    r"oh|ah|so\s+you.?re|so\s+it|so\s+we|so\s+at|so\s+concurrency|so\s+that|so\s+basically|"
    r"wait|huh|hmm|hm|jesus|holy|shit|damn|bro|alright|okay|alrighty|"
    r"i\s+see|got\s*cha|gotcha|no[,.]|yes[,.]|yeah|yep|nope|sure|right[,.]|"
    r"that.?s|it.?s|that\s+is|it\s+is|this\s+is|"
    r"you.?re|you\s+are|you\s+know|i\s+mean|i\s+think|i\s+guess|i\s+just|"
    r"literally|honestly|actually|basically|"
    r"well|like|ok[,. ]|k[,. ]"
    r")\b",
    re.IGNORECASE,
)
_REACTIVE_LIKE_RE = re.compile(
    r"\b(we (just|did|ended|were|started)|we literally|we had|"
    r"i (just|did|was|am|need|tested|asked|ended|wanted|started|think|"
    r"already|wanted|got|used|was|had|wrote|ran|saw|made|read|"
    r"mean|guess|believe|suppose)|i literally|i tested|i asked|"
    r"let.?s|let's|tell me about|tell me what|what did|"
    r"remember when|recall when|back when|"
    r"yesterday|today|tonight|earlier|just now|right now|last night)\b",
    re.IGNORECASE,
)
# Questions that look like the canonical MyAPI benchmark shape: a third-party
# noun phrase followed by a verb like "is", "did", "have", or a directive.
_BENCH_INTERROG_RE = re.compile(
    r"^\s*(?:what|which|who|when|where|why|how|find|show|list|summari[sz]e|"
    r"describe|explain|recap|recall|list out|walk me through|compare|contrast)\b",
    re.IGNORECASE,
)
# Strong benchmark signals: a noun phrase followed by a copula or possessive.
_BENCH_NOUN_PHRASE_RE = re.compile(
    r"^\s*(?:the|a|an|my|our)\s+[a-z0-9][\w\s\-./]{2,80}?\s+"
    r"(?:is|are|was|were|did|has|have|had|does|do|can|could|will|would|should|"
    r"of\b|for\b|that\b|which\b|who\b|where\b)\b",
    re.IGNORECASE,
)


def looks_like_question(text: str, category: str) -> bool:
    """Return True if a user message is genuinely a question or query.

    Heuristics are intentionally conservative. Graphify invocations are kept
    even if the surrounding text is terse, because the invocation itself is
    the question the agent had to answer.
    """
    if not text:
        return False
    norm = text.strip()
    if not norm:
        return False
    if _SETUP_HEADER_RE.match(norm):
        return False
    if _VERY_SHORT_RE.match(norm):
        return False
    # Length cap: a real question is rarely longer than a few paragraphs.
    # Anything past the per-category cap is treated as a pasted artifact.
    char_count = len(norm)
    if category == "graphify_invocation":
        if char_count > _MAX_GRAPHIFY_INVOCATION_CHARS:
            return False
    elif category == "graphify_meta":
        if char_count > _MAX_GRAPHIFY_META_CHARS:
            return False
    else:
        if char_count > _MAX_KNOWLEDGE_CHARS:
            return False
    # Reject obvious paste dumps even if they fit the cap: many long lines,
    # a markdown header at the top, or a code-fence header.
    line_count = norm.count("\n") + 1
    if line_count >= 4 and _LONG_PASTE_LINE_RE.search(norm):
        return False
    if line_count >= 6 and _PASTE_HEADER_RE.match(norm):
        return False
    # Graphify invocations: keep only true CLI invocations, not subagent
    # briefings that merely mention the path.
    if category == "graphify_invocation":
        return bool(_GRAPHIFY_SUBCOMMAND_RE.search(norm) or _GRAPHIFY_PATH_RE.search(norm))
    # Knowledge / meta: require a question mark, an interrogative lead, or a
    # directive verb pattern (find/show/explain). This excludes the bulk of
    # setup prompts and one-word confirmations.
    word_count = len(norm.split())
    if _QUESTION_MARK_RE.search(norm):
        return word_count >= 2
    if _INTERROGATIVE_RE.match(norm) and word_count >= 3:
        return True
    if _IMPERATIVE_QUESTION_RE.search(norm) and word_count >= 3:
        return True
    return False


def is_benchmark_shape(text: str) -> bool:
    """Return True if a question reads like a self-contained retrieval query.

    Conversational, reactive, and "did you" follow-ups are real questions
    but depend on prior context the bank cannot carry; they are kept in
    the full bank as `conversational` and excluded from the benchmark
    subset.
    """
    norm = text.strip()
    if not norm:
        return False
    # Reactive openers or reactive first-person: out of benchmark subset.
    if _REACTIVE_OPENER_RE.match(norm):
        return False
    if _REACTIVE_LIKE_RE.search(norm):
        return False
    # Benchmark-shaped leads.
    if _BENCH_INTERROG_RE.match(norm):
        return True
    if _BENCH_NOUN_PHRASE_RE.match(norm):
        return True
    # Default: keep graphify invocations and graphify meta out of the
    # benchmark-shape filter (they have their own subsets).
    return False


# ---- categorization ---------------------------------------------------------

_GRAPHIFY_BARE_RE = re.compile(r"\bgraphify\b", re.IGNORECASE)


def categorize(text: str) -> str:
    """Return one of: knowledge | graphify_invocation | graphify_meta.

    Invocations are direct calls (CLI path / subcommand). Meta-queries ask
    about graphify itself without invoking it. Everything else is a
    knowledge question.
    """
    if not text:
        return "knowledge"
    if _GRAPHIFY_SUBCOMMAND_RE.search(text) or _GRAPHIFY_PATH_RE.search(text):
        return "graphify_invocation"
    if _GRAPHIFY_BARE_RE.search(text):
        # Only treat as meta if the question is about graphify itself, not
        # work that happens to mention it. Look for interrogatives, or the
        # token immediately surrounding the mention.
        window = 80
        for m in _GRAPHIFY_BARE_RE.finditer(text):
            ctx = text[max(0, m.start() - window) : m.end() + window].lower()
            if any(q in ctx for q in ("what is graphify", "how does graphify", "graphify status", "graphify work", "explain graphify", "graphify output", "graphify report", "graphify schema")):
                return "graphify_meta"
        return "knowledge"
    return "knowledge"



# ---- extraction -------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class StoreSpec:
    host: str               # "mini" | "air" | "local"
    store: str              # "codex_sessions" | "pi_agent_sessions"
    path: Path              # local path (after ssh expansion if needed)
    host_label: str = ""    # pretty label for receipts


def _read_user_messages(path: Path, store: str) -> Iterator[tuple[int, str, str]]:
    """Yield (line_index, timestamp, text) for each user message in a session file."""
    with path.open("r", encoding="utf-8", errors="replace") as fp:
        for idx, raw in enumerate(fp):
            raw = raw.strip()
            if not raw:
                continue
            try:
                d = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if store == "codex_sessions":
                if d.get("type") != "response_item":
                    continue
                payload = d.get("payload") or {}
                if payload.get("role") != "user":
                    continue
                content = payload.get("content") or []
                if not isinstance(content, list):
                    continue
                text = ""
                for item in content:
                    if isinstance(item, dict) and item.get("type") in ("input_text", "text"):
                        text = item.get("text") or ""
                        break
            else:
                if d.get("type") != "message":
                    continue
                msg = d.get("message") or {}
                if msg.get("role") != "user":
                    continue
                content = msg.get("content")
                text = ""
                if isinstance(content, str):
                    text = content
                elif isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict) and item.get("type") in ("text", "input_text"):
                            text = item.get("text") or ""
                            break
            if not text or not text.strip():
                continue
            yield idx, d.get("timestamp") or "", text


def iter_store(spec: StoreSpec) -> Iterator[tuple[str, str, str, int, str, int, str]]:
    """Yield (host, store, session_path, line_idx, timestamp, char_count, text)."""
    if not spec.path.exists():
        return
    for path in sorted(spec.path.rglob("*.jsonl")):
        if not path.is_file():
            continue
        # Subagent traces are included; they are real Pi sessions.
        try:
            for line_idx, ts, text in _read_user_messages(path, spec.store):
                yield spec.host, spec.store, str(path), line_idx, ts, len(text), text
        except OSError:
            continue


# ---- ssh fan-out ------------------------------------------------------------


def ssh_list_jsonl(host_alias: str, remote_root: str) -> list[str]:
    """Return absolute paths to *.jsonl under remote_root via ssh."""
    cmd = [
        "ssh",
        "-o", "BatchMode=yes",
        host_alias,
        f"find {remote_root} -type f -name '*.jsonl' 2>/dev/null",
    ]
    try:
        out = subprocess.check_output(cmd, text=True, timeout=300)
    except subprocess.CalledProcessError:
        return []
    return [line.strip() for line in out.splitlines() if line.strip()]


def ssh_read_text(host_alias: str, remote_path: str) -> str:
    cmd = [
        "ssh",
        "-o", "BatchMode=yes",
        host_alias,
        f"cat -- {remote_path}",
    ]
    try:
        return subprocess.check_output(cmd, text=True, timeout=120)
    except subprocess.CalledProcessError:
        return ""


# ---- bank assembly ----------------------------------------------------------


def collect_questions(
    local_specs: list[StoreSpec],
    remote_specs: list[tuple[str, str, str]],  # (host_alias, host, store_root)
) -> tuple[list[dict], dict, dict, dict]:
    """Walk every store, extract user messages, and assemble dedup'd bank.

    Returns (questions, raw_stats, session_counts, per_host_session_counts)
    where questions is a list of bank records, raw_stats is a per-store
    extraction counter, session_counts is a per-store session-file counter,
    and per_host_session_counts aggregates session files by host.
    """
    raw_stats: Counter = Counter()
    session_counts: Counter = Counter()
    per_host_session_counts: Counter = Counter()
    by_key: dict[str, dict] = {}

    def register(host: str, store: str, path: str, line_idx: int, ts: str, text: str) -> None:
        raw_stats[(host, store)] += 1
        _register(by_key, host, store, path, line_idx, ts, text)

    def count_session(host: str, store: str, path: str) -> None:
        session_counts[(host, store)] += 1
        per_host_session_counts[host] += 1

    # local stores
    for spec in local_specs:
        for path in sorted(spec.path.rglob("*.jsonl")):
            if not path.is_file():
                continue
            count_session(spec.host, spec.store, path)
        for host, store, path, line_idx, ts, _cc, text in iter_store(spec):
            register(host, store, path, line_idx, ts, text)

    # remote stores (ssh) — read file once, then parse in-process
    for alias, host, store_root in remote_specs:
        paths = ssh_list_jsonl(alias, store_root)
        for rp in paths:
            store = "codex_sessions" if "/.codex/" in rp else "pi_agent_sessions"
            count_session(host, store, rp)
            txt = ssh_read_text(alias, rp)
            if not txt:
                continue
            scratch_path = scratch_dir_for(rp)
            scratch_path.write_text(txt)
            for line_idx, ts, text in _read_user_messages(scratch_path, store):
                register(host, store, rp, line_idx, ts, text)

    return (
        list(by_key.values()),
        {f"{h}|{s}": n for (h, s), n in raw_stats.items()},
        {f"{h}|{s}": n for (h, s), n in session_counts.items()},
        {h: n for h, n in per_host_session_counts.items()},
    )


def scratch_dir_for(remote_path: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", remote_path)
    return SCRATCH_DIR / f"{safe}.jsonl"


def _register(
    by_key: dict[str, dict],
    host: str,
    store: str,
    session_path: str,
    line_idx: int,
    timestamp: str,
    text: str,
) -> None:
    norm = normalize_text(text)
    if not norm:
        return
    key = norm_key(text)
    cat = categorize(text)
    if not looks_like_question(text, cat):
        return
    occ = {
        "host": host,
        "store": store,
        "session_path": session_path,
        "line_index": line_idx,
        "timestamp": timestamp,
        "text_fingerprint": text_fingerprint(text),
        "char_count": len(text),
    }
    if key in by_key:
        by_key[key]["occurrences"].append(occ)
        return
    # Determine shape: benchmark-shape (self-contained retrieval query) vs
    # conversational (reactive follow-up that depends on prior turn).
    if cat in ("graphify_invocation", "graphify_meta"):
        # Direct CLI invocations and explicit graphify meta-queries are
        # always self-contained.
        shape = "benchmark"
    elif cat == "knowledge":
        shape = "benchmark" if is_benchmark_shape(text) else "conversational"
    else:
        shape = "conversational"
    by_key[key] = {
        "key": key,
        "category": cat,
        "shape": shape,
        "char_count": len(text),
        "token_count_est": max(1, len(norm.split())),
        "text_fingerprint": text_fingerprint(text),
        "text": text,  # kept in-process only; never written to the tracked manifest
        "occurrences": [occ],
    }


# ---- output -----------------------------------------------------------------


def render_receipt(
    bank: list[dict],
    raw_stats: dict,
    session_counts: dict,
    host_session_counts: dict,
    hosts_scanned: list[str],
    stores_scanned: list[tuple[str, str]],
    generated_at: str,
    extra_notes: list[str] | None = None,
) -> str:
    by_cat: Counter = Counter(q["category"] for q in bank)
    by_shape: Counter = Counter(q.get("shape", "conversational") for q in bank)
    by_bench_cat: Counter = Counter(
        (q["category"], q.get("shape", "conversational")) for q in bank
    )
    by_store: Counter = Counter()
    for q in bank:
        for occ in q["occurrences"]:
            by_store[(occ["host"], occ["store"])] += 1
    by_host: Counter = Counter(occ["host"] for q in bank for occ in q["occurrences"])

    lines: list[str] = []
    lines.append("# Question Bank Receipt")
    lines.append("")
    lines.append(f"- Schema version: `{SCHEMA_VERSION}`")
    lines.append(f"- Bank version: `{BANK_VERSION}`")
    lines.append(f"- Generated: `{generated_at}`")
    lines.append(f"- Hosts scanned: {', '.join(hosts_scanned)}")
    lines.append("")
    lines.append("## Session coverage")
    lines.append("")
    lines.append("| Host | Store | Session files |")
    lines.append("| --- | --- | ---: |")
    for k, n in sorted(session_counts.items()):
        host, store = k.split("|", 1)
        lines.append(f"| {host} | {store} | {n} |")
    lines.append("")
    lines.append("| Host | Total session files |")
    lines.append("| --- | ---: |")
    for host, n in sorted(host_session_counts.items()):
        lines.append(f"| {host} | {n} |")
    lines.append("")
    lines.append("## Per-store extraction (raw user messages)")
    lines.append("")
    lines.append("| Host | Store | Raw user messages |")
    lines.append("| --- | --- | ---: |")
    for k, n in sorted(raw_stats.items()):
        host, store = k.split("|", 1)
        lines.append(f"| {host} | {store} | {n} |")
    lines.append("")
    lines.append("## Bank size after dedup")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("| --- | ---: |")
    lines.append(f"| Unique questions (after normalization dedup) | {len(bank)} |")
    lines.append(f"| Total question occurrences across all sessions | {sum(len(q['occurrences']) for q in bank)} |")
    lines.append("")
    lines.append("## Category breakdown")
    lines.append("")
    lines.append("| Category | Unique |")
    lines.append("| --- | ---: |")
    for cat, n in sorted(by_cat.items()):
        lines.append(f"| {cat} | {n} |")
    lines.append("")
    lines.append("## Shape breakdown (per category)")
    lines.append("")
    lines.append("| Category | Shape | Unique |")
    lines.append("| --- | --- | ---: |")
    for (cat, shape), n in sorted(by_bench_cat.items()):
        lines.append(f"| {cat} | {shape} | {n} |")
    lines.append("")
    bench_count = sum(n for shape, n in by_shape.items() if shape == "benchmark")
    conv_count = sum(n for shape, n in by_shape.items() if shape == "conversational")
    lines.append(f"**Benchmark-shape subset** (self-contained retrieval queries, "
                 f"suitable for `capture-live-vertex-baseline` and "
                 f"`prove-myapi-context-retrieval`): **{bench_count}** questions. "
                 f"Conversational follow-ups (real agent questions but "
                 f"context-dependent) add another **{conv_count}** for a total "
                 f"bank of **{len(bank)}**.")
    lines.append("")
    lines.append("## Per-host occurrence counts (post-dedup)")
    lines.append("")
    lines.append("| Host | Occurrences |")
    lines.append("| --- | ---: |")
    for host, n in sorted(by_host.items()):
        lines.append(f"| {host} | {n} |")
    lines.append("")
    lines.append("## Per-store occurrence counts (post-dedup)")
    lines.append("")
    lines.append("| Host | Store | Occurrences |")
    lines.append("| --- | --- | ---: |")
    for (host, store), n in sorted(by_store.items()):
        lines.append(f"| {host} | {store} | {n} |")
    lines.append("")
    if extra_notes:
        lines.append("## Notes")
        lines.append("")
        for note in extra_notes:
            lines.append(f"- {note}")
        lines.append("")
    lines.append("## Provenance")
    lines.append("")
    lines.append("Every bank entry in the JSONL records `host`, `store`, "
                 "`session_path`, `line_index`, `timestamp`, `text_fingerprint`, "
                 "`char_count`, `token_count_est`, `category`, and `shape`. The "
                 "tracked manifest carries the same fields except `text` and any "
                 "verbatim fragments: it is a fingerprint-and-provenance index. "
                 "Categories: `knowledge`, `graphify_invocation`, `graphify_meta`. "
                 "Shapes: `benchmark` (self-contained retrieval query) or "
                 "`conversational` (reactive follow-up depending on prior turn).")
    lines.append("")
    return "\n".join(lines)


def write_questions_jsonl(bank: list[dict], path: Path) -> None:
    """Write the full text-bearing bank to a gitignored JSONL file.

    The tracked manifest contains only fingerprints and tokens; the JSONL is
    the only artifact that carries the original question text. It lives
    outside tracked files so that downstream nodes (capture-live-vertex-
    baseline, prove-myapi-context-retrieval) can load real queries without
    the repo absorbing raw transcript content.
    """
    with path.open("w", encoding="utf-8") as fp:
        for q in bank:
            fp.write(json.dumps(q, ensure_ascii=False))
            fp.write("\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out-dir", default=str(REPO_ROOT / "evals" / "question-bank"))
    ap.add_argument("--mini-root", default="/Users/sab-mini")
    ap.add_argument("--air-alias", default="sab-air")
    ap.add_argument("--air-root", default="/Users/sab-mini")
    ap.add_argument("--include-air", action="store_true", default=True)
    ap.add_argument("--no-air", dest="include_air", action="store_false")
    ap.add_argument("--scratch-dir", default=None,
                    help="Directory for intermediate extracts (defaults to <out-dir>/_scratch).")
    args = ap.parse_args(argv)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    scratch = Path(args.scratch_dir) if args.scratch_dir else out_dir / "_scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    # Make the module-level scratch dir point at the chosen location so the
    # remote-extraction helper can write per-file blobs there.
    global SCRATCH_DIR
    SCRATCH_DIR = scratch

    mini_root = Path(args.mini_root)
    air_root = Path(args.air_root)

    local_specs = [
        StoreSpec("mini", "codex_sessions", mini_root / ".codex" / "sessions"),
        StoreSpec("mini", "pi_agent_sessions", mini_root / ".pi" / "agent" / "sessions"),
    ]

    remote_specs: list[tuple[str, str, str]] = []
    if args.include_air:
        remote_specs = [
            (args.air_alias, "air", f"{air_root}/.codex/sessions"),
            (args.air_alias, "air", f"{air_root}/.pi/agent/sessions"),
        ]

    bank, raw_stats, session_counts, host_session_counts = collect_questions(local_specs, remote_specs)

    # Sort: by category, then char_count desc, then key.
    cat_order = {"graphify_invocation": 0, "graphify_meta": 1, "knowledge": 2}
    bank.sort(key=lambda q: (cat_order.get(q["category"], 9), -q["char_count"], q["key"]))

    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "bank_version": BANK_VERSION,
        "generated_at": generated_at,
        "generator": "scripts/mine_agent_query_bank.py",
        "hosts_scanned": ["mini"] + (["air"] if args.include_air else []),
        "stores_scanned": [
            {"host": "mini", "store": "codex_sessions", "path": str(mini_root / ".codex" / "sessions")},
            {"host": "mini", "store": "pi_agent_sessions", "path": str(mini_root / ".pi" / "agent" / "sessions")},
        ] + (
            [
                {"host": "air", "store": "codex_sessions", "path": f"{air_root}/.codex/sessions"},
                {"host": "air", "store": "pi_agent_sessions", "path": f"{air_root}/.pi/agent/sessions"},
            ]
            if args.include_air else []
        ),
        "raw_extraction_counts": raw_stats,
        "session_counts": session_counts,
        "per_host_session_counts": host_session_counts,
        "unique_question_count": len(bank),
        "category_counts": dict(Counter(q["category"] for q in bank)),
        "shape_counts": dict(Counter(q.get("shape", "conversational") for q in bank)),
    }

    # Per-store occurrence counts (post-dedup).
    store_occ = Counter()
    for q in bank:
        for occ in q["occurrences"]:
            store_occ[(occ["host"], occ["store"])] += 1
    manifest["per_store_occurrence_counts"] = {
        f"{h}|{s}": n for (h, s), n in sorted(store_occ.items())
    }

    manifest_path = out_dir / "question-bank-manifest.json"
    questions_path = out_dir / "questions.jsonl"
    write_questions_jsonl(bank, questions_path)
    # Strip private fields from each bank record before writing the tracked
    # manifest. Tracked fields: key, category, shape, char_count,
    # token_count_est, text_fingerprint, occurrences. Private fields
    # (text, first_tokens) stay only in the gitignored JSONL.
    TRACKED_QUESTION_KEYS = (
        "key", "category", "shape", "char_count", "token_count_est",
        "text_fingerprint", "occurrences",
    )
    redacted = [
        {k_: v for k_, v in q.items() if k_ in TRACKED_QUESTION_KEYS}
        for q in bank
    ]
    manifest["questions"] = redacted
    manifest["questions_path"] = str(questions_path.relative_to(REPO_ROOT))
    manifest["questions_path_is_tracked"] = False
    manifest["questions_count_in_jsonl"] = len(bank)
    manifest["tracked_question_fields"] = list(TRACKED_QUESTION_KEYS)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

    receipt_path = out_dir / "benchmark-receipt.md"
    receipt_path.write_text(render_receipt(
        bank=bank,
        raw_stats=raw_stats,
        session_counts=session_counts,
        host_session_counts=host_session_counts,
        hosts_scanned=manifest["hosts_scanned"],
        stores_scanned=[(s["host"], s["store"]) for s in manifest["stores_scanned"]],
        generated_at=generated_at,
    ))

    print(f"manifest -> {manifest_path}")
    print(f"receipt  -> {receipt_path}")
    print(f"unique questions: {len(bank)}")
    print(f"raw extraction:   {sum(raw_stats.values())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
