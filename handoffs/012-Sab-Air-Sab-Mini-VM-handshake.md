# 002 — Sab-Air · Sab-Mini · VM handshake

**Date:** 2026-08-08  
**Written on:** `khoj-38` (this VM) as `sab-mini` / work under `/home/saboor`  
**Audience:** next session on **Sab Air**, **Sab Mini**, or **this VM** after a host drop  
**Scope:** the two main projects — **aa-cli** and **MyAPI** — plus the durability failure that made this handshake necessary

**Durable copy (git):** `MyAPI/handoffs/012-Sab-Air-Sab-Mini-VM-handshake.md` on branch `docs/semantic-graphify-cold-start-capture` (and later wherever this branch lands).

Original VM-root drop (may still exist on host):

```text
/home/saboor/002-Sab-Air-Sab-Mini-VM-handshake.md
```

Prefer the git path. Pull MyAPI; do not rely on VM home root alone.

---

## 1. What went wrong

### 1.1 The failure mode

Work was done on a **remote VM** and treated as “safe enough” because it was on disk and in an agent session. That is false durability.

| Wrong assumption | Reality |
|------------------|---------|
| Untracked `.scratch/` / wayfinder maps will still be here later | Host sleeps, dies, or is unreachable for ~**36h+** → operator cannot reach the work |
| “I’ll commit after Sab reviews” | Review never happens on a dead host; gold dies with the VM |
| Session transcript is the backup | Compaction / lost context / different machine = redo the wayfinder |
| Local commit alone is enough | On a VM, **push (or SCP)** is the backup; local-only git dies with the disk |

Concrete pain this cycle:

1. **Wayfinder / intent work** (product grilling → ticket maps → proposed GDDP nodes) was at risk of being **untracked on the VM**.
2. When the VM was down, Sab could not reach that work and had to **re-run / clean up** the process on a second pass.
3. The second pass was **cleaner** (pros of the failure), but the **cost** was real: redoing multi-hour intent capture that should have been on `origin`.

### 1.2 Process fix (already landed in repos)

Both main projects now carry an explicit **commit + push non-trivial work** rule for agents:

| Repo | Where |
|------|--------|
| **aa-cli** | `AGENTS.md` § “Durability — commit and push non-trivial work” (on `main`) |
| **MyAPI** | `AGENTS.md` + `.agents/rules/durable-work.md` + `.grok/rules/durable-work.md` (on docs branch + related commits) |

Global operator rule (Mini/Air side): durable work on VM hosts must commit early and push or SCP — see operator durable-work rules.

**Anti-pattern still forbidden:** “leave it in `.scratch/` untracked until review.”

### 1.3 What was *not* the main bug

- Not “wayfinder is bad.” Wayfinder did its job (intent lock).
- Not “GDDP failed.” GDDP was never the on-ramp; promotion was still pending by design.
- Not “Create vs Verify product confusion forever.” Product intent was locked; the durability layer failed under it.

---

## 2. Overall driving mission

One pipeline, two project instances:

```text
wayfinder (grill / decide)
    → map of nodes (tickets + proposed YAML under .scratch/)
    → human review / edit
    → promote into GDDP (canonical graph)
    → factory-droid / GDDP execute
    → evidence + human truth
```

| Layer | Owns | Does not own |
|-------|------|--------------|
| **Wayfinder** | Fog clear, product cuts, ticket maps, research | Dispatch, “done in production” |
| **Node map (`.scratch/`)** | Proposed graph shape; reviewable before promote | Canonical truth until human promotes |
| **GDDP config / graph** | Human-owned nodes, depends_on, acceptance | Inventing product identity mid-flight |
| **GDDP runtime / factory-droid** | Mission plan, execute, receipts | Silently rewriting intent |
| **Human (Sab)** | Accept / refire / refine; graph truth advancement | Blind autonomous loops |

**aa-cli instance of the mission:** Verify pathway as the stronger product half → usable Verify room → mark packet `done` / `validated` (three pillars: agent-call templates, git evidence, nvim). Deck stays thin fire + status + door.

**MyAPI instance of the mission:** Semantic Graphify cold-start → thinnest honest answer loop → node map for cold-start capabilities → GDDP execute when promoted.

