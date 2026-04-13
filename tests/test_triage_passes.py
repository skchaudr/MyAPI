import pytest
from context_refinery.triage.passes.status import StatusPass
from context_refinery.triage.passes.doctype import DocTypePass
from context_refinery.triage.passes.tags import TagsPass
from context_refinery.triage.passes.projects import ProjectsPass
from context_refinery.triage.passes.links import LinksPass

def test_status_pass_get_display_value():
    p = StatusPass()
    assert "scratchpad" in p.get_display_value({"status": "scratchpad"})

def test_doctype_pass_get_display_value():
    p = DocTypePass()
    assert "note" in p.get_display_value({"doc_type": "note"})

def test_tags_pass_get_display_value():
    p = TagsPass()
    assert "ai, web-dev" in p.get_display_value({"tags": ["ai", "web-dev", "python"]})

def test_projects_pass_get_display_value():
    p = ProjectsPass()
    assert "project1" in p.get_display_value({"projects": ["project1"]})

def test_links_pass_get_display_value():
    p = LinksPass()
    assert "2 links" in p.get_display_value({"related": ["note1", "note2"]})
