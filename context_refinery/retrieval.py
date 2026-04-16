"""
Smart Retrieval Pipeline — query classification, metadata-aware filtering,
reranking, and structured response assembly on top of Khoj vector search.
"""

import json
import logging
import math
import os
import re
import time
import urllib.request
import urllib.parse
import urllib.error
import yaml
from datetime import datetime, timezone, timedelta

logger = logging.getLogger(__name__)


class KhojUnavailableError(Exception):
    pass


# ── Khoj Client ─────────────────────────────────────────────────────────────

class KhojClient:
    """Wraps Khoj's HTTP search API."""

    def __init__(self, base_url=None):
        self.base_url = base_url or os.environ.get(
            "KHOJ_URL", "http://100.107.147.16:42110"
        )

    def search(self, query, n=10, max_distance=None):
        """GET /api/search — returns list of raw result dicts."""
        params = {"q": query, "n": str(n), "t": "all"}
        if max_distance is not None:
            params["max_distance"] = str(max_distance)

        url = f"{self.base_url}/api/search?{urllib.parse.urlencode(params)}"

        try:
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data if isinstance(data, list) else []
        except (urllib.error.URLError, OSError) as e:
            raise KhojUnavailableError(f"Khoj unreachable: {e}")
        except json.JSONDecodeError:
            logger.warning("Khoj returned non-JSON response")
            return []


# ── Metadata Parser ──────────────────────────────────────────────────────────

class MetadataParser:
    """Extracts YAML frontmatter from Khoj entry text."""

    _FM_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
    _SOURCE_PREFIXES = (
        ("obsidian-", "obsidian"),
        ("chatgpt-", "chatgpt"),
        ("claude-web-", "claude"),
        ("claude-", "claude-code"),
        ("codex-", "codex"),
    )

    @staticmethod
    def parse(entry, filename=None):
        """Parse entry text into (metadata_dict, body, snippet).

        Returns ({}, entry, entry[:500]) if no frontmatter found.
        Khoj may prepend the filename before the --- fence, so we
        strip any leading non-frontmatter lines first.
        """
        # Khoj prepends filename — skip to the first ---
        text = entry
        prefix_title = None
        if not text.startswith("---"):
            idx = text.find("\n---\n")
            if idx != -1:
                prefix = text[:idx].strip()
                if prefix:
                    prefix_title = prefix.splitlines()[0].strip() or None
                text = text[idx + 1:]  # skip to the ---

        match = MetadataParser._FM_RE.match(text)
        if not match:
            snippet = entry[:500].strip()
            inferred_source = MetadataParser._infer_source_from_filename(filename)
            return {
                "title": "untitled",
                "source": inferred_source,
                "created_at": None,
                "author": None,
                "status": None,
                "doc_type": None,
                "tags": [],
                "projects": [],
            }, entry, snippet

        try:
            fm = yaml.safe_load(match.group(1))
            if not isinstance(fm, dict):
                fm = {}
        except yaml.YAMLError:
            fm = {}

        body = text[match.end():].strip()
        snippet = body[:500].strip()
        inferred_source = MetadataParser._infer_source_from_filename(filename)

        metadata = {
            "title": fm.get("title") or prefix_title or "untitled",
            "source": fm.get("source") or inferred_source,
            "created_at": fm.get("created_at"),
            "author": fm.get("author"),
            "status": fm.get("status"),
            "doc_type": fm.get("doc_type"),
            "tags": fm.get("tags") or [],
            "projects": fm.get("projects") or [],
        }

        return metadata, body, snippet

    @staticmethod
    def _infer_source_from_filename(filename):
        if not filename:
            return "unknown"

        name = os.path.basename(str(filename)).lower()
        for prefix, source in MetadataParser._SOURCE_PREFIXES:
            if name.startswith(prefix):
                return source
        return "unknown"


# ── Keyword Searcher ─────────────────────────────────────────────────────────

