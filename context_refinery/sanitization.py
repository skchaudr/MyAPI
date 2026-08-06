import re
import string

MULTIPLE_NEWLINES_PATTERN = re.compile(r'\n{3,}')
INTERNAL_SPACES_PATTERN = re.compile(r'(?<=\S)[ \t]+')
TRAILING_SPACES_PATTERN = re.compile(r'[ \t]+\r?$', flags=re.MULTILINE)
HEADING_NORMALIZATION_PATTERN = re.compile(r'^(#{1,6})([^\s\d#].*)$', flags=re.MULTILINE)
STABLE_TEXT_WHITESPACE_PATTERN = re.compile(r'\s+')

BOILERPLATE_PATTERNS = [
    re.compile(p, re.IGNORECASE) for p in [
        r'^copyright\s+\(c\)',
        r'^copyright\s+\d{4}',
        r'^all rights reserved',
        r'^this page intentionally left blank',
        r'^unsubscribe$'
    ]
]

def normalize_whitespace(text: str) -> str:
    """Normalize whitespace and newlines."""
    if not text:
        return ""
    # replace internal multiple spaces/tabs with single space, preserving leading whitespace
    text = INTERNAL_SPACES_PATTERN.sub(' ', text)
    # right strip lines
    text = TRAILING_SPACES_PATTERN.sub('', text)
    # Replace 3 or more newlines with 2 newlines
    text = MULTIPLE_NEWLINES_PATTERN.sub('\n\n', text)
    return text.strip()

def normalize_headings(text: str) -> str:
    """Ensure proper markdown heading formatting (e.g. #Heading to # Heading)."""
    if not text:
        return ""

    def add_space(match):
        hashes = match.group(1)
        content = match.group(2)
        return f"{hashes} {content}"

    text = HEADING_NORMALIZATION_PATTERN.sub(add_space, text)
    return text

def strip_boilerplate(text: str) -> str:
    """Strip boilerplate/repeated footers/headers where identifiable."""
    if not text:
        return ""
    lines = text.split('\n')

    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        is_boilerplate = any(p.match(stripped_line) for p in BOILERPLATE_PATTERNS)
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
    return STABLE_TEXT_WHITESPACE_PATTERN.sub(' ', text).strip()

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
