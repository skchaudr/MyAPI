import pytest
import os
import yaml
import json
from context_refinery.triage.writers import write_related_section, parse_file, write_frontmatter, make_record
from context_refinery.triage.terminal import KEYS
from context_refinery.triage.passes.links import LinksPass
from context_refinery.triage.passes.status import StatusPass
from context_refinery.triage.passes.tags import TagsPass, normalize_tags, page_items, MAX_TAGS, PRESET_TAGS
from context_refinery.triage.passes.doctype import TypePass, TYPE_VALUES
import context_refinery.triage.passes.projects as projects_mod
from context_refinery.triage.review import review_phase
from context_refinery.triage.runner import (
    load_queue_files,
    load_queue_suggestions,
    parse_args,
    prefill_record_from_suggestion,
)
from context_refinery.triage.passes.v4schema import CONCEPT_PRESETS, _dedupe_preserving_order, _invalid_fields, _mark_needs_title, _normalize_tag_input, _page_items, _selected_display
from scripts.build_v4_owner_queue import build_queue
from scripts.normalize_vault_schema_v4 import normalize_tags as normalize_v4_tags

def test_write_related_section_injects_new():
    body = "# Title\n\nSome text."
    related = ["file1", "file2"]
    updated = write_related_section(body, related)
    assert "## Related\n- [[file1]]\n- [[file2]]" in updated

def test_write_related_section_replaces_existing():
    body = "# Title\n\nSome text.\n## Related\n- [[old]]\n\n## References\n- [[ref]]"
    related = ["new1", "new2"]
    updated = write_related_section(body, related)
    assert "## Related\n- [[new1]]\n- [[new2]]" in updated
    assert "## References\n- [[ref]]" in updated
    assert "[[old]]" not in updated

def test_keys_constraint():
    assert len(KEYS) == 36
    assert "0" in KEYS
    assert "9" in KEYS
    assert "a" in KEYS
    assert "z" in KEYS


# ── V4 type values ────────────────────────────────────────────────────────────

def test_type_values_v4():
    values = set(TYPE_VALUES.values())
    assert "project" in values
    assert "area" in values
    assert "resource" in values
    assert "concept" in values
    assert "event" in values
    assert "periodic" in values

def test_type_values_excludes_legacy():
    values = set(TYPE_VALUES.values())
    assert "log" not in values
    assert "task" not in values
    assert "utility" not in values


# ── tags ──────────────────────────────────────────────────────────────────────

def test_tags_max_is_eight():
    assert MAX_TAGS == 8


def test_v4_normalizer_preserves_up_to_eight_tags():
    tags, review = normalize_v4_tags(
        ["topic/ai", "tool/neovim", "scope/ops", "topic/log"],
        ["tool/terminal", "topic/workflow"],
    )

    assert review == []
    assert tags == [
        "topic/ai",
        "tool/neovim",
        "scope/ops",
        "topic/log",
        "tool/terminal",
        "topic/workflow",
    ]

def test_tags_presets_include_log_and_howto():
    assert "topic/log" in PRESET_TAGS
    assert "topic/howto" in PRESET_TAGS

def test_tags_paging_helpers():
    page0 = page_items(0)
    page1 = page_items(1)
    assert len(page0) == 9
    assert page0[0] == PRESET_TAGS[0]
    assert len(page1) == 9
    assert normalize_tags(["tool/git", "custom", "topic/ai"]) == ["topic/ai", "tool/git", "custom"]


# ── projects pass (legacy, if still present) ──────────────────────────────────

def test_projects_paging_helpers(monkeypatch):
    monkeypatch.setattr(
        projects_mod,
        "PRESET_PROJECTS",
        ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11"],
    )
    assert projects_mod.page_items(0) == ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9"]
    assert projects_mod.page_items(1) == ["p10", "p11"]
    assert projects_mod.normalize_projects(["p10", "custom", "p2"]) == ["p2", "p10", "custom"]

def test_links_pass_init():
    records = [{"filepath": "file1.md", "related": []}, {"filepath": "file2.md", "related": []}]
    pass_obj = LinksPass(records)
    assert pass_obj._all_records == records
    assert pass_obj.name == "RELATED LINKS"

def test_parse_and_write_roundtrip(tmp_path):
    filepath = tmp_path / "test.md"
    frontmatter = {"id": "123", "title": "Test", "type": "resource"}
    body = "Body text."
    write_frontmatter(str(filepath), frontmatter, body)

    parsed_fm, parsed_body = parse_file(str(filepath))
    assert parsed_fm["id"] == "123"
    assert parsed_fm["title"] == "Test"
    assert parsed_fm["type"] == "resource"
    assert parsed_body == "Body text."


# ── make_record V4 ────────────────────────────────────────────────────────────