These two projects are the **main** tracks. Other repos are secondary unless Sab says otherwise.

---

## 3. Work left up here (this VM) — reconcile snapshot

Status at write time on **this host**. Prefer `git fetch` + compare tips on Air/Mini.

### 3.1 aa-cli — **durable on origin/main**

| Item | Value |
|------|--------|
| Path | `/home/saboor/aa-cli` (also under sab-mini paths depending on layout) |
| Branch | `main` == `origin/main` |
| Tip | `944411d` — *docs: durable verify-pathway capture + agent commit/push rule* |
| Working tree | clean (no pending commit required for the wayfinder package) |

**Package (keep-worthy, already pushed):**

```text
.scratch/verify-pathway/
  TICKET-MAP.md                 # full thread → tickets
  FACTORY-DROID-HANDOFF.md      # mission brief + build order
  GDDP-EXECUTION-MAP.md         # execution graph narrative
  map.md                        # short closed intent
  nodes/*.yaml                  # PROPOSED — not yet gddp/nodes/
  research/01-inventory-…       # code facts
  issues/01–07                  # earlier wayfinder tickets
AGENTS.md                       # durability rule
```

**Proposed nodes (review outside wayfinder, then promote):**

1. `verify-room-shell` — enter room, Accept → done/validated (**build first**)
2. `verify-editor-jump` — nvim at workdir
3. `verify-git-evidence` — status/log/diff on packet workdir
4. `verify-agent-templates` — template-first agent-call
5. `deck-verification-review` (updated umbrella)
6. later: `verify-test-stack-navigator`

**Still open on aa-cli (not done this cycle):**

- [ ] Sab review/edit proposed YAML under `.scratch/verify-pathway/nodes/`
- [ ] Factory-droid mission plan from `FACTORY-DROID-HANDOFF.md`
- [ ] Promote into `gddp/nodes/` + `gddp/CANONICAL.md` when happy
- [ ] Implement minimum Verify circle in hub-rs (shell → pillars → Accept)
- [ ] Do **not** re-grill Create/Deck product shape unless building surfaces forces a cut

**Pull on Air / Mini:**

```bash
cd ~/repos/aa-cli   # or your clone path
git fetch origin && git checkout main && git pull origin main
# expect tip 944411d or newer
ls .scratch/verify-pathway/
```

### 3.2 MyAPI — **durable on docs branch (origin)**

| Item | Value |
|------|--------|
| Path | `/home/saboor/MyAPI` |
| Branch | `docs/semantic-graphify-cold-start-capture` tracking `origin/...` |
| Tips of interest | `007178e` wayfinder + node map · `4eba8dd` keep-worthy VM work + durable-work rules |
| Working tree | mostly clean; `venv/` untracked (trash / regenerable — do not commit) |

**Package (keep-worthy, already pushed on that branch):**

```text
.scratch/semantic-graphify-cold-start/
  WAYFINDER-TO-GDDP.md
  THREAD-CAPTURE-MAP.md
  NODE-MAP.md
  CANONICAL-INTENT-FOR-MISSION-PLANNING.md
  map.md
  research/01–02
  issues/01–08
  gddp-draft/myapi-cold-start/   # proposed nodes + project.yaml
```

Also on `4eba8dd`: durable-work rules in AGENTS/CLAUDE, plus some code/script keep-worthy bits (`api/`, `context_refinery/`, `scripts/khoj_backend`, etc.) — treat as “landed on this branch; merge strategy is Sab’s.”

**Still open on MyAPI:**

- [ ] Sab review cold-start node draft under `.scratch/.../gddp-draft/`
- [ ] Promote into real `gddp-config` / project graph when ready (path per WAYFINDER-TO-GDDP.md)
- [ ] Factory-droid / GDDP execute cold-start mission
- [ ] Decide merge path for `docs/semantic-graphify-cold-start-capture` → main (or long-lived docs branch)
- [ ] Optional junk: untracked `venv/`, any local `search_test.sh` / scratch nits — discard unless Sab says keep

**Pull on Air / Mini:**

```bash
cd ~/repos/MyAPI   # or your clone path
git fetch origin
git checkout docs/semantic-graphify-cold-start-capture
git pull origin docs/semantic-graphify-cold-start-capture
ls .scratch/semantic-graphify-cold-start/
```

