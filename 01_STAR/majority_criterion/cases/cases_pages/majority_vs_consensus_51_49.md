# Majority criterion vs. the consensus candidate — the 51/49 polarized electorate

*Generated from [`majority_vs_consensus_51_49.yaml`](../majority_vs_consensus_51_49.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../concepts) · **1 seat** · **Expected winner:** Celia

## Scenario

The textbook argument AGAINST the majority criterion, made runnable.

100 voters, sharply polarized. 51 love Alma and loathe Bruno; 49 love Bruno
and loathe Alma. Celia is nobody's champion but everybody's genuinely good
outcome — a 4 out of 5 from both camps, and a full 5 from the three Alma
voters who honestly have no preference between Alma and Celia.

Alma is max-scored by 51 voters — an outright MAJORITY. So any method
satisfying the majority criterion MUST elect Alma:
  - Choose-One: Alma 51 first choices, wins outright.
  - RCV-IRV: Alma has a first-round majority, wins in round 1.

Methods that read the whole ballot elect Celia instead:
  - Score (utilitarian sum): Celia 403, Alma 255, Bruno 245.
  - STAR: Celia and Alma are the finalists; the runoff is Celia 49, Alma 48,
    with 3 voters expressing Equal Support. Celia wins.
  - Ranked Robin: Celia beats Alma 49-48 and Bruno 51-49 — Condorcet winner.

THE THRESHOLD. Celia only overtakes Alma head-to-head because 3 of the 51
majority voters rate Alma and Celia equally. At 2 such voters the pairwise
count is 49-49, a tie, and Celia is no longer the Condorcet winner. So the
crossover sits just above 2% of the electorate — roughly 4% of the majority
bloc, which is exactly what the electowiki cardinal-voting article claims.
Verified, not assumed.

This case is deliberately double-edged. It shows what the majority criterion
costs (a candidate 100 out of 100 voters are content with, blocked by a bare
51% bloc) WITHOUT pretending the majority has no claim: Alma really is the
sincere favorite of more than half the room, and "the majority should win"
is a serious position, not a mistake. See the claim-check page for both sides.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Alma,Bruno,Celia
48:5,0,4   # Alma camp — prefer Alma, content with Celia
3:5,0,5    # Alma camp — honestly no preference between Alma and Celia
49:0,5,4   # Bruno camp — prefer Bruno, content with Celia
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Celia
  Choose-One (Plurality) = Alma   (differs from STAR)
  RCV-IRV                = Alma   (differs from STAR)
  Note: 3 of 100 ballots (3%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/majority_vs_consensus_51_49_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Alma,Bruno,Celia
   49 ×    0,    5,    4
   48 ×    5,    0,    4
    3 ×    5,    0,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Celia         -- 403 -- First place
   Alma          -- 255 -- Second place
   Bruno         -- 245
 Celia and Alma advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Celia         -- 49 -- First place
   Alma          -- 48
   Equal Support --  3
 Celia wins.
   Runoff math:
     100  ballots cast
   −   3  Equal Support (no preference between the two finalists)
     ───
      97  voters with a preference  (majority = 49)
           Celia 49 (51%)  ·  Alma 48 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Celia
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Alma    |    Bruno    |  * Celia    |
-------------------------------------------------------------
        * Alma > |     ---      |51 -  0 - 49 |48 -  3 - 49 |
         Bruno > | 49 -  0 - 51 |    ---      |49 -  0 - 51 |
       * Celia > | 49 -  3 - 48 |51 -  0 - 49 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Celia — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Bruno — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alma       51   0   0   0   0  49  |   255   2.6
Bruno      49   0   0   0   0  51  |   245   2.5
Celia       3  97   0   0   0   0  |   403   4.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/majority_vs_consensus_51_49_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/majority_criterion/cases/majority_vs_consensus_51_49.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/IRV_DIFFERS_ARTIFACT/majority_vs_consensus_51_49.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv95a_9m6rxr_favorite_survives_one_rival](bv95a_9m6rxr_favorite_survives_one_rival.md) · [bv95b_7pdq3r_favorite_loses_two_rivals](bv95b_7pdq3r_favorite_loses_two_rivals.md)
