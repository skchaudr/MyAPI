#!/usr/bin/env python3
"""
Batch ingest — runs all adapters and writes .md files ready for Khoj deployment.

Usage:
    python3 ingest_all.py [--output-dir ./khoj-ready-bundle]

Sources:
    1. ChatGPT   — conversations.json from export zip
    2. Codex CLI  — ~/.codex/command-logs/
    3. Claude Code — ~/.claude/projects/
"""

import argparse
import json
import logging
import os
import sys
import re
import yaml
from datetime import datetime, timezone

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from context_refinery.adapters.chatgpt import parse_chatgpt_conversation
from context_refinery.adapters.codex import scan_codex_sessions
from context_refinery.adapters.claude_code import scan_claude_sessions

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Field order per docs/02-target-output.md
FIELD_ORDER = [
    "id", "title", "source", "created_at", "author",
    "status", "doc_type", "tags", "projects",
]


def slugify(text, max_len=60):
    """Turn a title into a safe filename slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text[:max_len] or "untitled"


def doc_to_markdown(doc):
    """Convert a CanonicalDoc dict to a frontmatter + body markdown string."""
    fm = {}
    # Flatten timestamps into frontmatter
    fm["id"] = doc.get("id", "")
    fm["title"] = doc.get("title", "")
    fm["source"] = doc.get("source", {}).get("system", "")
    fm["created_at"] = doc.get("timestamps", {}).get("created_at", "")
    fm["author"] = doc.get("author", "")
    fm["status"] = doc.get("status", "scratchpad")
    fm["doc_type"] = doc.get("doc_type", "conversation")
    fm["tags"] = doc.get("tags", [])
    fm["projects"] = doc.get("projects", [])

    # Ordered frontmatter
    ordered = {}
    for key in FIELD_ORDER:
        if key in fm:
            ordered[key] = fm[key]

    yaml_str = yaml.dump(ordered, default_flow_style=False, sort_keys=False, allow_unicode=True)

    # Body content
    body = doc.get("content", {}).get("cleaned_markdown", "")
    if not body:
        body = doc.get("content", {}).get("raw_text", "")
    if not body:
        summary = doc.get("content", {}).get("summary", "")
        body = summary if summary else "(no content)"

    return f"---\n{yaml_str}---\n\n{body}\n"


def ingest_chatgpt(conversations_path, output_dir):
    """Process ChatGPT conversations.json and write .md files."""
    logger.info(f"Loading ChatGPT conversations from {conversations_path}")

    with open(conversations_path, "r", encoding="utf-8") as f:
        conversations = json.load(f)

    logger.info(f"Found {len(conversations)} ChatGPT conversations")

    written = 0
    failed = 0
    seen_slugs = set()

    for conv in conversations:
        try:
            doc = parse_chatgpt_conversation(conv)
            title = doc.get("title", "untitled")
            slug = slugify(title)

            # Deduplicate filenames
            base_slug = slug
            counter = 1
            while slug in seen_slugs:
                slug = f"{base_slug}-{counter}"
                counter += 1
            seen_slugs.add(slug)

            md_content = doc_to_markdown(doc)
            filename = f"chatgpt-{slug}.md"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md_content)
            written += 1
        except Exception as e:
            failed += 1
            if failed <= 5:
                logger.warning(f"ChatGPT parse error: {e}")

    logger.info(f"ChatGPT: {written} written, {failed} failed")
    return written


def ingest_codex(output_dir):
    """Process Codex CLI sessions and write .md files."""
    logger.info("Scanning Codex sessions...")
    docs = scan_codex_sessions()
    logger.info(f"Found {len(docs)} Codex sessions")

    written = 0
    for doc in docs:
        try:
            title = doc.get("title", "untitled")
            session_id = doc.get("id", "unknown")[:8]
            slug = slugify(title)
            filename = f"codex-{slug}-{session_id}.md"
            filepath = os.path.join(output_dir, filename)

            md_content = doc_to_markdown(doc)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md_content)
            written += 1
        except Exception as e:
            logger.warning(f"Codex write error: {e}")

    logger.info(f"Codex: {written} written")
    return written


def ingest_claude_code(output_dir):
    """Process Claude Code sessions and write .md files."""
    logger.info("Scanning Claude Code sessions...")
    docs = scan_claude_sessions()
    logger.info(f"Found {len(docs)} Claude Code sessions")

    written = 0
    for doc in docs:
        try:
            title = doc.get("title", "untitled")
            session_id = doc.get("id", "unknown")[:8]
            slug = slugify(title)
            filename = f"claude-{slug}-{session_id}.md"
            filepath = os.path.join(output_dir, filename)

            md_content = doc_to_markdown(doc)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md_content)
            written += 1
        except Exception as e:
            logger.warning(f"Claude Code write error: {e}")

    logger.info(f"Claude Code: {written} written")
    return written


def main():
    parser = argparse.ArgumentParser(description="Batch ingest all data sources to .md files for Khoj")
    parser.add_argument("--output-dir", default="./khoj-ready-bundle",
                        help="Output directory for .md files (default: ./khoj-ready-bundle)")
    parser.add_argument("--chatgpt", default=None,
                        help="Path to ChatGPT conversations.json")
    parser.add_argument("--skip-chatgpt", action="store_true",
                        help="Skip ChatGPT ingestion")
    parser.add_argument("--skip-codex", action="store_true",
                        help="Skip Codex session ingestion")
    parser.add_argument("--skip-claude", action="store_true",
                        help="Skip Claude Code session ingestion")
    args = parser.parse_args()

    output_dir = os.path.expanduser(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)

    total = 0
    start = datetime.now(timezone.utc)

    logger.info(f"Output directory: {output_dir}")
    logger.info("=" * 50)

    # ChatGPT
    if not args.skip_chatgpt:
        chatgpt_path = args.chatgpt
        if not chatgpt_path:
            # Auto-detect common locations
            candidates = [
                os.path.expanduser("~/repos/chatgpt_ALL_CONVOS-2026-02-01/conversations.json"),
                os.path.expanduser("~/Downloads/conversations.json"),
            ]
            for c in candidates:
                if os.path.exists(c):
                    chatgpt_path = c
                    break

        if chatgpt_path and os.path.exists(chatgpt_path):
            total += ingest_chatgpt(chatgpt_path, output_dir)
        else:
            logger.warning("ChatGPT conversations.json not found. Use --chatgpt to specify path, or --skip-chatgpt.")

    # Codex
    if not args.skip_codex:
        total += ingest_codex(output_dir)

    # Claude Code
    if not args.skip_claude:
        total += ingest_claude_code(output_dir)

    elapsed = (datetime.now(timezone.utc) - start).total_seconds()
    logger.info("=" * 50)
    logger.info(f"Done. {total} files written to {output_dir} in {elapsed:.1f}s")
    logger.info(f"Next: ./deploy_to_brain.sh  (enter: {output_dir})")


if __name__ == "__main__":
    main()
