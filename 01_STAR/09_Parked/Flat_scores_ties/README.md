# Flat scores & ties — eight engineered dead heats, one page

**Parked, on purpose.** These eight elections are *constructed* — ballots built to tie, not elections anyone would hold. They are worth keeping as engine fixtures and as the reference transcript for what STAR's tie-break cascade does when the score-based rungs run out. They are not worth walking through one at a time, which is why the whole set lives on this single page, here, rather than as eight lessons on the learning path.

The teaching version of tie-breaking is in [`03_Criteria`](../../03_Criteria/README.md): [the tie-break ladder](../../03_Criteria/tie_break_ladder/README.md) (elections that tie but settle on a deterministic rung) and [the dead rung](../../03_Criteria/tie_break_dead_rung/README.md) (when the five-star rung reads 0–0 and the lot decides). Start there. This page is the exhaustive edge-case sweep behind them.

Concept backing: [The Automatic Runoff Round](../../01_Learn/the_count/STAR_Automatic_Runoff.md) · [STAR Tie-Breaking](../../01_Learn/Tie_Breaking_STAR/tie_breaking.md) · [reporting true ties](../../01_Learn/reporting/reporting_ties.md) · [`GLOSSARY`](../../../07_Concepts/GLOSSARY.md) · [why these contrived cases are worth building](../../../07_Concepts/topics/ties/why_contrived_tie_cases.md).

---

## The tie-break cascade (the reference behavior) {#cascade}

STAR breaks ties **deterministically**, in a fixed order, and the LH engine *prints every step*. Two cascades, depending on where the tie is:

**Scoring Round** — which candidates become the two **Finalists**:

1. **Head-to-head** — the candidate(s) preferred in the most pairwise matchups advance.
2. **Most 5s** — the candidate(s) with the most top scores advance.
3. **Lot number** — a fixed, pre-published priority order (here: A, B, C, …). When no official lot numbers are supplied, the engine falls back to ballot-column order and says so.

**Automatic Runoff** — which finalist **wins**:

1. **Highest score** — the higher total wins.
2. **Most 5s** — the more top scores wins.
3. **Lot number** — as above.

The point of the lot number is **reproducibility**: any auditor with the same ballots and the same lot order gets the same winner.

Each scenario below has its own friendly cast in **lot-priority order**, so the first-named (A-initial) candidate is the one the lot favors and the cascade stays easy to follow. **Case 05 keeps bare `A–E`** — it matches the exact ballots in the BetterVoting election `xmyf7k`, so renaming would desync from that screenshot.

## The eight scenarios {#scenarios}