class KeywordSearcher:
    """Searches a markdown corpus for exact keyword matches."""

    def __init__(self, notes_dir=None):
        self.notes_dir = notes_dir or os.environ.get(
            "KHOJ_NOTES_DIR", "/home/sbkchaudry_gmail_com/khoj-data/notes"
        )
        self.parser = MetadataParser()

    def search(self, query, n=10):
        query = (query or "").strip()
        if not query or not os.path.isdir(self.notes_dir):
            return []

        phrases, terms = self._parse_query(query)
        if not phrases and not terms:
            return []

        results = []
        for root, _, files in os.walk(self.notes_dir):
            for name in files:
                if not name.lower().endswith(".md"):
                    continue

                path = os.path.join(root, name)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        entry = f.read()
                except OSError:
                    continue

                body = entry.lower()
                if phrases and any(phrase not in body for phrase in phrases):
                    continue

                if terms and not all(
                    re.search(rf"\b{re.escape(term)}\b", body) for term in terms
                ):
                    continue

                metadata, parsed_body, snippet = self.parser.parse(entry)
                haystack = f"{metadata.get('title', '')} {parsed_body}".lower()
                match_hits = sum(haystack.count(term) for term in terms)
                phrase_hits = sum(haystack.count(phrase) for phrase in phrases)
                total_words = max(len(haystack.split()), 1)
                density = (match_hits + (2 * phrase_hits)) / total_words

                results.append({
                    "corpus_id": path,
                    "khoj_score": max(0.0, 1.0 - min(1.0, density * 25)),
                    "entry": entry,
                    "body": parsed_body,
                    "snippet": snippet,
                    "metadata": metadata,
                    "file": path,
                    "keyword_match": True,
                })

        results.sort(
            key=lambda r: (
                r.get("khoj_score", 1.0),
                len(r.get("snippet", "")),
                r.get("file", ""),
            )
        )
        return results[:n]

    @staticmethod
    def _parse_query(query):
        phrases = re.findall(r'"([^"]+)"', query)
        stripped = re.sub(r'"[^"]+"', " ", query)
        terms = [t.lower() for t in re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]*", stripped)]
        phrases = [p.lower().strip() for p in phrases if p.strip()]
        return phrases, terms


# ── Query Classifier ─────────────────────────────────────────────────────────

