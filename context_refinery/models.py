from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional

@dataclass
class CanonicalDoc:
    id: str
    content: str
    title: Optional[str] = None
    provenance: Dict[str, Any] = field(default_factory=dict)
    timestamps: Dict[str, Any] = field(default_factory=dict)
    status: str = "draft"
    tags: List[str] = field(default_factory=list)
    projects: List[str] = field(default_factory=list)
    doc_type: str = "document"
    quality_warnings: List[str] = field(default_factory=list)
    summary: Optional[str] = None
