from context_refinery.normalization_schema import (
    V1Stamp,
    infer_primary_project,
    infer_source_type,
    infer_temporal_mode,
    merge_v1_into_frontmatter,
    stamp_from_path,
)


def test_infer_source_type_for_sab_air_obsidian_paths():
    assert (
        infer_source_type("/Users/sab-mini/Obsidian/SSD/02 Areas/MyAPI/Plan.md")
        == "project_doc"
    )
    assert (
        infer_source_type("/Users/sab-mini/Obsidian/SSD/03 Resources/Reference.md")
        == "reference"
    )
    assert (
        infer_source_type("/Users/sab-mini/Obsidian/SSD/04 Periodic/2026-07-01.md")
        == "daily_note"
    )


def test_infer_source_type_for_rebuild_project_docs_and_handoffs():
    assert (
        infer_source_type(
            "/Users/sab-mini/repos/MyAPI-rebuild/project-docs/source-type-taxonomy-plan.md"
        )
        == "project_doc"
    )
    assert (
        infer_source_type("/Users/sab-mini/repos/MyAPI-rebuild/.handoffs/001-port.md")
        == "handoff"
    )


def test_infer_source_type_for_codex_sessions_from_adapter_and_path():
    assert infer_source_type("ignored/path.jsonl", adapter="codex") == "cli_session"
    assert (
        infer_source_type(
            "/Users/sab-mini/.codex/sessions/2026/07/01/rollout-session.jsonl"
        )
        == "cli_session"
    )


def test_infer_temporal_mode_defaults():
    assert infer_temporal_mode("cli_session") == "episodic"
    assert infer_temporal_mode("conversation") == "episodic"
    assert infer_temporal_mode("daily_note") == "episodic"
    assert infer_temporal_mode("project_doc") == "meta"
    assert infer_temporal_mode("handoff") == "meta"


def test_infer_primary_project_from_path_and_title():
    assert infer_primary_project("/Users/sab-mini/repos/MyAPI-rebuild/README.md") == "myapi"
    assert infer_primary_project("/Users/sab-mini/Obsidian/SSD/02 Areas/Vault.md") == "vault"
    assert infer_primary_project("/tmp/note.md", title="Graph-driven GDDP plan") == "gddp"
    assert infer_primary_project("/tmp/unknown.md") == "unknown"


def test_stamp_from_path_combines_source_temporal_mode_and_project():
    stamp = stamp_from_path(
        "/Users/sab-mini/repos/MyAPI-rebuild/project-docs/source-type-taxonomy-plan.md"
    )

    assert stamp == V1Stamp(
        source_type="project_doc",
        temporal_mode="meta",
        primary_project="myapi",
    )


def test_merge_v1_into_frontmatter_preserves_existing_values_and_unknown_keys():
    existing = {
        "source_type": "reference",
        "temporal_mode": "",
        "primary_project": [],
        "review_status": "approved",
        "custom": "keep-me",
    }
    stamp = V1Stamp(
        source_type="project_doc",
        temporal_mode="meta",
        primary_project="myapi",
        work_type=["project_work"],
        thread_type="execution",
    )

    merged = merge_v1_into_frontmatter(existing, stamp)

    assert merged["source_type"] == "reference"
    assert merged["temporal_mode"] == "meta"
    assert merged["primary_project"] == "myapi"
    assert merged["review_status"] == "approved"
    assert merged["work_type"] == ["project_work"]
    assert merged["thread_type"] == "execution"
    assert merged["custom"] == "keep-me"


def test_merge_v1_into_frontmatter_accepts_empty_existing_frontmatter():
    stamp = V1Stamp(source_type="handoff", temporal_mode="meta", primary_project="myapi")

    assert merge_v1_into_frontmatter({}, stamp) == {
        "source_type": "handoff",
        "temporal_mode": "meta",
        "primary_project": "myapi",
        "review_status": "inferred",
    }
