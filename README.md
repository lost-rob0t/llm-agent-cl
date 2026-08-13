# llm-agent-cl

A production-oriented Common Lisp library for multi-provider LLM, agent, graph and retrieval applications.

## Current phase

**Auto-research is complete enough for design review. Runtime implementation is not authorized yet.**

The repository uses the document-driven workflow modeled on `lost-rob0t/starintel-auto-research`: canonical Org research/design nodes, approval tables, changelogs, stable IDs, one-active-design implementation handoff, skills and validation scripts.

The first provider is OpenRouter. The first major milestone requires behavioral capability parity with current LangChain + LangGraph, including provider-neutral models/messages, sync/async/batch invocation, streaming, tools, structured output, middleware, multi-turn state, graph reducers/routing/checkpoints/interrupts/time travel, MCP, document loaders, text splitters, embeddings, stores, vector stores, retrievers and RAG composition.

Dexador is the synchronous HTTP transport. [`lost-rob0t/carrier`](https://github.com/lost-rob0t/carrier) is the canonical maintained asynchronous HTTP fork. Carrier must be hardened according to the reviewed design before production provider use; current stock behavior is not treated as production-safe.

## Review entrypoints

- Research index: `roam/indexes/llm-agent-cl/LLM-AGENT-INDEX-000-canonical-research-index.org`
- Design index: `roam/design/llm-agent-cl/LLM-AGENT-DESIGN-INDEX-000-implementation-design-index.org`
- Carrier hardening design: `roam/design/llm-agent-cl/LLM-AGENT-DESIGN-006-carrier-hardening.org`

Merging research/design documents does not constitute implementation approval. Code begins only after the applicable canonical design is explicitly approved.

## Configuration philosophy

Production use can be fully explicit, while quick REPL/tests may intentionally use scoped/process defaults or provider-standard environment variables. Explicit values always win. The library never ships hard-coded credentials and secrets are redacted from logs/conditions/traces.

## Research workflow

```bash
python3 scripts/sync.py
python3 scripts/sync.py --check
python3 scripts/validate-docs.py
python3 scripts/validate_agent_pack.py
python3 scripts/list-unreviewed-research.py
```

Future approved designs use the one-active-design workflow:

```bash
python3 scripts/implement.py roam/design/<project>/<design>.org
python3 scripts/implement.py --status
python3 scripts/mark-design.py implemented --project <project> --summary <summary> --file <path> --test <observed-test>
python3 scripts/mark-design.py rejected --project <project> --reason <reason> --evidence <evidence>
```

## License

MIT.
