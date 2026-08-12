# Status ledgers

The workflow mirrors the design-slot model used by `starintel-auto-research`.

- `roam/design/<project>/` contains canonical designs.
- `roam/implement/<project>/` contains at most one active design copy.
- `roam/implement/<project>/.implemented.jsonl` records successful terminal handoffs.
- `roam/implement/<project>/.rejected.jsonl` records rejected terminal handoffs.
- Ledgers are append-only JSON Lines.
- Canonical design documents are never deleted by status transitions.
- Research approval is independent of implementation state.
