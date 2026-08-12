---
name: "search-roam"
description: "Find the smallest canonical research context."
version: "1.0.0"
author: "lost-rob0t"
category: "workflow"
tags: ["llm-agent-cl", "workflow", "research"]
---

# Search Roam

## Objective
Load only the canonical notes needed for the active question.

## Procedure
1. Read applicable `AGENTS.md`.
2. Search the project index first.
3. Follow direct `id:` links to research/design dependencies.
4. Prefer canonical current nodes over duplicated summaries.
5. Record contradictions instead of resolving them from memory.

## Exit criteria
The working set is bounded, current, and sufficient to answer or write the requested research without bulk-loading unrelated notes.
