from datetime import datetime, timezone
from pathlib import Path
import json
import os
import subprocess
import sys

from scripts.source_manifest import (
    Source,
    build_corpus_manifest,
    build_manifest,
    classify_corpus_tier,
    emit_json,
    manifest_row_for_file,
    sources_from_roots,
    summarize_source,
)


def test_missing_path_returns_zero_count(tmp_path):
    missing = tmp_path / "missing"

    row = summarize_source(Source("missing_family", missing, False))

    assert row == {
        "source_family": "missing_family",
        "path": str(missing),
        "exists": False,
        "file_count": 0,
        "newest_file": None,
        "newest_mtime_iso": None,
        "parser_available": "no",
    }


def test_temp_dir_source_counts_files_and_reports_newest(tmp_path):
    older = tmp_path / "older.md"
    nested = tmp_path / "nested"
    newest = nested / "newest.jsonl"
    nested.mkdir()
    older.write_text("older", encoding="utf-8")
    newest.write_text("newer", encoding="utf-8")

    older_mtime = 1_700_000_000
    newest_mtime = 1_700_000_100
    os.utime(older, (older_mtime, older_mtime))
    os.utime(newest, (newest_mtime, newest_mtime))

    row = summarize_source(Source("temp_source", tmp_path, True))

    assert row["source_family"] == "temp_source"
    assert row["path"] == str(tmp_path)
    assert row["exists"] is True
    assert row["file_count"] == 2
    assert row["newest_file"] == str(newest)
    assert row["newest_mtime_iso"] == datetime.fromtimestamp(
        newest_mtime, timezone.utc
    ).isoformat()
    assert row["parser_available"] == "yes"


def test_build_manifest_accepts_explicit_sources(tmp_path):
    source_file = tmp_path / "source.md"
    source_file.write_text("content", encoding="utf-8")

    rows = build_manifest((Source("single", source_file, True),))

    assert len(rows) == 1
    assert rows[0]["file_count"] == 1
    assert rows[0]["newest_file"] == str(source_file)


def test_classify_corpus_tier_marks_recent_files_hot(tmp_path):
    source_file = tmp_path / "recent.md"
    now = datetime(2026, 7, 2, tzinfo=timezone.utc)
    source_file.write_text("recent", encoding="utf-8")

    decision = classify_corpus_tier(
        source_file,
        source_family="obsidian",
        mtime=datetime(2026, 6, 20, tzinfo=timezone.utc).timestamp(),
        now=now,
    )

    assert decision.tier == "hot"
    assert decision.reason == "mtime_within_30_days"
    assert decision.include_in_active_bundle is True


def test_classify_corpus_tier_marks_handoffs_durable_even_when_old(tmp_path):
    handoffs = tmp_path / ".handoffs"
    handoffs.mkdir()
    source_file = handoffs / "026-cost-aware-mymcp-corpus-tiers.md"
    source_file.write_text("handoff", encoding="utf-8")
    now = datetime(2026, 7, 2, tzinfo=timezone.utc)

    decision = classify_corpus_tier(
        source_file,
        source_family="repo",
        mtime=datetime(2025, 1, 1, tzinfo=timezone.utc).timestamp(),
        now=now,
    )

    assert decision.tier == "durable"
    assert decision.reason == "durable_source_type:handoff"
    assert decision.include_in_active_bundle is True


def test_classify_corpus_tier_marks_old_baseline_cold(tmp_path):
    source_file = tmp_path / "baseline.md"
    source_file.write_text("old", encoding="utf-8")
    now = datetime(2026, 7, 2, tzinfo=timezone.utc)

    decision = classify_corpus_tier(
        source_file,
        source_family="corpus_v1_baseline",
        mtime=datetime(2025, 1, 1, tzinfo=timezone.utc).timestamp(),
        now=now,
    )

    assert decision.tier == "cold"
    assert decision.reason == "cold_source_family:corpus_v1_baseline"
    assert decision.include_in_active_bundle is False


def test_manifest_row_stamps_source_metadata_and_tier(tmp_path):
    source_file = tmp_path / "project-documents" / "ARCHITECTURE.md"
    source_file.parent.mkdir()
    source_file.write_text("architecture", encoding="utf-8")
    mtime = datetime(2025, 1, 1, tzinfo=timezone.utc).timestamp()
    os.utime(source_file, (mtime, mtime))

    row = manifest_row_for_file(
        Source("repo_docs", source_file.parent, True, (".md",)),
        source_file,
        now=datetime(2026, 7, 2, tzinfo=timezone.utc),
    )

    assert row["path"] == str(source_file)
    assert row["source_type"] == "project_doc"
    assert row["temporal_mode"] == "meta"
    assert row["corpus_tier"] == "durable"
    assert row["tier_reason"] == "canonical_path"
    assert row["include_in_active_bundle"] is True


def test_build_corpus_manifest_can_emit_active_bundle_only(tmp_path):
    hot = tmp_path / "hot.md"
    cold = tmp_path / "cold.md"
    hot.write_text("hot", encoding="utf-8")
    cold.write_text("cold", encoding="utf-8")
    os.utime(hot, (1_783_000_000, 1_783_000_000))
    os.utime(cold, (1_700_000_000, 1_700_000_000))
    now = datetime.fromtimestamp(1_783_100_000, timezone.utc)

    manifest = build_corpus_manifest(
        (Source("obsidian", tmp_path, True, (".md",)),),
        now=now,
        active_only=True,
    )

    assert manifest["active_only"] is True
    assert manifest["summary"]["file_count"] == 1
    assert manifest["summary"]["tier_counts"] == {"hot": 1, "durable": 0, "cold": 0}
    assert manifest["items"][0]["path"] == str(hot)


def test_sources_from_roots_builds_local_override_sources(tmp_path):
    first = tmp_path / "first"
    second = tmp_path / "second"

    sources = sources_from_roots((first, second))

    assert [source.source_family for source in sources] == [
        "local_override_1",
        "local_override_2",
    ]
    assert [source.path for source in sources] == [first, second]
    assert all(source.parser_available for source in sources)
    assert all(source.suffixes == (".md", ".jsonl") for source in sources)


def test_emit_json_writes_parent_directories(tmp_path):
    output = tmp_path / "nested" / "manifest.json"

    emit_json({"ok": True}, output)

    assert json.loads(output.read_text(encoding="utf-8")) == {"ok": True}


def test_cli_writes_active_manifest_for_source_root(tmp_path):
    source_root = tmp_path / "source"
    output = tmp_path / "out" / "active-manifest.json"
    source_root.mkdir()
    hot = source_root / "hot.md"
    ignored = source_root / "ignored.txt"
    hot.write_text("hot", encoding="utf-8")
    ignored.write_text("ignored", encoding="utf-8")
    os.utime(hot, (1_783_000_000, 1_783_000_000))

    result = subprocess.run(
        [
            sys.executable,
            "scripts/source_manifest.py",
            "--corpus-manifest-json",
            "--active-only",
            "--source-root",
            str(source_root),
            "--output",
            str(output),
        ],
        check=True,
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
    )

    assert result.stdout == ""
    manifest = json.loads(output.read_text(encoding="utf-8"))
    assert manifest["active_only"] is True
    assert manifest["summary"]["file_count"] == 1
    assert manifest["summary"]["source_counts"] == {"local_override_1": 1}
    assert manifest["items"][0]["path"] == str(hot)
