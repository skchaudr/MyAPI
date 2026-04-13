import pytest
from context_refinery.triage.writers import parse_file, write_frontmatter, write_related_section
from context_refinery.triage.runner import make_record

def test_write_related_section():
    body = "Test body\n\nSome content."
    res = write_related_section(body, ["note1", "note2"])
    assert "## Related" in res
    assert "- [[note1]]" in res
    assert "- [[note2]]" in res

    # Replace test
    res2 = write_related_section(res, ["note3"])
    assert "## Related" in res2
    assert "- [[note3]]" in res2
    assert "- [[note1]]" not in res2

def test_make_record():
    fm = {"status": "incubating", "tags": ["a", "b"], "related": ["c"]}
    rec = make_record("test.md", fm)
    assert rec["filepath"] == "test.md"
    assert rec["status"] == "incubating"
    assert rec["tags"] == ["a", "b"]
    assert rec["related"] == ["c"]
