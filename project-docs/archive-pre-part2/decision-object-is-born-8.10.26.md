MyAPI is no longer “RAG over my project documents.” 
- Closer to a continuously maintained semantic provenance graph for software projects.

Graphify answers something like:

“What exists in this codebase, and how is it structurally connected?”

Your system wants to answer:

“What exists, why does it exist, what decision produced it, what evidence proves that decision was realized, what replaced it, and what is true now?”

That distinction gives you a much cleaner architecture.

I would build the whole thing around one canonical unit: the decision. Not chunks. Not documents. Not embeddings.

A decision object could initially be almost embarrassingly small:

{
  "id": "dec_0182",
  "project": "gddp",
  "statement": "Evaluator pass unlocks dependent nodes.",
  "rationale": "The evaluator is the gating authority for graph progression.",
  "status": "active",
  "decided_at": "2026-08-02T18:42:00Z",
  "evidence": {
    "session": ["session_abc:turn_182"],
    "commits": ["87ae391"],
    "docs": ["architecture/evaluator.md#unlock-semantics"],
    "handoffs": ["handoff_2026-08-02"]
  },
  "code": {
    "files": ["src/evaluator.rs", "src/graph.rs"],
    "symbols": ["EvaluatorResult", "unlock_dependents"]
  },
  "supersedes": [],
  "confidence": 0.94
}

That immediately gives you something substantially more valuable than ordinary RAG. The embedding becomes an access mechanism to that object rather than the object itself.

I would think of your architecture as five layers:

1. Evidence collection. Sessions, Git commits/diffs, handoffs, README/project docs, golden briefs, Obsidian notes, Graphify artifacts.
2. Normalization. Everything becomes timestamped, project-scoped, addressable evidence. You don’t need one universal document format; you need universal IDs, timestamps, source types, and provenance.
3. Decision extraction/linking. Extract candidate decisions from sessions/handoffs/docs, then associate them with commits, files, symbols, and existing decisions.
4. Semantic/provenance graph. Decisions become nodes connected to evidence and to one another through relationships such as implements, supports, supersedes, contradicts, refines, affects, and derived_from.
5. Agent-facing retrieval API. Agents ask normal questions. Your API retrieves the relevant current decision state plus supporting evidence and code relationships.

The thing I’d be particularly strict about algorithmically is separating extraction from truth determination.

An LLM can quite safely say:

Candidate decision:
"Evaluator pass should unlock the next node."
Found in:
session X, turns 173-190
Possible rationale:
"Evaluator is intended to be the progression gate."
Potentially related commit:
87ae391

But that shouldn’t automatically become canonical truth.

Your deterministic pipeline can then test the candidate against the rest of the corpus:

session says decision D
        ↓
find commits in temporal window
        ↓
inspect touched files/symbols
        ↓
search docs/handoffs for same concept
        ↓
compare against existing active decisions
        ↓
classify:
    new
    duplicate
    refinement
    supersedes
    contradiction
    unsupported

That is where this gets really interesting technically. You’re not merely performing information extraction. You’re doing entity resolution over evolving software intent.

And Git becomes incredibly useful because it gives you a strong temporal/evidentiary spine.

For example:

Session
   │
   └─ expresses ──> Decision
                      │
              implemented_by
                      ↓
                    Commit
                      │
                    touches
                      ↓
               File / Symbol

Meanwhile:

Golden Brief ── defines ──> Project
Handoff ── confirms ──> Decision
Decision B ── supersedes ──> Decision A
Graphify Symbol ── related_to ──> Decision

That is basically semantic Graphify, except you’re giving the structural code graph a temporal and epistemic layer.

And I think there’s a very clean way to avoid overbuilding this.

Your MVP should prove exactly one hypothesis:

Given a question an agent naturally asks while entering an unfamiliar project, can MyAPI provide enough trustworthy context that the agent does not need to reconstruct the answer through repo exploration?

That means you already possess the ideal benchmark dataset: the fucking Graphify queries that failed.

I would pick perhaps 20 real cold-start questions from those historic agent runs. They become your evaluation set.

Then start with one project and only four input classes:

* recent agent sessions
* Git history
* handoffs
* one golden project brief

Ignore Obsidian, elaborate documentation ingestion, and even most Graphify artifacts initially unless required by one of the evaluation questions.

Build enough of the system to answer those 20 questions.

Your ingestion loop can initially be shockingly simple:

collect changed sources
        ↓
extract candidate decisions
        ↓
normalize / deduplicate
        ↓
link commits by time + semantic similarity + referenced files
        ↓
