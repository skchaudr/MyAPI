# V4 Triage CLI Brief

Purpose: align Codex and Claude on the interactive owner-pass tool after the batch normalizer has handled high-confidence structural metadata.

Schema source: `/Users/saboor/obsidian/SoloDeveloper/09 Utilities/_Vault System/Vault Schema V4 Reference.md`

## Product Goal

The CLI should make the owner pass feel light, fast, and obvious.

The batch normalizer owns repetitive structural metadata. The CLI owns judgment:

- ambiguous type
- conditional status for projects/events
- project link
- concepts
- tags that need human cleanup
- related notes

## Workflow Position

1. Batch normalizer writes high-confidence V4 structural metadata.
2. CLI opens medium/review notes from the generated report.
3. User confirms or fixes only the fields that need judgment.
4. Reindex Khoj.
5. Rerun retrieval benchmark.

## V4 Schema Rules

### `type`

Allowed values:

- `project`
- `area`
- `resource`
- `concept`
- `event`
- `periodic`

Default when unclear: `resource`.

Removed V3/legacy values:

- `log`
- `task`
- `utility`
- `note`
- `conversation`
- `spec`
- `article`
- `other`

### `status`

Allowed values:

- `active`
- `backlog`
- `blocked`
- `done`

Only applies when:

- `type: project`
- `type: event`

For all other types, the CLI should not prompt for status and should remove stale status during write.

### `format`

Removed.

`topic/log` and `topic/howto` tags replace the old format field.

The default pipeline should not include `FormatPass`.

### `area`

Almost always present.

Shape:

```yaml
area: "[[Area Name]]"
```

### `project`

Optional, only when relevant.

Shape:

```yaml
project: "[[--Project Name]]"
```

This replaces the old ambiguous plural `projects` field for V4 owner-pass work.

### `concepts`

One to three wikilinks.

Shape:

```yaml
concepts:
  - "[[Automation]]"
  - "[[AI Tooling]]"
```

Concepts are owner-owned. The CLI should make them easy to add, but the batch normalizer should not invent them.

### `tags`

Maximum: 3.

Allowed prefixes:

- `topic/`
- `tool/`
- `lang/`
- `scope/`

Required presets:

- `topic/log`
- `topic/howto`

## CLI Menu Target

Replace V3 labels with V4 labels:

```text
1. V4 Owner Pass (type -> project/status if needed -> area -> concepts -> tags -> related)
2. Type only
3. Project only
4. Status only
5. Area only
6. Concepts only
7. Tags only
8. Related only
9. Custom pipeline
```

The old `V3 Normalize` option should become `V4 Owner Pass`.

The old `Format only` option should disappear.

## Pass Changes

### `TypePass`

Update constants to:

```python
TYPE_VALUES = {
    "1": "project",
    "2": "area",
    "3": "resource",
    "4": "concept",
    "5": "event",
    "6": "periodic",
}
```

### `StatusPass`

Behavior:

- If record type is `project` or `event`, prompt normally.
- Otherwise skip automatically and clear stale status during write.

Display text should say `STATUS (projects/events only)`.

### `FormatPass`

Remove from default menu and default pipeline.

Keep the file only temporarily if backward compatibility is useful, but do not export it from the active V4 flow.

### `TagsPass`

Update behavior:

- max 3 tags
- include `topic/log`
- include `topic/howto`
- preserve prefix rule
- flag or discourage unprefixed tags

### `ProjectPass`

V4 needs singular `project`, not plural `projects`.

Behavior:

- writes `project: "[[--Project Name]]"`
- optional for notes where no project applies
- should be prompted after type, because type can influence relevance

### `V4SchemaPass`

Rename or replace `V3SchemaPass`.

Responsibilities:

- fill missing type with default `resource`
- validate V4 type set
- prompt status only for project/event
- prompt area if no area/project/concept connection exists
- prompt project when relevant
- prompt concepts
- prompt tags
- skip complete files

It should not prompt for `format`.

## Writer Changes

Frontmatter order:

```yaml
title:
aliases:
type:
status:
area:
project:
concepts:
tags:
related:
folder_origin:
migration_status:
source:
created:
modified:
```

Write behavior:

- preserve unknown existing fields after known fields
- remove `format`
- remove `status` unless type is project/event
- prefer `project` over old `projects`
- preserve old fields only if present and not actively deprecated

## UX Principles

- Enter accepts a safe default.
- `s` skips current field or file.
- `q` exits the current pass.
- Show why a file is in the owner queue when possible.
- Show existing value and suggested value side by side.
- Avoid making the user review fields that the batch normalizer already handled confidently.

## Implementation Sequence

1. Update `TypePass`.
2. Update `TagsPass`.
3. Add/convert singular `ProjectPass`.
4. Replace `V3SchemaPass` with `V4SchemaPass`.
5. Update `runner.py` menu and default pipeline.
6. Update writer field order and V4 cleanup behavior.
7. Update tests.
8. Run targeted triage tests.
9. Run full test suite.

## Test Expectations

Add tests for:

- V4 type values include `event` and `periodic`.
- V4 type values exclude `log`, `task`, `utility`.
- Status is retained for project/event.
- Status is removed for resource/area/concept/periodic.
- `format` is removed from writes.
- tags allow max 3.
- `topic/log` and `topic/howto` are presets.
- singular `project` survives frontmatter round trip.

## First Real Use

After code changes, use the CLI against the My_DevInfra medium/review queue, not the entire vault.

That keeps the owner pass focused and avoids recreating brute-force triage.
