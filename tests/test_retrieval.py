"""Tests for the smart retrieval pipeline."""

import pytest
from context_refinery.retrieval import (
    KeywordSearcher,
    MetadataParser,
    QueryClassifier,
    ResultFilter,
    ResultReranker,
    ResultGrouper,
    RetrievalPipeline,
)


# ── MetadataParser ───────────────────────────────────────────────────────────

SAMPLE_ENTRY = """---
id: abc-123
title: Test Document
source: chatgpt
created_at: "2026-04-10T12:00:00+00:00"
author: Me
status: scratchpad
doc_type: conversation
tags:
- python
- api
projects:
- context-refinery
---

This is the body text of the document."""


def test_parse_valid_frontmatter():
    meta, body, snippet = MetadataParser.parse(SAMPLE_ENTRY)
    assert meta["title"] == "Test Document"
    assert meta["source"] == "chatgpt"
    assert meta["tags"] == ["python", "api"]
    assert meta["projects"] == ["context-refinery"]
    assert "body text" in body
    assert "body text" in snippet


def test_parse_missing_frontmatter():
    meta, body, snippet = MetadataParser.parse("Just plain text without frontmatter.")
    assert meta["title"] == "untitled"
    assert meta["source"] == "unknown"
    assert body == "Just plain text without frontmatter."
    assert "plain text" in snippet


def test_parse_malformed_yaml():
    entry = "---\n!!python/object: __main__.Exploit\n---\nBody here."
    meta, body, snippet = MetadataParser.parse(entry)
    # safe_load rejects dangerous tags — returns empty metadata
    assert meta.get("title") == "untitled"
    assert meta.get("source") == "unknown"
    assert "Body here" in body


def test_parse_empty_entry():
    meta, body, snippet = MetadataParser.parse("")
    assert meta["title"] == "untitled"
    assert meta["source"] == "unknown"
    assert body == ""
    assert snippet == ""


def test_parse_empty_entry_infers_source_from_filename():
    meta, body, snippet = MetadataParser.parse("", filename="chatgpt-empty.md")
    assert meta["title"] == "untitled"
    assert meta["source"] == "chatgpt"
    assert body == ""
    assert snippet == ""


def test_parse_defaults_unknown_source_and_filename_title():
    entry = """my-note.md\n---\ntitle:\nsource:\ncreated_at: '2026-04-10T12:00:00+00:00'\n---\n\nBody text."""
    meta, body, snippet = MetadataParser.parse(entry)
    assert meta["source"] == "unknown"
    assert meta["title"] == "my-note.md"
    assert "Body text" in body


@pytest.mark.parametrize(
    "filename,expected_source",
    [
        ("obsidian-note.md", "obsidian"),
        ("chatgpt-note.md", "chatgpt"),
        ("claude-web-note.md", "claude"),
        ("claude-note.md", "claude-code"),
        ("codex-note.md", "codex"),
        ("other-note.md", "unknown"),
    ],
)
def test_parse_infers_source_from_filename_prefix(filename, expected_source):
    entry = """---\ntitle: Sample Note\ncreated_at: '2026-04-10T12:00:00+00:00'\n---\n\nBody text."""
    meta, _, _ = MetadataParser.parse(entry, filename=filename)
    assert meta["source"] == expected_source


def test_parse_infers_source_when_frontmatter_missing_source():
    entry = """---\ntitle: Sample Note\nsource:\ncreated_at: '2026-04-10T12:00:00+00:00'\n---\n\nBody text."""
    meta, _, _ = MetadataParser.parse(entry, filename="claude-web-example.md")
    assert meta["source"] == "claude"


def _write_note(root, relpath, frontmatter, body):
    path = root / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{frontmatter}\n---\n\n{body}\n", encoding="utf-8")
    return path


def test_keyword_exact_phrase(tmp_path):
    notes_dir = tmp_path / "notes"
    _write_note(
        notes_dir,
        "goldmine-note.md",
        "title: Goldmine Note\nsource: obsidian",
        "This note mentions goldmine exactly once.",
    )
    _write_note(
        notes_dir,
        "other-note.md",
        "title: Other Note\nsource: obsidian",
        "This note is about mining but not the keyword.",
    )

    results = KeywordSearcher(notes_dir=str(notes_dir)).search('"goldmine"', n=10)
    assert len(results) == 1
    assert results[0]["file"].endswith("goldmine-note.md")
    assert results[0]["keyword_match"] is True


