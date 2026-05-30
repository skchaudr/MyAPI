import re
import string

_WS_TRAILING_RE = re.compile(r'[ \t]+\r?$', flags=re.MULTILINE)
_WS_INTERNAL_RE = re.compile(r'(?<=\S)[ \t]+')
_WS_NEWLINES_RE = re.compile(r'\n{3,}')

def normalize_whitespace(text: str) -> str:
    """Normalize whitespace and newlines."""
    if not text:
        return ""
    # remove trailing whitespace
    text = _WS_TRAILING_RE.sub('', text)
    # collapse multiple spaces/tabs internally (not leading)
    text = _WS_INTERNAL_RE.sub(' ', text)
    # replace 3 or more newlines with 2 newlines
    text = _WS_NEWLINES_RE.sub('\n\n', text)
    return text.strip()

_HEADING_RE = re.compile(r'^(#{1,6})([^\s#].*)$', flags=re.MULTILINE)

def normalize_headings(text: str) -> str:
    """Ensure proper markdown heading formatting (e.g. #Heading to # Heading)."""
    if not text:
        return ""
    return _HEADING_RE.sub(r'\1 \2', text)

_BOILERPLATE_RE = re.compile(
    r'^[ \t]*(?:(?:copyright\s+\(c\)|copyright\s+\d{4}|all rights reserved|this page intentionally left blank)[^\r\n]*|unsubscribe[ \t]*)(?=\r?\n|$)\r?\n?',
    flags=re.IGNORECASE | re.MULTILINE
)

def strip_boilerplate(text: str) -> str:
    """Strip boilerplate/repeated footers/headers where identifiable."""
    if not text:
        return ""
    return _BOILERPLATE_RE.sub('', text).strip()

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
