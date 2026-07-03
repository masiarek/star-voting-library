# Dead rung 05 — five-star rung alive but non-separating

*Generated from [`tie_break_09_five_star_tied_nonzero.yaml`](../tie_break_09_five_star_tied_nonzero.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ben

**Official tie-break (lot) order:** Ben > Ann — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The subtler failure mode: the rung is NOT dead — both candidates have
exactly one 5 — but 1-1 separates nobody, so the tie still falls to the
lot (Ben). A rung can run, count real votes, and still decide nothing.
Compare case 03 (rung separates) and case 04 (rung dead).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Ben
5,0   # one 5 for Ann
0,5   # one 5 for Ben
```

## What the engine says

Full report from the [`_tabulated` mirror](../tie_break_dead_rung_tabulated/tie_break_09_five_star_tied_nonzero_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ann    |  * Ben    |
-----------------------------------------
       * Ann > |    ---     |1 - 0 - 1  |
       * Ben > | 1 - 0 - 1  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Ann, Ben (pairwise ties)

[Divergence from STAR]
  STAR    = Ben
  RCV-IRV = Ann   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: tie_break_dead_rung_tabulated/tie_break_09_five_star_tied_nonzero_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Ann,Ben
  5,  0
  0,  5

[Score Distribution] (number of ballots giving each score)
     5  4  3  2  1  0  | Total   Avg
Ann  1  0  0  0  0  1  |     5   2.5
Ben  1  0  0  0  0  1  |     5   2.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ann           -- 5 -- First place
   Ben           -- 5 -- Second place
 Ann and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ann           -- 1 -- Tied for first place
   Ben           -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Ann           -- 5 -- Tied for first place
   Ben           -- 5 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Ann           -- 1 -- Tied for first place
   Ben           -- 1 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ben', 'Ann']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ann', 'Ben']
  Resolved: ['Ben'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ben
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/tie_break_09_five_star_tied_nonzero.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/CYCLE_OR_THREE_WAY/tie_break_09_five_star_tied_nonzero.md) — its entry in the divergence review ledger
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [dead_rung_scoring_dead_cap2](dead_rung_scoring_dead_cap2.md) · [dead_rung_scoring_dead_cap3](dead_rung_scoring_dead_cap3.md) · [dead_rung_scoring_dead_cap4](dead_rung_scoring_dead_cap4.md) · [tie_break_01_scoring_five_star_breaks](tie_break_01_scoring_five_star_breaks.md) · [tie_break_02_scoring_no_fives_to_lot](tie_break_02_scoring_no_fives_to_lot.md) · [tie_break_03_runoff_no_fives_to_lot](tie_break_03_runoff_no_fives_to_lot.md) · [tie_break_04_runoff_five_star_breaks](tie_break_04_runoff_five_star_breaks.md) · [tie_break_05_scoring_five_star_vs_adversarial_lot](tie_break_05_scoring_five_star_vs_adversarial_lot.md) · [tie_break_06_scoring_dead_rung_adversarial_lot](tie_break_06_scoring_dead_rung_adversarial_lot.md) · [tie_break_07_runoff_five_star_vs_adversarial_lot](tie_break_07_runoff_five_star_vs_adversarial_lot.md) · [tie_break_08_runoff_dead_rung_adversarial_lot](tie_break_08_runoff_dead_rung_adversarial_lot.md)
