import os
import shutil
import logging
from typing import List
from fastapi import APIRouter, HTTPException
from api.schemas import CanonicalDocumentResponse

router = APIRouter()
logger = logging.getLogger(__name__)

EXPORT_DIR = os.path.join(os.getcwd(), "exports", "khoj-ready-bundle")

@router.post("/")
async def export_to_khoj_bundle(documents: List[CanonicalDocumentResponse]):
    try:
        # Clear previous exports to ensure a pristine bundle
        if os.path.exists(EXPORT_DIR):
            shutil.rmtree(EXPORT_DIR)
        os.makedirs(EXPORT_DIR, exist_ok=True)
        
        saved_files = []
        for doc in documents:
            filename = f"{doc.title}.md".replace("/", "-").replace("\\", "-")
            filepath = os.path.join(EXPORT_DIR, filename)
            
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
            
        return {
            "status": "success", 
            "message": f"Successfully exported {len(saved_files)} documents to {EXPORT_DIR}",
            "export_path": EXPORT_DIR
        }
    except Exception as e:
        logger.error(f"Failed to generate export bundle: {e}")
        raise HTTPException(status_code=500, detail=str(e))
