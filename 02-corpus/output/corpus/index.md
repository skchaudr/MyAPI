---
type: "decision-corpus-index"
schema_version: "1.0"
source: "01-decisions/output/decisions-canonical.jsonl"
source_sha256: "09c15aebd3a424e7f09ce2c27985fa0cbc24a23d9c474182ea4c912b926750a8"
decision_count: 17
project_homes:
  - "GDDP"
  - "Khoj"
  - "MyAPI"
  - "Pi"
---

# Canonical decision corpus

Generated deterministically from `01-decisions/output/decisions-canonical.jsonl` (17 decisions).

Project values remain verbatim in each decision's YAML frontmatter. Index homes are derived exclusively with `project.split("/")`; a multi-home decision is listed under every resulting home.

## Project homes

### GDDP

- [D01 — GDDP role vs harness](D01.md) — `GDDP`
- [D02 — Job disposal path](D02.md) — `GDDP`
- [D03 — No silent system-python eval fallback](D03.md) — `GDDP`
- [D04 — `agent` is literal, not wildcard](D04.md) — `GDDP`
- [D05 — Empty allow-list → operator / default executor](D05.md) — `GDDP`
- [D06 — Bookkeeping mismatch is evidence, not a hard block](D06.md) — `GDDP`
- [D07 — Human is last provisional gate](D07.md) — `GDDP`
- [D08 — Reject revokes dependent admission](D08.md) — `GDDP`
- [D09 — Nodes enter graphs only via import tool](D09.md) — `GDDP`
- [D10 — No merge-to-main by default on acceptance](D10.md) — `GDDP`
- [D12 — Prefer flow-on-provisional unless strict canary](D12.md) — `GDDP`
- [D13 — Prove pass-write and reject-revoke before mission scale](D13.md) — `GDDP`
- [D15 — Graphify structural, Khoj semantic](D15.md) — `MyAPI/Pi/GDDP`

### Khoj

- [D14 — Khoj corpus composition](D14.md) — `MyAPI/Khoj`

### MyAPI

- [D14 — Khoj corpus composition](D14.md) — `MyAPI/Khoj`
- [D15 — Graphify structural, Khoj semantic](D15.md) — `MyAPI/Pi/GDDP`
- [D16 — Decision scan order](D16.md) — `MyAPI`

### Pi

- [D15 — Graphify structural, Khoj semantic](D15.md) — `MyAPI/Pi/GDDP`
- [D17 — Read code before new machinery](D17.md) — `Pi`
- [D18 — No load-bearing unverified assumptions](D18.md) — `Pi`

## All decisions

- [D01 — GDDP role vs harness](D01.md) — `GDDP`
- [D02 — Job disposal path](D02.md) — `GDDP`
- [D03 — No silent system-python eval fallback](D03.md) — `GDDP`
- [D04 — `agent` is literal, not wildcard](D04.md) — `GDDP`
- [D05 — Empty allow-list → operator / default executor](D05.md) — `GDDP`
- [D06 — Bookkeeping mismatch is evidence, not a hard block](D06.md) — `GDDP`
- [D07 — Human is last provisional gate](D07.md) — `GDDP`
- [D08 — Reject revokes dependent admission](D08.md) — `GDDP`
- [D09 — Nodes enter graphs only via import tool](D09.md) — `GDDP`
- [D10 — No merge-to-main by default on acceptance](D10.md) — `GDDP`
- [D12 — Prefer flow-on-provisional unless strict canary](D12.md) — `GDDP`
- [D13 — Prove pass-write and reject-revoke before mission scale](D13.md) — `GDDP`
- [D14 — Khoj corpus composition](D14.md) — `MyAPI/Khoj`
- [D15 — Graphify structural, Khoj semantic](D15.md) — `MyAPI/Pi/GDDP`
- [D16 — Decision scan order](D16.md) — `MyAPI`
- [D17 — Read code before new machinery](D17.md) — `Pi`
- [D18 — No load-bearing unverified assumptions](D18.md) — `Pi`
