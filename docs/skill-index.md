# Skill index

`skills/manifest.json` is the machine-readable index. The pack mirrors the auto-research lifecycle while specializing technical skills for `llm-agent-cl`.

## Workflow

- `search-roam` — load the smallest canonical research context.
- `save-research` — create sourced Org research with required metadata.
- `source-verification` — prefer primary sources and track retrieval dates.
- `branch-workflow` — reconcile state and isolate changes.
- `implement-one-design` — future one-slot implementation handoff after approval.
- `mark-implemented` / `mark-rejected` — terminal ledger transitions.

## Design and parity

- `create-design-file`
- `review-design`
- `design-to-issues`
- `feature-parity` — mandatory LangChain + LangGraph capability matrix, including retrieval in the first major milestone.
- `provider-research`
- `model-contract`
- `transport-contract` — Dexador sync + maintained `lost-rob0t/carrier` async direction.
- `streaming-contract`
- `tool-contract`
- `mcp-contract`
- `agent-runtime-contract`
- `retrieval-contract` — documents/loaders/splitters/embeddings/vector stores/retrievers/RAG.
- `production-readiness`

The current research/design phase does not authorize runtime implementation. Skills that perform implementation handoff remain gated on explicit design approval.
