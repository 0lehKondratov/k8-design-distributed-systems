# StreamForge Example Microservices

This directory contains simplified mockups for the three services described in the
project outline:

- **queue-manager** – a minimal HTTP service with `/queue/start`, `/queue/stop`,
  and `/queue/status` endpoints.
- **loader-producer** – a job script that pretends to load data from Binance and
  sends a webhook when finished.
- **arango-connector** – an asynchronous library that mimics basic CRUD
  operations against ArangoDB. This library is tested with `pytest`.

These implementations are intentionally lightweight and do not rely on external
packages so they can run in a restricted environment.
