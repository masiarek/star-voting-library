---
search:
  exclude: true
---

# Equal ranks — 38 of 74 rally to Alice, and consecutive scores elect her

*Generated from [`equal_rank_cohesive_consecutive.yaml`](../equal_rank_cohesive_consecutive.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Alice

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/j9wvv4) · **[results ↗](https://bettervoting.com/j9wvv4/results)** (election `j9wvv4` · test `BV2297`).

## Scenario

Figure 11 of Théo Delemazure & Dominik Peters, "Generalizing Instant Runoff Voting to Allow Indifferences" (EC'24, arXiv:2404.11407), doubled so every bloc clears the house minimum of 6. Matched pair with equal_rank_cohesive_wide_gaps.yaml — the SAME 74 voters holding the SAME preference order, using the 0-5 scale differently. Same cast because it is the same election with one thing changed.
The paper's point is an axiom called RESPECT FOR COHESIVE MAJORITIES: if more than half the voters all rank some candidate first (possibly alongside others), the winner must be someone at least one of them ranked first. Here 38 of 74 voters put Alice in their top class — 18 as Alice=Bilal=Cato, 10 as Alice=Bilal, 10 as Alice=Cato — so the axiom permits Alice, Bilal or Cato and forbids Delia. Split-IRV elects Delia and fails the axiom. Approval-IRV cannot: Theorem 3.5 proves it always satisfies it.
On these ballots STAR elects Alice, inside the permitted set. But that is the encoding talking as much as the electorate, which is why this file has a twin. Every voter here uses consecutive scores (a three-way top class is 5,5,5 and the class below it is 4). Give the same voters the same preference order with wide gaps instead and STAR elects Delia — see the companion file. Across 20,000 random strictly-decreasing 0-5 encodings of this weak order STAR's winner is genuinely unstable: Delia 35%, Alice 19%, Bilal 12%, Cato 11%, the rest ties.
Two things follow, and the second one cuts against this library's own preferred method. First, a weak order does not determine a STAR result — the gaps carry real information and this profile is where that stops being a slogan. Second, STAR does NOT satisfy respect for cohesive majorities: the companion file is a legitimate 0-5 profile whose induced weak order is exactly the one above, and STAR elects the one candidate the cohesive majority excluded. Approval-IRV satisfies the axiom on both files; STAR satisfies it on one.
A discrepancy worth recording, since this library runs the figures it cites. The paper writes that on this profile "Approval-IRV selects a" (Alice). Counted, Approval-IRV eliminates Delia, then ALICE, and ends in a 64-64 tie between Bilal and Cato. The theorem is untouched — Bilal and Cato are both inside the permitted set, so respect for cohesive majorities holds exactly as Theorem 3.5 says — but the illustrative sentence names the wrong candidate. The count is in the report; check it against the round table rather than taking this file's word for it.
For the Approval-IRV and Split-IRV counts, and the axiom check itself, run tools_adam/pref_voting_tabulation_engine/approval_irv_report.py.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Alice,Bilal,Cato,Delia
18:5,5,5,4    # Alice, Bilal and Cato equal-first
10:5,5,3,4    # Alice and Bilal equal-first
10:5,3,5,4    # Alice and Cato equal-first
16:4,5,5,5    # Bilal, Cato and Delia equal-first
20:4,4,4,5    # Delia alone on top
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR   = Alice
  RCV-RR = Delia   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: cases_tabulated/equal_rank_cohesive_consecutive_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 74 ballots.
Count × Alice,Bilal,Cato,Delia
   20 ×     4,    4,   4,    5
   18 ×     5,    5,   5,    4
   16 ×     4,    5,   5,    5
   10 ×     5,    5,   3,    4
   10 ×     5,    3,   5,    4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alice         -- 334 -- First place
   Delia         -- 332 -- Second place
   Bilal         -- 330
   Cato          -- 330
 Alice and Delia advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alice         -- 38 -- First place
   Delia         -- 36
   Equal Support --  0
 Alice wins.
   Runoff math:
     74  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     74  voters with a preference  (majority = 38)
           Alice 38 (51%)  ·  Delia 36 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alice
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Alice    |    Bilal    |     Cato    |  * Delia    |
---------------------------------------------------------------------------
       * Alice > |     ---      |10 - 48 - 16 |10 - 48 - 16 |38 -  0 - 36 |
         Bilal > | 16 - 48 - 10 |    ---      |10 - 54 - 10 |28 - 16 - 30 |
          Cato > | 16 - 48 - 10 |10 - 54 - 10 |    ---      |28 - 16 - 30 |
       * Delia > | 36 -  0 - 38 |30 - 16 - 28 |30 - 16 - 28 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Alice > Delia > Bilal > Alice)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alice      38  36   0   0   0   0  |   334   4.5
Bilal      44  20  10   0   0   0  |   330   4.5
Cato       44  20  10   0   0   0  |   330   4.5
Delia      36  38   0   0   0   0  |   332   4.5
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/equal_rank_cohesive_consecutive_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/equal_rank_irv/cases/equal_rank_cohesive_consecutive.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/equal_rank_cohesive_consecutive.md) — its entry in the divergence review ledger
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [equal_rank_clone_with](equal_rank_clone_with.md) · [equal_rank_clone_without](equal_rank_clone_without.md) · [equal_rank_cohesive_wide_gaps](equal_rank_cohesive_wide_gaps.md) · [equal_rank_five_voters](equal_rank_five_voters.md) · [equal_rank_majority_alternative](equal_rank_majority_alternative.md)
