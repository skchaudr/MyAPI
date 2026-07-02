from datetime import datetime, timezone
import os

from scripts.source_manifest import (
    Source,
    build_corpus_manifest,
    build_manifest,
    classify_corpus_tier,
    manifest_row_for_file,
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
