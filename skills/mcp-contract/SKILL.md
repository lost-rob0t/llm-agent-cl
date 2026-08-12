---
name: "mcp-contract"
description: "Research current MCP client/server contracts and transports."
version: "1.0.0"
author: "lost-rob0t"
category: "research"
tags: ["llm-agent-cl", "mcp"]
---

# MCP Contract

Use the current MCP specification, not remembered pre-2026 session semantics. Track version negotiation/backward compatibility, JSON-RPC patterns, stdio, Streamable HTTP, request metadata, cancellation, tools, resources, prompts, discovery, structured content, pagination/caching, authorization, and extensions. Prefer a client-first integration that maps MCP tools/content into the same canonical contracts used by native tools, with server export as a separate library layer.
