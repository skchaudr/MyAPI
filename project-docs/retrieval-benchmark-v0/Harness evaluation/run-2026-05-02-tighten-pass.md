# Run — Tighten Pass (Trust-Categorized v1)

Date: 2026-05-02

First run since 2026-04-25 blocker pass. Goal: validate H-lane queries against the classifier patches that landed last session, and close A7's partial via vocab expansion.

## Result: mixed — sentinels held, A7 fix was wrong diagnosis, F5 regressed

| Query | Verdict | Bucket | Severity | Notes |
|---|---|---:|---|---|
| H1 | weak win | intent gap | annoying | Anchors top-3, but routes via OPERATIONAL when human-find-thread expected sessions |
| H2 | fail | corpus or retrieval gap | annoying | `source-aware-priors` design note absent from top 5 |
| H3 | fail | retrieval gap | acceptable | Temporal probe — expected to fail per bank hypothesis |
| H4 | ✅ pass | win | blocking | Trust-Threshold plan #1, fs=0.838 (margin 0.371 over #2 — much wider than 04-25's 0.068) |
| H5 | ✅ win | win | acceptable | Surfaces dispatch-handoff + claude vault-inbox-triage at top |
| A7 | partial — same as 04-25 | subject-scope gap (re-diagnosed) | blocking | Vocab bridge had no effect; real issue is eval notes are scoped to "retrieval benchmark," not "MyAPI" |
| F5 | 🆘 regression | candidate-set gap | blocking | Trust-Threshold plan absent from top 20 for full sentence; bare `gold mine` query still surfaces it at #1 (ks=0.87) |

## What landed

### Vocab bridge in `_expand_query_for_retrieval` (deployed, no-op on target)

`context_refinery/retrieval.py`: when an operational query contains a problem verb (`broken|blocked|stuck|failing|...`), append `known issues / fragile / thin / gap / weak / unimproved / queue / refinement queue` to the Khoj query string.

**Patch is deployed and live on the VM** as of 2026-05-02. H4 sentinel verified unchanged (fs=0.838, same as pre-patch). A7 result identical pre/post — patch is a no-op for the target query.

### Why the patch didn't fix A7

Probed A7 with four query variants:

- `"What's broken or blocked in MyAPI right now?"` (the bank query) → 3 results, both anchors + 1 claude-caveat note. **Eval notes absent from top 20.**
- `"What's broken or blocked or known issues or queue or fragile in MyAPI right now?"` (explicit bridge tokens in the query itself) → identical result. Same 3 candidates.
- `"What are the known issues with MyAPI?"` → routes to project_overview (not operational); Trust-Threshold plan #1, GitHub REST issues #2. Still no eval notes.
- `"What are the known issues with the retrieval benchmark?"` → routes to factual; **eval notes #1 and #2 cleanly** (run-2026-04-23-post-anchor-v2.md fs=0.858; refinement-queue-2026-04-20.md fs=0.674).

The eval notes are findable when the query subject is "retrieval benchmark" — their actual top-level subject. They're invisible when the query subject is "MyAPI," even with terminology bridging. The candidate set selection for operational+MyAPI queries is dominated by MyAPI-subject anchors (khoj-deployment, vm-tailscale), and no amount of vocab expansion pulls eval-of-retrieval-benchmark notes into that set.

**Re-diagnosis: A7 is a subject-scope gap, not a terminology gap.**

### Real fix paths (deferred to next session)

1. **Anchor approach**: build a `myapi-status-anchor.md` that explicitly enumerates current open items and points at the eval notes. Aligns with the trust-threshold plan's "agent-cold-start" framing — agent asking "what's broken in MyAPI" should hit a status anchor, not eval notes directly.
2. **Metadata approach**: add `myapi` to a tags/projects field on the eval notes' frontmatter so they associate with MyAPI subject in the index. Less robust because it depends on retrieval to honor that field for subject-scoping.
3. **Filter approach**: loosen the operational filter so more candidates pass through. Risky — would affect every operational query.

Anchor approach (1) is highest-leverage and lowest-risk.

## F5 regression — separate, blocking

F5 passed on 2026-04-25 with margin 0.006 over a paypal-recruiter note. On 2026-05-02 baseline, the Trust-Threshold plan does not appear in the top 20 results for the full sentence query. **Probed:**

- `"Find the note where I used the term 'gold mine'"` → plan absent; #1 is `chatgpt-claude-workflow-demo.md` at fs=0.86 (boost-driven, ks=0.0).
- `"gold mine"` (bare phrase) → plan #1, ks=0.87, fs=0.54. Margin 0.011 over paypal-noise.
- `"gold-mine"` (hyphenated) → plan #1, ks=0.18, fs=0.78. Clean win.

**Failure mode:** Khoj's semantic ranking on the long sentence query pushes the plan out of the candidate set entirely. The exact-phrase boost can only re-rank items in Khoj's candidates; if Khoj doesn't return the plan, the boost can't fire on it.

The bank flagged this risk in the 04-25 open items: *"F5 thin-margin (0.006): paypal-recruiter note got incidental 'gold mine' match. Not blocking but flag if it inverts on future index churn."* Outcome is worse than inversion — the plan dropped out of the candidate set.

Real fix is Khoj-layer: either **expand candidate retrieval n** (request more candidates from Khoj before reranking) or **add a phrase-aware retrieval lane** that bypasses semantic similarity for documents containing exact query phrases. Out of scope tonight.

## State of the system

- Phase 2 trust-bank: blocker set still mostly closed (F5 regression is the new gap).
- Vocab bridge patch deployed but no-op on its target — kept deployed (small surface, no negative effect on H4 sentinel).
- A7 re-diagnosed as subject-scope gap, not terminology gap.
- F5 sentinel regressed; H4 sentinel widened margin.
- H-lane regression check complete: no new code-layer issues introduced by the 04-25 classifier patches; H1/H2/H3 failures are pre-existing and acceptable severity.

## Open items (next session)

- **Build `myapi-status-anchor.md`** — closes A7 properly via subject-scope alignment.
- **F5 candidate-set fix** — expand retrieval n or add phrase-aware retrieval lane.
- **H1 intent re-routing** — bank says human-find-thread should route to lookup, not operational. Worth a small classifier tweak.
- **H2 corpus check** — does a `source-aware-priors` design note exist? If yes, why doesn't it surface? If no, it's a corpus gap.
- **27 obsidian files still missing from index** — carry-over from 04-25.
- **Source: "unknown" on anchors** — carry-over from 04-25.
- **A4, A5, A6, F1–F4** — bank still has these untested.

## Lane attribution

- Saboor: ran the deploy command on the VM, made the call to keep the no-op patch rather than re-deploying a revert
- Claude: ran baseline and post-patch query batches, identified the subject-scope re-diagnosis via probe queries, surfaced F5 regression, drafted this note
