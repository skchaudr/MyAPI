from datetime import datetime, timezone
import os

from scripts.source_manifest import Source, build_manifest, summarize_source


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