def test_keyword_multi_term(tmp_path):
    notes_dir = tmp_path / "notes"
    _write_note(
        notes_dir,
        "match-note.md",
        "title: Match Note\nsource: obsidian",
        "openclaw harness leak happened here",
    )
    _write_note(
        notes_dir,
        "partial-note.md",
        "title: Partial Note\nsource: obsidian",
        "openclaw harness only",
    )

    results = KeywordSearcher(notes_dir=str(notes_dir)).search("openclaw harness leak", n=10)
    assert len(results) == 1
    assert results[0]["file"].endswith("match-note.md")


# ── QueryClassifier ──────────────────────────────────────────────────────────

def test_classify_temporal():
    intent, mode, conf, hint = QueryClassifier().classify("what did I work on last week?")
    assert intent == "temporal"
    assert mode == "timeline"
    assert hint is not None


def test_classify_temporal_yesterday():
    intent, _, _, hint = QueryClassifier().classify("what happened yesterday?")
    assert intent == "temporal"
    assert "yesterday" in hint.lower()


def test_classify_temporal_around_the_time():
    intent, mode, _, _ = QueryClassifier().classify(
        "What was I doing around the time I was debugging Tailscale?"
    )
    assert intent == "temporal"
    assert mode == "timeline"


def test_classify_factual():
    intent, mode, _, _ = QueryClassifier().classify("how does the auth flow work?")
    assert intent == "factual"
    assert mode == "lookup"


def test_classify_project_overview():
    intent, mode, _, _ = QueryClassifier().classify("What is My_DevInfra?")
    assert intent == "project_overview"
    assert mode == "dossier"


def test_classify_cross_source():
    intent, mode, _, _ = QueryClassifier().classify("what did chatgpt and claude say about deployment?")
    assert intent == "cross_source"
    assert mode == "summary"


def test_classify_source_specific():
    intent, mode, _, _ = QueryClassifier().classify(
        "Find the Claude Code session where I set up the web adapter."
    )
    assert intent == "source_specific"
    assert mode == "lookup"


def test_classify_operational():
    intent, mode, _, _ = QueryClassifier().classify("What is the status of the API deployment?")
    assert intent == "operational"
    assert mode == "summary"


def test_classify_decision():
    intent, mode, _, _ = QueryClassifier().classify("What did I decide about the vault schema?")
    assert intent == "decision"
    assert mode == "summary"


def test_classify_meta():
    intent, mode, _, _ = QueryClassifier().classify(
        "Which notes discuss tagging strategy and taxonomy?"
    )
    assert intent == "meta"
    assert mode == "summary"


def test_classify_synthesis():
    intent, mode, _, _ = QueryClassifier().classify(
        "What docs should I use to understand the current system end to end?"
    )
    assert intent == "synthesis"
    assert mode == "summary"


def test_classify_pattern():
    intent, mode, _, _ = QueryClassifier().classify("what recurring patterns show up in my notes?")
    assert intent == "pattern"
    assert mode == "coach"


def test_classify_ambiguous_defaults_to_factual():
    intent, mode, conf, _ = QueryClassifier().classify("hello")
    assert intent == "factual"
    assert conf == 0.50


# ── ResultFilter ─────────────────────────────────────────────────────────────

def _make_result(source="chatgpt", tags=None, projects=None, created_at=None):
    return {
        "metadata": {
            "source": source,
            "tags": tags or [],
            "projects": projects or [],
            "created_at": created_at,
        },
        "khoj_score": 0.3,
    }


def test_filter_by_source():
    results = [_make_result("chatgpt"), _make_result("codex"), _make_result("claude")]
    filtered = ResultFilter.apply(results, sources=["codex"])
    assert len(filtered) == 1
    assert filtered[0]["metadata"]["source"] == "codex"


def test_filter_by_tags_or():
    results = [
        _make_result(tags=["python", "api"]),
        _make_result(tags=["react"]),
        _make_result(tags=["python"]),
    ]
    filtered = ResultFilter.apply(results, tags=["python"])
    assert len(filtered) == 2


def test_filter_by_date_range():
    results = [
        _make_result(created_at="2026-04-01T00:00:00+00:00"),
        _make_result(created_at="2026-04-10T00:00:00+00:00"),
        _make_result(created_at="2026-03-01T00:00:00+00:00"),
    ]
    filtered = ResultFilter.apply(results, date_from="2026-04-01")
    assert len(filtered) == 2