class QueryClassifier:
    """Heuristic query intent classification — no LLM call."""

    _TEMPORAL = [
        re.compile(r"\b(yesterday|today|last\s+week|this\s+week|last\s+month|this\s+month|recently|ago)\b", re.I),
        re.compile(r"\baround\s+the\s+time\b", re.I),
        re.compile(r"\bwhat\s+have\s+i\s+been\s+working\s+on\b", re.I),
        re.compile(r"\bwhat\s+was\s+i\s+doing\b", re.I),
        re.compile(r"\bwhat\s+did\s+i\s+do\b", re.I),
        re.compile(r"\b(before|after|since|during)\s+\w+", re.I),
        re.compile(r"\b\d{4}[-/]\d{2}", re.I),
        re.compile(r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b", re.I),
    ]

    _PROJECT = [
        re.compile(r"\b(summarize|overview|status\s+of|what\s+is|tell\s+me\s+about)\b.*\b(project|repo)\b", re.I),
        re.compile(r"\b(bdr|context.refinery|socialxp|smb.ops|water.and.stone|cim|my[_\s-]?devinfra)\b", re.I),
    ]

    _OPERATIONAL = [
        re.compile(r"\bstatus\s+of\s+(the\s+)?api\s+deployment\b", re.I),
        re.compile(r"\b(khoj\s+deployment|khoj\s+indexing|re-index(?:ing)?|health\s+endpoint)\b", re.I),
        re.compile(r"\b(tailscale|ssh|vm\s+access|virtual\s+machine|vm)\b", re.I),
    ]

    _SYNTHESIS = [
        re.compile(r"\bwhat\s+docs\s+should\s+i\s+use\b", re.I),
        re.compile(r"\bwhat\s+was\s+i\s+learning\s+about\b", re.I),
        re.compile(r"\bend\s+to\s+end\b", re.I),
        re.compile(r"\bworking\s+together\b", re.I),
    ]

    _CROSS_SOURCE = [
        re.compile(r"\bacross\s+(sources|tools|sessions|platforms)\b", re.I),
    ]

    _DECISION = [
        re.compile(r"\bwhat\s+did\s+i\s+decide\b", re.I),
        re.compile(r"\bdecide(d)?\s+about\b", re.I),
        re.compile(r"\bdecision\b", re.I),
    ]

    _META = [
        re.compile(r"\b(prompt|prompts|schema|schemas|taxonomy|tagging\s+strategy|rubric|rubrics|evaluation|metadata|frontmatter)\b", re.I),
        re.compile(r"\bwhat\s+did\s+i\s+write\s+about\b.*\b(notes?|passes?|cleanup|clean-up)\b", re.I),
    ]

    _SOURCE_SPECIFIC = [
        re.compile(r"\b(find|show|where|session|export|note|notes|setup|document)\b", re.I),
    ]

    _PATTERN = [
        re.compile(r"\b(pattern|recurring|habit|trend|advice|coach|improve|theme|keep\s+doing)\b", re.I),
    ]

    _INTENT_TO_MODE = {
        "temporal": "timeline",
        "factual": "lookup",
        "project_overview": "dossier",
        "operational": "summary",
        "cross_source": "summary",
        "source_specific": "lookup",
        "decision": "summary",
        "meta": "summary",
        "synthesis": "summary",
        "pattern": "coach",
    }

    _SOURCE_PATTERNS = [
        ("claude-code", re.compile(r"\bclaude\s+code\b", re.I)),
        ("chatgpt", re.compile(r"\bchatgpt\b", re.I)),
        ("codex", re.compile(r"\bcodex\b", re.I)),
        ("obsidian", re.compile(r"\bobsidian\b", re.I)),
        ("claude", re.compile(r"\bclaude\b", re.I)),
        ("jules", re.compile(r"\bjules\b", re.I)),
    ]

    def classify(self, query):
        """Returns (intent, answer_mode, confidence, temporal_hint)."""
        temporal_hint = None

        # Check temporal first — strongest signal
        for pat in self._TEMPORAL:
            m = pat.search(query)
            if m:
                temporal_hint = m.group(0).strip()
                return "temporal", "timeline", 0.85, temporal_hint

        # Cross-source
        source_hits = self._matched_sources(query)
        if len(source_hits) >= 2 and re.search(r"\b(and|vs|versus|compared|between|together|both|or)\b", query, re.I):
            return "cross_source", "summary", 0.82, None

        # Source-specific lookup
        if len(source_hits) == 1 and any(pat.search(query) for pat in self._SOURCE_SPECIFIC):
            return "source_specific", "lookup", 0.78, None

        # Project overview
        for pat in self._PROJECT:
            if pat.search(query):
                return "project_overview", "dossier", 0.75, None

        # Operational recall
        for pat in self._OPERATIONAL:
            if pat.search(query):
                return "operational", "summary", 0.76, None

        # Decision recall
        for pat in self._DECISION:
            if pat.search(query):
                return "decision", "summary", 0.76, None

        # Meta-work / schema / taxonomy
        for pat in self._META:
            if pat.search(query):
                return "meta", "summary", 0.74, None

        # Broad synthesis / overview
        for pat in self._SYNTHESIS:
            if pat.search(query):
                return "synthesis", "summary", 0.73, None

        # Pattern/coach
        for pat in self._PATTERN:
            if pat.search(query):
                return "pattern", "coach", 0.70, None

        # Default: factual
        return "factual", "lookup", 0.50, None

    def _matched_sources(self, query):
        q = query.lower()
        hits = []

        if "claude code" in q:
            hits.append("claude-code")
        if "chatgpt" in q:
            hits.append("chatgpt")
        if "codex" in q:
            hits.append("codex")
        if "obsidian" in q:
            hits.append("obsidian")
        if "claude code" not in q and "claude" in q:
            hits.append("claude")
        if "jules" in q:
            hits.append("jules")

        return hits


# ── Result Filter ────────────────────────────────────────────────────────────

class ResultFilter:
    """Post-filters parsed results by metadata."""

    @staticmethod
    def apply(results, sources=None, projects=None, tags=None,
              date_from=None, date_to=None):
        """Filter results. All conditions are AND'd. Tags are OR'd."""
        filtered = []
        for r in results:
            meta = r.get("metadata", {})

            # Source filter
            if sources:
                doc_source = meta.get("source", "")
                if doc_source not in sources:
                    continue

            # Project filter
            if projects:
                doc_projects = meta.get("projects", [])
                if not any(p in doc_projects for p in projects):
                    continue

            # Tag filter (OR — at least one match)
            if tags:
                doc_tags = meta.get("tags", [])
                if not any(t in doc_tags for t in tags):
                    continue

            # Date range filter
            created = meta.get("created_at")
            if created and (date_from or date_to):
                try:
                    doc_date = _parse_date(created)
                    if date_from and doc_date < _parse_date(date_from):
                        continue
                    if date_to and doc_date > _parse_date(date_to):
                        continue
                except (ValueError, TypeError):
                    pass  # Can't parse date — include the result

            filtered.append(r)

        return filtered


# ── Result Reranker ──────────────────────────────────────────────────────────

class ResultReranker:
    """Composite scoring from semantic, recency, trust, and reinforcement."""

    # Default weights
    W_SEMANTIC = 0.34
    W_RECENCY = 0.16
    W_TRUST = 0.10
    W_REINFORCE = 0.08
    W_KEYWORD = 0.12
    W_SOURCE = 0.14
    W_TITLE = 0.18

    # Intent-specific weight overrides
    _WEIGHT_OVERRIDES = {
        "temporal": {"W_SEMANTIC": 0.24, "W_RECENCY": 0.46},
        "pattern": {"W_REINFORCE": 0.26, "W_RECENCY": 0.08},
        "project_overview": {"W_SEMANTIC": 0.16, "W_TITLE": 0.46, "W_SOURCE": 0.08},
        "source_specific": {"W_SEMANTIC": 0.20, "W_TITLE": 0.34, "W_SOURCE": 0.28, "W_KEYWORD": 0.20},
        "operational": {"W_TITLE": 0.30, "W_SOURCE": 0.24, "W_KEYWORD": 0.10},
        "decision": {"W_TITLE": 0.22, "W_SOURCE": 0.14},
        "meta": {"W_TITLE": 0.22, "W_SOURCE": 0.12},
        "synthesis": {"W_TITLE": 0.18, "W_SOURCE": 0.12},
    }

    _TRUST_MAP = {
        "mature": 1.0,
        "incubating": 0.8,
        "reference": 0.7,
        "scratchpad": 0.5,
        "deprecated": 0.1,
    }

    def rerank(self, results, intent="factual", query=None):
        """Compute final_score and sort descending."""
        overrides = self._WEIGHT_OVERRIDES.get(intent, {})
        w_sem = overrides.get("W_SEMANTIC", self.W_SEMANTIC)
        w_rec = overrides.get("W_RECENCY", self.W_RECENCY)
        w_trust = overrides.get("W_TRUST", self.W_TRUST)
        w_reinf = overrides.get("W_REINFORCE", self.W_REINFORCE)
        w_title = overrides.get("W_TITLE", self.W_TITLE)
        w_source = overrides.get("W_SOURCE", self.W_SOURCE)
        w_keyword = overrides.get("W_KEYWORD", self.W_KEYWORD)
        source_family = self._source_family_from_query(query)
        query_terms = self._query_terms(query)
        anchor_terms = self._anchor_terms_from_query(query, intent)

        # Collect all tags/titles for reinforcement scoring
        all_tags = []
        for r in results:
            all_tags.append(set(r.get("metadata", {}).get("tags", [])))

        for i, r in enumerate(results):
            meta = r.get("metadata", {})
            sem = self._semantic_score(r.get("khoj_score", 1.0))
            rec = self._recency_score(meta.get("created_at"), intent)
            trust = self._trust_score(meta.get("status", "scratchpad"))
            reinf = self._reinforcement_score(i, all_tags)
            keyword = 1.0 if r.get("keyword_match") else 0.0
            source_match = 1.0 if source_family and meta.get("source") == source_family else 0.0
            title_boost = self._title_body_path_score(
                query_terms,
                anchor_terms,
                meta.get("title"),
                r.get("file"),
                r.get("body"),
            )

            r["final_score"] = (w_sem * sem + w_rec * rec +
                                w_trust * trust + w_reinf * reinf +
                                w_keyword * keyword +
                                w_source * source_match +
                                w_title * title_boost)

        results.sort(key=lambda r: r.get("final_score", 0), reverse=True)
        return results

    def _semantic_score(self, khoj_score):
        """Khoj returns distance (lower=better). Normalize to 0-1 similarity."""
        return max(0.0, 1.0 - min(khoj_score, 1.0))

    def _recency_score(self, created_at, intent="factual"):
        """Exponential decay. Sharper for temporal queries."""
        if not created_at:
            return 0.3  # neutral default for missing dates

        try:
            doc_date = _parse_date(created_at)
            now = datetime.now(timezone.utc)
            days_old = max(0, (now - doc_date).days)
            half_life = 30 if intent == "temporal" else 180
            return math.exp(-days_old / half_life)
        except (ValueError, TypeError):
            return 0.3

    def _trust_score(self, status):
        return self._TRUST_MAP.get(status, 0.5)

    def _source_family_from_query(self, query):
        if not query:
            return None

        q = query.lower()
        if "claude code" in q:
            return "claude-code"
        if "chatgpt" in q:
            return "chatgpt"
        if "codex" in q:
            return "codex"
        if "obsidian" in q:
            return "obsidian"
        if "claude" in q:
            return "claude"
        if "jules" in q:
            return "claude"
        return None

    def _query_terms(self, query):
        if not query:
            return []
        terms = re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]*", query.lower())
        stopwords = {
            "what", "is", "the", "a", "an", "of", "and", "or", "to", "i", "me",
            "my", "was", "were", "did", "do", "does", "for", "in", "on", "about",
            "show", "find", "where", "should", "use", "docs", "document", "notes",
            "note", "session", "this", "that", "how", "have", "been", "around",
        }
        return [term for term in terms if term not in stopwords]

    def _anchor_terms_from_query(self, query, intent):
        if not query:
            return []

        q = query.lower()
        compact = re.sub(r"[^a-z0-9]+", "", q)
        anchors = []

        project_aliases = {
            "my_devinfra": ["my_devinfra", "mydevinfra", "devinfra", "dev infra"],
            "bdr": ["bdr"],
            "cim": ["cim"],
            "socialxp": ["socialxp"],
            "openclaw": ["openclaw", "open claw"],
        }
        operational_aliases = {
            "khoj": ["khoj"],
            "deployment": ["deployment", "deploy", "deployed"],
            "indexing": ["index", "indexing", "reindex", "re-index", "re-indexing"],
            "access": ["tailscale", "ssh", "vm", "virtual machine", "remote access"],
            "api": ["api", "endpoint", "health", "service"],
        }

        for canonical, variants in project_aliases.items():
            if any(variant in q or re.sub(r"[^a-z0-9]+", "", variant) in compact for variant in variants):
                anchors.extend(variants)

        for canonical, variants in operational_aliases.items():
            if any(variant in q or re.sub(r"[^a-z0-9]+", "", variant) in compact for variant in variants):
                anchors.extend(variants)

        if "obsidian" in q:
            anchors.append("obsidian")
        if "schema" in q:
            anchors.append("schema")
        if "vault" in q:
            anchors.append("vault")

        if intent == "operational":
            anchors.extend([
                "khoj",
                "deployment",
                "deploy",
                "indexing",
                "reindex",
                "health",
                "api",
                "tailscale",
                "ssh",
                "vm",
                "virtual machine",
                "remote access",
            ])
        if intent == "project_overview":
            anchors.extend(["my_devinfra", "mydevinfra", "devinfra", "bdr", "cim", "socialxp", "openclaw"])

        seen = set()
        deduped = []
        for anchor in anchors:
            if anchor not in seen:
                seen.add(anchor)
                deduped.append(anchor)
        return deduped

    def _title_body_path_score(self, query_terms, anchor_terms, title, file_path, body):
        if not query_terms:
            query_terms = []
        file_name = os.path.basename(file_path or "")
        text = f"{title or ''} {file_name}".lower()
        body_text = (body or "").lower()
        if not text.strip():
            return 0.0

        matches = 0
        exact_phrase_hits = 0
        for term in query_terms:
            if term in text:
                matches += 1
        if len(query_terms) >= 2:
            joined = " ".join(query_terms[:4])
            if joined and joined in text:
                exact_phrase_hits = 1

        score = (matches / max(len(query_terms), 1)) * 0.7
        score += 0.3 * exact_phrase_hits

        if anchor_terms:
            compact_text = re.sub(r"[^a-z0-9]+", "", text)
            compact_body = re.sub(r"[^a-z0-9]+", "", body_text)
            anchor_hits = 0
            for anchor in anchor_terms:
                normalized_anchor = re.sub(r"[^a-z0-9]+", "", anchor.lower())
                in_title_or_path = bool(anchor and anchor.lower() in text)
                in_body = bool(anchor and anchor.lower() in body_text)
                in_compact_title = bool(normalized_anchor and normalized_anchor in compact_text)
                in_compact_body = bool(normalized_anchor and normalized_anchor in compact_body)
                if in_title_or_path or in_compact_title:
                    anchor_hits += 1
                    score += 0.32 if len(anchor) > 3 else 0.22
                elif in_body or in_compact_body:
                    anchor_hits += 1
                    score += 0.18 if len(anchor) > 3 else 0.12
            score += min(0.35, anchor_hits * 0.08)

        return min(1.0, score)

    def _reinforcement_score(self, index, all_tags):
        """Boost if this doc's tags overlap with tags from other docs."""
        if not all_tags or index >= len(all_tags):
            return 0.0
        my_tags = all_tags[index]
        if not my_tags:
            return 0.0

        overlap_count = 0
        for j, other_tags in enumerate(all_tags):
            if j == index:
                continue
            if my_tags & other_tags:
                overlap_count += 1

        # Normalize: more overlapping docs = higher score, capped at 1.0
        return min(1.0, overlap_count / max(len(all_tags) - 1, 1))


