import os
import re
import json
import yaml
from datetime import datetime, timezone
from typing import List, Dict, Any
from .models import CanonicalDoc

class KhojExporter:
    @staticmethod
    def get_safe_filename(title: str, id: str) -> str:
        """Converts a string to a safe filesystem filename."""
        if not title and not id:
            return 'document.md'

        base = title if title else id

        # Lowercase
        base = base.lower()
        # Replace spaces with hyphens
        base = re.sub(r'\s+', '-', base)
        # Remove non-alphanumeric (except hyphens and underscores)
        base = re.sub(r'[^a-z0-9-_]', '', base)

        # Default to ID if title becomes empty after sanitization
        if not base:
            base = id

        return f"{base}.md"

    def export(self, docs: List[CanonicalDoc], output_dir: str) -> Dict[str, Any]:
        """
        Exports a list of CanonicalDoc objects to the specified output directory.
        Generates markdown files with YAML frontmatter and an output_manifest.json.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        manifest = {
            "exported_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"), # simulate JS toISOString format
            "documents": []
        }

        for doc in docs:
            filename = self.get_safe_filename(doc.title, doc.id)
            doc_path = os.path.join(output_dir, filename)

            frontmatter = {
                "id": doc.id,
                "title": doc.title,
                "provenance": doc.provenance,
                "timestamps": doc.timestamps,
                "status": doc.status,
                "tags": doc.tags,
                "projects": doc.projects,
                "doc_type": doc.doc_type,
                "quality_warnings": doc.quality_warnings
            }

            if doc.summary:
                frontmatter["summary"] = doc.summary

            yaml_string = yaml.dump(frontmatter, sort_keys=False)
            content = doc.content if doc.content else ''
            markdown_content = f"---\n{yaml_string}---\n\n{content}"

            with open(doc_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            manifest["documents"].append({
                "id": doc.id,
                "title": doc.title,
                "filename": filename,
                "path": doc_path
            })

        manifest_path = os.path.join(output_dir, 'output_manifest.json')
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)

        return manifest
