import os
import yaml
import uuid
import datetime

def parse_obsidian_file(filepath: str) -> dict:
    """
    Reads a markdown file, extracts YAML frontmatter if present, and returns a dictionary
    mapping to the CanonicalDocument schema.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    title = os.path.splitext(filename)[0]

    frontmatter = {}
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
            except yaml.YAMLError:
                # Fallback if frontmatter parsing fails
                pass

    if not isinstance(frontmatter, dict):
        frontmatter = {}

    # Handle possible tags in frontmatter
    tags = frontmatter.get('tags') or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]

    projects = frontmatter.get('projects') or []
    if isinstance(projects, str):
        projects = [p.strip() for p in projects.split(",") if p.strip()]

    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # Valid taxonomy values per docs/01-taxonomy.md
    _VALID_STATUSES = {"mature", "incubating", "scratchpad", "deprecated", "reference"}
    _VALID_DOC_TYPES = {"conversation", "note", "spec", "log", "article", "other"}

    # Extract metadata from frontmatter — sanitize against taxonomy, fall back to safe defaults
    author = frontmatter.get("author") or "Unknown"
    raw_status = frontmatter.get("status") or ""
    status = raw_status if raw_status in _VALID_STATUSES else "scratchpad"
    raw_doc_type = frontmatter.get("doc_type") or ""
    doc_type = raw_doc_type if raw_doc_type in _VALID_DOC_TYPES else "note"

    created_at_raw = frontmatter.get("created_at")
    if created_at_raw:
        if isinstance(created_at_raw, datetime.datetime) or isinstance(created_at_raw, datetime.date):
            created_at = created_at_raw.isoformat()
        else:
            created_at = str(created_at_raw)
    else:
        created_at = now_iso

    updated_at_raw = frontmatter.get("updated_at")
    if updated_at_raw:
        if isinstance(updated_at_raw, datetime.datetime) or isinstance(updated_at_raw, datetime.date):
            updated_at = updated_at_raw.isoformat()
        else:
            updated_at = str(updated_at_raw)
    else:
        updated_at = created_at

    summary = frontmatter.get("summary") or ""

    canonical_doc = {
        "id": frontmatter.get("id", str(uuid.uuid4())),
        "title": frontmatter.get("title", title),
        "source": {
            "system": "obsidian",
            "type": "md",
            "original_file_name": filename,
        },
        "timestamps": {
            "created_at": created_at,
            "updated_at": updated_at,
            "ingested_at": now_iso
        },
        "author": author,
        "status": status,
        "doc_type": doc_type,
        "tags": tags,
        "projects": projects,
        "content": {
            "raw_text": content,
            "cleaned_markdown": body,
        },
        "quality": {
            "is_noisy": False,
            "warnings": []
        }
    }

    if summary:
        canonical_doc["content"]["summary"] = summary

    url = frontmatter.get("url", "")
    if url:
        canonical_doc["source"]["url"] = url

    # simple quality check
    if len(body) < 10:
        canonical_doc["quality"]["warnings"].append("Very short")

    return canonical_doc
