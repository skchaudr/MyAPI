import re
import string

def normalize_whitespace(text: str) -> str:
    """Normalize whitespace and newlines."""
    if not text:
        return ""
    # Replace 3 or more newlines with 2 newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    lines = []
    for line in text.split('\n'):
        # match leading whitespace to keep it
        match = re.match(r'^(\s*)', line)
        leading = match.group(1) if match else ""

        # replace internal multiple spaces/tabs with single space
        content = line[len(leading):]
        content = re.sub(r'[ \t]+', ' ', content)

        # combine and right strip
        lines.append((leading + content).rstrip())

    # join with newlines, but remove more than 2 consecutive newlines again
    joined = '\n'.join(lines).strip()
    joined = re.sub(r'\n{3,}', '\n\n', joined)
    return joined

def normalize_headings(text: str) -> str:
    """Ensure proper markdown heading formatting (e.g. #Heading to # Heading)."""
    if not text:
        return ""

    def add_space(match):
        hashes = match.group(1)
        content = match.group(2)
        return f"{hashes} {content}"

    # Matches ^#{1,6}[^\s#]
    text = re.sub(r'^(#{1,6})([^\s#].*)$', add_space, text, flags=re.MULTILINE)
    return text

def strip_boilerplate(text: str) -> str:
    """Strip boilerplate/repeated footers/headers where identifiable."""
    if not text:
        return ""
    lines = text.split('\n')

    # Common boilerplate patterns
    boilerplate_patterns = [
        r'^copyright\s+\(c\)',
        r'^copyright\s+\d{4}',
        r'^all rights reserved',
        r'^this page intentionally left blank',
        r'^unsubscribe$'
    ]

    compiled_patterns = [re.compile(p, re.IGNORECASE) for p in boilerplate_patterns]

    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        is_boilerplate = any(p.match(stripped_line) for p in compiled_patterns)
        if not is_boilerplate:
            cleaned_lines.append(line)

    return '\n'.join(cleaned_lines).strip()

def detect_noise(text: str) -> list[str]:
    """Detect noisy/very-short/near-empty content and populate quality warnings."""
    warnings = []
    if not text or not text.strip():
        warnings.append("Document is empty.")
        return warnings

    stripped_text = text.strip()
    if len(stripped_text) < 50:
        warnings.append("Document is very short (under 50 characters).")

    alnum_count = sum(c.isalnum() for c in stripped_text)
    if len(stripped_text) > 0 and alnum_count / len(stripped_text) < 0.5:
        warnings.append("Document contains excessive non-alphanumeric characters (noisy content).")

    return warnings

def normalize_stable_text(text: str) -> str:
    """Stable text normalization for deduplication."""
    if not text:
        return ""
    # Lowercase, remove punctuation, collapse whitespace
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return re.sub(r'\s+', ' ', text).strip()

def normalize_stable_title(title: str) -> str:
    """Stable title normalization for deduplication."""
    return normalize_stable_text(title)

def sanitize_document(text: str) -> dict:
    """
    Sanitize document by applying normalizations and returning a dict containing
    cleaned_markdown and a list of warnings.
    """
    if text is None:
        text = ""

    cleaned = text
    cleaned = strip_boilerplate(cleaned)
    cleaned = normalize_headings(cleaned)
    cleaned = normalize_whitespace(cleaned)

    warnings = detect_noise(cleaned)

    return {
        "cleaned_markdown": cleaned,
        "warnings": warnings
    }
