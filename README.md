# llm-agent-cl

A production-oriented Common Lisp library for multi-provider LLM and agent applications.

## Current phase

**Research only. No agent runtime is implemented yet.**

The repository is being bootstrapped with the same document-driven research workflow used by `lost-rob0t/starintel-auto-research`: canonical Org research, project indexes, approval tables, changelogs, stable IDs, research/design/implementation separation, status ledgers, skills, and validation scripts.

The first planned provider is OpenRouter. The target architecture is comparable in capability to LangChain + LangGraph while remaining a library rather than a hosted harness. Required future capabilities include provider-neutral model/message contracts, synchronous and asynchronous transports, streaming, tools, structured output, multi-turn state, middleware, durable state/checkpoint interfaces, interrupts, composable agent graphs, and MCP.

Dexador is the required synchronous HTTP transport. The requested asynchronous Common Lisp HTTP library named `Lobster` could not be verified during the initial research pass; no substitute is silently selected. See the transport research note.

## Research workflow

```bash
python3 scripts/sync.py
python3 scripts/sync.py --check
python3 scripts/validate-docs.py
python3 scripts/validate_agent_pack.py
python3 scripts/list-unreviewed-research.py
```

Future approved designs use the same one-active-design-slot workflow:

```bash
python3 scripts/implement.py roam/design/<project>/<design>.org
python3 scripts/implement.py --status
python3 scripts/mark-design.py implemented --project <project> --summary <summary> --file <path> --test <observed-test>
python3 scripts/mark-design.py rejected --project <project> --reason <reason> --evidence <evidence>
```

## License

MIT.