### 3.3 Explicitly *not* left stranded (this pass)

| Item | Status |
|------|--------|
| aa-cli verify-pathway package | **Pushed** `main` |
| MyAPI semantic-graphify package | **Pushed** docs branch |
| Durability rules | **In both repos** |
| Pending local commit for the above | **None** for those packages |

If Air/Mini cannot see those tips after pull, the problem is remote/auth/clone path — not “work only on VM.”

---

## 4. Machine roles (handshake map)

| Host | Typical role | Notes |
|------|--------------|--------|
| **Sab Air** | Human daily driver / travel | Prefer Tailscale to VM when possible; don’t leave unpushed gold only on Air either |
| **Sab Mini** | Human cockpit / primary agent home | Pull both repos; review nodes; fire factory-droid / hub TUI feel |
| **This VM (`khoj-38` / saboor home)** | Heavy / remote agent work | **Must push.** Host can vanish. Home root may hold transient handshakes like this file |

Older names in older handoffs (`sab-dev-2`, `khoj-vm-restore`, `khoj-vm-new`) may still appear in docs — do not assume one hostname forever; use Tailscale + `git remote` truth.

**Access (from earlier VM prep notes — verify live):**

- Tailscale SSH preferred when scheduled
- Work under saboor home / `/home/saboor` layout on this box
- Runtime state for aa (`~/.local/share/aa`) is **host-local** — clone + pull ≠ full cockpit state (see `aa-cli/docs/cross-machine.md`)

---

## 5. What to do next (ordered)

### Immediate (any machine after pull)

1. **Confirm tips** for aa-cli `main` and MyAPI docs branch (table above).
2. **Read** (do not re-wayfinder from zero):
   - aa-cli: `.scratch/verify-pathway/FACTORY-DROID-HANDOFF.md` + `TICKET-MAP.md` § product intent
   - MyAPI: `.scratch/semantic-graphify-cold-start/CANONICAL-INTENT-FOR-MISSION-PLANNING.md` + `WAYFINDER-TO-GDDP.md`
3. **Human edit** proposed nodes if wrong; then promote; then mission-plan / execute.

### aa-cli execution spine

```text
verify-room-shell
  → verify-editor-jump
  → verify-git-evidence
  → verify-agent-templates
  → umbrella deck-verification-review
  → (later) test-stack navigator
```

Success: fire → ◆ → Verify room → git + nvim + optional template agent → Accept → `done`/`validated` without living in an agent TUI.

### MyAPI execution spine

Cold-start capability slices already drafted under `gddp-draft/myapi-cold-start/nodes/` — promote only after Sab is happy with intent docs. Runtime executes; human accepts graph truth.

### This handshake file

- Optional: `scp` to Air/Mini home if you want it without git.
- Optional: commit a copy into a shared notes vault later — **not required** if both project packages are already on origin.
- Do **not** treat this root file as the source of truth over the pushed `.scratch/` packages.

---

## 6. One-paragraph brief (paste into next agent)

> Multi-machine durability failed once: wayfinder/intent work sat on a VM untracked and the host went away ~36h, forcing a cleaner second pass. Fix: agents commit+push keep-worthy work same session (rules in aa-cli + MyAPI AGENTS). Two main missions share one pipeline — wayfinder → node map → human promote → GDDP/factory-droid execute. **aa-cli:** verify pathway package is on `main` @ `944411d` under `.scratch/verify-pathway/` (proposed nodes not yet canonical); next is Sab review → factory-droid mission → promote/implement minimum Verify circle (shell, nvim, git, agent templates → done/validated). **MyAPI:** semantic graphify cold-start package is on `docs/semantic-graphify-cold-start-capture` under `.scratch/semantic-graphify-cold-start/`; next is review → promote to real GDDP graph → execute. Do not re-grill locked product intent; do not leave new gold only on this VM.

---

## 7. Co-author / provenance

Session context: Grok CLI on this VM after wayfinder second pass + reconcile of aa-cli vs MyAPI.  
Handoff authoring: grok-cli.

```
Co-authored-by: grok-cli <grok-cli@x.ai>
```
