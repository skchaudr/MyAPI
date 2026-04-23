# Vault Schema V4 Normalizer Plan

Schema source: `/Users/saboor/obsidian/SoloDeveloper/09 Utilities/_Vault System/Vault Schema V4 Reference.md`

## Core Loop

Capture without hesitation -> normalize with intent -> connect through concepts.

The normalizer should handle structural metadata and route uncertain notes into an owner pass.

## Machine-Owned Fields

These can be inferred safely from path, filename, and existing frontmatter:

- `type`
- `status` for `project` and `event`
- `area`
- `project`
- `tags`
- `folder_origin`
- `migration_status`
- destination folder

## Owner-Owned Fields

These remain judgment-heavy:

- `concepts`
- semantic `related` links
- source-of-truth claims
- summaries
- decisions
- source evidence

## Confidence Model

High confidence:

- old folder path maps clearly to a V4 folder
- existing frontmatter does not conflict with inferred type
- area or project can be inferred from the old path
- tags are already prefixed or can be conservatively inferred

Medium confidence:

- mostly valid metadata but needs tag cleanup or concept assignment
- archive/private/system routing is clear but type needs review

Needs review:

- type conflict between current frontmatter and inferred path
- no area/project/concept connection
- status exists on a type where V4 says status should not apply
- invalid tags or unprefixed tags dominate the note

## Migration Rule

Normalize metadata before flattening folders.

The current folder tree contains useful signal:

- `00 Inbox` -> `inbox/`
- `01 Projects` -> `projects/`
- `02 Areas` -> `areas/`
- `03 Resources` -> `resources/`
- `04 Periodic` -> `periodics/`
- `05 Archive` -> `archive/`
- `09 Utilities` and `Templates` -> `system/`
- `Confidential` path segments -> `_private/`

## Pilot Command

Run on Mac:

```bash
python3 scripts/normalize_vault_schema_v4.py --limit 50
```

## Full Dry Run

Run on Mac:

```bash
python3 scripts/normalize_vault_schema_v4.py
```

## Outputs

- `project-docs/vault-schema-v4-normalization-dry-run.md`
- `project-docs/vault-schema-v4-normalization-dry-run.json`

## Adoption Rule

The first useful win is not perfect classification.

The first useful win is shrinking the owner pass to the notes where human judgment actually matters.
