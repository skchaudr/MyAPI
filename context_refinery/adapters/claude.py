"""
Adapter for Claude.ai conversation exports (conversations.json from data export).

Each conversation has a flat chat_messages list with sender/text fields.
Much simpler than ChatGPT's tree structure.
"""

import uuid
from typing import Any, Dict, List
from datetime import datetime, timezone


def parse_claude_conversation(conversation: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parses a Claude.ai conversation dict and returns a CanonicalDocument dict.
    """
    messages = conversation.get("chat_messages", [])

    # Build markdown body from flat message list
    cleaned_markdown = ""
    for msg in messages:
        sender = msg.get("sender", "unknown")
        role = "Human" if sender == "human" else "Assistant"

        # text field is the primary content
        text = msg.get("text", "")

        # Some messages use content blocks instead of text
        if not text and msg.get("content"):
            parts = []
            for block in msg["content"]:
                if isinstance(block, dict) and block.get("type") == "text":
                    parts.append(block.get("text", ""))
                elif isinstance(block, str):
                    parts.append(block)
            text = "\n".join(parts)

        if text.strip():
            cleaned_markdown += f"**{role}**: {text.strip()}\n\n"

    # Timestamps
    created_at = conversation.get("created_at")
    updated_at = conversation.get("updated_at")

    title = conversation.get("name") or conversation.get("summary") or "Untitled Conversation"
    conversation_id = conversation.get("uuid") or str(uuid.uuid4())

    return {
        "id": conversation_id,
        "title": title,
        "source": {
            "system": "claude",
            "type": "json"
        },
        "timestamps": {
            "created_at": created_at,
            "updated_at": updated_at,
            "ingested_at": datetime.now(timezone.utc).isoformat()
        },
        "author": "Me",
        "status": "scratchpad",
        "doc_type": "conversation",
        "tags": [],
        "projects": [],
        "content": {
            "cleaned_markdown": cleaned_markdown.strip()
        },
        "quality": {
            "is_noisy": False,
            "warnings": []
        }
    }


def load_claude_export(zip_path: str) -> List[Dict[str, Any]]:
    """Load conversations.json from a Claude data export zip."""
    import json
    import zipfile

    with zipfile.ZipFile(zip_path) as z:
        data = json.loads(z.read("conversations.json"))

    return [parse_claude_conversation(conv) for conv in data]
