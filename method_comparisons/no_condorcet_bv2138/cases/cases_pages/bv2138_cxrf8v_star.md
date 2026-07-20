# No Condorcet Winner — STAR (ranks→scores): Brad wins the runoff

*Generated from [`bv2138_cxrf8v_star.yaml`](../bv2138_cxrf8v_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Brad

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/cxrf8v) · **[results ↗](https://bettervoting.com/cxrf8v/results)** (election `cxrf8v`).

## Scenario

One of four races in the 'One Ranked Electorate, Many Tabulations' election (BV2138, bvid cxrf8v; BV-confirmed). 921 voters, five candidates, NO Condorcet winner (Smith set = Abby, Brad, Dave, Erin). Robert LeGrand's flagship 'the method decides' example: across ~15 methods the win splits five ways. Ranks mapped to 0–5 scores. Abby tops the score round (2836) but Brad wins the automatic runoff head-to-head (463–458) → STAR → Brad (agreeing with BV's Ranked Robin, not LH's).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Abby,Brad,Cora,Dave,Erin
98: 5,1,4,2,3
64: 4,5,2,1,3
12: 4,5,1,2,3
98: 3,5,2,1,4
13: 3,5,1,2,4
125: 2,5,1,3,4
124: 4,1,5,2,3
76: 3,1,5,2,4
21: 4,3,1,5,2
30: 3,4,1,5,2
98: 1,4,2,5,3
139: 3,2,4,5,1
23: 2,3,4,5,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Brad
  RCV-IRV  = Dave   (differs from STAR)
  Approval = Erin   (differs from STAR)
  RCV-RR   = Abby   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2138_cxrf8v_star_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/bv2138_cxrf8v_star_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Abby)
 - Runoff Round Winner   = (Brad)
  Candidate Abby earned the highest total score, but
  Candidate Brad won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 921 ballots.
Count × Abby,Brad,Cora,Dave,Erin
  139 ×    3,   2,   4,   5,   1
  125 ×    2,   5,   1,   3,   4
  124 ×    4,   1,   5,   2,   3
   98 ×    5,   1,   4,   2,   3
   98 ×    3,   5,   2,   1,   4
   98 ×    1,   4,   2,   5,   3
   76 ×    3,   1,   5,   2,   4
   64 ×    4,   5,   2,   1,   3
   30 ×    3,   4,   1,   5,   2
   23 ×    2,   3,   4,   5,   1
   21 ×    4,   3,   1,   5,   2
   13 ×    3,   5,   1,   2,   4
   12 ×    4,   5,   1,   2,   3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Abby          -- 2836 -- First place
   Brad          -- 2780 -- Second place
   Cora          -- 2761
   Dave          -- 2738
   Erin          -- 2700
 Abby and Brad advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Brad          -- 463 -- First place
   Abby          -- 458
   Equal Support --   0
 Brad wins.
   Runoff math:
     921  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     921  voters with a preference  (majority = 461)
           Brad 463 (50%)  ·  Abby 458 (50%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Brad
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |     * Abby      |    * Brad      |      Cora      |      Dave      |      Erin      |
-----------------------------------------------------------------------------------------------------------
           * Abby > |       ---       |458 -   0 - 463 |461 -   0 - 460 |485 -   0 - 436 |511 -   0 - 410 |
           * Brad > | 463 -   0 - 458 |      ---       |461 -   0 - 460 |312 -   0 - 609 |623 -   0 - 298 |
             Cora > | 460 -   0 - 461 |460 -   0 - 461 |      ---       |460 -   0 - 461 |460 -   0 - 461 |
             Dave > | 436 -   0 - 485 |609 -   0 - 312 |461 -   0 - 460 |      ---       |311 -   0 - 610 |
             Erin > | 410 -   0 - 511 |298 -   0 - 623 |461 -   0 - 460 |610 -   0 - 311 |      ---       |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Abby > Dave > Brad > Abby)

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
Abby        98  221  356  148   98    0  |  2836   3.1
Brad       312  128   44  139  298    0  |  2780   3.0
Cora       200  260    0  260  201    0  |  2761   3.0
Dave       311    0  125  323  162    0  |  2738   3.0
Erin         0  312  396   51  162    0  |  2700   2.9
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2138_cxrf8v_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/no_condorcet_bv2138/cases/bv2138_cxrf8v_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/bv2138_cxrf8v_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2138_cxrf8v_irv](bv2138_cxrf8v_irv.md) · [bv2138_cxrf8v_ranked_robin](bv2138_cxrf8v_ranked_robin.md) · [bv2138_cxrf8v_stv](bv2138_cxrf8v_stv.md)
