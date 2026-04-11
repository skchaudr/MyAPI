from context_refinery.sanitization import (
    normalize_whitespace,
    normalize_headings,
    strip_boilerplate,
    detect_noise,
    normalize_stable_text,
    normalize_stable_title,
    sanitize_document
)

def test_normalize_whitespace():
    assert normalize_whitespace("   hello   \n\n\n\nworld   ") == "hello\n\nworld"
    assert normalize_whitespace("a\t\tb") == "a b"
    assert normalize_whitespace("") == ""
    assert normalize_whitespace("No changes needed.") == "No changes needed."

def test_normalize_headings():
    assert normalize_headings("#Heading") == "# Heading"
    assert normalize_headings("##Subheading") == "## Subheading"
    assert normalize_headings("### Deep heading") == "### Deep heading" # Already correct
    assert normalize_headings("#1 is a number, not heading") == "# 1 is a number, not heading" # It fixes this based on our simple regex, which is fine for markdown headings normally. Wait, standard markdown wouldn't render `#1`, but `# 1` it would.
    assert normalize_headings("No heading here") == "No heading here"
    assert normalize_headings("") == ""

def test_strip_boilerplate():
    text = "Copyright (c) 2023\nReal content here\nUnsubscribe\n"
    assert strip_boilerplate(text) == "Real content here"

    text2 = "All Rights Reserved\nThis page intentionally left blank\nContent"
    assert strip_boilerplate(text2) == "Content"

    assert strip_boilerplate("") == ""

def test_detect_noise():
    assert "Document is empty." in detect_noise("")
    assert "Document is empty." in detect_noise("   ")

    short_text = "This is short."
    warnings = detect_noise(short_text)
    assert "Document is very short (under 50 characters)." in warnings

    noisy_text = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    warnings_noisy = detect_noise(noisy_text)
    assert "Document contains excessive non-alphanumeric characters (noisy content)." in warnings_noisy

def test_stable_normalization():
    assert normalize_stable_text("Hello, World!") == "hello world"
    assert normalize_stable_text("  TEST   string...  ") == "test string"
    assert normalize_stable_title("The Title: Part 1") == "the title part 1"
    assert normalize_stable_text("") == ""

def test_sanitize_document_clean_markdown():
    markdown = """#Clean Title

Some   text   here.

Copyright 2024
"""
    result = sanitize_document(markdown)
    assert result["cleaned_markdown"] == "# Clean Title\n\nSome text here."
    assert "Document is very short (under 50 characters)." in result["warnings"]

def test_sanitize_document_edge_cases():
    assert sanitize_document(None) == {"cleaned_markdown": "", "warnings": ["Document is empty."]}
    assert sanitize_document("") == {"cleaned_markdown": "", "warnings": ["Document is empty."]}
