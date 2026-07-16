# Why YAML? One file a person reads and a computer runs

The core design goal of this library: **each test case is a single file that is, at the same time, human-readable and machine-runnable.** A person can read the scenario and the ballots and understand the election; the engine can parse the same file, tabulate it, and a test can verify the winner. No translation step, no second copy.

That one decision is why the library can be *taught, run, and audited* from the same source — instead of forcing a choice between "readable for people" and "usable by tools."

## The problem it avoids

The usual way to keep test cases splits them in two: prose for humans (a doc describing the scenario) and data for machines (a CSV/JSON/fixture the code runs). The two **drift apart** — the doc says one thing, the fixture does another, and nobody notices until a count is wrong. You also can't *read* the machine copy or *run* the human copy.

This library refuses that split. There is **one artifact**, and it's legible both ways.

## What that looks like

A whole election, in one small YAML:

```yaml
voting_method: STAR
num_winners: 1
ballots: |-
  Ann,Bob,Cal
  5,4,0
  3,5,2
  0,3,5
expected_winners:
- Bob
```

- **A person** reads the candidate names, the three ballot rows, and the expected winner — and understands the whole case at a glance.
- **The engine** reads `voting_method`, `num_winners`, and `ballots`, and produces an annotated, round-by-round count; the **pytest** suite reads `expected_winners` and fails if the engine disagrees.

Same file. Two readers. Never out of sync — because there's nothing to keep in sync.

Richer files keep more *human* context in the same file — an `election_title`, a `scenario_description`, inline per-voter notes on the ballot rows, and `options:` to shape the report — all stored in the one artifact and never shown on screen unless you ask. → [YAML authoring template](YAML_authoring_template.md)

## Everything else is *generated* from it

The YAML is the **one source of truth**; every other surface is derived from it and never hand-maintained in parallel:

- the **on-screen tabulation report** (what you show live),
- the full-detail **`_tabulated.txt`** record (the audit copy),
- the browsable **`.md` page** (the reader-facing surface, built by `build_yaml_pages.py`),
- the sortable **registry** (`BV_registry.md` / `bv_cases.csv`, built by `build_bv_registry.py` from the `bv_*` fields).

Because these are generated, they can't drift from the source. Edit the YAML, regenerate, done.

## The companion ideas

- **Store rich, display clean.** Keep all the context *in* the YAML; control what appears on screen with `options:` (e.g. `show_description: false`). You never delete information to get a clean demo. → [ORGANIZATION.md — storage ≠ display](ORGANIZATION.md) The sharpest example is the **marker vocabulary** (`-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued): all tabulate as `0`, yet the file records *why* each line is zero — a distinction a flat CSV of scores would flatten away. → [Abstention vs. a zero vs. "None of the Above"](../STAR_Voting/properties_and_limits/abstention_vs_zero_vs_nota.md)
- **The pipeline.** author → validate → tabulate → verify → publish, all wrapped around the one file. → [readme.md — one YAML file, a pipeline around it](../../readme.md)
- **The shape of a case.** Which fields are for humans vs the engine, ready to copy. → [YAML authoring template](YAML_authoring_template.md)

## The payoff

Because the case is legible *and* runnable *and* self-checking, the same file simultaneously:

1. **teaches** — a reader (or an audience) understands the election from the file/its page,
2. **runs** — the engine tabulates it with a transparent, reproducible count,
3. **verifies** — the embedded expected winner is enforced by CI, so a regression can't sneak in,
4. **audits** — a real BetterVoting export becomes a frozen, re-countable case that guards against the platform's bugs.

One file doing all four is the whole point. That's the YAML approach.
