# Two views of the same scores — down the columns, across the rows

**Level: 201 · deep dive**

**One line:** BetterVoting's **Range of Scores** chart and the LH engine's **`[Score Distribution]`** table look like two versions of the same feature, but they read the *same* ballot grid along **opposite margins** — LH reads a **column** (one candidate, every voter), BetterVoting reads a **row** (one voter, every candidate) — so neither can be recovered from the other, and each report is missing exactly what the other has.

→ Hub: [STAR Reporting](README.md) · the LH table in detail: [Score Distribution](reporting_LH/score_distribution.md) · the BV display: [How BetterVoting reports](reporting_BV/README.md) · where the two genuinely *disagree*: [Where the two reports differ](reporting_diff_BV_LH.md).

---

## A score ballot is a grid, and a grid has two margins

Every score election is one table: **voters down the side, candidates across the top**. Seven people picking a sandwich, on a 0–5 ballot:

| | Avocado | Bacon | Cheddar | ← **range used** |
|---|:--:|:--:|:--:|:--:|
| Voter 1 | 5 | 3 | 0 | **5** |
| Voter 2 | 5 | 4 | 0 | **5** |
| Voter 3 | 5 | 3 | 1 | **4** |
| Voter 4 | 4 | 4 | 4 | **0** |
| Voter 5 | 0 | 3 | 5 | **5** |
| Voter 6 | 1 | 4 | 5 | **4** |
| Voter 7 | 5 | 2 | 3 | **3** |
| **↓ total** | **25** | **23** | **18** | |

Both engines start from this grid. Then they **collapse it in different directions**:

- Sum **down a column** and you learn about a *candidate*: 25 stars for Avocado, and — more usefully — the *shape* of those stars.
- Subtract **across a row** and you learn about a *voter*: this one used all 5 rungs of the ballot, that one used none of them.

Neither summary is a summary of the other. That is the whole point of this page.

## Down the columns — LH's `[Score Distribution]`

The LH engine prints, per candidate, how many ballots gave each star rating ([`show_score_counts: true`](reporting_LH/options.md)):

```text title="Abridged — the Score Distribution block only; the whole count is at the bottom of this page"
[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Avocado    4  1  0  0  1  1  |    25   3.6
Bacon      0  3  3  1  0  0  |    23   3.3
Cheddar    2  1  1  0  1  2  |    18   2.6
```

The totals `25` and `23` are two points apart. The *shapes* are nothing alike:

- **Avocado is polarizing** — four 5s, but also a 1 and a 0. Loved and loathed.
- **Bacon is the consensus** — no 5s at all and nothing below a 2. Never anyone's favourite, never anyone's enemy.

That contrast is invisible in the Scoring Round, which prints only the totals. It is the column margin's whole job. (Rounding of the `Avg` column has its own story: [Score Distribution and averages](score_distribution_and_averages.md).)

## Across the rows — BetterVoting's "Range of Scores"

BetterVoting's *Stats for Nerds* panel offers a chart captioned *"Difference between maximum and minimum score on ballots."* For each ballot it computes `max − min`, then histograms the results across voters. On the grid above that would be:

> **You probably can't see this panel.** `Results.tsx` gates it — along with *Column Distribution* and *Name Recognition* — behind the `ALL_STATS` feature flag, described in BetterVoting's own `flagDefinitions` as *"Show all work in progress widgets under 'Stats for Nerds'"*. A normal STAR results page shows four panels and this is not one of them; a screenshot of it means the flag was set. Treat what follows as a description of a **work-in-progress** widget. What's actually on a live results page, panel by panel: [How to read a BetterVoting results page](../../../07_Concepts/tabulation_engines/BV/reading_a_bv_results_page.md).

| Range used | Ballots | Share |
|:--:|:--:|--:|
| 5 | 3 | 43% |
| 4 | 2 | 29% |
| 3 | 1 | 14% |
| 0 | 1 | 14% |

Its question is about **voter behaviour, not candidates**: *did people actually use the ballot they were given?* BetterVoting's own note under the chart explains why it cares — a voter who never marks a 0 and never marks a 5 has less influence on the scoring round, though their ballot still counts at full strength in the automatic runoff. (BetterVoting is right to add that failing to follow the instructions is far less costly here than on a ranked ballot, where duplicate first choices can spoil the ballot outright.)

Nothing in the LH report can produce that table. Nothing in this table can produce the LH one.

