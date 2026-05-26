import re
import string

_MULTI_NEWLINE_RE = re.compile(r'\n{3,}')
_TRAILING_WS_RE = re.compile(r'[ \t]+$', re.MULTILINE)
_INTERNAL_WS_RE = re.compile(r'(?<=\S)[ \t]+')
_HEADING_RE = re.compile(r'^(#{1,6})([^\s#].*)$', re.MULTILINE)
_BOILERPLATE_RE = re.compile(
    r'^(?:copyright\s+\(c\)|copyright\s+\d{4}|all rights reserved|this page intentionally left blank|unsubscribe$)',
    re.IGNORECASE
)
_WHITESPACE_COLLAPSE_RE = re.compile(r'\s+')

def normalize_whitespace(text: str) -> str:
    """Normalize whitespace and newlines."""
    if not text:
        return ""
    text = _TRAILING_WS_RE.sub('', text)
    text = _INTERNAL_WS_RE.sub(' ', text)
    text = _MULTI_NEWLINE_RE.sub('\n\n', text)
    return text.strip()

def normalize_headings(text: str) -> str:
    """Ensure proper markdown heading formatting (e.g. #Heading to # Heading)."""
    if not text:
        return ""
    return _HEADING_RE.sub(r'\1 \2', text)

def strip_boilerplate(text: str) -> str:
    """Strip boilerplate/repeated footers/headers where identifiable."""
    if not text:
        return ""
    lines = text.split('\n')

    cleaned_lines = []
    for line in lines:
        if not _BOILERPLATE_RE.match(line.strip()):
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

    alnum_count = sum(map(str.isalnum, stripped_text))
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
    return _WHITESPACE_COLLAPSE_RE.sub(' ', text).strip()

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
