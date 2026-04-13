import pytest
from context_refinery.triage.writers import write_related_section, make_record, parse_file, write_frontmatter
from context_refinery.triage.passes.status import StatusPass
from context_refinery.triage.passes.doctype import DocTypePass
from context_refinery.triage.passes.tags import TagsPass
from context_refinery.triage.passes.projects import ProjectsPass
from context_refinery.triage.passes.links import LinksPass
import yaml
import tempfile
import os

def test_write_related_section_new():
    body = "Hello world\nThis is a test."
    related = ["file1", "file2"]
    new_body = write_related_section(body, related)

    expected = "Hello world\nThis is a test.\n\n## Related\n- [[file1]]\n- [[file2]]"
    assert new_body == expected

def test_write_related_section_replace():
    body = "Hello world\n\n## Related\n- [[old_file]]\n"
    related = ["file1", "file2"]
    new_body = write_related_section(body, related)

    expected = "Hello world\n\n## Related\n- [[file1]]\n- [[file2]]"
    assert new_body == expected

def test_make_record_includes_related():
    fm = {
        "status": "mature",
        "related": ["file1", "file2"]
    }
    record = make_record("dummy.md", fm)

    assert record["status"] == "mature"
    assert record["related"] == ["file1", "file2"]
    assert "doc_type" in record
    assert "tags" in record
    assert "projects" in record

def test_frontmatter_roundtrip():
    with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as f:
        filepath = f.name

    initial_fm = {
        "id": "123",
        "title": "Test Note",
        "source": "obsidian",
        "status": "scratchpad",
        "doc_type": "note",
        "tags": ["test"],
        "projects": ["my-proj"],
        "related": ["other-note"]
    }
    initial_body = "Some body text."

    try:
        write_frontmatter(filepath, initial_fm, initial_body)

        parsed_fm, parsed_body = parse_file(filepath)

        assert parsed_fm == initial_fm
        assert parsed_body == initial_body

        # Modify and rewrite
        parsed_fm["status"] = "mature"
        parsed_fm["related"].append("new-note")

        write_frontmatter(filepath, parsed_fm, parsed_body)

        final_fm, final_body = parse_file(filepath)
        assert final_fm["status"] == "mature"
        assert final_fm["related"] == ["other-note", "new-note"]

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

def test_pass_interface():
    passes = [
        StatusPass(),
        DocTypePass(),
        TagsPass(),
        ProjectsPass(),
        LinksPass(all_records=[])
    ]

    for p in passes:
        assert hasattr(p, "name")
        assert isinstance(p.name, str)
        assert hasattr(p, "print_legend")
        assert hasattr(p, "process_file")
        assert hasattr(p, "get_display_value")

        # Test get_display_value with empty record
        val = p.get_display_value({})
        assert isinstance(val, str)
def test_write_related_section_replace_with_following_sections():
    body = "Hello world\n\n## Related\n- [[old_file]]\n\n## Next Section\nMore text."
    related = ["file1", "file2"]
    new_body = write_related_section(body, related)

    expected = "Hello world\n\n## Related\n- [[file1]]\n- [[file2]]\n\n## Next Section\nMore text."
    assert new_body == expected
