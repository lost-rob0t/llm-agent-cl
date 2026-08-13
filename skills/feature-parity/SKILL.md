---
name: "feature-parity"
description: "Measure mandatory behavioral parity against current LangChain and LangGraph."
version: "1.1.0"
author: "lost-rob0t"
category: "research"
tags: ["llm-agent-cl", "langchain", "langgraph", "retrieval"]
---

# Feature Parity

Build and maintain the capability matrix from current official LangChain/LangGraph documentation. Semantic parity is required; do not defer an entire documented capability class merely because the first provider slice can function without it.

Track provider-neutral models/messages/content, sync/async/batch invocation, token and orchestration streaming, tools, structured output, middleware/runtime context, multi-turn state, retries/fallbacks, model profiles, graph state/reducers, conditional routing, Send/Command, parallel supersteps, checkpoints/pending writes, interrupts/resume, subgraphs, replay/fork time travel, short/long-term memory, observability, MCP, documents, document loaders, text splitters, embeddings, embedding caches, stores, vector stores, retrievers and RAG composition.

The first major parity milestone includes the retrieval/data-plane capability family. Literal parity with the number of third-party LangChain integration packages is not required; stable protocols, representative adapters and tested composition are required. Record gaps explicitly and do not call the milestone parity-complete while required matrix rows remain open.
