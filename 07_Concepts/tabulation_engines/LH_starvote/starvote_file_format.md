# The `.starvote` ballot file format — write an election, get a report

**Level: reference · deep dive**

**One line:** Larry Hastings' engine reads a small INI-like text format where an election is just `[options]` plus a `[ballots]` block of `candidate = score` lines — hand-writable, diff-able, and enough on its own to produce a full audit report.

→ The engine itself: [The LH starvote engine](README.md) · reading its output: [How to read a STAR report](reading_a_star_report.md) · the report's sections flag-by-flag: [LH reporting options](../../../01_STAR/01_Learn/reporting/reporting_LH/options.md). Upstream: [`larryhastings/starvote`](https://github.com/larryhastings/starvote) · [PyPI](https://pypi.org/project/starvote/). Terms: [`GLOSSARY`](../../GLOSSARY.md).

---

## Why a text format at all

Larry's own answer, at the bottom of the parser's docstring:

> (Why'd I write this? I got tired of CSV files.)

A CSV row is positional — you count columns to find out who a `4` belongs to, and a candidate added in the middle silently shifts every ballot. The `.starvote` format is *named*: each line says which candidate got which score, so a ballot reads like a ballot and a diff of two elections is legible. It also carries its own settings, so the file is the whole experiment — no command-line flags to remember or forget.

## Three front doors, and they do not share a tiebreak default

The engine family accepts three inputs. This matters more than it looks: **the same ballots can elect different people through different doors**, because each door defaults to a different tie policy. The worked example below is built to expose exactly that.

| Input | Run it with | Defaults it brings |
|---|---|---|
| **`.starvote`** (this page) | `python -m starvote FILE.starvote` | Whatever the file's `[options]` say; `tiebreaker` defaults to `hashed_ballots` |
| **`.csv`** ([star.vote](https://star.vote) export shape) | `python -m starvote -m star FILE.csv` | STAR, 1 seat, `verbosity=1`, **no tiebreaker** |
| **`.yaml`** (this repo's house format) | `python starvote_larry_hastings.py FILE.yaml` | The [wrapper](../../../STARVote_LH_tabulation_engine/README_larry_hastings.md)'s reporting layer + a **lot-order** tiebreaker |

The CSV shape is not a bare score table: the loader **clips the first three columns** (`voterid`, `date`, `pollid`) before reading candidate names from the header, because it targets star.vote's export. A three-column CSV of pure scores therefore parses as *zero* candidates.

Only the `.yaml` door gets this repo's presentation layer — the matrix, `[Divergence from STAR]`, Equal Support labelling, and the `_tabulated` mirror. The `.starvote` door is upstream's own report, which is what makes it the honest place to document the format.

## The format in one screen

It is line-oriented and looks like INI without being INI:

- Leading and trailing whitespace is stripped. Blank lines and `#` comments are ignored — **except** in `[ballots]`, where they are the ballot separator.
- `[name]` on its own line opens a **section**. Only two exist — `[options]` and `[ballots]` — and each may appear only once.
- A line with `=` is an **assignment**: name before, value after.
- A value of `[` opens **list mode**; every following line is appended as a string until a line containing just `]`.
- A line ending in `:` is a **pragma**. Exactly one is defined (`n ballots:`), and pragmas are matched before assignments.

### `[options]` — the seven keys

Each may be given at most once. Names map to arguments of `starvote.election()`.

| Key | Value | Default | Notes |
|---|---|---|---|
| `method` | `star` · `bloc` · `allocated` · `rrv` · `sss` | *(required)* | Long names (`Bloc STAR Voting`) also work |
| `seats` | integer | `1` | Required for every method except single-winner STAR |
| `maximum score` | integer | `5` | The scale cap — what the [five-star rung](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) counts |
| `verbosity` | integer | `0` | `0` prints the winner only; `1` prints the round-by-round report |
| `tiebreaker` | name, `name(seed=N)`, or a list | `hashed_ballots` | `none` means *refuse to break ties*; a list is a pre-set candidate order |
| `print averages` | boolean | `false` | Adds `(average 4)` to each score line |
| `print maximum score` | boolean | `false` | Adds the `Maximum score is 5.` line |

Booleans accept `1/true/yes/on` and `0/false/no/off`.

**Two of those defaults are ours, not Larry's.** `print averages` and `print maximum score` are the only functional edits in the [vendored fork](../../../STARVote_LH_tabulation_engine/FORK_NOTES.md); upstream prints both lines unconditionally. So a report copied from stock `starvote` has two lines this repo's run will not show until you switch them on. That is the single most common "why doesn't my output match?" between the two.

### `[ballots]` — one assignment per candidate

Inside `[ballots]`, names are candidates and values are scores. **A blank line or a comment line starts a new ballot** — which is why the separator rule is inverted here. Candidates are discovered from the ballots; there is no roster to declare, so a typo silently invents a candidate.

To repeat a ballot, put the `n ballots:` pragma above it:

```
5 ballots:
Amy = 1
Brian = 3
Chuck = 3
```

Blank lines between the pragma and the ballot it repeats are explicitly allowed. List values are *not* permitted in this section.

## Worked example — a Bloc STAR race that ties all the way down

Three candidates, two seats, three ballots, and the scores rotate — ballot 1 ranks `c > b > a`, ballot 2 `a > c > b`, ballot 3 `b > a > c`. Perfect rock-paper-scissors.

```
[options]
seats = 2
method=bloc
tiebreaker = none
verbosity = 1

[ballots]

a = 3
b = 4
c = 5

a = 5
b = 3
c = 4

a = 4
b = 5
c = 3
```

Note `tiebreaker = none`. That is the point of the file: it tells the engine **not** to invent an answer, so the report stops at the tie instead of papering over it.

### The report

`python -m starvote bloc_three_way.starvote`, with `print averages` and `print maximum score` switched on so it matches stock upstream output. It opens by restating the parameters it parsed out of `[options]` — a free check that the file said what you meant:

```text
[Bloc STAR]
 Tabulating 3 ballots.
 Maximum score is 5.
 Want to fill 2 seats.
```

**Scoring round.** Every candidate collects one 3, one 4 and one 5:

```text
[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   a -- 12 (average 4) -- Tied for first place
   b -- 12 (average 4) -- Tied for first place
   c -- 12 (average 4) -- Tied for first place
 There's a three-way tie for first.
```

**First tiebreaker — the pairwise rung.** Read the number carefully: it is not matchups won, it is the count of **ballot-level preferences** each candidate collects across all its head-to-head matchups:

```text
[Bloc STAR: Round 1: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   a             -- 3 -- Tied for first place
   b             -- 3 -- Tied for first place
   c             -- 3 -- Tied for first place
   No Preference -- 0
```

Each candidate also wins exactly one matchup 2–1 (b beats a, c beats b, a beats c — the cycle), so the rung ties on either reading: 3 + 3 + 3 = 9, which is 3 matchups × 3 ballots. `No Preference` is 0 because no ballot ever scores two candidates equally. (The repo's wrapper renders that bucket as **Equal Support**; upstream's own report keeps the older label.)

**Second tiebreaker — the five-star rung**, which counts votes equal to the scale maximum. One each:

```text
[Bloc STAR: Round 1: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   a -- 1 -- Tied for first place
   b -- 1 -- Tied for first place
   c -- 1 -- Tied for first place
 There's still a three-way tie for first.
```

**And then it stops.** Every deterministic rung is exhausted and `tiebreaker = none` forbids a draw, so the engine declines to name a winner — the one outcome no other front door will give you:

```text
[Bloc STAR: Round 1: Scoring Round: Unbreakable Tie]
 Tie between a, b, and c.
```

Through the Python API the same election raises `UnbreakableTieError`; the CLI prints the block above and exits 0.

### The same election through the repo's wrapper

The house `.yaml` door runs the identical ballots through the presentation layer, and because it supplies a lot-order tiebreaker it *does* seat two candidates. This is the full LH report, embedded from the generated case page so it tracks the engine rather than going stale (candidates renamed for the public BetterVoting election: a → Arden, b → Blythe, c → Corin):

<!-- report:b484mbm_tie_every_rung -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 3 ballots to fill 2 seats.
Arden,Blythe,Corin
    3,     4,    5
    5,     3,    4
    4,     5,    3

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Arden         -- 12 -- Tied for first place
   Blythe        -- 12 -- Tied for first place
   Corin         -- 12 -- Tied for first place
 There's a three-way tie for first.

[Bloc STAR: Round 1: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Arden         -- 3 -- Tied for first place
   Blythe        -- 3 -- Tied for first place
   Corin         -- 3 -- Tied for first place
   Equal Support -- 0
 There's still a three-way tie for first.

[Bloc STAR: Round 1: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Arden         -- 1 -- Tied for first place
   Blythe        -- 1 -- Tied for first place
   Corin         -- 1 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Blythe', 'Arden', 'Corin']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Arden', 'Blythe', 'Corin']
  Resolved: ['Blythe', 'Arden'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Blythe        -- 2 -- First place
   Arden         -- 1
   Equal Support -- 0
 Blythe wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Blythe 2 (67%)  ·  Arden 1 (33%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Arden         -- 12 -- First place
   Corin         -- 12 -- Second place
 Arden and Corin advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Arden         -- 2 -- First place
   Corin         -- 1
   Equal Support -- 0
 Arden wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Arden 2 (67%)  ·  Corin 1 (33%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Blythe
 Arden
```
<!-- /report -->

Same three rungs, same three ties — then the matrix, the Condorcet check, the `⚠ Lot-decided tie` warning, and the two seats filled by the lot. Side by side, the two reports are the clearest statement of what a tiebreak policy actually decides.

Two footnotes on the rungs. The five-star rung here is the neighbour of the ["dead rung"](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) cases, where it reads 0–0 because nobody scored a 5 at all — here it fires and *still* cannot separate anyone. And `tiebreaker = none` is what makes the refusal visible: every other setting would have quietly produced two winners from a ballot set that does not contain them.

### The same ballots, four different answers

Change nothing but the door, and the winners change:

| How it's run | Tie policy | Winners |
|---|---|---|
| `tiebreaker = none` (above) | refuses | **none — unbreakable tie** |
| `.starvote` with `tiebreaker` omitted | `hashed_ballots` (deterministic from ballot content) | **a, c** |
| the same election as repo `.yaml` | lot order, falling back to CSV column order `[a, b, c]` | **b, a** |
| the same election [live on BetterVoting](https://bettervoting.com/484mbm/results) | seeded random draw | **b, a** |

None of these is more correct than the others. When the ballots genuinely do not distinguish the candidates, the winner is decided by whatever tiebreak policy was configured *before* the count — which is the argument for publishing that policy in advance, and the reason the wrapper prints a `⚠ Lot-decided tie — rare` warning naming the fallback it used. See [Bloc STAR tiebreaks](../../../02_STAR_Bloc/01_Learn/bloc_tiebreaks.md) and [the full tie-breaking chain](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md).

### The same election on BetterVoting

This election is live as **[`484mbm`](https://bettervoting.com/484mbm/results)** so the two engines can be read side by side, with the cast renamed for the public page: **a → Arden, b → Blythe, c → Corin**.

BetterVoting elects **Blythe and Arden** — the same pair the repo wrapper picks, but by a different route, and its ladder is genuinely shorter: it **skips the pairwise rung whenever more than two candidates are tied** (`pairwise_too_many_candidates`) and goes straight from score to five-star to a seeded random draw. The LH engine computes that rung and reports it tied 3–3–3. Here the shortcut costs nothing; on ballots where pairwise *would* separate three tied candidates, the two engines would disagree.

Worth knowing before citing a BV results page as evidence of a tie: round 0 records `tieBreakType: "random"`, but the **top-level `tieBreakType` reads `"none"` and `tied` is `[]`**, so the public page shows a flat 12/12/12 followed by a Blythe-vs-Arden runoff with nothing saying the finalists were drawn rather than earned. The two-view write-up — screenshot, BV's round logs, and the LH report with BV's draw pinned so the two reproduce each other — is [a three-way tie no rung can break](../../../02_STAR_Bloc/02_Examples/b484mbm_tie_every_rung.md).

## Errata — the unbreakable-tie message leaks a placeholder

**Fixed in this repo's vendored engine (2026-08); still present upstream.** Originally found against `starvote 2.1.6`: ask for the tie through the API rather than the CLI, and the exception message arrived unformatted.

```
UnbreakableTieError: Round 1: Scoring Round: {int_to_words(len(tie), flowery=False)}-way tie in Scoring Round
```

Both `UnbreakableTieError` strings in `_star_round()` were missing their `f` prefix, so the placeholder was never interpolated. `allocated_score_voting()` and `sequentially_spent_score()` build the same message correctly, which is why only STAR and Bloc STAR showed it — `_star_round()` serves both. The printed report was never affected — this is the exception text only, and the CLI prints its own `[Unbreakable Tie]` block and exits 0 — but any tool that surfaces the exception to a user showed the raw source. Upstream, not a fork regression.

The fix is two characters (`"…"` → `f"…"`) and changes no winner: the message is built only once a tie is already unbreakable. The vendored engine now reports it properly, and [`tests/test_unbreakable_tie_message.py`](../../../STARVote_LH_tabulation_engine/tests/test_unbreakable_tie_message.py) keeps it that way:

```
UnbreakableTieError: Round 1: Scoring Round: three-way tie in Scoring Round
```

Reproduce the *upstream* behaviour with a stock `pip install starvote==2.1.6`; it is unchanged on upstream `main` too (the same two lines, there numbered 1690 and 1717). Reported to Larry as [larryhastings/starvote#18](https://github.com/larryhastings/starvote/issues/18), separately from [#17](https://github.com/larryhastings/starvote/issues/17) (the SSS verbosity bug) because that one changes winners and this one cannot. See [`FORK_NOTES.md`](../../../STARVote_LH_tabulation_engine/FORK_NOTES.md) for the fork's record of the edit.

## The same election as repo YAML

For anything that belongs in the library, use the house format — it is what the [wrapper](../../../STARVote_LH_tabulation_engine/README_larry_hastings.md) reads, and only YAML cases get a `_tabulated` mirror and a generated case page.

| `.starvote` | repo `.yaml` |
|---|---|
| `method = bloc` | `voting_method: Bloc STAR` |
| `seats = 2` | `num_winners: 2` |
| `maximum score = 5` | implied by the 0–5 scale |
| `tiebreaker = [...]` | `lot_numbers: [...]` |
| `verbosity` / `print averages` | the `options:` block |
| `[ballots]` name = score | `ballots: \|-` CSV block |

```yaml
election_title: "Bloc STAR — 3 candidates / 2 seats, tied at every rung"

options:
  brief: true
  show_matrix: false
  show_condorcet: false

num_winners: 2
voting_method: Bloc STAR
ballots: |-
  a,b,c
  3,4,5
  5,3,4
  4,5,3
```

The trade-off is legibility against tooling: `.starvote` keeps candidate names next to their scores, which is easier to hand-write and to review; the YAML block is positional but carries the repo's reporting options, expected winners, and teaching text. Use `.starvote` to sketch or to reproduce an upstream report, YAML for anything that ships.

## See also

- [The LH starvote engine — what it is, and what we added](README.md) — the two layers, and what the wrapper adds on top.
- [How to read a STAR report](reading_a_star_report.md) — the section-by-section walkthrough of the output.
- [STAR Tie-Breaking — the full chain](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) · [the dead rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) — where this example's three rungs come from.
- [Bloc STAR](../../../02_STAR_Bloc/README.md) — the method the example uses, and why it is not proportional.
- [Vendored engine README](../../../STARVote_LH_tabulation_engine/README.md) — upstream's own description of the format.
