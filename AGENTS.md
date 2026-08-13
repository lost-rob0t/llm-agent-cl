# llm-agent-cl Agent Instructions

This file is repository-wide authority for humans and automated agents working in this repository.

## Scope and mandatory reconciliation

1. Read this file before changing anything.
2. Read any nested `AGENTS.md` that applies to edited paths.
3. Reconcile the tracked tree, branch, remote, open PRs/issues, current tests, and current scripts before relying on remembered state.
4. Preserve unrelated work.

Before editing, record:

```bash
git status --short
git branch --show-current
git remote -v
find .. -name AGENTS.md -print
```

## Mission and boundary

`llm-agent-cl` is a reusable Common Lisp **library**, not an agent hosting service, daemon, SaaS harness, StarIntel subsystem, or application-specific runtime.

The library must reach behavioral feature parity with the current LangChain + LangGraph capability classes, including the retrieval/data plane: document abstractions, document loaders, text splitters, embedding models, vector stores, retrievers, key/value stores and embedding caches. Those capabilities are part of the first major parity milestone and MUST NOT be deferred merely because the initial OpenRouter/agent path can run without them.

StarIntel may depend on this library later, but StarIntel-specific APIs, persistence, actor runtime, policies, schemas, and deployment assumptions must not leak into the core library.

Current phase: **research and design only**. Canonical design documents may be created and revised, but do not add runtime Common Lisp source, ASDF runtime systems, provider implementations, HTTP adapters, MCP implementations, Carrier changes, or agent execution code until the applicable design documents are explicitly approved by the maintainer.

License: MIT.

## Canonical workflow

Research lifecycle mirrors `starintel-auto-research`:

```bash
python3 scripts/sync.py
python3 scripts/sync.py --check
python3 scripts/validate-docs.py
python3 scripts/validate_agent_pack.py
python3 scripts/list-unreviewed-research.py
```

Future implementation lifecycle:

```bash
python3 scripts/implement.py roam/design/<project>/<design>.org
python3 scripts/implement.py --status
python3 scripts/mark-design.py implemented --project <project> --summary <summary> --file <path> --test <observed-test>
python3 scripts/mark-design.py rejected --project <project> --reason <reason> --evidence <evidence>
python3 scripts/sync.py
```

Each immediate `roam/implement/<project>/` directory may contain zero or one active design copy. Canonical designs remain under `roam/design/`. `.implemented.jsonl` and `.rejected.jsonl` ledgers are append-only.

## Research contracts

Use current primary sources for changing external facts and record retrieval dates. Distinguish verified facts, recommendations, maintainer decisions, assumptions, contradictions, and unresolved questions.

For provider/API research record: endpoint, authentication, request fields, response fields, tool behavior, structured output, streaming framing, usage accounting, model capability discovery, embeddings where available, cancellation, timeout/deadline behavior, retries, rate limits, error envelopes, idempotency/ambiguous submission behavior, privacy/logging, and test requirements.

For framework parity research record both high-level LangChain-style and low-level LangGraph-style capabilities. Feature parity is behavioral parity, not Python API cloning and not literal parity with every third-party integration package.

## Required architecture invariants for future designs

- Provider-neutral canonical messages and typed content blocks.
- Provider adapters translate at the boundary; provider-native fields remain accessible without contaminating core types.
- Sync and async invocation are first-class and semantically equivalent.
- Streaming is typed event streaming, not raw string concatenation.
- Tool calls preserve stable call IDs and JSON Schema argument/result contracts.
- Structured output supports provider-native and tool-mediated strategies.
- Multi-turn state is explicit and caller-owned unless a pluggable checkpoint store is supplied.
- Middleware/interceptors can observe and transform model calls, tools, state transitions, retries, limits, and errors.
- Agent loops and graph execution are library abstractions; no hosted control plane is required.
- Graph parity includes state reducers, dynamic sends, command/update routing, parallel supersteps, checkpoints, pending writes, interrupts/resume, subgraphs, replay/fork time travel, short-term memory, long-term stores, and typed event streams.
- Retrieval parity includes documents, loaders, splitters, embeddings, vector stores, retrievers and caching/store protocols in the first major milestone.
- Cancellation, deadlines, bounded retries, backpressure, and partial-stream failures are explicit.
- Secrets never enter logs, fixtures, research notes, ledgers, or generated artifacts.
- MCP support follows the current protocol specification and keeps stdio/HTTP transports pluggable.

## Configuration and REPL convenience

The production core must remain explicit and testable, but end users MUST also have convenient quick-testing configuration.

Approved direction:

- explicit per-call values override everything;
- explicit client/provider configuration is the normal production path;
- scoped dynamic defaults are supported for REPL/tests;
- process-wide convenience defaults may be set intentionally by the caller;
- provider-standard environment variables such as `OPENROUTER_API_KEY` may be used as a convenience fallback;
- there is never a hard-coded credential in the library;
- resolved secrets must be redacted from printing, logs, traces and conditions.

Global convenience state is therefore allowed; hidden, unavoidable global state is not.

## HTTP requirement

Dexador is the required synchronous HTTP library.

`lost-rob0t/carrier` is the canonical maintained asynchronous HTTP fork for this project. It is currently a direct fork of `orthecreedence/carrier`, which is MIT-licensed, built on `cl-async` + `fast-http`, returns Blackbird promises, and supports incremental response-body callbacks suitable for SSE.

Stock Carrier MUST NOT be used for production provider traffic unchanged. The maintained fork must fix, at minimum:

- verified TLS certificate chains and hostname validation, fail-closed;
- first-class cancellable request handles;
- deterministic deadline/timeout behavior;
- connection and TLS-context reuse;
- correct octet/binary request serialization and streaming upload support;
- redirect credential stripping and origin-safe redirect behavior;
- proxy behavior or explicit unsupported errors;
- deterministic conformance, TLS, race, malformed-response and lifecycle tests.

The earlier libcurl-multi option is no longer the active design direction. It remains historical contingency research only; changing away from the maintained Carrier fork requires a new explicit maintainer decision.

Do not modify `lost-rob0t/carrier` until the Carrier hardening design in this repository is approved.

## Substantive Org documents

Every substantive research, design, implementation, specification, provider, architecture, index, or operations Org document requires:

```org
:PROPERTIES:
:ID: stable-id
:END:
#+title:
#+description:
#+status:
#+filetags:
```

It also requires an approval table, changelog, and `* Footnotes and Glossary` section. Preserve stable IDs. Duplicate IDs and unresolved `id:` links are validation failures. Update the project index whenever canonical documents are added, moved, superseded, or materially changed.

Approval states: `PENDING`, `NOT STARTED`, `APPROVED`, `REJECTED`, `SUPERSEDED`, `NOT APPLICABLE`. Never infer approval from merge status or green CI.

## Source hierarchy

For changing technical facts prefer, in order:

1. normative specification or official API documentation;
2. official repository/source and tests;
3. official release notes/changelog;
4. package registry metadata;
5. secondary sources only when primary sources do not answer the question.

## Validation and completion

Before completion run, where available:

```bash
git diff --check
python3 -m py_compile scripts/*.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/sync.py
python3 scripts/sync.py --check
python3 scripts/validate-docs.py
python3 scripts/validate_agent_pack.py
git status --short
git diff --name-only
```

Do not claim commands ran unless observed. Do not enable auto-merge. Merge only after required checks for the exact current head are green and review requirements are satisfied. Merging research/design documents does not authorize implementation.
