# Preference vs Support — the center TOLERATED (wings score Blair 1)

*Generated from [`bv2225_ywx39y_center_tolerated.yaml`](../bv2225_ywx39y_center_tolerated.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Alex

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ywx39y) · **[results ↗](https://bettervoting.com/ywx39y/results)** (election `ywx39y`).

## Scenario

The "tolerated" half of a matched pair (companion: the SUPPORTED election,
bv2226_82gg36_center_supported). Three candidates on a spectrum — Alex (a pole),
Blair (the center), Cole (the other pole). Blair is every faction's second choice
and the Condorcet winner, but the two wings score him only a GRUDGING 1.
The rankings here are byte-identical to the SUPPORTED election; the ONLY thing
that changes between the two is Blair's score from the wings (1 here, 4 there).
Because the orders are identical, the ranked methods can't tell the two elections
apart: RCV-IRV center-squeezes Blair both times (-> Alex); Ranked Robin finds Blair
the Condorcet winner both times (-> Blair). Only STAR responds to the support level:
with Blair at a thin 1 he misses the runoff, and STAR elects the candidate with a
real base, Alex. Flip the wings' Blair score to 4 (the companion) and STAR alone
moves to Blair. That is the whole preference-vs-support lesson as a live election.
Live results: https://bettervoting.com/ywx39y/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Alex,Blair,Cole
15:5,1,0   # Alex > Blair > Cole   (Blair a grudging 2nd — scored 1)
6:1,5,0    # Blair > Alex > Cole   (Blair's base — unchanged in both elections)
15:0,1,5   # Cole > Blair > Alex   (Blair a grudging 2nd — scored 1)
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR               = Alex
  RCV-RR (Condorcet) = Blair   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: cases_tabulated/bv2225_ywx39y_center_tolerated_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 36 ballots.
Count × Alex,Blair,Cole
   15 ×    5,    1,   0
   15 ×    0,    1,   5
    6 ×    1,    5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alex          -- 81 -- First place
   Cole          -- 75 -- Second place
   Blair         -- 60
 Alex and Cole advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alex          -- 21 -- First place
   Cole          -- 15
   Equal Support --  0
 Alex wins.
   Runoff math:
     36  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     36  voters with a preference  (majority = 19)
           Alex 21 (58%)  ·  Cole 15 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alex
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Alex    |    Blair    |   * Cole    |
-------------------------------------------------------------
        * Alex > |     ---      |15 -  0 - 21 |21 -  0 - 15 |
         Blair > | 21 -  0 - 15 |    ---      |21 -  0 - 15 |
        * Cole > | 15 -  0 - 21 |15 -  0 - 21 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Blair — STAR elected Alex instead (Blair was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alex       15   0   0   0   6  15  |    81   2.3
Blair       6   0   0   0  30   0  |    60   1.7
Cole       15   0   0   0   0  21  |    75   2.1
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2225_ywx39y_center_tolerated_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/preference_vs_support/cases/bv2225_ywx39y_center_tolerated.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/bv2225_ywx39y_center_tolerated.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2226_82gg36_center_supported](bv2226_82gg36_center_supported.md)
