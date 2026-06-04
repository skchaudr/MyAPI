import json
import logging
import tempfile
import os
from fastapi import APIRouter, HTTPException, UploadFile, File, Body
from api.schemas import CanonicalDocumentResponse
from context_refinery.adapters.obsidian import parse_obsidian_file
from context_refinery.adapters.chatgpt import parse_chatgpt_conversation
from context_refinery.adapters.codex import scan_codex_sessions
from context_refinery.adapters.claude_code import scan_claude_sessions
from pydantic import BaseModel
from typing import Optional

router = APIRouter()
logger = logging.getLogger(__name__)

def validate_safe_path(user_path: Optional[str], base_dir: str) -> str:
    """Validates that a user-supplied path is strictly within the allowed base directory."""
    resolved_base = os.path.abspath(os.path.expanduser(base_dir))
    target_path = os.path.abspath(os.path.expanduser(user_path or base_dir))

    if os.path.commonpath([resolved_base, target_path]) != resolved_base:
        raise HTTPException(status_code=400, detail="Invalid path: Path traversal detected.")
    return target_path

class CodexImportRequest(BaseModel):
    root: Optional[str] = "~/.codex/command-logs"

class ClaudeCodeImportRequest(BaseModel):
    root: str = "~/.claude/projects"

@router.post("/obsidian", response_model=CanonicalDocumentResponse)
async def import_obsidian(file: UploadFile = File(...)):
    if not file.filename.endswith(".md"):
        raise HTTPException(status_code=400, detail="Only .md files are supported for Obsidian import.")

    with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        result = parse_obsidian_file(tmp_path)
        # Only override title if it wasn't extracted from frontmatter
        if "title" not in result or not result["title"]:
            result["title"] = file.filename.replace(".md", "")
        elif result.get("title") == tmp_path.split("/")[-1]:
            result["title"] = file.filename.replace(".md", "")

        if "source" in result:
            result["source"]["original_file_name"] = file.filename
        return CanonicalDocumentResponse(**result)
    except Exception as e:
        logger.error("An error occurred during Obsidian import", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal server error occurred")
    finally:
        os.remove(tmp_path)

@router.post("/chatgpt", response_model=list[CanonicalDocumentResponse])
async def import_chatgpt(file: UploadFile = File(...)):
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="Only .json files are supported for ChatGPT import.")

    content = await file.read()
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        raise HTTPException(status_code=422, detail="Invalid JSON file.")

    if isinstance(data, dict):
        data = [data]

    results = []
    for item in data:
        try:
            doc = parse_chatgpt_conversation(item)
            results.append(CanonicalDocumentResponse(**doc))
        except Exception as e:
            logger.error("Skipping a conversation due to parsing error", exc_info=True)

    return results

@router.post("/codex", response_model=list[CanonicalDocumentResponse])
async def import_codex(request: CodexImportRequest = CodexImportRequest()):
    try:
        safe_path = validate_safe_path(request.root, "~/.codex/command-logs")
        results = scan_codex_sessions(root=safe_path)

        parsed_results = []
        for doc in results:
            parsed_results.append(CanonicalDocumentResponse(**doc))

        return parsed_results
    except Exception as e:
        logger.error("Error scanning codex sessions", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal server error occurred")

@router.post("/claude-code", response_model=list[CanonicalDocumentResponse])
async def import_claude_code(request: ClaudeCodeImportRequest = ClaudeCodeImportRequest()):
    try:
        safe_path = validate_safe_path(request.root, "~/.claude/projects")
        docs = scan_claude_sessions(root=safe_path)
        return [CanonicalDocumentResponse(**doc) for doc in docs]
    except Exception as e:
        logger.error("Error importing claude code sessions", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal server error occurred")
