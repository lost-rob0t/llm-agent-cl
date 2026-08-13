---
name: "transport-contract"
description: "Research Dexador sync and maintained Carrier async HTTP semantics, security and lifecycle."
version: "1.2.0"
author: "lost-rob0t"
category: "research"
tags: ["llm-agent-cl", "http", "dexador", "carrier", "tls"]
---

# Transport Contract

Dexador is the required synchronous transport. `lost-rob0t/carrier` is the canonical maintained asynchronous Common Lisp HTTP fork for this project.

Do not use current stock/fork baseline for production provider traffic before the approved Carrier hardening design is implemented. Required fork guarantees include fail-closed certificate-chain + hostname verification, cancellable request handles, deterministic deadlines/timeouts, connection/TLS-context reuse, octet-safe request serialization, streaming uploads, redirect credential safety, explicit proxy behavior, and a deterministic security/lifecycle test suite.

Research and test semantic equivalence across sync/async request execution, headers/body streaming, deadlines, cancellation, TLS, proxies, redirects, retries, ambiguous submission, connection reuse and cleanup. Keep SSE decoding above the HTTP adapter.

libcurl multi is historical contingency research only. Do not switch away from the maintained Carrier fork without a new explicit maintainer decision.
