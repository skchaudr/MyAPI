# MyAPI Decision Graph

MyAPI maintains evidence-backed project intent across time and serves that intent
to agents as compact, navigable context.

## Language

**Evidence**:
An addressable, timestamped source record that can support or challenge a project
claim.
_Avoid_: Chunk, context blob

**EvidenceRef**:
A stable locator from a Decision or DecisionCandidate to one Evidence record.
_Avoid_: Citation string, source note

**DecisionCandidate**:
A proposed statement of project intent and rationale extracted from Evidence and
awaiting resolution.
_Avoid_: Decision draft, inferred truth

**Decision**:
An accepted statement of project intent with rationale, status, provenance, and
relationships to implementation and other Decisions.
_Avoid_: Chunk, document, embedding, claim

**DecisionRelation**:
A directed semantic relationship between Decisions, such as supersedes, refines,
or contradicts.
_Avoid_: Link, association

**AcceptanceReceipt**:
The durable record of who promoted a DecisionCandidate, when, and from which
resolved evidence.
_Avoid_: Approval flag, accepted boolean

**SourceCursor**:
The last successfully processed position or content identity for one evidence
source.
_Avoid_: Sync timestamp, checkpoint file

**DecisionAnswer**:
The current Decision state, rationale, evidence, history, and code context returned
for one agent question.
_Avoid_: Search result, RAG response

**DecisionCodeDivergence**:
A recorded disagreement between accepted project intent and current implementation.
_Avoid_: Hallucination, stale answer

**ContextBrief**:
The budgeted machine-readable and human-readable envelope used to deliver a
DecisionAnswer.
_Avoid_: Decision, canonical record

**MyAPI**:
The engine that collects evidence, maintains the Decision graph, and retrieves
current project intent.
_Avoid_: MCP server, document corpus

**MyMCP**:
The small public doorway that exposes MyAPI context through two stable tools.
_Avoid_: Retrieval engine, Decision graph
