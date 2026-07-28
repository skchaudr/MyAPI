
# Entire plan

  This is completion and redirection of V1—not “V2,” not a rewrite.

  Supersedes: `prove-first-durable-handoff` (gddp/nodes/ on
  origin/main) is superseded by this plan. It is not a dependency
  of any node below.

  ## 1. Preserve the real starting state

  - Work from a clean MyAPI worktree based on origin/main.
  - Leave the current Mini branch, Corpus v1.0/, and scratch/
    untouched.

  - Use Air for sources only available there: larger session
    history, valid GitHub auth, and working Vertex credentials.

  - Never modify original sessions, vault notes, or GitHub records.

  ## 2. Freeze the perishable Vertex baseline immediately

  The benchmark-search Vertex engine is live and answering from
  Air.

  Run three query sets against it:

  - Existing 18-query MyAPI benchmark.
  - Existing golden-brief questions.
  - A curated set of actual questions mined from Pi/Codex sessions
    on Mini and Air.

  Record privately:

  - exact query;
  - answer;
  - citations;
  - latency;
  - timestamp;
  - engine;
  - source freshness visible in the answer;
  - obvious stale or incorrect claims.

  This preserves what the current 1,545-document database can do
  before access disappears. Do not alter that engine.

  ## 3. Build one broad source registry

  The query benchmark is Pi/Codex-derived. The corpus is not Pi/
  Codex-only.

  Register:

  - Obsidian notes;
  - Pi sessions;
  - Codex sessions;
  - Claude Code sessions;
  - Grok sessions;
  - Cline sessions;
  - Factory/Droid sessions;
  - Hermes traces;
  - Zed and Obsidian ACP threads;
  - GitHub issues, PRs, reviews, comments, and discussions;
  - repository briefs, decisions, docs, and handoffs;
  - Needle’s already-curated datasets;
  - Vertex/Khoj manifests and benchmark results;
  - Corpus v1 as existing candidate/cold material.

  Registration is cheap and automatic. Each source gets:

  - logical source ID;
  - machine;
  - source family;
  - path or remote URL;
  - stable native ID where available;
  - content hash;
  - created/updated/observed timestamps;
  - project/CWD hint;
  - parser status.

  Mini/Air copies deduplicate by native ID and hash.

  ## 4. Finish V1’s unfinished machinery

  Reuse:

  - source_manifest.py for inventory and temporal tiers;
  - normalization_schema.py for canonical metadata;
  - existing Obsidian and Claude adapters;
  - Needle’s Pi/Codex/Claude parsers;
  - historical normalize_corpus.py scanning logic;
  - build_vault_v1.py provenance, manifests, safe-write guards, and
    failure receipts;

  - owner-queue secret and duplicate checks;
  - ContextPacket/ContextBrief;
  - existing benchmark and retrieval pipeline.

  Add only missing readers:

  - current Codex rollout JSONL;
  - Pi session JSONL;
  - GitHub records;
  - other agent formats where existing Needle inventory cannot
    already parse them.

  One source registry, one active-corpus builder, one benchmark
  miner. Not separate pipelines per source.

  ## 5. Generate candidates—not another raw vault

  Different source shapes receive different treatment:

  - Existing high-quality Obsidian anchors, project briefs,
    decisions, and handoffs can enter as candidate documents
    directly.

  - GitHub issues/PRs become bounded project events with linked
    discussion evidence.

  - Agent sessions produce candidate events, decisions, failures,
    commands, and handoffs—not one corpus document per session.

  - Corpus v1 provides existing candidates and historical evidence;
    it is not recopied.

  - Needle datasets provide already-extracted prompt/action
    evidence and parser logic.

  Raw material remains where it lives.

  ## 6. Promote candidates into the active corpus

  A promoted item must be one of:

  - current-state brief;
  - event trace;
  - decision;
  - project handoff;
  - person-context anchor;
  - operational runbook;
  - durable reference;
  - verified source note.

  Required admission fields:

  - what happened or what is true;
  - why it matters;
  - project/person association;
  - evidence pointers;
  - event or validity time;
  - observation and last-verification time;
  - freshness/tier;
  - supersedes/superseded-by relationship where applicable;
  - confidence or unresolved status;
  - sanitization result.

  No item is promoted merely because its source exists.

  ## 7. Keep three physically separate layers

  - Source registry: pointers and fingerprints for everything.
  - Candidate store: generated excerpts/events awaiting promotion.
  - Active corpus: promoted context items used by ordinary
    retrieval.

  Corpus v1 remains a fourth, cold historical store. It is not
  merged into active retrieval.

  Private corpus content remains outside tracked source files. The
  repo contains schemas, adapters, tests, sanitized fixtures, and
  aggregate receipts.

  ## 8. Temporal behavior

  Dynamic sources use a recent active window initially. Older items
  remain usable when:

  - explicitly promoted as durable;
  - linked as evidence for a current event;
  - requested for history/recovery;
  - required to explain a decision’s evolution.

  Every context response must expose:

  - newest supporting evidence;
  - oldest supporting evidence;
  - last verification;
  - known superseded material;
  - unresolved temporal contradictions.

  Recency affects ordinary ranking; it never silently erases
  durable history.

  ## 9. Prove retrieval before building MCP

  Point the existing MyAPI retrieval pipeline at the active corpus.
  Do not invent another database first.

  Run the same query bank against:

  1. Current Vertex baseline.
  2. Active MyAPI corpus.
  3. Active corpus plus Corpus v1 cold fallback.

  Evaluate:

  - factual correctness;
  - current-state correctness;
  - temporal correctness;
  - citation quality;
  - stale-claim rate;
  - whether raw conversations dominate;
  - whether the answer supports the next agent action;
  - whether project/person context stays within the requested
    budget.

  Only after the active corpus proves value should it optionally be
  indexed into a separate Vertex datastore. Never overwrite
  benchmark-search.

  ## 10. Serve the proven path through MCP

  Implement only:

  - get_project_context
  - get_person_context

  Both return the existing ContextBrief envelope:

  - short answer;
  - relevant current state;
  - decisions/events;
  - next useful action;
  - evidence paths;
  - freshness;
  - unresolved risks;
  - budget metadata.

  No large tool roster, new workflow engine, or mandatory graph
  traversal.

  ## 11. GDDP execution graph

  The canonical execution graph is the six-node list below. Node
  names are actions; artifacts are named separately (the “frozen
  baseline” is the artifact produced by node 1).

  ### Ready now, parallel

  1. capture-live-vertex-baseline

     Run the existing and newly mined questions against Air’s live
     benchmark-search. Preserve answers, citations, timestamps, and
     latency. Do not mutate the engine. Runs from Air, where the
     live engine and credentials are.

  2. assemble-current-personal-corpus

     Continue V1 using current Obsidian, all relevant agent
     sessions, GitHub, repo docs/handoffs, Needle datasets, and
     existing V1 material. Reuse existing adapters, manifests,
     provenance, sanitization, and review machinery. Produce an
     actual versioned corpus—not merely a plan.

  3. mine-real-agent-query-benchmark

     Finish the Mini+Air Pi/Codex mining. Deduplicate, categorize,
     preserve provenance, and produce the real question bank agents
     have demonstrated they need.

  ### Then

  4. prove-myapi-context-retrieval (depends on 1, 2, 3)

     Run the same questions against Vertex and the generated MyAPI
     corpus. Produce evidence-backed project/person context briefs
     and compare correctness, freshness, citations, and usefulness.

  5. serve-context-via-mcp (depends on 4)

     Expose the proven retrieval through get_project_context and
     get_person_context.

  6. prove-incremental-refresh (depends on 2; parallel with 4)

     Demonstrate that new notes, sessions, and GitHub activity
     update the corpus without rebuilding or duplicating
     everything. Proof scope is corpus update only; refreshed-
     retrieval proof is out of scope for this node.

  Nodes 1–3 are ready now. They produce real MyAPI code and data
  contracts without prematurely ingesting or rewriting the corpus.
  Human review controls every graph transition.

  The session-query extraction already begun (Mini complete, Air
  pending) feeds nodes 2 and 3 directly—productive work, not
  something to discard.



