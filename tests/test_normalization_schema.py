"""Tests for context_refinery.normalization_schema."""

from __future__ import annotations

import pytest

from context_refinery.normalization_schema import (
    SOURCE_TYPES,
    TEMPORAL_MODES,
    V1Stamp,
    infer_primary_project,
    infer_source_type,
    infer_temporal_mode,
    merge_v1_into_frontmatter,
    stamp_from_path,
)


class TestInferSourceType:
    @pytest.mark.parametrize("path,expected", [
        ("project-docs/source-of-truth-anchors/myapi-status-anchor.md", "anchor"),
        ("handoffs/004-corpus-v1-field-test-realization.md", "handoff"),
        ("01 Projects/MyAPI/notes.md", "project_doc"),
        ("02 Areas/Health/sleep.md", "project_doc"),
        ("03 Resources/Books/grokking.md", "reference"),
        ("04 Periodic/2026-05-14.md", "daily_note"),
        ("00 Inbox/random-thought.md", "note"),
        ("05 Archive/old-thing.md", "note"),
        ("Templates/daily.md", "config"),
        ("project-docs/STATUS_AND_NEXT_STEPS.md", "project_doc"),
        ("some/random/file.md", "note"),
    ])
    def test_path_inference(self, path, expected):
        assert infer_source_type(path) == expected

    @pytest.mark.parametrize("adapter,expected", [
        ("chatgpt", "conversation"),
        ("claude_web", "conversation"),
        ("claude_code", "cli_session"),
        ("codex", "cli_session"),
    ])
    def test_adapter_wins(self, adapter, expected):
        # Even with a path that would otherwise infer as anchor, the adapter
        # decides for conversation/CLI sources.
        assert infer_source_type(
            "source-of-truth-anchors/x.md", adapter=adapter
        ) == expected

    def test_obsidian_adapter_falls_through_to_path(self):
        assert infer_source_type(
            "handoffs/000-x.md", adapter="obsidian"
        ) == "handoff"

    def test_daily_filename_pattern(self):
        assert infer_source_type("some/random/2026-04-18.md") == "daily_note"
        assert infer_source_type("any/4.18.26.daily.project.md") == "daily_note"

    def test_returned_value_is_in_vocab(self):
        for path in ["a/b.md", "handoffs/x.md", "Templates/y.md"]:
            assert infer_source_type(path) in SOURCE_TYPES


class TestInferTemporalMode:
    @pytest.mark.parametrize("source_type,expected", [
        ("conversation", "episodic"),
        ("cli_session", "episodic"),
        ("daily_note", "episodic"),
        ("anchor", "meta"),
        ("project_doc", "meta"),
        ("handoff", "meta"),
        ("note", "meta"),
    ])
    def test_modes(self, source_type, expected):
        assert infer_temporal_mode(source_type) == expected
        assert infer_temporal_mode(source_type) in TEMPORAL_MODES


class TestInferPrimaryProject:
    @pytest.mark.parametrize("path,expected", [
        ("01 Projects/MyAPI/x.md", "myapi"),
        ("context_refinery/retrieval.py", "myapi"),
        ("01 Projects/GDDP/spec.md", "gddp"),
        ("notes/graph-driven-thinking.md", "gddp"),
        ("openclaw/dispatch.md", "openclaw"),
        ("01 Projects/devinfra/tailscale.md", "devinfra"),
        ("Templates/daily.md", "vault"),  # path contains 'vault'? no — falls through
        ("00 Inbox/random.md", "unknown"),
    ])
    def test_inference(self, path, expected):
        # The 'Templates/daily.md' case will be 'unknown', not 'vault'.
        result = infer_primary_project(path)
        if path == "Templates/daily.md":
            assert result == "unknown"
        else:
            assert result == expected


class TestStampFromPath:
    def test_obsidian_anchor(self):
        stamp = stamp_from_path(
            "project-docs/source-of-truth-anchors/myapi-status-anchor.md",
            adapter="obsidian",
        )
        assert stamp.source_type == "anchor"
        assert stamp.temporal_mode == "meta"
        assert stamp.primary_project == "myapi"
        assert stamp.review_status == "inferred"

    def test_chatgpt_conversation(self):
        stamp = stamp_from_path(
            "exports/chatgpt/some-thread.json",
            adapter="chatgpt",
            title="MyAPI retrieval debugging",
        )
        assert stamp.source_type == "conversation"
        assert stamp.temporal_mode == "episodic"
        assert stamp.primary_project == "myapi"


class TestMergeFrontmatter:
    def test_fills_blanks(self):
        existing = {"title": "x", "tags": ["a"]}
        stamp = V1Stamp(source_type="anchor", temporal_mode="meta",
                       primary_project="myapi")
        merged = merge_v1_into_frontmatter(existing, stamp)
        assert merged["title"] == "x"
        assert merged["tags"] == ["a"]
        assert merged["source_type"] == "anchor"
        assert merged["temporal_mode"] == "meta"
        assert merged["primary_project"] == "myapi"

    def test_existing_value_wins(self):
        existing = {"source_type": "handoff", "primary_project": "gddp"}
        stamp = V1Stamp(source_type="anchor", temporal_mode="meta",
                       primary_project="myapi")
        merged = merge_v1_into_frontmatter(existing, stamp)
        # Operator-curated values are preserved.
        assert merged["source_type"] == "handoff"
        assert merged["primary_project"] == "gddp"
        # But blanks still get filled.
        assert merged["temporal_mode"] == "meta"

    def test_empty_existing(self):
        stamp = V1Stamp(source_type="note", temporal_mode="meta")
        merged = merge_v1_into_frontmatter({}, stamp)
        assert merged["source_type"] == "note"
        assert merged["review_status"] == "inferred"

    def test_conversation_fields_included_when_set(self):
        stamp = V1Stamp(
            source_type="conversation",
            temporal_mode="episodic",
            thread_type="execution",
            signal_strength="high",
            raw_thread_weight="normal",
        )
        merged = merge_v1_into_frontmatter({}, stamp)
        assert merged["thread_type"] == "execution"
        assert merged["signal_strength"] == "high"
        assert merged["raw_thread_weight"] == "normal"
        assert "outcome" not in merged  # left None on stamp
