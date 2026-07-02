# MyAPI Reuse Map - 2026-07-01

Purpose: prevent repeat work while moving existing MyAPI normalization into
MyAPI-rebuild. Source repo inspected read-only: `/Users/sab-mini/repos/MyAPI`.

## Short Answer

MyAPI-rebuild already contains the legacy `context_refinery` parser surface,
including the Obsidian adapter and tests. The repeat-work risk is rebuilding
the later corpus-v1 normalization layer from scratch: `normalization_schema.py`,
`normalize_corpus.py`, and the vault-v1 materializer already solve path-based
source typing, metadata stamping, provenance frontmatter, generated-note safety,
and owner-review queues.

Recommended first slice: copy `context_refinery/normalization_schema.py` into
MyAPI-rebuild, add focused tests for `stamp_from_path()` and
`merge_v1_into_frontmatter()`, then wrap the existing Obsidian adapter so parsed
notes can receive v1 stamps without changing its current tests.

## Reuse Candidates

| Existing module/file | What it already solves | Decision | First rebuild integration point |
|---|---|---|---|
| `MyAPI/context_refinery/adapters/obsidian.py` | Reads Markdown, parses YAML frontmatter, normalizes tags/projects, applies safe defaults for `author`, `status`, `doc_type`, timestamps, summary, URL, raw body, and short-content warnings. | Reuse as the compatibility parser. It is byte-identical to `MyAPI-rebuild/context_refinery/adapters/obsidian.py`, so do not recopy it unless the source changes. | Keep `MyAPI-rebuild/context_refinery/adapters/obsidian.py` stable and add a separate normalization wrapper that enriches the returned canonical doc. |
| `MyAPI/context_refinery/normalization_schema.py` | Defines corpus-v1 vocabulary, path/adapter source typing, temporal mode inference, primary-project inference, `V1Stamp`, and a merge helper that preserves existing frontmatter. | Copy into MyAPI-rebuild. This is the missing reusable core. | Add `MyAPI-rebuild/context_refinery/normalization_schema.py` plus tests for Obsidian paths, CLI-session adapters, and preservation of hand-curated fields. |
| `MyAPI/scripts/normalize_corpus.py` | Provides a scan/copy/inspect CLI across Obsidian, repo docs, ChatGPT, Claude web, Claude Code, and Codex; materializes Markdown with v1 metadata while reusing existing adapters. | Wrap/copy in slices, not whole-script first. The scanner and stamp/copy helpers are useful; host-specific defaults need rebuild paths. | Extract the Obsidian/repo-doc scan and `copy_markdown_entry()` path into a small rebuild command after the schema lands. |
| `MyAPI/scripts/build_vault_v1.py` | Builds a visible Obsidian vault from selected raw corpus files; handles provenance frontmatter, generated-note overwrite safety, source-family folders, conversation/session rendering, manifests, reports, and validation. | Reuse design and selected helpers; do not drop it in unchanged. It is a materializer for a specific frozen corpus layout. | Port `split_frontmatter()`, `write_generated_note()`, `provenance_fm()`, and generated-note safety into the rebuild reader/export layer. |
| `MyAPI/scripts/build_vault_v1_owner_queue.py` | Scans generated vault notes for metadata-floor violations, forbidden fields, invalid roles, malformed list fields, duplicate clusters, and secret-shaped values; emits JSON and Markdown review queues. | Reuse as owner-review logic. It is valuable after the first generated notes exist. | Adapt required fields and valid note roles to the rebuild's handoff/context-brief schema, then run it on generated examples. |
| `MyAPI-rebuild/context_refinery/adapters/obsidian.py` | Existing copied adapter, currently identical to MyAPI source. | Keep. It protects existing parser behavior and keeps tests green. | Add integration beside it, not inside it, until the v1 stamp behavior has its own tests. |
| `MyAPI-rebuild/tests/test_obsidian.py` | Verifies the current parser contract: frontmatter parsing, defaults, list coercion, summary/URL extraction, short-content warning, missing-file error. | Keep and extend around new wrapper behavior. | Add a new test file for normalization schema first; later add an adapter-wrapper test that proves parsed Obsidian docs can be stamped. |

## Repeat-Work Risks

- Rebuilding source classification would duplicate `infer_source_type()` and lose
  already encoded rules for Obsidian paths, repo docs, daily notes, and CLI/chat
  adapters.
- Rewriting frontmatter merging would risk overwriting operator-curated metadata;
  `merge_v1_into_frontmatter()` already preserves existing values.
- Expanding `parse_obsidian_file()` directly would blur parser behavior with
  corpus-v1 stamping. Keeping a wrapper preserves the tested parser contract.
- Treating `build_vault_v1.py` as only a script would miss its reusable safety
  primitives: generated-note overwrite checks, provenance fields, manifests, and
  failure reports.
- Delaying owner-queue reuse would repeat manual review logic for missing fields,
  duplicate groups, invalid roles, and secret-shaped metadata.

## Recommended First Implementation Slice

1. Copy `MyAPI/context_refinery/normalization_schema.py` to
   `MyAPI-rebuild/context_refinery/normalization_schema.py`.
2. Add focused tests for `stamp_from_path()` and `merge_v1_into_frontmatter()`.
3. Add a small wrapper, for example `normalize_obsidian_document(path, rel_path)`,
   that calls `parse_obsidian_file()` and attaches/returns the v1 stamp without
   changing existing parser output.
4. Use that wrapper as the first rebuild integration point for the reader layer:
   Obsidian note -> canonical parser result -> v1 stamp -> future
   handoff/context-brief graph input.

That slice builds on existing code, keeps the old parser tests intact, and makes
the missing normalization contract available before porting larger materializer
scripts.
