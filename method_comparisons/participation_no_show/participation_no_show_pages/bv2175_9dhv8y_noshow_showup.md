# No-show paradox (2 of 2) — the 8 April fans vote; RCV-IRV hands them their LAST choice

*Generated from [`bv2175_9dhv8y_noshow_showup.yaml`](../bv2175_9dhv8y_noshow_showup.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** April

## Scenario

The Participation criterion, live — the show-up half of the matched pair
(see 00_start_here/topics/participation/). Identical to
bv2174_yyhr66_noshow_baseline.yaml plus 8 more sincere April>Bruno>Celia
ballots: 62 voters — 24 April>Bruno>Celia, 18 Bruno>Celia>April,
20 Celia>April>Bruno.

What showing up buys the 8, by method:
- Choose-One: Celia -> April. Helped — last choice replaced by favorite.
- STAR: Bruno -> April (scores 160/138/136; runoff April 44-18). Helped —
  their favorite wins; more sincere support moved the result their way.
- RCV-IRV: Bruno -> CELIA. HURT — their extra first-choice votes kept
  April alive past round one, which got Bruno (their fallback) eliminated
  at 18 instead; Bruno's transfers then elect Celia 38-24, their LAST
  choice. Voting sincerely for their favorite made their outcome worse
  than staying home — the no-show paradox, and (read forward) the Twin
  paradox: 8 voters identical to the 16 arrived, and the group did worse.
Same Condorcet cycle as the baseline (April 44-18, Bruno 42-20, Celia
38-24); no Ranked Robin BV race for the same freezability reason (LH's
margin tiebreak: April, +6 — shown in this file's mirror).

LIVE on BetterVoting as BV2175 (three races: STAR, RCV-IRV, Choose-One).
Live results: https://bettervoting.com/9dhv8y/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:April,Bruno,Celia
24:5,2,0   # April > Bruno > Celia   (16 + the 8 who showed up)
18:0,5,2   # Bruno > Celia > April
20:2,0,5   # Celia > April > Bruno
```

## What the engine says

Full report from the [`_tabulated` mirror](../participation_no_show_tabulated/bv2175_9dhv8y_noshow_showup_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * April    |  * Bruno    |    Celia    |
-------------------------------------------------------------
       * April > |     ---      |44 -  0 - 18 |24 -  0 - 38 |
       * Bruno > | 18 -  0 - 44 |    ---      |42 -  0 - 20 |
         Celia > | 38 -  0 - 24 |20 -  0 - 42 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: April > Bruno > Celia > April)

[Divergence from STAR]
  STAR    = April
  RCV-IRV = Celia   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: participation_no_show_tabulated/bv2175_9dhv8y_noshow_showup_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 62 ballots.
Count × April,Bruno,Celia
   24 ×     5,    2,    0
   20 ×     2,    0,    5
   18 ×     0,    5,    2

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
April      24   0   0  20   0  18  |   160   2.6
Bruno      18   0   0  24   0  20  |   138   2.2
Celia      20   0   0  18   0  24  |   136   2.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   April         -- 160 -- First place
   Bruno         -- 138 -- Second place
   Celia         -- 136
 April and Bruno advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   April         -- 44 -- First place
   Bruno         -- 18
   Equal Support --  0
 April wins.
   Runoff math:
     62  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     62  voters with a preference  (majority = 32)
           April 44 (71%)  ·  Bruno 18 (29%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 April
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/participation_no_show/bv2175_9dhv8y_noshow_showup.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2174_yyhr66_noshow_baseline](bv2174_yyhr66_noshow_baseline.md)