resolve supersession / status
        ↓
write graph records
        ↓
embed searchable fields
        ↓
update retrieval index

Importantly, incremental ingestion should operate on deltas, not rebuild the corpus.

Keep something like:

source_cursor:
    git: 87ae391
    sessions: 2026-08-09T23:41
    handoffs: handoff_391
    docs:
        architecture.md: sha256:abc...

Then your daily updater asks only:

What changed since these cursors?

That gets you your “three or four fresh sources every day” model without turning ingestion into a giant batch operation.

The query algorithm also shouldn’t begin as “vector search → shove chunks into model.”

I’d do something closer to:

question
   ↓
semantic + lexical retrieval
   ↓
candidate Decisions
   ↓
graph expansion
   ├── supporting evidence
   ├── superseding decisions
   ├── relevant commits
   └── affected code entities
   ↓
rank current truth
   ↓
answer

So if an agent asks:

Why does GDDP block dependent nodes here?

you don’t want the six most semantically similar paragraphs.

You want:

Current decision
    ↓
preceding decision
    ↓
relevant implementation commit
    ↓
current implementing symbols

and then something like:

Dependent nodes are intended to remain locked until
the evaluator returns pass.
Decision:
dec_0182 — active
Rationale:
Evaluator results are the progression authority; executor
completion alone is insufficient.
Implemented:
87ae391
Current code:
src/evaluator.rs::EvaluatorResult
src/graph.rs::unlock_dependents
Supersedes:
dec_0149

That response is tremendously useful to an agent because it is both compressed and navigable. The agent can then drill down only when it wants to.

There is another design choice here that I think will matter enormously: don’t try to make MyAPI answer everything itself.

Give it graduated tools.

Something conceptually like:

mygraph.project("gddp")
mygraph.ask(
  project="gddp",
  question="Why does evaluator pass unlock nodes?"
)
mygraph.decision("dec_0182")
mygraph.history(
  topic="evaluator progression"
)
mygraph.evidence("dec_0182")
mygraph.code_context("dec_0182")

Now an agent can start broad and progressively deepen its context instead of doing the traditional horrifying thing:

read README
find docs
grep repo
inspect git log
read 14 files
search previous session
...
context window is now 40% full

That’s the cold-start problem you’re actually attacking.

And your “golden briefs/project anchors” fit really cleanly into this architecture. I’d treat them as priors, not ordinary retrieval material.

A golden brief says:

This is what the project fundamentally is.
These are its invariants.
These are its major systems.
These concepts currently matter.

Decisions then describe how that project evolved.

Git establishes what happened.

Code establishes what exists now.

Sessions/handoffs explain why.

That’s a surprisingly coherent epistemic hierarchy:

Golden anchor
      ↓
project meaning
Decisions
      ↓
intent / rationale
Git
      ↓
historical implementation evidence
Current code
      ↓
current material state

And when those disagree, disagreement itself becomes useful information rather than something RAG silently averages together.

You could literally return:

⚠ Decision/code divergence
Decision dec_0182 states:
Evaluator pass unlocks dependent nodes.
Current implementation:
Dependent nodes remain blocked after evaluator pass.
Relevant change:
commit 8291ef0
Possible interpretation:
implementation drift

That begins overlapping beautifully with GDDP, because now your project-memory system isn’t simply remembering history. It can identify when declared architecture, historical decisions, and current implementation diverge.

That’s considerably more interesting than “personal RAG.”

The product-level description I’d use internally is something like:

MyGraph is a continuously updated semantic provenance graph for software projects that connects architectural decisions and rationale to the sessions, documentation, commits, and code that produced them, giving agents evidence-backed project context without repository cold starts.

And I think your smallest serious implementation is only:

1 project
4 source types
~20 historical Graphify queries
decision extraction
Git linking
supersession
hybrid retrieval
5-ish API operations
daily incremental update

No giant ontology. No elaborate multi-agent ingestion pipeline. No comprehensive knowledge graph platform.

If that system takes one of those historically garbage Graphify questions and consistently returns the correct current decision + rationale + commit + code location in one call, you’ve proved the core architecture.

At that point, all the other stuff you’ve accumulated — Obsidian, richer session history, Graphify maps, deeper provenance, automatic drift detection — becomes additive rather than necessary for the idea to stand up.

And yes: “semantic Graphify” is almost exactly the right mental model. Graphify maps the implementation space. MyGraph maps the implementation space plus the decision space across time. That second graph is the thing agents currently have to reconstruct over and over again from scratch.
