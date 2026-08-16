# Corpus reproducibility report

**Node:** `node-06-build-corpus`  
**Execution attempt:** `job_20260814T221953847cb1e568ca22:attempt:0`  
**Checked:** 2026-08-14  
**Base commit:** `d301bd26fccf285a546b1935830c4db43d245b99`  
**Result:** **PASS — a clean temporary rebuild has the identical file set and bytes as `02-corpus/output/corpus/`.**

## Fixed input

| Input | SHA-256 | Records |
|---|---|---:|
| `01-decisions/output/decisions-canonical.jsonl` | `09c15aebd3a424e7f09ce2c27985fa0cbc24a23d9c474182ea4c912b926750a8` | 17 |

## Rebuild procedure

Run on Mac, from the repository root. The check created a new `mktemp` directory, invoked the builder against the canonical JSONL, compared the checked snapshot and temporary rebuild recursively, and then removed only that temporary directory.

```bash
python3 02-corpus/build_corpus.py --input 01-decisions/output/decisions-canonical.jsonl --output "$tmp_dir/corpus"
diff -qr 02-corpus/output/corpus "$tmp_dir/corpus"
```

A Python standard-library SHA-256 manifest was also computed independently for every relative file path in both directories and compared as dictionaries.

## Evidence

| Check | Result |
|---|---|
| Builder exit | `0` |
| Builder output | `built 17 decisions + index` |
| Checked snapshot file count | `18` |
| Temporary rebuild file count | `18` |
| `diff -qr` exit | `0` (no output) |
| Relative-path SHA-256 manifest entries | `18` |
| Manifest equality | `true` |

The identical manifest proves both the file-set and byte-for-byte checks. There are no differences to explain or fix.

## Snapshot shape and taxonomy check

- `D01.md` through the 17 admitted canonical IDs provide one Markdown document per decision; `index.md` is the eighteenth file.
- Decision YAML frontmatter preserves each canonical `project` value verbatim, including `MyAPI/Khoj` and `MyAPI/Pi/GDDP`.
- The index derives homes only with `project.split("/")`, so multi-home decisions appear under each resulting home without changing their frontmatter.
- The builder and check did not read or modify graph truth or any runtime database.
