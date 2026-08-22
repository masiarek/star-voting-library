---
search:
  exclude: true
---

# Equal ranks — the same 74 voters use the whole scale, and Delia wins

*Generated from [`equal_rank_cohesive_wide_gaps.yaml`](../equal_rank_cohesive_wide_gaps.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Delia

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/j9wvv4) · **[results ↗](https://bettervoting.com/j9wvv4/results)** (election `j9wvv4` · test `BV2297`).

## Scenario

The twin of equal_rank_cohesive_consecutive.yaml: the SAME 74 voters, the SAME preference order over Alice, Bilal, Cato and Delia — Figure 11 of Théo Delemazure & Dominik Peters, "Generalizing Instant Runoff Voting to Allow Indifferences" (EC'24, arXiv:2404.11407) — with exactly one thing changed. Every voter now uses the full width of the 0-5 scale instead of consecutive numbers: a top class is still 5, but everything the voter is not enthusiastic about drops toward 0.
Check it: each row below induces the same indifference classes as the matching row in the companion file. Row 1 is still Alice=Bilal=Cato > Delia. Row 5 is still Delia > Alice=Bilal=Cato. Nobody reordered anybody. Only the gaps moved.
STAR elects DELIA. The companion file, same order, elected Alice. And 38 of these 74 voters rank Alice in their top class, so by the paper's respect-for-cohesive-majorities axiom the winner had to be Alice, Bilal or Cato — Delia is precisely the candidate that cohesive majority excluded. Approval-IRV, which the paper proves satisfies the axiom, elects inside the permitted set on both files. Split-IRV elects Delia on both.
So this file is the witness for a claim this library should state about its own preferred method rather than wait to be told: STAR does not satisfy respect for cohesive majorities. The axiom is defined on weak orders, a score ballot induces one, and here is a perfectly ordinary 0-5 profile that breaks it. That is not a defect peculiar to STAR — the paper proves no Condorcet method that reads only pairwise margins satisfies the axiom either (Proposition 3.4), so Ranked Robin, Schulze, Ranked Pairs and Minimax are all outside it. Approval-IRV's claim is genuinely unusual, and worth reporting straight.
One reading note, so the report does not surprise anyone: Bilal and Cato post identical score totals here, so STAR's second finalist slot is settled by lot. It does not touch the result — Delia beats Bilal 30-28 and Cato 30-28 on the same ballots, so the lot picks the loser of the runoff either way.
For the Approval-IRV and Split-IRV counts, and the axiom check itself, run tools_adam/pref_voting_tabulation_engine/approval_irv_report.py.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Alice,Bilal,Cato,Delia
18:5,5,5,0    # Alice, Bilal and Cato equal-first
10:5,5,0,3    # Alice and Bilal equal-first
10:5,0,5,3    # Alice and Cato equal-first
16:0,5,5,5    # Bilal, Cato and Delia equal-first
20:0,0,0,5    # Delia alone on top
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Delia
  Choose-One (Plurality) = Alice   (differs from STAR)
  RCV-IRV                = Alice   (differs from STAR)
  Note: 54 of 74 ballots (73%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/equal_rank_cohesive_wide_gaps_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 74 ballots.
Count × Alice,Bilal,Cato,Delia
   20 ×     0,    0,   0,    5
   18 ×     5,    5,   5,    0
   16 ×     0,    5,   5,    5
   10 ×     5,    5,   0,    3
   10 ×     5,    0,   5,    3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Delia         -- 240 -- First place
   Bilal         -- 220 -- Tied for second place
   Cato          -- 220 -- Tied for second place
   Alice         -- 190
 Delia advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Bilal         -- 10 -- Tied for second place
   Cato          -- 10 -- Tied for second place
   Equal Support -- 54
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Bilal         -- 44 -- Tied for second place
   Cato          -- 44 -- Tied for second place
 There's still a two-way tie for second.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Alice', 'Bilal', 'Cato', 'Delia']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Bilal', 'Cato']
  Resolved: ['Bilal'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Delia         -- 30 -- First place
   Bilal         -- 28
   Equal Support -- 16
 Delia wins.
   Runoff math:
     74  ballots cast
   − 16  Equal Support (no preference between the two finalists)
     ──
     58  voters with a preference  (majority = 30)
           Delia 30 (52%)  ·  Bilal 28 (48%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Delia
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
        Note: Bilal and Cato tied at 220 in the Scoring Round, and the lot
              rung (the ballots could not separate them) advanced Bilal. The *
              marks who advanced, not who scored highest.

                 |     Alice    |  * Bilal    |     Cato    |  * Delia    |
---------------------------------------------------------------------------
         Alice > |     ---      |10 - 48 - 16 |10 - 48 - 16 |38 -  0 - 36 |
       * Bilal > | 16 - 48 - 10 |    ---      |10 - 54 - 10 |28 - 16 - 30 |
          Cato > | 16 - 48 - 10 |10 - 54 - 10 |    ---      |28 - 16 - 30 |
       * Delia > | 36 -  0 - 38 |30 - 16 - 28 |30 - 16 - 28 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Alice > Delia > Bilal > Alice)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alice      38   0   0   0   0  36  |   190   2.6
Bilal      44   0   0   0   0  30  |   220   3.0
Cato       44   0   0   0   0  30  |   220   3.0
Delia      36   0  20   0   0  18  |   240   3.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/equal_rank_cohesive_wide_gaps_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/equal_rank_irv/cases/equal_rank_cohesive_wide_gaps.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_DIFFERS_ARTIFACT/equal_rank_cohesive_wide_gaps.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [equal_rank_clone_with](equal_rank_clone_with.md) · [equal_rank_clone_without](equal_rank_clone_without.md) · [equal_rank_cohesive_consecutive](equal_rank_cohesive_consecutive.md) · [equal_rank_five_voters](equal_rank_five_voters.md) · [equal_rank_majority_alternative](equal_rank_majority_alternative.md)
