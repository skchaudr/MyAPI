import os
import re
import yaml

def sanitize_filename(filename: str) -> str:
    """Sanitizes a string to be safe for use as a filename."""
    if not filename:
        return "document"
    # Replace invalid characters with underscores
    s = str(filename).strip()
    s = re.sub(r'(?u)[^-\w.]', '_', s)
    return s

def export_for_khoj(doc_dict: dict, output_dir: str):
    """
    Exports a document dictionary to a Markdown file with YAML frontmatter.

    Args:
        doc_dict: A dictionary representing a CanonicalDocument.
                  Must contain 'content' and metadata fields.
        output_dir: The directory where the .md file should be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    doc_copy = doc_dict.copy()
    content = doc_copy.pop('content', '')

    # Use title or id for the filename, fallback to "document"
    filename_base = doc_copy.get('title') or doc_copy.get('id') or "document"
    filename = sanitize_filename(filename_base) + ".md"

    output_path = os.path.join(output_dir, filename)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("---\n")
        if doc_copy:
            yaml.dump(doc_copy, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        f.write("---\n\n")
        f.write(content)
