---
name: "design-to-issues"
description: "Split an approved design into dependency-ordered issues."
version: "1.0.0"
author: "lost-rob0t"
category: "design"
tags: ["llm-agent-cl", "issues"]
---

# Design To Issues

Only approved designs become implementation issues. Order foundational types and error contracts before providers, transports before streaming, tools before agent loops, checkpoint abstractions before durable graphs, and MCP adapters after the shared tool/content contracts they reuse.
