import pytest

from context_refinery.context_packets import (
    ContextBrief,
    ContextPacketError,
    packet_from_ctxpack,
)


def test_packet_from_ctxpack_json_style_payload():
    payload = {
        "summary": {"item_count": 2, "chars": 72, "approx_tokens": 18},
        "items": [
            {
                "path": "02 Areas/MyAPI/Anchor.md",
                "depth": 0,
                "mtime": 1782864000.0,
                "chars": 44,
                "content": "# Anchor\nMyAPI rebuild direction.",
                "approx_tokens": 11,
            },
            {
                "path": "02 Areas/MyAPI/Risks.md",
                "depth": 1,
                "mtime": 1782864100.0,
                "chars": 28,
                "content": "Open risk: source defaults.",
                "approx_tokens": 7,
            },
        ],
    }

    packet = packet_from_ctxpack(payload)

    assert packet.source == "ctxpack"
    assert packet.total_chars == 72
    assert packet.approx_tokens == 18
    assert packet.evidence_paths == [
        "02 Areas/MyAPI/Anchor.md",
        "02 Areas/MyAPI/Risks.md",
    ]
    assert packet.as_dict()["summary"]["item_count"] == 2


def test_packet_rejects_missing_items_list():
    with pytest.raises(ContextPacketError, match="items list"):
        packet_from_ctxpack({"summary": {}})


def test_context_brief_renders_and_validates_envelope_from_packet():
    packet = packet_from_ctxpack(
        {
            "items": [
                {
                    "path": "project-documents/REBUILD-CONTEXT-ANCHOR.md",
                    "depth": 0,
                    "content": "Rebuild MyAPI around durable handoffs and ContextBriefs.",
                }
            ]
        }
    )

    brief = ContextBrief.from_packet(
        packet,
        subject="MyAPI-rebuild",
        intent="project_overview",
        context_type="project",
        short_answer=(
            "MyAPI-rebuild should return a human-checkable ContextBrief backed "
            "by bounded packet evidence."
        ),
        why_this_matters=(
            "The same contract can feed goldens, aa-cli handoffs, and future MCP calls."
        ),
        open_risks=["MCP integration still needs to consume the envelope."],
    )
    envelope = brief.as_envelope()

    assert envelope["metadata"]["brief_id"] == "project_overview:myapi-rebuild"
    assert envelope["metadata"]["intent"] == "project_overview"
    assert envelope["metadata"]["packet"]["item_count"] == 1
    assert envelope["metadata"]["evidence_paths"] == [
        "project-documents/REBUILD-CONTEXT-ANCHOR.md"
    ]
    assert "## Short Answer" in envelope["markdown"]
    assert "## Evidence" in envelope["markdown"]
    assert "MCP integration still needs" in envelope["markdown"]


def test_context_brief_validation_requires_evidence_paths():
    brief = ContextBrief(
        subject="No Evidence",
        intent="project_overview",
        context_type="project",
        markdown=(
            "# Context Brief: No Evidence\n\n"
            "## Short Answer\nEmpty.\n\n"
            "## Evidence\n- No evidence paths supplied.\n\n"
            "## Open Risks / Unknowns\n- Missing evidence.\n"
        ),
    )

    with pytest.raises(ContextPacketError, match="evidence path"):
        brief.as_envelope()
