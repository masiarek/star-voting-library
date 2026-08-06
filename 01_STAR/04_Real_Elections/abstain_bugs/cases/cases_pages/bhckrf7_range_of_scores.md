---
search:
  exclude: true
---

# hckrf7 — Range of Scores counts 3 ballots on a page that says 1 voter

*Generated from [`bhckrf7_range_of_scores.yaml`](../bhckrf7_range_of_scores.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Cal Creative

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/hckrf7) · **[results ↗](https://bettervoting.com/hckrf7/results)** (election `hckrf7`).

## Scenario

Three voters, three candidates. Two ballots are **flat all-zeros**; one ballot
scores Cal 2, Bob 1, Ann 0.

BetterVoting's tabulator applies its flat-ballot rule (bettervoting#884): an
all-equal ballot is an **abstention**, so it reports `nAbstentions: 2` and
`nTallyVotes: 1`, and the results page headline reads **"1 voters"**. Cal wins
the runoff 1–0.

The **"Range of Scores"** chart under *Stats for Nerds* then shows two bars —
range 2 at **33%** and range 0 at **67%**. Those are thirds: the chart is
computed over **all three** ballots, because its data source
(`ballotsForRace()`) drops only a *truly blank* ballot, not a flat one. So the
chart's 67% bar is made entirely of ballots the same page says did not vote —
and the number **3** appears nowhere on the page for the reader to divide by.

Nothing is miscounted: the winner, the scores and the runoff are all correct.
It is a **denominator/labelling** problem, and it is the mirror image of the
already-fixed "Distribution of Equal Support" chart (bettervoting#1390), which
dropped ballots the tabulator kept. Here the chart keeps ballots the tabulator
dropped. Filed as bettervoting#1487.

LH states its denominator inline instead: `Voters with a preference: 1 of 3
(2 Equal Support)` — the 1, the 3 and the gap between them all on one line.

## Ballots

The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| Ballot as marked | Ann Ambitious | Bob Bossy | Cal Creative |
|:--|:--:|:--:|:--:|
| <img src="../img/bhckrf7_range_of_scores_ballot_1.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — flat ballot — range 0 (BetterVoting files this as an abstention): Ann Ambitious 0, Bob Bossy 0, Cal Creative 0."> | 0 | 0 | 0 |
| <img src="../img/bhckrf7_range_of_scores_ballot_2.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — the only tallied ballot — range 2, on a 0-5 ballot: Ann Ambitious 0, Bob Bossy 1, Cal Creative 2."> | 0 | 1 | 2 |
| <img src="../img/bhckrf7_range_of_scores_ballot_3.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — flat ballot — range 0 (BetterVoting files this as an abstention): Ann Ambitious 0, Bob Bossy 0, Cal Creative 0."> | 0 | 0 | 0 |

The same ballots as the file records them:

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann Ambitious,Bob Bossy,Cal Creative
0,0,0   # flat ballot — range 0 (BetterVoting files this as an abstention)
0,1,2   # the only tallied ballot — range 2, on a 0-5 ballot
0,0,0   # flat ballot — range 0 (BetterVoting files this as an abstention)
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Cal Creative
  Approval = Ann Ambitious   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Count × Ann Ambitious,Bob Bossy,Cal Creative
    2 ×             0,        0,           0
    1 ×             0,        1,           2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cal Creative  -- 2 -- First place
   Bob Bossy     -- 1 -- Second place
   Ann Ambitious -- 0
 Cal Creative and Bob Bossy advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cal Creative  -- 1 -- First place
   Bob Bossy     -- 0
   Equal Support -- 2
 Cal Creative wins.
   Runoff math:
     3  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Cal Creative 1 (100%)  ·  Bob Bossy 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cal Creative
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                      |    Ann Ambitious  |   * Bob Bossy    | * Cal Creative   |
---------------------------------------------------------------------------------
      Ann Ambitious > |        ---        |    0 - 2 - 1     |    0 - 2 - 1     |
        * Bob Bossy > |     1 - 2 - 0     |       ---        |    0 - 2 - 1     |
     * Cal Creative > |     1 - 2 - 0     |    1 - 2 - 0     |       ---        |

[Condorcet Winner]
  Condorcet Winner: Cal Creative — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ann Ambitious — loses every head-to-head matchup — elected by Approval!

[Score Distribution] (how many ballots gave each star rating)
                    Score
Candidate      5  4  3  2  1  0  | Total   Avg
Ann Ambitious  0  0  0  0  0  3  |     0   0.0
Bob Bossy      0  0  0  0  1  2  |     1   0.3
Cal Creative   0  0  0  1  0  2  |     2   0.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bhckrf7_range_of_scores_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/04_Real_Elections/abstain_bugs/cases/bhckrf7_range_of_scores.yaml
```

## See also

- [Methods disagree on this election](../../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/bhckrf7_range_of_scores.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../../02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv11_6xhfp8_full_equal_support](bv11_6xhfp8_full_equal_support.md) · [bv1570_6hv7jf_undecided_plurality](bv1570_6hv7jf_undecided_plurality.md) · [bv655_jfrk9t_equal_opposition](bv655_jfrk9t_equal_opposition.md)
