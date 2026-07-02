from pathlib import Path

from mcp import get_person_context, get_project_context

REPO_ROOT = Path(__file__).resolve().parents[1]
GOLDEN_BRIEFS_DIR = REPO_ROOT / "evals" / "golden_briefs"


def test_get_project_context_returns_myapi_rebuild_golden_brief():
    fixture_path = GOLDEN_BRIEFS_DIR / "get_project_context_myapi_rebuild.md"

    result = get_project_context("MyAPI-rebuild")

    assert result["tool_name"] == "get_project_context"
    assert result["project"] == "MyAPI-rebuild"
    assert result["markdown"] == fixture_path.read_text(encoding="utf-8")
    assert str(fixture_path) in result["evidence_paths"]
    assert result["source_manifest_summary"]["source_family"] == "golden_briefs"


def test_get_person_context_returns_sab_golden_brief_by_default():
    fixture_path = GOLDEN_BRIEFS_DIR / "get_person_context_sab.md"

    result = get_person_context()

    assert result["tool_name"] == "get_person_context"
    assert result["subject"] == "Sab"
    assert result["markdown"] == fixture_path.read_text(encoding="utf-8")
    assert str(fixture_path) in result["evidence_paths"]
    assert result["source_manifest_summary"]["file_count"] >= 2
