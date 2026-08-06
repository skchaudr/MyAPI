import os
import shutil
import logging
import asyncio
from typing import List
from fastapi import APIRouter, HTTPException
from api.schemas import CanonicalDocumentResponse

router = APIRouter()
logger = logging.getLogger(__name__)

EXPORT_DIR = os.path.join(os.getcwd(), "exports", "khoj-ready-bundle")

def _process_export(documents: List[CanonicalDocumentResponse], export_dir: str):
    if os.path.exists(export_dir):
        shutil.rmtree(export_dir)
    os.makedirs(export_dir, exist_ok=True)

    saved_files = []
    for doc in documents:
        filename = f"{doc.title}.md".replace("/", "-").replace("\\", "-")
        filepath = os.path.join(export_dir, filename)
        
        # Construct Khoj-optimized markdown with frontmatter
        frontmatter = f"""---
title: "{doc.title}"
source: "{doc.source.system}"
doc_type: "{doc.doc_type}"
tags: {doc.tags}
author: "{doc.author}"
status: "{doc.status}"
---

"""
        # Prefer the summary if available, otherwise fallback to cleaned markdown or raw text
        content = doc.content.summary or doc.content.cleaned_markdown or doc.content.raw_text

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + content)
            
        saved_files.append(filepath)
    return saved_files

@router.post("/")
async def export_to_khoj_bundle(documents: List[CanonicalDocumentResponse]):
    try:
        loop = asyncio.get_running_loop()
        saved_files = await loop.run_in_executor(None, _process_export, documents, EXPORT_DIR)

        return {
            "status": "success", 
            "message": f"Successfully exported {len(saved_files)} documents to {EXPORT_DIR}",
            "export_path": EXPORT_DIR
        }
    except Exception:
        logger.error("Failed to generate export bundle", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal server error occurred")
