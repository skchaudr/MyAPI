import uuid
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone

def parse_chatgpt_conversation(conversation: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parses a ChatGPT conversation dictionary and returns a CanonicalDocument dictionary.
    Traverses the conversation tree from the current_node backwards to reconstruct
    the conversation flow, ignoring unused branches.
    """
    # Helper to traverse the linked list
    def traverse_conversation(mapping: Dict[str, Any], current_node_id: Optional[str]) -> List[Dict[str, Any]]:
        messages = []
        node_id = current_node_id
        while node_id:
            node = mapping.get(node_id)
            if not node:
                break

            message = node.get("message")
            if message:
                author_role = message.get("author", {}).get("role", "")
                parts = message.get("content", {}).get("parts", [])

                # Combine parts into a single string
                text_parts = [str(part) for part in parts if isinstance(part, str)]
                text = "".join(text_parts).strip()

                if text:
                    messages.append({
                        "role": author_role,
                        "text": text
                    })

            # Move backwards in the tree
            node_id = node.get("parent")

        # Reverse to get chronological order (from root to leaf)
        messages.reverse()
        return messages

    mapping = conversation.get("mapping", {})
    current_node = conversation.get("current_node")

    # Extract chronological messages
    messages = traverse_conversation(mapping, current_node)

    # Format messages into markdown
    cleaned_markdown = ""
    for msg in messages:
        role = msg["role"].capitalize()
        text = msg["text"]
        cleaned_markdown += f"**{role}**: {text}\n\n"

    # Handle temporal data
    created_timestamp = conversation.get("create_time")
    updated_timestamp = conversation.get("update_time")

    # Convert timestamps if available
    created_at = None
    if created_timestamp:
        created_at = datetime.fromtimestamp(created_timestamp, timezone.utc).isoformat()

    updated_at = None
    if updated_timestamp:
        updated_at = datetime.fromtimestamp(updated_timestamp, timezone.utc).isoformat()

    title = conversation.get("title") or "Untitled Conversation"
    conversation_id = conversation.get("id") or str(uuid.uuid4())

    canonical_doc = {
        "id": conversation_id,
        "title": title,
        "source": {
            "system": "chatgpt",
            "type": "json"
        },
        "timestamps": {
            "created_at": created_at,
            "updated_at": updated_at,
            "ingested_at": datetime.now(timezone.utc).isoformat()
        },
        "author": "Me", # Defaulting as per the user's data exports
        "status": "scratchpad", # Default maturity
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

    return canonical_doc
