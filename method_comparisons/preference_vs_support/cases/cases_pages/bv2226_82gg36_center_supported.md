# Preference vs Support — the center SUPPORTED (wings score Blair 4)

*Generated from [`bv2226_82gg36_center_supported.yaml`](../bv2226_82gg36_center_supported.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Blair

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/82gg36) · **[results ↗](https://bettervoting.com/82gg36/results)** (election `82gg36`).

## Scenario

The "supported" half of a matched pair (companion: the TOLERATED election,
bv2225_ywx39y_center_tolerated). Same three candidates on a spectrum — Alex (a pole),
Blair (the center), Cole (the other pole) — and BYTE-IDENTICAL rankings to the
tolerated election. The ONLY change: the two wings now score the centrist Blair a
genuine 4 instead of a grudging 1. Because the orders didn't move, the ranked methods
don't move either: RCV-IRV still center-squeezes Blair (-> Alex); Ranked Robin still
finds him the Condorcet winner (-> Blair). But STAR reads the support — Blair's real
4s lift him into the runoff, which he wins — so STAR flips from Alex (tolerated) to
Blair (supported). Two elections, identical ranks, and only the score-reading method
can tell that in one Blair is merely tolerated and in the other he is genuinely backed.
Live results: https://bettervoting.com/82gg36/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Alex,Blair,Cole
15:5,4,0   # Alex > Blair > Cole   (SAME order — Blair now a strong 2nd, scored 4)
6:1,5,0    # Blair > Alex > Cole   (Blair's base — unchanged in both elections)
15:0,4,5   # Cole > Blair > Alex   (SAME order — Blair now a strong 2nd, scored 4)
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Blair
  Choose-One (Plurality) = Alex   (differs from STAR)
  RCV-IRV                = Alex   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2226_82gg36_center_supported_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 36 ballots.
Count × Alex,Blair,Cole
   15 ×    5,    4,   0
   15 ×    0,    4,   5
    6 ×    1,    5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Blair         -- 150 -- First place
   Alex          --  81 -- Second place
   Cole          --  75
 Blair and Alex advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Blair         -- 21 -- First place
   Alex          -- 15
   Equal Support --  0
 Blair wins.
   Runoff math:
     36  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     36  voters with a preference  (majority = 19)
           Blair 21 (58%)  ·  Alex 15 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Blair
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Alex    |  * Blair    |     Cole    |
-------------------------------------------------------------
        * Alex > |     ---      |15 -  0 - 21 |21 -  0 - 15 |
       * Blair > | 21 -  0 - 15 |    ---      |21 -  0 - 15 |
          Cole > | 15 -  0 - 21 |15 -  0 - 21 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Blair — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alex       15   0   0   0   6  15  |    81   2.3
Blair       6  30   0   0   0   0  |   150   4.2
Cole       15   0   0   0   0  21  |    75   2.1
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2226_82gg36_center_supported_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/preference_vs_support/cases/bv2226_82gg36_center_supported.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2226_82gg36_center_supported.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2225_ywx39y_center_tolerated](bv2225_ywx39y_center_tolerated.md)
