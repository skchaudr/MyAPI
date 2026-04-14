import pytest
import os
import yaml
from context_refinery.triage.writers import write_related_section, parse_file, write_frontmatter
from context_refinery.triage.terminal import KEYS
from context_refinery.triage.passes.links import LinksPass
from context_refinery.triage.passes.status import StatusPass
from context_refinery.triage.passes.tags import TagsPass
from context_refinery.triage.review import review_phase

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

def test_links_pass_init():
    records = [{"filepath": "file1.md", "related": []}, {"filepath": "file2.md", "related": []}]
    pass_obj = LinksPass(records)
    assert pass_obj._all_records == records
    assert pass_obj.name == "RELATED LINKS"

def test_parse_and_write_roundtrip(tmp_path):
    filepath = tmp_path / "test.md"
    frontmatter = {"id": "123", "title": "Test", "status": "mature"}
    body = "Body text."
    write_frontmatter(str(filepath), frontmatter, body)

    parsed_fm, parsed_body = parse_file(str(filepath))
    assert parsed_fm["id"] == "123"
    assert parsed_fm["title"] == "Test"
    assert parsed_fm["status"] == "mature"
    assert parsed_body == "Body text."