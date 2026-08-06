"""Tests for scripts.normalize_corpus."""

from __future__ import annotations

import json

from scripts.normalize_corpus import _load_chatgpt_blob, scan_chatgpt


def _write_shard(path, conversations):
    path.write_text(json.dumps(conversations), encoding="utf-8")


def test_scan_chatgpt_accepts_export_shard_directory(tmp_path):
    export_dir = tmp_path / "chatgpt-export"
    export_dir.mkdir()
    _write_shard(
        export_dir / "conversations-000.json",
        [
            {"id": "conv-a", "title": "MyAPI shard one"},
            {"id": "conv-b", "title": "Vault schema"},
        ],
    )
    _write_shard(
        export_dir / "conversations-001.json",
        [{"id": "conv-c", "title": "GDDP follow-up"}],
    )
    (export_dir / "message_feedback.json").write_text("[]", encoding="utf-8")

    entries = list(scan_chatgpt(str(export_dir)))

    assert [entry.extra["conversation_id"] for entry in entries] == [
        "conv-a",
        "conv-b",
        "conv-c",
    ]
    assert {entry.source for entry in entries} == {"chatgpt"}
    assert {entry.source_type for entry in entries} == {"conversation"}


def test_load_chatgpt_blob_accepts_export_shard_directory(tmp_path):
    export_dir = tmp_path / "chatgpt-export"
    export_dir.mkdir()
    _write_shard(export_dir / "conversations-001.json", [{"id": "later"}])
    _write_shard(export_dir / "conversations-000.json", [{"id": "earlier"}])

    conversations = _load_chatgpt_blob(str(export_dir))

    assert [conversation["id"] for conversation in conversations] == [
        "earlier",
        "later",
    ]


def test_copy_cli_session_entry_avoids_duplicate_output_paths(tmp_path, monkeypatch):
    from context_refinery.adapters import codex
    from scripts.normalize_corpus import copy_cli_session_entry

    def fake_parse_codex_session(_src_path):
        return {
            "id": "unknown",
            "title": "Repeated Session Title",
            "source": {"system": "codex"},
            "timestamps": {"created_at": "2026-05-29T00:00:00Z"},
            "author": "codex",
            "tags": [],
            "projects": [],
            "content": {"cleaned_markdown": "# Session"},
        }

    monkeypatch.setattr(codex, "parse_codex_session", fake_parse_codex_session)

    first = {
        "source": "codex",
        "src_path": str(tmp_path / "first"),
        "rel_path": "2026-05-01/session-a",
        "title": "Repeated Session Title",
        "source_type": "cli_session",
        "temporal_mode": "episodic",
        "primary_project": "unknown",
    }
    second = {
        **first,
        "src_path": str(tmp_path / "second"),
        "rel_path": "2026-05-01/session-b",
    }

    first_path = copy_cli_session_entry(first, tmp_path / "corpus")
    second_path = copy_cli_session_entry(second, tmp_path / "corpus")

    assert first_path != second_path
    assert first_path.exists()
    assert second_path.exists()
