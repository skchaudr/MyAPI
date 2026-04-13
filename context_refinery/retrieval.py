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

    @staticmethod
    def parse(entry):
        """Parse entry text into (metadata_dict, body, snippet).

        Returns ({}, entry, entry[:500]) if no frontmatter found.
        """
        match = MetadataParser._FM_RE.match(entry)
        if not match:
            snippet = entry[:500].strip()
            return {}, entry, snippet

        try:
            fm = yaml.safe_load(match.group(1))
            if not isinstance(fm, dict):
                fm = {}
        except yaml.YAMLError:
            fm = {}

        body = entry[match.end():].strip()
        snippet = body[:500].strip()

        metadata = {
            "title": fm.get("title"),
            "source": fm.get("source"),
            "created_at": fm.get("created_at"),
            "author": fm.get("author"),
            "status": fm.get("status"),
            "doc_type": fm.get("doc_type"),
            "tags": fm.get("tags") or [],
            "projects": fm.get("projects") or [],
        }

        return metadata, body, snippet


# ── Query Classifier ─────────────────────────────────────────────────────────

class QueryClassifier:
    """Heuristic query intent classification — no LLM call."""

    _TEMPORAL = [
        re.compile(r"\b(yesterday|today|last\s+week|this\s+week|last\s+month|this\s+month|recently|ago)\b", re.I),
        re.compile(r"\b(before|after|since|during)\s+\w+", re.I),
        re.compile(r"\b\d{4}[-/]\d{2}", re.I),
        re.compile(r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b", re.I),
    ]

    _PROJECT = [
        re.compile(r"\b(summarize|overview|status\s+of|what\s+is|tell\s+me\s+about)\b.*\b(project|repo)\b", re.I),
        re.compile(r"\b(bdr|context.refinery|socialxp|smb.ops|water.and.stone|cim)\b", re.I),
    ]

    _CROSS_SOURCE = [
        re.compile(r"\b(chatgpt|claude|codex)\b.*\b(and|vs|versus|compared|or)\b", re.I),
        re.compile(r"\bacross\s+(sources|tools|sessions|platforms)\b", re.I),
    ]

    _PATTERN = [
        re.compile(r"\b(pattern|recurring|habit|trend|advice|coach|improve|theme|keep\s+doing)\b", re.I),
    ]

    _INTENT_TO_MODE = {
        "temporal": "timeline",
        "factual": "lookup",
        "project_overview": "dossier",
        "cross_source": "summary",
        "pattern": "coach",
    }

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
        for pat in self._CROSS_SOURCE:
            if pat.search(query):
                return "cross_source", "summary", 0.80, None

        # Project overview
        for pat in self._PROJECT:
            if pat.search(query):
                return "project_overview", "dossier", 0.75, None

        # Pattern/coach
        for pat in self._PATTERN:
            if pat.search(query):
                return "pattern", "coach", 0.70, None

        # Default: factual
        return "factual", "lookup", 0.50, None


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
    W_SEMANTIC = 0.50
    W_RECENCY = 0.20
    W_TRUST = 0.15
    W_REINFORCE = 0.15

    # Intent-specific weight overrides
    _WEIGHT_OVERRIDES = {
        "temporal": {"W_SEMANTIC": 0.30, "W_RECENCY": 0.40},
        "pattern": {"W_REINFORCE": 0.30, "W_RECENCY": 0.10},
    }

    _TRUST_MAP = {
        "mature": 1.0,
        "incubating": 0.8,
        "reference": 0.7,
        "scratchpad": 0.5,
        "deprecated": 0.1,
    }

    def rerank(self, results, intent="factual"):
        """Compute final_score and sort descending."""
        overrides = self._WEIGHT_OVERRIDES.get(intent, {})
        w_sem = overrides.get("W_SEMANTIC", self.W_SEMANTIC)
        w_rec = overrides.get("W_RECENCY", self.W_RECENCY)
        w_trust = overrides.get("W_TRUST", self.W_TRUST)
        w_reinf = overrides.get("W_REINFORCE", self.W_REINFORCE)

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

            r["final_score"] = (w_sem * sem + w_rec * rec +
                                w_trust * trust + w_reinf * reinf)

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
                keys = [r.get("metadata", {}).get("source", "unknown")]

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

        # Step 3: Parse metadata from each result
        parsed = []
        for r in raw_results:
            entry = r.get("entry", "")
            metadata, body, snippet = self.parser.parse(entry)
            parsed.append({
                "corpus_id": r.get("corpus-id", ""),
                "khoj_score": r.get("score", 1.0),
                "entry": entry,
                "body": body,
                "snippet": snippet,
                "metadata": metadata,
                "file": r.get("additional", {}).get("file"),
            })

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
        reranked = self.reranker.rerank(filtered, intent=intent)

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
