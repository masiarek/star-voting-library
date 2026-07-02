# YAML_library — the import pipeline & validation fixtures

Two jobs live here. **Teaching elections do not** — those live in
[`01_STAR/`](../01_STAR/), [`02_STAR_Bloc/`](../02_STAR_Bloc/), [`03_STAR_PR/`](../03_STAR_PR/),
and [`method_comparisons/`](../method_comparisons/), one canonical copy each.

## `1_positive/` — the BetterVoting import pipeline

- `01_convert_json_yaml.py` — converts a real BetterVoting JSON export into a
  canonical election YAML (real candidate names, aligned columns, the
  election's official lot order, embedded `expected_results`).
- `S_W1_N_*.json` — frozen real exports used as converter inputs.
- `_generated/` + `_generated_tabulated/` — converter output and its
  tabulation mirror.

Guarded by `tests/test_json_to_yaml_conversion.py` and
`tests/test_lot_number_tiebreak.py` (converter → YAML → engine, end to end).

## `2_negative/` — the manual-authoring validation library

Every file here is a deliberately broken election that must make the engine
**reject it with a plain-language, user-friendly error and no traceback**.
This is the safety net for people writing YAML elections **by hand**: every
realistic mistake gets a fixture, and the fixture pins the exact message the
author will see.

**Self-describing contract** — each fixture declares its expected message as
comments, so adding a case never touches the test suite:

```yaml
# NEGATIVE: what's wrong with this file, in one line.
# expect: substring that must appear in the error output
# expect: another required substring
voting_method: STAR
...
```

`tests/test_negative_validation.py` auto-discovers every `*.yaml` here and
asserts: non-zero exit, no traceback, an Error message, and every declared
`# expect:` substring. A fixture that tabulates "successfully" is a bug.

**Covered mistake catalog** (each has a fixture): bad YAML syntax · missing /
empty ballots · ballots written as a YAML list instead of a `|-` block ·
wrong / extra columns · out-of-range, negative, decimal, and two-digit scores ·
invalid characters and the removed `^` marker · ranked ballots under a score
method (STAR and Approval) · mixed ranked + score rows · 0–5 scores under
Approval · unknown `voting_method` (typos get a "did you mean" suggestion) ·
`num_winners` zero / non-numeric / exceeding the candidate count ·
single-winner method asked for multiple seats · duplicate candidate names ·
`lot_numbers` naming a candidate not on the ballot · header with no voter
rows · a completely blank file, comments-only file, and empty ballots block ·
multiple races in one YAML (one election per file; multi-race BV *JSON*
exports are legitimate — the converter splits them into one YAML per race) ·
duplicate top-level keys (YAML silently keeps the last!) · two `---` YAML
documents in one file · multiple errors reported together.

## History note

Until 2026-07 this folder also held flattened copies of the `Runoff_*`,
`Flat_scores_ties_*`, `Whoops_*`, and `center_squeeze_voteline_1d` teaching
cases. They had already diverged from their canonical siblings and the test
harness runs the canonical files directly, so the copies were removed. If you
need one of those cases, use the canonical copy in `01_Single_winner/`.

# file: README_YAML_library.md
