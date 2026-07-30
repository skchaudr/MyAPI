"""Tests for the question-bank miner.

The miner is a read-only extractor; these tests do not require network
access and they do not scan the live session stores. They validate the
filter and dedup logic on synthetic inputs.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "mine_agent_query_bank.py"


def _load_miner():
    spec = importlib.util.spec_from_file_location("mine_agent_query_bank", SCRIPT)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def miner():
    return _load_miner()


# ---- normalization ----------------------------------------------------------


def test_normalize_strips_instructions_block(miner):
    raw = "<INSTRUCTIONS>be terse</INSTRUCTIONS>\n\nwhat is myapi?"
    out = miner.normalize_text(raw)
    assert "<INSTRUCTIONS>" not in out
    assert "be terse" not in out
    assert "what is myapi" in out


def test_normalize_collapses_whitespace_and_folds_case(miner):
    a = miner.normalize_text("  WHAT  is  MyAPI?\n")
    b = miner.normalize_text("what is myapi?")
    assert a == b


def test_norm_key_stable_for_rephrasings(miner):
    a = miner.normalize_text("What is MyAPI?")
    b = miner.normalize_text("what is myapi")
    assert miner.norm_key(a) == miner.norm_key(b)


# ---- categorization ---------------------------------------------------------


def test_categorize_graphify_invocation(miner):
    assert miner.categorize("run graphify extract on the corpus") == "graphify_invocation"
    assert miner.categorize("look at graphify-out/graph.json please") == "graphify_invocation"


def test_categorize_graphify_meta(miner):
    assert miner.categorize("what is graphify and how does it work?") == "graphify_meta"
    assert miner.categorize("explain graphify schema") == "graphify_meta"


def test_categorize_knowledge(miner):
    assert miner.categorize("what is the retrieval system?") == "knowledge"
    assert miner.categorize("I think graphify is fine, let's move on") == "knowledge"


# ---- question-shape filter --------------------------------------------------


def test_setup_prompt_rejected(miner):
    assert not miner.looks_like_question(
        "# AGENTS.md instructions for /tmp\n\n<INSTRUCTIONS>...</INSTRUCTIONS>", "knowledge"
    )


def test_very_short_rejected(miner):
    assert not miner.looks_like_question("yes", "knowledge")
    assert not miner.looks_like_question("ok", "knowledge")


def test_long_knowledge_paste_rejected(miner):
    paste = "header\n" + ("x" * 600 + "\n") * 5
    assert not miner.looks_like_question(paste, "knowledge")


def test_real_question_kept(miner):
    assert miner.looks_like_question("What is the MyAPI retrieval pipeline?", "knowledge")
    assert miner.looks_like_question("find the session where I set up the web adapter", "knowledge")


def test_graphify_invocation_kept(miner):
    assert miner.looks_like_question("please run graphify extract .", "graphify_invocation")


def test_benchmark_shape_self_contained(miner):
    assert miner.is_benchmark_shape("What is the MyAPI retrieval pipeline?")
    assert miner.is_benchmark_shape("Find the session where I set up the web adapter.")


def test_benchmark_shape_reactive_excluded(miner):
    assert not miner.is_benchmark_shape("oh that's interesting. so you're literally doing it that way?")
    assert not miner.is_benchmark_shape("I tested it out, I asked pi to do X")


# ---- bank artifacts ---------------------------------------------------------


BANK_DIR = REPO_ROOT / "evals" / "question-bank"


def test_bank_artifacts_consistent():
    manifest_path = BANK_DIR / "question-bank-manifest.json"
    questions_path = BANK_DIR / "questions.jsonl"
    if not manifest_path.exists() or not questions_path.exists():
        pytest.skip("question-bank artifacts not generated in this worktree")
    manifest = json.loads(manifest_path.read_text())
    # Manifest must not carry raw transcript text or verbatim fragments.
    private_fields = {"text", "first_tokens", "last_tokens"}
    for q in manifest["questions"]:
        leaked = private_fields & set(q.keys())
        assert not leaked, f"manifest leaks private fields {leaked} for key {q.get('key')}"
    # JSONL row count must match manifest claim.
    n_jsonl = sum(1 for _ in questions_path.open())
    assert n_jsonl == manifest["questions_count_in_jsonl"]
    # Every JSONL row must carry the fields downstream consumers need.
    required = {"key", "category", "shape", "text", "occurrences"}
    for line in questions_path.open():
        row = json.loads(line)
        missing = required - set(row.keys())
        assert not missing, f"row {row.get('key')} missing {missing}"
    # Aggregates must add up.
    cats = {}
    for line in questions_path.open():
        row = json.loads(line)
        cats[row["category"]] = cats.get(row["category"], 0) + 1
    assert cats == manifest["category_counts"]
