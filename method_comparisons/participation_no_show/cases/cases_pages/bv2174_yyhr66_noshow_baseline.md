# No-show paradox (1 of 2) — 8 April fans stay home; RCV-IRV elects Bruno

*Generated from [`bv2174_yyhr66_noshow_baseline.yaml`](../bv2174_yyhr66_noshow_baseline.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bruno

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/yyhr66) · **[results ↗](https://bettervoting.com/yyhr66/results)** (election `yyhr66`).

## Scenario

The Participation criterion, live — the baseline half of a matched pair
(see 00_start_here/topics/participation/). 54 voters: 16 April>Bruno>Celia,
18 Bruno>Celia>April, 20 Celia>April>Bruno. Eight MORE April fans (same
sincere ranking) exist but stay home here; the companion file adds them.

With the 8 absent: RCV-IRV eliminates April (16 first choices) and elects
Bruno 34-20. STAR is a Runoff Reversal — Celia tops the scores 136/122/120
but Bruno wins the automatic runoff 34-20. Choose-One elects Celia
(20/18/16). The pairwise picture is a perfect Condorcet cycle (April 36-18
Bruno, Bruno 34-20 Celia, Celia 38-16 April) — the soil every no-show
paradox grows in. No Ranked Robin BV race: a Copeland three-way tie
resolves at RANDOM on BetterVoting (not freezable); LH's margin tiebreak
resolves it deterministically to Celia (+4), shown in this file's mirror.

LIVE on BetterVoting as BV2174 (three races: STAR, RCV-IRV, Choose-One).
Live results: https://bettervoting.com/yyhr66/results
Matched file: bv2175_9dhv8y_noshow_showup.yaml (the 8 fans vote — and
RCV-IRV hands them their LAST choice).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:April,Bruno,Celia
16:5,2,0   # April > Bruno > Celia
18:0,5,2   # Bruno > Celia > April
20:2,0,5   # Celia > April > Bruno
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Bruno
  Choose-One (Plurality) = Celia   (differs from STAR)
  Approval               = Celia   (differs from STAR)
  RCV-RR                 = Celia   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: cases_tabulated/bv2174_yyhr66_noshow_baseline_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Celia)
 - Runoff Round Winner   = (Bruno)
  Candidate Celia earned the highest total score, but
  Candidate Bruno won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 54 ballots.
Count × April,Bruno,Celia
   20 ×     2,    0,    5
   18 ×     0,    5,    2
   16 ×     5,    2,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Celia         -- 136 -- First place
   Bruno         -- 122 -- Second place
   April         -- 120
 Celia and Bruno advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 34 -- First place
   Celia         -- 20
   Equal Support --  0
 Bruno wins.
   Runoff math:
     54  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     54  voters with a preference  (majority = 28)
           Bruno 34 (63%)  ·  Celia 20 (37%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bruno
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     April    |  * Bruno    |  * Celia    |
-------------------------------------------------------------
         April > |     ---      |36 -  0 - 18 |16 -  0 - 38 |
       * Bruno > | 18 -  0 - 36 |    ---      |34 -  0 - 20 |
       * Celia > | 38 -  0 - 16 |20 -  0 - 34 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: April > Bruno > Celia > April)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
April      16   0   0  20   0  18  |   120   2.2
Bruno      18   0   0  16   0  20  |   122   2.3
Celia      20   0   0  18   0  16  |   136   2.5
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2174_yyhr66_noshow_baseline_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/participation_no_show/cases/bv2174_yyhr66_noshow_baseline.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/bv2174_yyhr66_noshow_baseline.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2175_9dhv8y_noshow_showup](bv2175_9dhv8y_noshow_showup.md)