def test_filter_combined():
    results = [
        _make_result("chatgpt", tags=["python"], created_at="2026-04-10T00:00:00+00:00"),
        _make_result("codex", tags=["python"], created_at="2026-04-10T00:00:00+00:00"),
        _make_result("chatgpt", tags=["react"], created_at="2026-04-10T00:00:00+00:00"),
    ]
    filtered = ResultFilter.apply(results, sources=["chatgpt"], tags=["python"])
    assert len(filtered) == 1


def test_filter_missing_metadata_passes():
    results = [{"metadata": {}, "khoj_score": 0.3}]
    filtered = ResultFilter.apply(results, sources=["chatgpt"])
    assert len(filtered) == 0  # source doesn't match empty string

    filtered = ResultFilter.apply(results, date_from="2026-01-01")
    assert len(filtered) == 1  # no created_at → passes date filter


# ── ResultReranker ───────────────────────────────────────────────────────────

def test_rerank_preserves_all_results():
    results = [
        _make_result(created_at="2026-04-10T00:00:00+00:00"),
        _make_result(created_at="2026-04-05T00:00:00+00:00"),
    ]
    for r in results:
        r["khoj_score"] = 0.3
    reranked = ResultReranker().rerank(results, intent="factual")
    assert len(reranked) == 2
    assert all("final_score" in r for r in reranked)


def test_rerank_temporal_boosts_recent():
    recent = _make_result(created_at="2026-04-12T00:00:00+00:00")
    recent["khoj_score"] = 0.5
    old = _make_result(created_at="2025-01-01T00:00:00+00:00")
    old["khoj_score"] = 0.3  # old has better semantic score

    reranked = ResultReranker().rerank([old, recent], intent="temporal")
    # Recent should rank higher despite worse semantic score
    assert reranked[0]["metadata"]["created_at"] == "2026-04-12T00:00:00+00:00"


def test_rerank_trust_score():
    reranker = ResultReranker()
    assert reranker._trust_score("mature") == 1.0
    assert reranker._trust_score("deprecated") == 0.1
    assert reranker._trust_score("unknown") == 0.5


def test_rerank_keyword_boost_ranking():
    reranker = ResultReranker()
    keyword = _make_result(created_at="2026-04-10T00:00:00+00:00")
    keyword["khoj_score"] = 0.0
    keyword["keyword_match"] = True
    semantic = _make_result(created_at="2026-04-10T00:00:00+00:00")
    semantic["khoj_score"] = 0.45

    reranked = reranker.rerank([semantic, keyword], intent="factual")
    assert reranked[0].get("keyword_match") is True


def test_rerank_source_family_boost_ranking():
    reranker = ResultReranker()
    general = _make_result(source="chatgpt")
    general["khoj_score"] = 0.0
    source_specific = _make_result(source="claude-code")
    source_specific["khoj_score"] = 0.45

    reranked = reranker.rerank(
        [general, source_specific],
        intent="source_specific",
        query="Find the Claude Code session where I set up the web adapter.",
    )
    assert reranked[0]["metadata"]["source"] == "claude-code"


# ── ResultGrouper ────────────────────────────────────────────────────────────

def test_group_by_source():
    results = [
        _make_result("chatgpt"),
        _make_result("codex"),
        _make_result("chatgpt"),
    ]
    groups = ResultGrouper.group(results, intent="factual")
    assert len(groups) == 2
    keys = {g["key"] for g in groups}
    assert "chatgpt" in keys
    assert "codex" in keys


def test_group_by_source_defaults_unknown():
    results = [
        _make_result(None),
        _make_result("chatgpt"),
    ]
    groups = ResultGrouper.group(results, intent="factual")
    keys = {g["key"] for g in groups}
    assert "unknown" in keys
    assert "chatgpt" in keys


# ── RetrievalPipeline (mocked Khoj) ─────────────────────────────────────────

class MockKhojClient:
    def search(self, query, n=10, max_distance=None):
        return [
            {
                "entry": SAMPLE_ENTRY,
                "score": 0.25,
                "additional": {"file": "chatgpt-test-doc.md", "source": "computer"},
                "corpus-id": "mock-1",
            },
            {
                "entry": "---\ntitle: Codex Session\nsource: codex\ncreated_at: '2026-04-08T10:00:00+00:00'\nstatus: scratchpad\ndoc_type: conversation\ntags: [devops]\nprojects: []\n---\n\nCodex session content here.",
                "score": 0.40,
                "additional": {"file": "codex-session.md", "source": "computer"},
                "corpus-id": "mock-2",
            },
        ]


