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

The eventual library must support multi-provider LLM access and composable agent behavior with production-grade contracts comparable in capability to LangChain + LangGraph. StarIntel may depend on this library later, but StarIntel-specific APIs, persistence, actor runtime, policies, schemas, and deployment assumptions must not leak into the core library.

Current phase: **deep research only**. Do not add runtime Common Lisp source, ASDF systems, provider implementations, HTTP adapters, MCP implementations, or agent execution code until research is reviewed and an implementation design is explicitly approved.

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

Use current primary sources for changing external facts and record retrieval dates. Distinguish verified facts, recommendations, assumptions, contradictions, and unresolved questions.

For provider/API research record: endpoint, authentication, request fields, response fields, tool behavior, structured output, streaming framing, usage accounting, model capability discovery, cancellation, timeout/deadline behavior, retries, rate limits, error envelopes, idempotency/ambiguous submission behavior, privacy/logging, and test requirements.

For framework parity research record both high-level LangChain-style and low-level LangGraph-style capabilities. Feature parity is behavioral parity, not Python API cloning.

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
- Cancellation, deadlines, bounded retries, backpressure, and partial-stream failures are explicit.
- Secrets never enter logs, fixtures, research notes, ledgers, or generated artifacts.
- MCP support follows the current protocol specification and keeps stdio/HTTP transports pluggable.

## HTTP requirement

Dexador is the required synchronous HTTP library.

Carrier (`orthecreedence/carrier`) is the identified native asynchronous Common Lisp HTTP client and the reference implementation for async transport research. It is MIT-licensed, built on `cl-async` + `fast-http`, returns Blackbird promises, supports response body chunk callbacks, redirects, cookies, timeouts, and HTTPS through `cl-async-ssl`.

Stock Carrier MUST NOT be treated as production-approved without remediation. Current upstream evidence shows:

- `cl-async-ssl` configures client verification with `SSL_VERIFY_NONE`; certificate/hostname verification is therefore not acceptable for production provider traffic.
- Carrier does not expose a first-class request cancellation handle; the socket is internal to `request`.
- Carrier closes the socket after each completed response, so connection pooling/reuse is absent.
- request-body streaming is not implemented upstream.
- upstream issues document SSL compatibility and TLS-context reuse/performance gaps.

Future designs must preserve the async transport behind a library interface. The preferred order is: (1) evaluate a hardened Carrier fork/adapter with verified TLS, cancellation and connection reuse; (2) if that cannot satisfy the contract cleanly, implement a small Common Lisp async client over libcurl's multi interface. Do not weaken TLS verification to retain Carrier compatibility.

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

Do not claim commands ran unless observed. Do not enable auto-merge. Merge only after required checks for the exact current head are green and review requirements are satisfied.