## Why neither is derivable from the other

Two 2-voter elections with **identical** column margins:

| Election A | X | Y | | Election B | X | Y |
|---|:--:|:--:|---|---|:--:|:--:|
| Voter 1 | 5 | 0 | | Voter 1 | 5 | 5 |
| Voter 2 | 0 | 5 | | Voter 2 | 0 | 0 |

In **both**, X received one 5 and one 0, and so did Y — the `[Score Distribution]` tables are character-for-character the same. But A is two voters in opposite camps (both ranges = **5**) and B is two voters with no preference at all (both ranges = **0**). Same column margin, opposite row margin.

It works the other way too. Put `5,0 / 5,0` beside Election A: both have every ballot at range 5, but one gives X two 5s and the other splits. Same row margin, different column margin.

So the two views are **independent projections** of the grid. Reporting one and calling it the other is a category error — and if a report shows only one, a real fact about the election is simply unavailable.

## Who answers which question

| Question about the election | LH engine | BetterVoting |
|---|---|---|
| How many voters gave candidate X a 5? a 4? a 0? | **`[Score Distribution]` row** | — *nothing* |
| Is X polarizing or broadly liked? | the shape of that row | — (inferable only by eye from the Voter Profile widget) |
| Total stars for X | `Total` column, and the Scoring Round | Scores Table |
| Mean stars for X among voters who scored X | `Avg` column (blanks excluded) | — (the Voter Profile "average ballot" uses a *different* denominator: only that candidate's top-scorers) |
| How many voters left X blank? | `Abs` column | Name Recognition widget — `ALL_STATS` only |
| Did each voter use the full 0–5 range? | — *nothing* | **Range of Scores** — `ALL_STATS` only |
| How many candidates did each voter bother to score? | — *nothing* | Column Distribution — `ALL_STATS` only |
| How did the two frontrunners split a given candidate's supporters? | the [preference matrix](reporting_LH/matrix.md) (pairwise, not by supporter group) | Voter Profile / Head-to-head widgets |

Read the table as a **division of labour, not a scoreboard**. LH is a text audit report built around candidates; BetterVoting's nerd stats are a visual panel built around voters. The honest summary is that **each has a hole exactly where the other has content**.

With one caveat worth stating plainly: the three rows marked `ALL_STATS` only are **work-in-progress widgets a normal visitor never sees**. Counting only what ships today, BetterVoting answers *none* of the row-margin questions — so the per-ballot margin is currently unreported by both tools, and the LH-vs-BV division of labour above is the *potential* one, not the live one.

## One thing to watch: the chart's denominator

BetterVoting's Range of Scores is computed over **every non-blank ballot**, including the flat ballots its own tabulator files as abstentions — while the headline voter count on the same page excludes them. On a three-ballot election that means a chart reading `33% / 67%` sits directly under the words *"1 voters"*, with the number 3 nowhere on the page.

Worked in full, with BetterVoting's source: [hckrf7 — "Range of Scores" counts 3 ballots on a page that says 1 voter](../../04_Real_Elections/abstain_bugs/bhckrf7_range_of_scores.md). The underlying flat-ballot rule is the same one behind [Where the two reports differ](reporting_diff_BV_LH.md) and the whole [abstain_bugs](../../04_Real_Elections/abstain_bugs/README.md) folder.

## The engine's count for the grid above

<!-- report:same_total_different_shape_c3_b7 -->
```text
[Divergence from STAR]
  STAR     = Avocado
  Approval = Bacon   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 7 ballots.
Avocado,Bacon,Cheddar
      5,    3,      0
      5,    4,      0
      5,    3,      1
      4,    4,      4
      0,    3,      5
      1,    4,      5
      5,    2,      3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Avocado       -- 25 -- First place
   Bacon         -- 23 -- Second place
   Cheddar       -- 18
 Avocado and Bacon advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Avocado       -- 4 -- First place
   Bacon         -- 2
   Equal Support -- 1
 Avocado wins.
   Runoff math:
     7  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     6  voters with a preference  (majority = 4)
           Avocado 4 (67%)  ·  Bacon 2 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Avocado
```
<!-- /report -->

The preference matrix, the Condorcet check and the `[Score Distribution]` block in place are on the case page: [`same_total_different_shape_c3_b7.md`](cases/cases_pages/same_total_different_shape_c3_b7.md) · source [`.yaml`](cases/same_total_different_shape_c3_b7.yaml).
