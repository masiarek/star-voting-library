# Why YAML? One file a person reads and a computer runs

The core design goal of this library: **each test case is a single file that is, at the same time, human-readable and machine-runnable.** A person can read the scenario and the ballots and understand the election; the engine can parse the same file, tabulate it, and a test can verify the winner. No translation step, no second copy.

That one decision is why the library can be *taught, run, and audited* from the same source — instead of forcing a choice between "readable for people" and "usable by tools."

## The problem it avoids

The usual way to keep test cases splits them in two: prose for humans (a doc describing the scenario) and data for machines (a CSV/JSON/fixture the code runs). The two **drift apart** — the doc says one thing, the fixture does another, and nobody notices until a count is wrong. You also can't *read* the machine copy or *run* the human copy.

This library refuses that split. There is **one artifact**, and it's legible both ways.

## What that looks like

A whole election, in one small YAML ([`01a_c2_b2_two-candidates.yaml`](../01_STAR/_main/01a_c2_b2_two-candidates.yaml)):

```yaml
election_title: Same as before - but this time two ballots

scenario_description: |-              # ← for the human: what this case teaches
  The same election as 01a_c2_b1 with one more identical ballot: two voters,
  both scoring Chocolate 5 and Vanilla 3. Nothing changes but the totals.

video_script: |-                      # ← for the human: presenter notes, never echoed

ballots: |-                           # ← for BOTH: a person reads it as a table;
  Chocolate,Vanilla                   #    the engine reads it as the cast votes
          5,      3       # Caroline - she likes both flavors
          5,      3       # Bob - he likes both flavors too

options:                              # ← for the engine: how to render the report
  show_matrix: false
  brief: true

expected_winners:                     # ← for BOTH: the human sees the claim,
  - Chocolate                         #    the test suite enforces it
```

- **A person** reads `election_title`, `scenario_description`, the ballot table (with inline per-voter comments), and the expected winner — and understands the whole case at a glance.
- **The engine** reads `ballots`, `voting_method` (defaulted here), and `options` and produces an annotated, round-by-round count; the **pytest** suite reads `expected_winners` and fails if the engine disagrees.

Same file. Two readers. Never out of sync — because there's nothing to keep in sync.

## Everything else is *generated* from it

The YAML is the **one source of truth**; every other surface is derived from it and never hand-maintained in parallel:

- the on-screen **tabulation echo** (what you show live),
- the full-detail **`_tabulated.txt`** record (the audit copy),
- the browsable **`.md` page** (the reader-facing surface, built by `build_yaml_pages.py`),
- the sortable **registry** (`BV_registry.md` / `bv_cases.csv`, built by `build_bv_registry.py` from the `bv_*` fields).

Because these are generated, they can't drift from the source. Edit the YAML, regenerate, done.

## The companion ideas

- **Store rich, display clean.** Keep all the context *in* the YAML; control what appears on screen with `options:` (e.g. `show_description: false`). You never delete information to get a clean demo. → [ORGANIZATION.md — storage ≠ display](ORGANIZATION.md)
- **The pipeline.** author → validate → tabulate → verify → publish, all wrapped around the one file. → [readme.md — one YAML file, a pipeline around it](../readme.md)
- **The shape of a case.** Which fields are for humans vs the engine, ready to copy. → [YAML authoring template](YAML_authoring_template.md)

## The payoff

Because the case is legible *and* runnable *and* self-checking, the same file simultaneously:

1. **teaches** — a reader (or an audience) understands the election from the file/its page,
2. **runs** — the engine tabulates it with a transparent, reproducible count,
3. **verifies** — the embedded expected winner is enforced by CI, so a regression can't sneak in,
4. **audits** — a real BetterVoting export becomes a frozen, re-countable case that guards against the platform's bugs.

One file doing all four is the whole point. That's the YAML approach.
