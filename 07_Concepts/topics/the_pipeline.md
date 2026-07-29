# The pipeline — one YAML file, wrapped in tooling

Everything in this library orbits a single, human-readable **YAML election file** as the source of truth. The pieces fit together as a pipeline:

> **The founding idea:** [Why YAML? One file a person reads and a computer runs](../about_this_repo/why_yaml_test_cases.md) — how each case is human-readable and machine-runnable at once, so it can be taught, run, and audited from the same source.

```
 author ──▶ validate ──▶ tabulate ──▶ verify ──▶ publish
   │                         │                       │
   │                         ├─▶ on-screen report           └─▶ a browsable <name>.md page
   │                         └─▶ _tabulated.txt          (the friendly, linkable surface)
   │                             (the full record)
   ├─ hand-write the YAML, or
   └─ import a BetterVoting JSON export (converter → canonical YAML)
```

1. **Author.** Write a small YAML election by hand, *or* import a real **BetterVoting JSON export** with the converter. The converter produces a canonical YAML: real candidate names as IDs, aligned ballot columns, the election's official tie-break (lot) order, and the embedded expected winner.
2. **Validate.** The engine rejects malformed files with clear, plain-language errors and **no Python tracebacks** (bad YAML, missing `ballots:`, wrong column counts, out-of-range scores, ranked ballots under a score method, method/seat mismatches…). Negative test cases lock this behavior in.
3. **Tabulate.** Run the YAML election file through the engine. It prints an annotated, round-by-round **interactive on-screen report**, and writes a full-detail **`_tabulated.txt`** sibling for the record. STAR (single / Bloc / PR), Approval, **Ranked Robin**, and RCV-IRV are dispatched automatically based on the file.
4. **Verify.** Each file embeds its expected winner — `expected_winners:` in hand-written files, an `expected_results:` block in BetterVoting imports — and a **pytest** suite checks them (positive winners, negative errors, JSON→YAML conversion, tie-break logic, Ranked Robin, plus non-vacuous self-checks), wired into a pre-commit hook.
5. **Publish.** `../STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py` renders each election into a **browsable Markdown page** (`<folder>/<folder>_pages/<name>.md`) — title, method, the scenario description, the ballots, and the full tabulation report, with auto cross-references. A pytest keeps these pages in sync with their YAML, so they're always current. This `.md` page — not the raw `.yaml` — is the reader-facing surface.

> **House rule — link the `.md` page, not the raw `.yaml`.** The generated pages are the friendly, reader-first surface: lead with them in tables, navs, and cross-references; link a `.yaml` only when the *runnable source* is genuinely the point (e.g. a "run this file" command), and demote it. See [`../CLAUDE.md`](../../CLAUDE.md).

This is *not* a black box that just prints a winner — the whole point is that the count is **legible and reproducible**, so it can be taught and audited.