def test_make_record_v4_fields():
    fm = {
        "type": "project",
        "status": "active",
        "area": "[[Career]]",
        "project": "[[--MyProject]]",
        "concepts": ["[[Automation]]"],
        "tags": ["topic/ai"],
    }
    rec = make_record("test.md", fm)
    assert rec["type"] == "project"
    assert rec["status"] == "active"
    assert rec["area"] == "[[Career]]"
    assert rec["project"] == "[[--MyProject]]"
    assert rec["concepts"] == ["[[Automation]]"]
    assert rec["tags"] == ["topic/ai"]
    assert "format" not in rec

def test_make_record_no_format_field():
    rec = make_record("test.md", {"type": "resource"})
    assert "format" not in rec


# ── status conditional on type ────────────────────────────────────────────────

def test_write_removes_status_for_non_project_event(tmp_path):
    from context_refinery.triage.review import execute_writes
    filepath = tmp_path / "note.md"
    filepath.write_text("---\ntype: resource\nstatus: active\n---\n\nBody.", encoding="utf-8")
    records = [make_record(str(filepath), {"type": "resource", "status": "active"})]
    records[0]["type"] = "resource"
    execute_writes(records)
    fm, _ = parse_file(str(filepath))
    assert "status" not in fm

def test_write_keeps_status_for_project(tmp_path):
    from context_refinery.triage.review import execute_writes
    filepath = tmp_path / "proj.md"
    filepath.write_text("---\ntype: project\nstatus: active\n---\n\nBody.", encoding="utf-8")
    records = [make_record(str(filepath), {"type": "project", "status": "active"})]
    records[0]["type"] = "project"
    records[0]["status"] = "active"
    execute_writes(records)
    fm, _ = parse_file(str(filepath))
    assert fm["status"] == "active"

def test_write_removes_format_field(tmp_path):
    from context_refinery.triage.review import execute_writes
    filepath = tmp_path / "note.md"
    filepath.write_text("---\ntype: resource\nformat: note\n---\n\nBody.", encoding="utf-8")
    records = [make_record(str(filepath), {"type": "resource", "format": "note"})]
    execute_writes(records)
    fm, _ = parse_file(str(filepath))
    assert "format" not in fm

def test_project_field_roundtrip(tmp_path):
    from context_refinery.triage.review import execute_writes
    filepath = tmp_path / "note.md"
    filepath.write_text("---\ntype: project\n---\n\nBody.", encoding="utf-8")
    records = [make_record(str(filepath), {"type": "project"})]
    records[0]["project"] = "[[--MyAPI]]"
    records[0]["status"] = "active"
    execute_writes(records)
    fm, _ = parse_file(str(filepath))
    assert fm["project"] == "[[--MyAPI]]"


def test_review_flags_roundtrip(tmp_path):
    from context_refinery.triage.review import execute_writes
    filepath = tmp_path / "note.md"
    filepath.write_text("---\ntype: resource\n---\n\nBody.", encoding="utf-8")
    records = [make_record(str(filepath), {"type": "resource"})]
    records[0]["review_flags"] = ["needs_title"]
    execute_writes(records)
    fm, _ = parse_file(str(filepath))
    assert fm["review_flags"] == ["needs_title"]


def test_build_owner_queue_collapses_duplicate_stems(tmp_path):
    vault = tmp_path / "vault"
    folder = vault / "02 Areas" / "My_DevInfra"
    duplicate_folder = folder / "AI"
    duplicate_folder.mkdir(parents=True)
    (folder / "Same Note.md").write_text("---\ntype: resource\narea: '[[My_DevInfra]]'\n---\n\nBody.", encoding="utf-8")
    (duplicate_folder / "Same Note.md").write_text("---\ntype: resource\narea: '[[My_DevInfra]]'\n---\n\nBody.", encoding="utf-8")

    queue, duplicate_groups = build_queue(vault, "02 Areas/My_DevInfra", collapse_duplicates=True)

    assert len(queue) == 1
    assert len(duplicate_groups) == 1
    assert "duplicate cluster collapsed" in "; ".join(queue[0].review_needed)


def test_build_owner_queue_skips_valid_notes(tmp_path):
    vault = tmp_path / "vault"
    folder = vault / "02 Areas" / "My_DevInfra"
    folder.mkdir(parents=True)
    (folder / "Good.md").write_text(
        "---\ntype: resource\narea: '[[My_DevInfra]]'\nconcepts:\n- '[[RAG Pipeline]]'\ntags:\n- topic/ai\n---\n\nBody.",
        encoding="utf-8",
    )

    queue, duplicate_groups = build_queue(vault, "02 Areas/My_DevInfra", collapse_duplicates=True)

    assert queue == []
    assert duplicate_groups == {}


# ── owner queue CLI helpers ───────────────────────────────────────────────────

