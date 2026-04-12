import json
import logging
import tempfile
import os
from fastapi import APIRouter, HTTPException, UploadFile, File
from api.schemas import CanonicalDocumentResponse
from context_refinery.adapters.obsidian import parse_obsidian_file
from context_refinery.adapters.chatgpt import parse_chatgpt_conversation

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/obsidian", response_model=CanonicalDocumentResponse)
async def import_obsidian(file: UploadFile = File(...)):
    if not file.filename.endswith(".md"):
        raise HTTPException(status_code=400, detail="Only .md files are supported for Obsidian import.")

    with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        result = parse_obsidian_file(tmp_path)
        # Override the title and filename because the tempfile obscures them
        result["title"] = file.filename.replace(".md", "")
        if "source" in result:
            result["source"]["original_file_name"] = file.filename
        return CanonicalDocumentResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
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
            logger.error(f"Skipping a conversation due to parsing error: {e}")

    return results
