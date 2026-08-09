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

Richer files keep more *human* context in the same file — an `election_title`, a `scenario_description`, inline per-voter notes on the ballot rows — all stored in the one artifact and never shown on screen unless you ask (the engine's `--full` run and the `_tabulated` copy show everything). → [YAML authoring template](YAML_authoring_template.md)

The same tiny format holds every method in the repo: swap `voting_method:` to `Approval`, `RankedRobin`, or a multi-winner count and only that line and the ballot rows change. What the methods *do differently* — and when to reach for each — is [Voting 201](../07_Concepts/curriculum/CURRICULUM_201.md), not this page's job.

**Not the only ballot format.** The election-methods world has a dedicated ballot-*interchange* format, **ABIF**, that packs ranks and scores into one dense line (`Allie/5 =Billy/5 >Candace/4`). It maps to just our **`ballots:` block** — our file wraps method, options, and an enforced answer key around that. The full decode and an honest side-by-side: [ABIF vs. our YAML grid](../07_Concepts/scores_and_ranks/abif_format.md).

## Why the first line is `voting_method:`

Because a ballot is not valid or invalid on its own. **It is only valid *relative to a method*** — and a bare grid of numbers doesn't say which one. Here is the same election as a plain CSV, the way ballots usually get passed around:

```text title="ex1 — a bare CSV, from bettervoting#778"
line 1:   0,1,0,0
line 2:   0,0,0,0
line 3:   0,1,0
line 4:   0,0,1,1
line 5:   0,0,0,0
line 6:   0,1,0
line 7:   0,0,0,0
line 8:   0, ,0,,
```

Nothing here can be validated, because nothing here can be *interpreted*. Are those scores or ranks? Single-winner or multi? Three candidates or four? And each line has several readings:

- **Line 4 (`0,0,1,1`)** is a perfectly good **Approval** or **STAR** ballot — and an **invalid Plurality** ballot, two votes in a one-vote race. Same eight characters, valid or spoiled depending entirely on a fact the file doesn't carry.
- **Lines 2 and 7 (`0,0,0,0`)** could be a voter who deliberately scored everyone zero, a blank ballot, a spoiled ballot, or a truncation bug. Four different things, one string.
- **Lines 3 and 6** have three values where the others have four; **line 8** has five fields. Deliberate blanks, abstentions, or stray commas?

Declaring the method in the file is what turns those from unanswerable questions into checks a machine can run. Set `voting_method: Approval` and a stray `3` is caught, with the fix named:

```text
Error: Approval ballots may only use scores {0, 1} (0 = not approved, 1 = approved).
    ballot 2: 0,3,1,0   (invalid: B=3)
  Fix or remove these rows. If they are 0..5 score ballots, set voting_method to STAR.
```

Set a *score* method and hand it ranked rows, and that's caught too:

```text
Error: mixed ballot styles — this file has ranked rows ('A>B>C') AND comma-separated rows.
  Use ONE style: either every row ranked (RCV-IRV / Ranked Robin),
  or a score grid (header row of names, then 0..5 scores) under a score method.
```

Neither check is possible without the declaration. That's the whole reason the method, the seat count and the candidate names live *in* the file rather than in the head of whoever loads it — and the same principle covers the second half of the problem, the **intent behind a zero**: a real low score, a blank, a deliberate abstention and a spoiled ballot all tabulate as `0`, so the file records which is which with a marker (`-` `~` `&` `?` `%`) instead of flattening them into one character.

→ All eight lines worked through, and the same eight in this schema: **[Eight lines of CSV, eight questions](csv_ambiguity.md)**

## Everything else is *generated* from it

The YAML is the **one source of truth**. The on-screen report, the full-detail `_tabulated.txt` audit copy, the browsable `.md` page, and the sortable registry are all derived from it and never hand-maintained in parallel — so they can't drift from the source. Edit the YAML, regenerate, done.

→ The five stages that do the deriving, from writing the file to publishing it: [YAML election files — why, what, how](README.md)

## The companion ideas

- **Store rich, display clean.** Keep all the context *in* the YAML; the engine's default on-screen report already hides the heavier sections (the long description stays in the file, on screen only via `--full` — and always in the `_tabulated` copy). You never delete information to get a clean demo. → [ORGANIZATION.md — storage ≠ display](ORGANIZATION.md) The sharpest example is the **marker vocabulary** (`-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued): all tabulate as `0`, yet the file records *why* each line is zero — a distinction a flat CSV of scores would flatten away. → [Abstention vs. a zero vs. "None of the Above"](../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md)
- **The shape of a case.** Which fields are for humans vs the engine, ready to copy. → [YAML authoring template](YAML_authoring_template.md)

## The payoff

Because the case is legible *and* runnable *and* self-checking, the same file simultaneously:

1. **teaches** — a reader (or an audience) understands the election from the file/its page,
2. **runs** — the engine tabulates it with a transparent, reproducible count,
3. **verifies** — the embedded expected winner is enforced by CI, so a regression can't sneak in,
4. **audits** — a real BetterVoting export becomes a frozen, re-countable case that guards against the platform's bugs.

One file doing all four is the whole point. That's the YAML approach.
