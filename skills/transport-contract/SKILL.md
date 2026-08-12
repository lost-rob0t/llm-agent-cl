---
name: "transport-contract"
description: "Research sync/async HTTP, deadlines, cancellation and retries."
version: "1.1.0"
author: "lost-rob0t"
category: "research"
tags: ["llm-agent-cl", "http", "dexador", "carrier", "libcurl"]
---

# Transport Contract

Dexador is the required synchronous transport. Carrier (`orthecreedence/carrier`) is the identified native asynchronous Common Lisp HTTP client and the reference async implementation for research.

Do not treat stock Carrier as production-ready without verification and hardening. Its current `cl-async-ssl` path disables certificate verification, Carrier exposes no first-class request cancellation handle, closes sockets after responses instead of pooling/reusing them, and does not stream request bodies. Research semantic equivalence across sync/async request execution, connection reuse, deadlines, cancellation, TLS, proxies, headers, body streaming, retries, ambiguous submission, and resource cleanup. Keep SSE decoding above the HTTP adapter.

A future design should first evaluate a hardened Carrier fork/adapter. If the production contract cannot be satisfied cleanly, use a small Common Lisp wrapper around libcurl's multi interface rather than weakening the contract.
