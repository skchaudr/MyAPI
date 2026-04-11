import pytest
from pydantic import ValidationError
from datetime import datetime
from context_refinery.models import CanonicalDocument

def test_valid_document_string_date():
    doc = CanonicalDocument(
        id="doc1",
        source_type="obsidian",
        content="This is a test content.",
        metadata={"author": "Jules"},
        tags=["test", "pytest"],
        created_at="2023-10-27T10:00:00Z"
    )
    assert doc.id == "doc1"
    assert doc.source_type == "obsidian"
    assert doc.content == "This is a test content."
    assert doc.metadata == {"author": "Jules"}
    assert doc.tags == ["test", "pytest"]
    assert doc.created_at == "2023-10-27T10:00:00Z"

def test_valid_document_datetime():
    dt = datetime.now()
    doc = CanonicalDocument(
        id="doc2",
        source_type="slack",
        content="Hello world",
        metadata={},
        tags=[],
        created_at=dt
    )
    assert doc.created_at == dt

def test_invalid_document_missing_fields():
    with pytest.raises(ValidationError):
        CanonicalDocument(
            id="doc3",
            source_type="slack"
        )

def test_invalid_document_wrong_type():
    with pytest.raises(ValidationError):
        CanonicalDocument(
            id={"invalid": "type"}, # should be str, dict is not coercible
            source_type="slack",
            content="Hello world",
            metadata={},
            tags=[],
            created_at=datetime.now()
        )
