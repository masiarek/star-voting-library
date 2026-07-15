# Flat scores 07 — fully flat ballots (the maximal tie + abstention trap)

*Generated from [`Flat_scores_ties_07_fully_flat.yaml`](../Flat_scores_ties_07_fully_flat.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ararat

## Scenario

Every voter scores every mountain 5: a maximal tie that ties in BOTH rounds and resolves
by lot -> Ararat. Also where BV mis-files a fully-flat ballot as an ABSTENTION (#1407) and
shows NaN on equal ties (BV200 #1035). Capstone. Level 301.
Lesson: Flat_scores_ties_07_fully_flat.md  (BV id pending).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ararat, Blanc, Cook
5, 5, 5
5, 5, 5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Count × Ararat,Blanc,Cook
    2 ×      5,    5,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ararat        -- 10 -- Tied for first place
   Blanc         -- 10 -- Tied for first place
   Cook          -- 10 -- Tied for first place
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Ararat        -- 0 -- Tied for first place
   Blanc         -- 0 -- Tied for first place
   Cook          -- 0 -- Tied for first place
   Equal Support -- 2
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Ararat        -- 2 -- Tied for first place
   Blanc         -- 2 -- Tied for first place
   Cook          -- 2 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ararat', 'Blanc', 'Cook']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ararat', 'Blanc', 'Cook']
  Resolved: ['Ararat', 'Blanc'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ararat        -- 0 -- Tied for first place
   Blanc         -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Ararat        -- 10 -- Tied for first place
   Blanc         -- 10 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Ararat        -- 2 -- Tied for first place
   Blanc         -- 2 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ararat', 'Blanc']
  Resolved: ['Ararat'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ararat
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Ararat  | * Blanc   |    Cook   |
-----------------------------------------------------
    * Ararat > |    ---     |0 - 2 - 0  |0 - 2 - 0  |
     * Blanc > | 0 - 2 - 0  |   ---     |0 - 2 - 0  |
        Cook > | 0 - 2 - 0  |0 - 2 - 0  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Ararat, Blanc, Cook (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ararat     2  0  0  0  0  0  |    10   5.0
Blanc      2  0  0  0  0  0  |    10   5.0
Cook       2  0  0  0  0  0  |    10   5.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../Flat_scores_ties_tabulated/Flat_scores_ties_07_fully_flat_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/Flat_scores_ties/Flat_scores_ties_07_fully_flat.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Ballot & terminology basics](../../../00_start_here/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [Flat_scores_ties_01_baseline_clean](Flat_scores_ties_01_baseline_clean.md) · [Flat_scores_ties_02_runoff_tie_2cand](Flat_scores_ties_02_runoff_tie_2cand.md) · [Flat_scores_ties_03_runoff_tie_split](Flat_scores_ties_03_runoff_tie_split.md) · [Flat_scores_ties_04_scoring_tie_2way](Flat_scores_ties_04_scoring_tie_2way.md) · [Flat_scores_ties_05_scoring_tie_3way_xmyf7k](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) · [Flat_scores_ties_06_scoring_tie_4way](Flat_scores_ties_06_scoring_tie_4way.md) · [Flat_scores_ties_08_all_flat_zero_count](Flat_scores_ties_08_all_flat_zero_count.md)
