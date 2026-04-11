import os
import pytest
from context_refinery.exporter import export_for_khoj, sanitize_filename

def test_sanitize_filename():
    assert sanitize_filename("valid_name") == "valid_name"
    assert sanitize_filename("invalid/name") == "invalid_name"
    assert sanitize_filename("name with spaces") == "name_with_spaces"
    assert sanitize_filename("") == "document"
    assert sanitize_filename(None) == "document"

def test_export_for_khoj(tmp_path):
    doc_dict = {
        "id": "12345",
        "title": "Test Document",
        "author": "Alice",
        "tags": ["testing", "python"],
        "content": "This is the body of the test document."
    }

    output_dir = str(tmp_path)
    export_for_khoj(doc_dict, output_dir)

    # Expected filename should be based on sanitized title
    expected_filename = "Test_Document.md"
    expected_filepath = os.path.join(output_dir, expected_filename)

    assert os.path.exists(expected_filepath)

    with open(expected_filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    assert content.startswith("---\n")
    assert "title: Test Document\n" in content
    assert "author: Alice\n" in content
    assert "id: '12345'\n" in content
    assert "tags:\n- testing\n- python\n" in content
    assert "---\n\nThis is the body of the test document." in content

def test_export_for_khoj_fallback_filename(tmp_path):
    doc_dict = {
        "author": "Bob",
        "content": "No title or id here."
    }

    output_dir = str(tmp_path)
    export_for_khoj(doc_dict, output_dir)

    expected_filepath = os.path.join(output_dir, "document.md")
    assert os.path.exists(expected_filepath)

    with open(expected_filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    assert "---\n\nNo title or id here." in content
