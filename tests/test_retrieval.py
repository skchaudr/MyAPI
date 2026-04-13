"""Tests for the smart retrieval pipeline."""

import pytest
from context_refinery.retrieval import (
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
    assert meta == {}
    assert body == "Just plain text without frontmatter."
    assert "plain text" in snippet


def test_parse_malformed_yaml():
    entry = "---\n!!python/object: __main__.Exploit\n---\nBody here."
    meta, body, snippet = MetadataParser.parse(entry)
    # safe_load rejects dangerous tags — returns empty metadata
    assert meta.get("title") is None
    assert "Body here" in body


def test_parse_empty_entry():
    meta, body, snippet = MetadataParser.parse("")
    assert meta == {}
    assert body == ""
    assert snippet == ""


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


def test_classify_factual():
    intent, mode, _, _ = QueryClassifier().classify("how does the auth flow work?")
    assert intent == "factual"
    assert mode == "lookup"


def test_classify_project_overview():
    intent, mode, _, _ = QueryClassifier().classify("give me an overview of the BDR project")
    assert intent == "project_overview"
    assert mode == "dossier"


def test_classify_cross_source():
    intent, mode, _, _ = QueryClassifier().classify("what did chatgpt and claude say about deployment?")
    assert intent == "cross_source"
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
