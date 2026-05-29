# Bounded Chunk

Use this workflow when the operator has approved a specific implementation chunk.

1. Restate the approved chunk in one sentence.
2. Identify allowed surfaces, out-of-scope surfaces, stop condition, and verification.
3. Inspect current state before changing anything.
4. Execute only the approved chunk.
5. Run targeted verification.
6. Stop at the chunk boundary and report changed files, verification result, residual risk, and any next operator decision.

Do not expand into VM, GCS, Khoj, SSH, live-vault mutation, dependency installation, destructive git, or architecture changes unless the approved chunk explicitly includes that class of action.