def test_parse_args_queue_json():
    positional, queue_json, vault_root, confidences = parse_args([
        "--queue-json", "report.json",
        "--vault-root", "/vault",
        "--confidence", "medium,review",
    ])
    assert positional == []
    assert queue_json == "report.json"
    assert vault_root == "/vault"
    assert confidences == {"medium", "review"}


def test_load_queue_files_filters_by_confidence(tmp_path):
    vault = tmp_path / "vault"
    vault.mkdir()
    keep = vault / "keep.md"
    skip = vault / "skip.md"
    keep.write_text("---\ntype: resource\n---\n", encoding="utf-8")
    skip.write_text("---\ntype: resource\n---\n", encoding="utf-8")
    report = tmp_path / "report.json"
    report.write_text(json.dumps([
        {"path": "keep.md", "confidence": "review"},
        {"path": "skip.md", "confidence": "high"},
    ]), encoding="utf-8")

    assert load_queue_files(str(report), str(vault), {"review"}) == [str(keep)]


def test_load_queue_suggestions_filters_by_confidence(tmp_path):
    vault = tmp_path / "vault"
    vault.mkdir()
    keep = vault / "keep.md"
    skip = vault / "skip.md"
    keep.write_text("---\ntype: resource\n---\n", encoding="utf-8")
    skip.write_text("---\ntype: resource\n---\n", encoding="utf-8")
    report = tmp_path / "report.json"
    report.write_text(json.dumps([
        {"path": "keep.md", "confidence": "review", "suggested": {"area": "[[My_DevInfra]]"}},
        {"path": "skip.md", "confidence": "high", "suggested": {"area": "[[Health]]"}},
    ]), encoding="utf-8")

    suggestions = load_queue_suggestions(str(report), str(vault), {"review"})

    assert suggestions == {str(keep): {"area": "[[My_DevInfra]]"}}


def test_prefill_record_from_suggestion_applies_safe_fields():
    record = {
        "filepath": "note.md",
        "type": "task",
        "area": "",
        "concepts": [],
        "tags": ["task"],
    }
    changed = prefill_record_from_suggestion(record, {
        "type": "resource",
        "area": "[[My_DevInfra]]",
        "concepts": ["[[Should Stay Manual]]"],
        "tags": ["topic/ai"],
    })

    assert changed == ["area", "tags", "type"]
    assert record["type"] == "resource"
    assert record["area"] == "[[My_DevInfra]]"
    assert record["tags"] == ["topic/ai"]
    assert record["concepts"] == []


def test_v4schema_rejects_tag_shaped_concepts():
    issues = _invalid_fields({
        "type": "resource",
        "area": "[[My_DevInfra]]",
        "concepts": ["[[topic/agents]]"],
        "tags": ["topic/agents"],
    })
    assert "concepts" in issues


def test_v4schema_allows_more_than_three_concepts():
    issues = _invalid_fields({
        "type": "resource",
        "area": "[[My_DevInfra]]",
        "concepts": ["[[AI Tooling]]", "[[Agent Collaboration]]", "[[Infrastructure]]", "[[RAG Pipeline]]"],
        "tags": ["topic/agents"],
    })
    assert "concepts" not in issues


def test_v4schema_concept_presets_seed_owner_pass():
    assert "Retrieval Quality" in CONCEPT_PRESETS
    assert "VM Operations" in CONCEPT_PRESETS
    assert _dedupe_preserving_order(["AI Tooling", "AI Tooling", "RAG Pipeline"]) == ["AI Tooling", "RAG Pipeline"]


def test_v4schema_rejects_secret_shaped_tags():
    issues = _invalid_fields({
        "type": "resource",
        "area": "[[My_DevInfra]]",
        "concepts": ["[[Terminal Workflow]]"],
        "tags": ["topic/sk-1234567890abcdefghijklmnop"],
    })
    assert "tags" in issues


def test_v4schema_tag_aliases_avoid_long_trigger_words():
    assert _normalize_tag_input("tterm") == "topic/terminal"
    assert _normalize_tag_input("uterm") == "tool/terminal"


def test_v4schema_page_items_maps_zero_to_tenth_item():
    items = [f"item-{i}" for i in range(12)]

    assert _page_items(items, 0) == [
        ("1", "item-0"),
        ("2", "item-1"),
        ("3", "item-2"),
        ("4", "item-3"),
        ("5", "item-4"),
        ("6", "item-5"),
        ("7", "item-6"),
        ("8", "item-7"),
        ("9", "item-8"),
        ("0", "item-9"),
    ]
    assert _page_items(items, 1) == [("1", "item-10"), ("2", "item-11")]


def test_v4schema_selected_display_is_compact():
    assert _selected_display([]) == "[dim]none[/dim]"
    assert "topic/ai" in _selected_display(["topic/ai"])


def test_v4schema_mark_needs_title_is_idempotent():
    record = {"review_flags": ["needs_title"]}
    _mark_needs_title(record)
    assert record["review_flags"] == ["needs_title"]