# ── Result Grouper ───────────────────────────────────────────────────────────

class ResultGrouper:
    """Groups results by source or project."""

    @staticmethod
    def group(results, intent="factual"):
        """Auto-select grouping strategy based on intent."""
        if intent == "project_overview":
            return ResultGrouper._by_key(results, "projects", "project")
        return ResultGrouper._by_key(results, "source", "source")

    @staticmethod
    def _by_key(results, field, group_type):
        groups = {}
        for r in results:
            if field == "projects":
                keys = r.get("metadata", {}).get("projects", []) or ["ungrouped"]
            else:
                keys = [r.get("metadata", {}).get("source") or "unknown"]

            for key in keys:
                if key not in groups:
                    groups[key] = []
                groups[key].append(r)

        return [
            {"key": k, "group_type": group_type, "documents": docs, "count": len(docs)}
            for k, docs in groups.items()
        ]


# ── Retrieval Pipeline ───────────────────────────────────────────────────────

class RetrievalPipeline:
    """Orchestrates the full retrieval flow."""

    def __init__(self, khoj_client=None):
        self.khoj = khoj_client or KhojClient()
        self.classifier = QueryClassifier()
        self.parser = MetadataParser()
        self.keyword_searcher = KeywordSearcher()
        self.filter = ResultFilter()
        self.reranker = ResultReranker()
        self.grouper = ResultGrouper()

    def execute(self, q, n=10, sources=None, projects=None, tags=None,
                date_from=None, date_to=None, answer_mode=None):
        """Run the full pipeline. Returns a dict matching QueryResponse schema."""
        start = time.monotonic()

        # Step 1: Classify query
        intent, auto_mode, confidence, temporal_hint = self.classifier.classify(q)
        mode = answer_mode or auto_mode

        # Auto-derive date filter from temporal hint
        if intent == "temporal" and temporal_hint and not date_from:
            date_from = self._resolve_temporal_hint(temporal_hint)

        # Step 2: Search Khoj (over-fetch to compensate for filtering)
        fetch_n = min(n * 3, 50)
        raw_results = self.khoj.search(q, n=fetch_n)
        total_from_khoj = len(raw_results)

        keyword_results = self.keyword_searcher.search(q, n=fetch_n)

        # Step 3: Parse metadata from each result
        parsed = []
        for r in raw_results:
            entry = r.get("entry", "")
            filename = r.get("additional", {}).get("file")
            metadata, body, snippet = self.parser.parse(entry, filename=filename)
            parsed.append({
                "corpus_id": r.get("corpus-id", ""),
                "khoj_score": r.get("score", 1.0),
                "entry": entry,
                "body": body,
                "snippet": snippet,
                "metadata": metadata,
                "file": filename,
            })

        seen = {self._dedupe_key(r) for r in parsed}
        for r in keyword_results:
            key = self._dedupe_key(r)
            if key in seen:
                for existing in parsed:
                    if self._dedupe_key(existing) == key:
                        existing["keyword_match"] = True
                        existing["khoj_score"] = min(
                            existing.get("khoj_score", 1.0),
                            r.get("khoj_score", 1.0),
                        )
                        break
                continue
            parsed.append(r)
            seen.add(key)

        # Step 4: Filter
        filtered = self.filter.apply(
            parsed,
            sources=sources,
            projects=projects,
            tags=tags,
            date_from=date_from,
            date_to=date_to,
        )
        total_after_filter = len(filtered)

        # Step 5: Rerank
        reranked = self.reranker.rerank(filtered, intent=intent, query=q)

        # Step 6: Trim to requested count
        top_results = reranked[:n]

        # Step 7: Group
        groups_raw = self.grouper.group(top_results, intent=intent)

        # Step 8: Assemble response
        result_docs = []
        for r in top_results:
            meta = r.get("metadata", {})
            result_docs.append({
                "corpus_id": r.get("corpus_id", ""),
                "snippet": r.get("snippet", ""),
                "khoj_score": r.get("khoj_score", 0.0),
                "final_score": r.get("final_score", 0.0),
                "title": meta.get("title"),
                "source": meta.get("source"),
                "created_at": meta.get("created_at"),
                "tags": meta.get("tags", []),
                "projects": meta.get("projects", []),
                "file": r.get("file"),
            })

        group_docs = []
        for g in groups_raw:
            gdocs = []
            for r in g["documents"]:
                meta = r.get("metadata", {})
                gdocs.append({
                    "corpus_id": r.get("corpus_id", ""),
                    "snippet": r.get("snippet", ""),
                    "khoj_score": r.get("khoj_score", 0.0),
                    "final_score": r.get("final_score", 0.0),
                    "title": meta.get("title"),
                    "source": meta.get("source"),
                    "created_at": meta.get("created_at"),
                    "tags": meta.get("tags", []),
                    "projects": meta.get("projects", []),
                    "file": r.get("file"),
                })
            group_docs.append({
                "key": g["key"],
                "group_type": g["group_type"],
                "documents": gdocs,
                "count": g["count"],
            })

        elapsed = (time.monotonic() - start) * 1000

        return {
            "query": q,
            "classification": {
                "intent": intent,
                "answer_mode": mode,
                "confidence": confidence,
                "temporal_hint": temporal_hint,
            },
            "results": result_docs,
            "groups": group_docs,
            "total_from_khoj": total_from_khoj,
            "total_after_filter": total_after_filter,
            "answer_mode": mode,
            "timing_ms": round(elapsed, 1),
        }

    def _resolve_temporal_hint(self, hint):
        """Convert temporal phrases to ISO date strings."""
        now = datetime.now(timezone.utc)
        hint_lower = hint.lower().strip()

        if "yesterday" in hint_lower:
            return (now - timedelta(days=1)).strftime("%Y-%m-%d")
        if "today" in hint_lower:
            return now.strftime("%Y-%m-%d")
        if "last week" in hint_lower or "this week" in hint_lower:
            return (now - timedelta(days=7)).strftime("%Y-%m-%d")
        if "last month" in hint_lower or "this month" in hint_lower:
            return (now - timedelta(days=30)).strftime("%Y-%m-%d")

        # Try to extract "N days/weeks ago"
        m = re.search(r"(\d+)\s+(day|week|month)s?\s+ago", hint_lower)
        if m:
            amount = int(m.group(1))
            unit = m.group(2)
            if unit == "day":
                return (now - timedelta(days=amount)).strftime("%Y-%m-%d")
            if unit == "week":
                return (now - timedelta(weeks=amount)).strftime("%Y-%m-%d")
            if unit == "month":
                return (now - timedelta(days=amount * 30)).strftime("%Y-%m-%d")

        return None

    @staticmethod
    def _dedupe_key(result):
        raw = result.get("file") or result.get("corpus_id") or result.get("metadata", {}).get("title") or ""
        return os.path.basename(str(raw))


# ── Helpers ──────────────────────────────────────────────────────────────────

def _parse_date(date_str):
    """Parse an ISO date string to a timezone-aware datetime."""
    if not date_str:
        raise ValueError("Empty date string")

    # Handle date-only strings
    if len(date_str) == 10:
        return datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)

    # Handle full ISO timestamps
    # Python 3.10 doesn't support datetime.fromisoformat with Z suffix
    date_str = date_str.replace("Z", "+00:00")
    return datetime.fromisoformat(date_str)
