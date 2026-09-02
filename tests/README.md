# Test map

The test suite separates deterministic units, cross-module integration,
environment compliance, and stress coverage. The repository's configured
`pytest` options stop on the first failure.

| Area | Public path |
| --- | --- |
| Unit tests | [`tests/unit`](https://github.com/glennmatlin/wopr/tree/main/tests/unit) |
| Integration tests | [`tests/integration`](https://github.com/glennmatlin/wopr/tree/main/tests/integration) |
| Stress tests | [`tests/stress`](https://github.com/glennmatlin/wopr/tree/main/tests/stress) |
| Benchmark checks | [`benchmarks`](https://github.com/glennmatlin/wopr/tree/main/benchmarks) |

Run the full local checks from the repository root:

```bash
uv sync --extra dev
uv run pytest
uv run ruff check src tests
uv run pyright
```

For the contest release, the exact-export integration test materializes files
from a committed Git revision, runs the offline Room rehearsal in isolation,
and verifies that private outputs and the closed engine are absent from the
curated export:

```bash
uv run pytest -q tests/integration/test_public_export_release.py
```

Passing tests demonstrate their stated software contracts. They do not convert
scripted fixtures into live DATE or model-behavior evidence.