class HybridMockKhojClient:
    def search(self, query, n=10, max_distance=None):
        return [
            {
                "entry": """---\ntitle: Semantic Mining Note\nsource: obsidian\ncreated_at: '2026-04-09T10:00:00+00:00'\nstatus: scratchpad\ndoc_type: note\ntags: [bitcoin]\nprojects: []\n---\n\nThis is about bitcoin mining and related concepts.""",
                "score": 0.05,
                "additional": {"file": "semantic-mining.md", "source": "computer"},
                "corpus-id": "mock-semantic",
            },
            {
                "entry": """---\ntitle: Goldmine Note\nsource: obsidian\ncreated_at: '2026-04-09T10:00:00+00:00'\nstatus: scratchpad\ndoc_type: note\ntags: [goldmine]\nprojects: []\n---\n\nThis note contains the exact word goldmine.""",
                "score": 0.45,
                "additional": {"file": "goldmine-note.md", "source": "computer"},
                "corpus-id": "mock-keyword",
            },
        ]


class FilenameOnlyMockKhojClient:
    def search(self, query, n=10, max_distance=None):
        return [
            {
                "entry": """---\ntitle: Missing Source Note\ncreated_at: '2026-04-09T10:00:00+00:00'\nstatus: scratchpad\ndoc_type: note\ntags: [obsidian]\nprojects: []\n---\n\nThis note omits source frontmatter.""",
                "score": 0.2,
                "additional": {"file": "obsidian-missing-source-note.md", "source": "computer"},
                "corpus-id": "mock-filename-only",
            }
        ]


def test_pipeline_full_response():
    pipeline = RetrievalPipeline(khoj_client=MockKhojClient())
    result = pipeline.execute(q="test query", n=5)

    assert result["query"] == "test query"
    assert result["classification"]["intent"] == "factual"
    assert result["total_from_khoj"] == 2
    assert result["total_after_filter"] == 2
    assert len(result["results"]) == 2
    assert result["timing_ms"] > 0

    # Check first result has expected fields
    doc = result["results"][0]
    assert "corpus_id" in doc
    assert "snippet" in doc
    assert "khoj_score" in doc
    assert "final_score" in doc
    assert doc["final_score"] > 0


def test_pipeline_temporal_query():
    pipeline = RetrievalPipeline(khoj_client=MockKhojClient())
    result = pipeline.execute(q="what did I do last week?")
    assert result["classification"]["intent"] == "temporal"
    assert result["classification"]["answer_mode"] == "timeline"


def test_pipeline_with_source_filter():
    pipeline = RetrievalPipeline(khoj_client=MockKhojClient())
    result = pipeline.execute(q="test", sources=["codex"])
    assert result["total_after_filter"] == 1
    assert result["results"][0]["source"] == "codex"


def test_pipeline_infers_source_from_additional_file():
    pipeline = RetrievalPipeline(khoj_client=FilenameOnlyMockKhojClient())
    result = pipeline.execute(q="test")
    assert result["results"][0]["source"] == "obsidian"
    assert result["results"][0]["file"].endswith("obsidian-missing-source-note.md")


def test_pipeline_hybrid_merge_and_keyword_boost(tmp_path):
    notes_dir = tmp_path / "notes"
    _write_note(
        notes_dir,
        "goldmine-note.md",
        "title: Goldmine Note\nsource: obsidian\ncreated_at: '2026-04-09T10:00:00+00:00'\nstatus: scratchpad\ndoc_type: note\ntags: [goldmine]\nprojects: []",
        "This note contains the exact word goldmine.",
    )

    pipeline = RetrievalPipeline(khoj_client=HybridMockKhojClient())
    pipeline.keyword_searcher = KeywordSearcher(notes_dir=str(notes_dir))
    result = pipeline.execute(q="goldmine", n=5)

    assert result["total_from_khoj"] == 2
    assert len(result["results"]) == 2
    assert result["results"][0]["file"].endswith("goldmine-note.md")
    assert result["results"][0]["final_score"] >= result["results"][1]["final_score"]
