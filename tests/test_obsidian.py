import os
import pytest
from context_refinery.adapters.obsidian import parse_obsidian_file

def test_parse_obsidian_file_full_frontmatter(tmp_path):
    content = """---
title: Test Note
author: Test Author
status: mature
doc_type: article
tags: tag1, tag2
projects: project1
id: 12345
summary: This is a test summary.
url: https://example.com
---
# Test Heading
This is the test body content.
"""
    test_file = tmp_path / "test_full.md"
    test_file.write_text(content)

    doc = parse_obsidian_file(str(test_file))

    assert doc["title"] == "Test Note"
    assert doc["author"] == "Test Author"
    assert doc["status"] == "mature"
    assert doc["doc_type"] == "article"
    assert doc["tags"] == ["tag1", "tag2"]
    assert doc["projects"] == ["project1"]
    assert doc["id"] == 12345
    assert doc["content"]["summary"] == "This is a test summary."
    assert doc["source"]["url"] == "https://example.com"
    assert doc["content"]["cleaned_markdown"] == "# Test Heading\nThis is the test body content."
    assert doc["source"]["system"] == "obsidian"
    assert doc["source"]["type"] == "md"
    assert doc["source"]["original_file_name"] == "test_full.md"
    assert "Very short" not in doc["quality"]["warnings"]


def test_parse_obsidian_file_no_frontmatter(tmp_path):
    content = """# Just a note
Here is some content with no frontmatter at all.
"""
    test_file = tmp_path / "test_none.md"
    test_file.write_text(content)

    doc = parse_obsidian_file(str(test_file))

    assert doc["title"] == "test_none"
    assert doc["author"] == "Unknown"
    assert doc["status"] == "scratchpad"
    assert doc["doc_type"] == "note"
    assert doc["tags"] == []
    assert doc["projects"] == []
    assert "summary" not in doc["content"]
    assert "url" not in doc["source"]
    assert doc["content"]["cleaned_markdown"] == content
    assert doc["content"]["raw_text"] == content


def test_parse_obsidian_file_partial_frontmatter(tmp_path):
    content = """---
tags:
  - test
  - partial
---
Just some partial stuff.
"""
    test_file = tmp_path / "test_partial.md"
    test_file.write_text(content)

    doc = parse_obsidian_file(str(test_file))

    assert doc["title"] == "test_partial"
    assert doc["tags"] == ["test", "partial"]
    assert doc["content"]["cleaned_markdown"] == "Just some partial stuff."

def test_parse_obsidian_file_short_content(tmp_path):
    content = """---
title: Short Note
---
Hi
"""
    test_file = tmp_path / "test_short.md"
    test_file.write_text(content)

    doc = parse_obsidian_file(str(test_file))

    assert "Very short" in doc["quality"]["warnings"]

def test_parse_obsidian_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_obsidian_file("nonexistent.md")