| # | What it isolates | Cast | Where the tie is | LH winner |
|---|---|---|---|:---:|
| [01](#case-01) | clean top two — the control, no tie at all | fruits | none | Apple |
| [02](#case-02) | runoff tie, two candidates, everyone equal | ice cream | runoff (all Equal Support) | Almond |
| [03](#case-03) | runoff tie from a real even 1–1 split | capitals | runoff (real split) | Athens |
| [04](#case-04) | scoring-round tie for the 2nd finalist slot | lakes | scoring round | Aral |
| [05](#case-05) | 3-way scoring tie — every rung ties | A–E | scoring round | A |
| [06](#case-06) | 4-way scoring tie — ties at every step, both rounds | names | both rounds | Ava |
| [07](#case-07) | fully flat ballots — the maximal tie | mountains | both rounds | Ararat |
| [08](#case-08) | every ballot flat, each at a different level | pizza | both rounds | Anchovy |

**"But 5,5,5,0 works fine?"** Worth flagging up front: `5,5,5,0` does **not** sidestep the problem — in STAR it is a genuine **3-way tie** (all three total 10), the same shape as case 05. What actually works cleanly — no tie-break at all — is scores that leave an **unambiguous top two and a decisive runoff** (case 01). So the honest contrast isn't "flat vs not-flat," it's **"tie vs no-tie."** Flat-*looking* high scores are fine *until* they produce an exact tie.

---

## Case 01 — clean top two (the baseline) {#case-01}

The control. Distinct totals leave an unambiguous top two and a decisive runoff, so **no tie-break fires anywhere.** This is the contrast every later case is measured against.

```
Apple, Banana, Cherry
5, 3, 1
5, 3, 1
```

Totals are **Apple 10, Banana 6, Cherry 2** — all different. The top two are unambiguous, and in the runoff every voter scored Apple above Banana, so Apple wins outright. No head-to-head step, no "most 5s" step, no lot number.

<!-- report:Flat_scores_ties_01_baseline_clean -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Count × Apple,Banana,Cherry
    2 ×     5,     3,     1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Apple         -- 10 -- First place
   Banana        --  6 -- Second place
   Cherry        --  2
 Apple and Banana advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Apple         -- 2 -- First place
   Banana        -- 0
   Equal Support -- 0
 Apple wins.
   Runoff math:
     2  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Apple 2 (100%)  ·  Banana 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Apple
```
<!-- /report -->
Source: [`Flat_scores_ties_01_baseline_clean.yaml`](cases/Flat_scores_ties_01_baseline_clean.yaml) · audit copy: [`_tabulated`](cases/cases_tabulated/Flat_scores_ties_01_baseline_clean_tabulated.txt).

**Takeaway.** When scores are distinct, tie-breaking never runs and every tabulator agrees. Every case from here on changes exactly one thing — makes the top scores *equal* — and watches what happens.

## Case 02 — runoff tie, two candidates, everyone equal {#case-02}

The smallest tie there is. Two flavors, both scored **5** by every voter. Both advance (there are only two), the runoff is **0–0 Equal Support**, and the cascade decides.

```
Almond, Brownie
5, 5
5, 5
```

Both total 10 and both advance. In the runoff every ballot scored them **equally**, so both are **Equal Support** — the runoff is 0–0. The cascade runs: **highest score** (10 = 10, tied), **most 5s** (2 = 2, tied), then the **lot number** picks Almond.

<!-- report:Flat_scores_ties_02_runoff_tie_2cand -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Count × Almond,Brownie
    2 ×      5,      5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Almond        -- 10 -- First place
   Brownie       -- 10 -- Second place
 Almond and Brownie advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Almond        -- 0 -- Tied for first place
   Brownie       -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Almond        -- 10 -- Tied for first place
   Brownie       -- 10 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Almond        -- 2 -- Tied for first place
   Brownie       -- 2 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Almond', 'Brownie']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Almond', 'Brownie']
  Resolved: ['Almond'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Almond
```
<!-- /report -->
Source: [`Flat_scores_ties_02_runoff_tie_2cand.yaml`](cases/Flat_scores_ties_02_runoff_tie_2cand.yaml) · audit copy: [`_tabulated`](cases/cases_tabulated/Flat_scores_ties_02_runoff_tie_2cand_tabulated.txt).

**Takeaway.** A pure flat ballot is a *cast vote with no preference* (**Equal Support**), not an abstention — and an all-equal runoff is resolved, not undefined. The answer the cascade lands on is reproducible by anyone holding the published lot order.

## Case 03 — runoff tie, an even 1–1 split {#case-03}

The other flavor of runoff tie. Unlike case 02 (everyone *equal*), here two voters have **real, opposing preferences**: one prefers Athens, one prefers Berlin.

```
Athens, Berlin, Cairo
5, 4, 0
4, 5, 0
```

Athens and Berlin each total 9 (Cairo totals 0), so they advance with no scoring-round tie. In the runoff, voter 1 prefers Athens and voter 2 prefers Berlin — a genuine **1–1 split**, no Equal Support. The cascade runs: **highest score** (9 = 9), **most 5s** (1 = 1), then **lot** → Athens.

<!-- report:Flat_scores_ties_03_runoff_tie_split -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Athens,Berlin,Cairo
     5,     4,    0
     4,     5,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Athens        -- 9 -- First place
   Berlin        -- 9 -- Second place
   Cairo         -- 0
 Athens and Berlin advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Athens        -- 1 -- Tied for first place
   Berlin        -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Athens        -- 9 -- Tied for first place
   Berlin        -- 9 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Athens        -- 1 -- Tied for first place
   Berlin        -- 1 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Athens', 'Berlin', 'Cairo']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Athens', 'Berlin']
  Resolved: ['Athens'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Athens
```
<!-- /report -->
Source: [`Flat_scores_ties_03_runoff_tie_split.yaml`](cases/Flat_scores_ties_03_runoff_tie_split.yaml) · audit copy: [`_tabulated`](cases/cases_tabulated/Flat_scores_ties_03_runoff_tie_split_tabulated.txt).

**Takeaway.** Two runoff ties, two different causes — **all-Equal-Support** (case 02) vs **a real even split** (this one) — resolve through the *same* cascade to the *same* reproducible answer. The distinction matters for reading the report, not for how the tie is broken.

## Case 04 — scoring-round tie for the 2nd finalist slot {#case-04}

The first *scoring-round* tie. Aral leads outright; **Baikal and Crater tie for the second finalist slot**, so the cascade runs in the scoring round to decide *who advances*.

```
Aral, Baikal, Crater
5, 4, 4
5, 4, 4
5, 0, 0
```

Totals: **Aral 15, Baikal 8, Crater 8.** Aral is first outright; Baikal and Crater are tied for the **second** slot — and *which one advances can change the winner*, so the tie must be broken. Cascade: **head-to-head** (0–0, three Equal Support → tied), **most 5s** (0 = 0, tied), then **lot** → **Baikal** advances. Aral then beats Baikal 3–0.

<!-- report:Flat_scores_ties_04_scoring_tie_2way -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Count × Aral,Baikal,Crater
    2 ×    5,     4,     4
    1 ×    5,     0,     0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Aral          -- 15 -- First place
   Baikal        --  8 -- Tied for second place
   Crater        --  8 -- Tied for second place
 Aral advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Baikal        -- 0 -- Tied for second place
   Crater        -- 0 -- Tied for second place
   Equal Support -- 3
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Baikal        -- 0 -- Tied for second place
   Crater        -- 0 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Aral', 'Baikal', 'Crater']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Baikal', 'Crater']
  Resolved: ['Baikal'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Aral          -- 3 -- First place
   Baikal        -- 0
   Equal Support -- 0
 Aral wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Aral 3 (100%)  ·  Baikal 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Aral
```
<!-- /report -->
Source: [`Flat_scores_ties_04_scoring_tie_2way.yaml`](cases/Flat_scores_ties_04_scoring_tie_2way.yaml) · audit copy: [`_tabulated`](cases/cases_tabulated/Flat_scores_ties_04_scoring_tie_2way_tabulated.txt).

**Takeaway.** A scoring-round tie isn't always about the winner — here it decides the *runner-up's seat*. The engine shows that Baikal only edged out Crater by lot number, so the choice is auditable.

## Case 05 — 3-way scoring tie, every rung ties (`xmyf7k`) {#case-05}

The cleanest possible test of "does your tabulator break a fully-tied race *deterministically*, and does it *show its work*?" Three candidates tie at the top and **every score-based tiebreaker stays tied**, so the winner turns entirely on the **terminal tiebreak**.

```
A, B, C, D, E
5, 5, 5, 4, 4
5, 5, 5, 4, 4
```

With the published lot order `[A, B, C, D, E]` the LH reference answer is **A**. Head-to-head is a **no-op** here — there is no preference among A, B and C — and the five-star count ties too, so rung 3 decides.

<!-- report:Flat_scores_ties_05_scoring_tie_3way_xmyf7k -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Count × A,B,C,D,E
    2 × 5,5,5,4,4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 10 -- Tied for first place
   B             -- 10 -- Tied for first place
   C             -- 10 -- Tied for first place
   D             --  8
   E             --  8
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   A             -- 0 -- Tied for first place
   B             -- 0 -- Tied for first place
   C             -- 0 -- Tied for first place
   Equal Support -- 2
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   A             -- 2 -- Tied for first place
   B             -- 2 -- Tied for first place
   C             -- 2 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['A', 'B', 'C', 'D', 'E']

[Tiebreaker: Lot Number Priority]
  Tie among: ['A', 'B', 'C']
  Resolved: ['A', 'B'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 0 -- Tied for first place
   B             -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   A             -- 10 -- Tied for first place
   B             -- 10 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   A             -- 2 -- Tied for first place
   B             -- 2 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['A', 'B']
  Resolved: ['A'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```
<!-- /report -->
Source: [`Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml`](cases/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml) · audit copy: [`_tabulated`](cases/cases_tabulated/Flat_scores_ties_05_scoring_tie_3way_xmyf7k_tabulated.txt) · BV: <https://bettervoting.com/xmyf7k/results>.

**LH-only / not freezable.** This case turns on the terminal tiebreak, and that is the one rung where two conforming engines can legitimately part company: LH breaks the dead heat by **pre-published lot**, BetterVoting by **random shuffle** (BV's protocol deliberately skips head-to-head for 3+ way ties — a documented design choice, [confirmed working-as-intended](https://github.com/Equal-Vote/bettervoting/issues/1379)). A random terminal rung means there is no stable BV result to record, so this case carries no `_bv_export.json` and documents the LH ladder specifically. The Ranked Robin analog of exactly this story is [rr_tiebreak_lh_vs_bv.md](../../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md).

**Takeaway.** When every score-based tiebreaker ties, the only thing that lets two independent systems agree is a **shared, deterministic tie-break order**. LH publishes its lot order and prints every step, so **A** is reproducible from the ballots plus that order; a random terminal rung is not a function of the ballots at all.

## Case 06 — 4-way scoring tie, ties at every step {#case-06}

The full cascade, both rounds. Four candidates tie at 10; the ties persist through **every** score-based tiebreaker; the lot picks two finalists; and then the **runoff also ties** → lot again.

```
Ava, Ben, Cara, Dan, Eve
5, 5, 5, 5, 1
5, 5, 5, 5, 1
```

Ava, Ben, Cara and Dan all total 10 — a **four-way tie** for two finalist slots. Head-to-head: all 0 (everyone Equal Support). Most 5s: all 2. The **lot** picks **Ava, Ben**. The runoff is then 0–0 → highest score tied → most 5s tied → **lot** → **Ava**.

<!-- report:Flat_scores_ties_06_scoring_tie_4way -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Count × Ava,Ben,Cara,Dan,Eve
    2 ×   5,  5,   5,  5,  1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ava           -- 10 -- Tied for first place
   Ben           -- 10 -- Tied for first place
   Cara          -- 10 -- Tied for first place
   Dan           -- 10 -- Tied for first place
   Eve           --  2
 There's a four-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Ava           -- 0 -- Tied for first place
   Ben           -- 0 -- Tied for first place
   Cara          -- 0 -- Tied for first place
   Dan           -- 0 -- Tied for first place
   Equal Support -- 2
 There's still a four-way tie for first.
 Every head-to-head among the tied candidates is a draw, so none of them won a matchup.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Ava           -- 2 -- Tied for first place
   Ben           -- 2 -- Tied for first place
   Cara          -- 2 -- Tied for first place
   Dan           -- 2 -- Tied for first place
 There's still a four-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ava', 'Ben', 'Cara', 'Dan', 'Eve']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ava', 'Ben', 'Cara', 'Dan']
  Resolved: ['Ava', 'Ben'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ava           -- 0 -- Tied for first place
   Ben           -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Ava           -- 10 -- Tied for first place
   Ben           -- 10 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Ava           -- 2 -- Tied for first place
   Ben           -- 2 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ava', 'Ben']
  Resolved: ['Ava'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ava
```
<!-- /report -->
Source: [`Flat_scores_ties_06_scoring_tie_4way.yaml`](cases/Flat_scores_ties_06_scoring_tie_4way.yaml) · audit copy: [`_tabulated`](cases/cases_tabulated/Flat_scores_ties_06_scoring_tie_4way_tabulated.txt).

**Takeaway.** No matter how many candidates tie or how many steps stay tied, a published lot order terminates the cascade with a reproducible winner — and every step is printed, so even a maximally tied election stays fully auditable.

## Case 07 — fully flat ballots, the maximal tie {#case-07}

Every voter scores **every** candidate 5. Tied in **both** rounds, resolved entirely by lot.

```
Ararat, Blanc, Cook
5, 5, 5
5, 5, 5
```

All three total 10 — a three-way tie. Head-to-head: all 0 (every pair is Equal Support). Most 5s: all 2. The **lot** advances **Ararat, Blanc**; the runoff is 0–0 → lot → **Ararat**. Crucially, both ballots are **counted** the whole way — they are Equal Support, not abstentions, so they sit in the score totals and in the runoff's Equal-Support bucket. Nothing is dropped.

<!-- report:Flat_scores_ties_05_scoring_tie_3way_xmyf7k -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Count × A,B,C,D,E
    2 × 5,5,5,4,4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 10 -- Tied for first place
   B             -- 10 -- Tied for first place
   C             -- 10 -- Tied for first place
   D             --  8
   E             --  8
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   A             -- 0 -- Tied for first place
   B             -- 0 -- Tied for first place
   C             -- 0 -- Tied for first place
   Equal Support -- 2
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   A             -- 2 -- Tied for first place
   B             -- 2 -- Tied for first place
   C             -- 2 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['A', 'B', 'C', 'D', 'E']

[Tiebreaker: Lot Number Priority]
  Tie among: ['A', 'B', 'C']
  Resolved: ['A', 'B'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 0 -- Tied for first place
   B             -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   A             -- 10 -- Tied for first place
   B             -- 10 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   A             -- 2 -- Tied for first place
   B             -- 2 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['A', 'B']
  Resolved: ['A'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```
<!-- /report -->
Source: [`Flat_scores_ties_07_fully_flat.yaml`](cases/Flat_scores_ties_07_fully_flat.yaml) · audit copy: [`_tabulated`](cases/cases_tabulated/Flat_scores_ties_07_fully_flat_tabulated.txt).

**Takeaway.** The maximal tie is still deterministic — lot order decides, every step shown. It is also the sharpest illustration of the distinction the whole set turns on: **"no preference" is not "no vote."** A fully-flat ballot is Equal Support, counts in full, and belongs in the tie.

## Case 08 — every ballot flat, at a different level {#case-08}

Where case 07 had everyone score the *same* value, here each voter is flat at a *different* level — 1s, then 2s, … then 5s. Still every ballot is flat.

```
Anchovy, Basil, Caper
1, 1, 1
2, 2, 2
3, 3, 3
4, 4, 4
5, 5, 5
```

Every row is flat — each voter likes all three equally, just at a different intensity. Totals: **Anchovy 15, Basil 15, Caper 15**, a three-way tie resolved by lot to **Anchovy**. All five ballots count; each is Equal Support, not an abstention.

<!-- report:Flat_scores_ties_08_all_flat_zero_count -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Anchovy,Basil,Caper
      1,    1,    1
      2,    2,    2
      3,    3,    3
      4,    4,    4
      5,    5,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Anchovy       -- 15 -- Tied for first place
   Basil         -- 15 -- Tied for first place
   Caper         -- 15 -- Tied for first place
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Anchovy       -- 0 -- Tied for first place
   Basil         -- 0 -- Tied for first place
   Caper         -- 0 -- Tied for first place
   Equal Support -- 5
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Anchovy       -- 1 -- Tied for first place
   Basil         -- 1 -- Tied for first place
   Caper         -- 1 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Anchovy', 'Basil', 'Caper']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Anchovy', 'Basil', 'Caper']
  Resolved: ['Anchovy', 'Basil'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Anchovy       -- 0 -- Tied for first place
   Basil         -- 0 -- Tied for first place
   Equal Support -- 5
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Anchovy       -- 15 -- Tied for first place
   Basil         -- 15 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Anchovy       -- 1 -- Tied for first place
   Basil         -- 1 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['Anchovy', 'Basil']
  Resolved: ['Anchovy'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Anchovy
```
<!-- /report -->
Source: [`Flat_scores_ties_08_all_flat_zero_count.yaml`](cases/Flat_scores_ties_08_all_flat_zero_count.yaml) · audit copy: [`_tabulated`](cases/cases_tabulated/Flat_scores_ties_08_all_flat_zero_count_tabulated.txt).

**Takeaway.** "Flat" is not "blank." A ballot that scores every candidate — even all at 1, or all at 5 — is a **cast vote with no preference**, and it belongs in the count, the score totals, and the tie. Treating "no preference" as "no vote" is what would turn five real voters into a reported zero.

---

## Why the set exists {#why}

Every scenario above is a probe, not an election. Together they sweep the tie surface: no tie (01), each locus of tie on its own (02–04), a tie that reaches the terminal rung (05), ties at every step of both rounds (06), and the two degenerate shapes where the ballots say nothing at all (07–08). Held together they answer one question — *what does the count do when the ballots refuse to separate anyone?* — and the answer is that a pre-published lot order terminates the cascade every time, with each step printed.

That reproducibility argument is also what makes the set useful as a **conformance suite**: any tabulator handed these eight files and the published lot order should reach the same eight winners. Cases 05, 07 and 08 in particular sit on the **Equal Support vs abstention** distinction, which is the single easiest thing for an implementation to get wrong. Worked end-to-end elsewhere in the library: [`Runoff_07`](../../04_Real_Elections/runoff_reversal_bv_cases/Runoff_07_flat_ballot_bv_bug_tf73v9.md) · [`small_case_abstention_lesson`](../../04_Real_Elections/pet_real_bv_election/small_case_abstention_lesson.md) · [abstain / blank / zero handling](../../04_Real_Elections/abstain_bugs/README.md).

## BetterVoting QA notes {#bv-status}

Kept here because this set is where the fixtures live, not because it belongs on the learning path. Several of these scenarios were built to reproduce BetterVoting reports; the tracker is the source of truth for status.

| Report | What it's about | Cases |
|--------|-----------------|-------|
| [#1407 — flat ballot mis-filed as abstention](https://github.com/Equal-Vote/bettervoting/issues/1407) | a fully-flat (every-candidate-equal) ballot is dropped as an abstention | 07, 08 |
| [#1035 — BV200, "NaN" on equal ties/prefs](https://github.com/Equal-Vote/bettervoting/issues/1035) | NaN displayed for equal ties and equal preferences | 02, 07 |
| [#1052 — BV126, "no ballots cast" message](https://github.com/Equal-Vote/bettervoting/issues/1052) | wrong "no ballots have been cast" message when ties hit every step | 06 |
| [#1379 — BV555, scoring-round 3-way tie](https://github.com/Equal-Vote/bettervoting/issues/1379) ✅ closed · **WAI** | the tie-break *logic* is working-as-intended: the protocol deliberately skips head-to-head for 3+ way ties | 05 |
| [#1432 — surface tie-break explanations](https://github.com/Equal-Vote/bettervoting/issues/1432) 🔀 open | expose the existing `roundResults.logs` + `tieBreakType` in the human-readable report and JSON; builds on [PR #1419](https://github.com/Equal-Vote/bettervoting/pull/1419) | 05 |
| [#1371 — JSON: tie-break priority sequence](https://github.com/Equal-Vote/bettervoting/issues/1371) ✅ closed | the randomized tie-break order is now in the export, so another engine can import it and reproduce the result | all |
| [#1063 — deterministic lot-number tie-breaking](https://github.com/Equal-Vote/bettervoting/issues/1063) | a pre-published lot order (a public draw before the election) rather than a post-hoc random shuffle | all |
| [#906 — BV1805, Average Supporter Profile](https://github.com/Equal-Vote/bettervoting/issues/906) | "Stats for Nerds" profile wrong under pending tie-breaking | reporting note |
| [#242 — Approval/Plurality tie handling](https://github.com/Equal-Vote/bettervoting/issues/242) · [PR #229](https://github.com/Equal-Vote/bettervoting/pull/229) | tabulators break when random tie-breakers are disabled | method note |

Design docs: [tie-breaking lot numbers / scenarios](https://docs.google.com/document/d/15NvrJoZ0f_Zhr3vh5uE2LVw-D8EZhBI2PFnTowYgoZM/edit?tab=t.0) · [tie scenarios (2)](https://docs.google.com/document/d/1KqWriu7rTduQf1esebH5iMvcgueCdkLvBB02NS9MZ5Y/edit?tab=t.0).

## 💡 Proposal (idea — not yet adopted): color-coded coalition casts {#proposal}

> **Status: discussion only.** A proposed convention for tie-breaking / coalition examples, recorded here so it isn't lost. It is **not** a house rule — don't apply it to existing cases until it's decided. (Today's casts follow the standard rule: a fresh, friendly, distinct-initial set per scenario.)

**The idea.** For examples that turn on *coalitions* or *vote-splitting*, encode the coalition structure into the candidate names/colors so the structure is visible at a glance:

- **Hue = coalition / faction** — greens together, reds together.
- **Shade = candidate within the coalition** — *dark green* vs *light green* are two center candidates competing for the **same** voters.
- **Vote-splitting then looks like what it is:** one big coalition's support sliced into two thinner same-hue bars under Plurality (a spoiler), versus holding together under STAR's runoff. Same colors, opposite outcome.

**Why it could help tie-breaking examples specifically.** A tie is often *because* two near-identical candidates draw equal support; same-hue/different-shade names make "these two are basically the same coalition" obvious, which is exactly the intuition behind why they tied and how the lot order separates them. Pairs with the engine's existing `blocs:` vote-splitting check (see CLAUDE.md → Engines).

**Open questions for the vote:** (1) does color/shade naming fight the "distinct initials, phonetically distinct" rule? (2) accessibility — names must still work in plain text and for color-blind readers (so the *word* "green-dark" carries it, not the color alone); (3) scope — coalition/vote-splitting demos only, or any multi-candidate tie? Decide, then promote to CLAUDE.md / AGENTS.md if adopted.

## Run them yourself {#run}

```
uv run python STARVote_LH_tabulation_engine/starvote_larry_hastings.py "01_STAR/09_Parked/Flat_scores_ties/cases/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml"
```

Every file writes a full audit copy to its `cases/cases_tabulated/` sibling.

---

**Related:** the rest of the parked shelf → [09_Parked](../README.md) · the tie-breaking that *is* on the learning path → [the tie-break ladder](../../03_Criteria/tie_break_ladder/README.md) · [the dead rung](../../03_Criteria/tie_break_dead_rung/README.md) · the topic hub → [ties](../../../07_Concepts/topics/ties/README.md).
