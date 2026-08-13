---
name: "retrieval-contract"
description: "Research and review document, loader, splitter, embedding, vector-store, retriever and RAG parity."
version: "1.0.0"
author: "lost-rob0t"
category: "research"
tags: ["llm-agent-cl", "retrieval", "embeddings", "vector-store", "documents"]
---

# Retrieval Contract

Treat retrieval/data-plane capabilities as mandatory for the first major LangChain + LangGraph parity milestone.

Research and design canonical documents/provenance, eager and lazy document loaders, text splitters, tokenizer boundaries, query/document/batch embeddings, embedding caches, key/value stores, vector stores, metadata filtering, scored similarity search, retrievers, RAG composition, cancellation/deadlines and representative built-ins.

Require an in-memory store and exact-search vector store as deterministic reference implementations. OpenRouter is the first remote embedding adapter. Do not equate parity with reproducing every LangChain community integration; require stable extension protocols and an end-to-end tested load -> split -> embed -> store -> retrieve -> generate path.
