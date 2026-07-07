# Felsenthal Ex.3 District I — STAR: also Bruno

*Generated from [`bv2147_9gdrqg_star.yaml`](../bv2147_9gdrqg_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bruno

## Scenario

Race 2 of 2 in District I of the Felsenthal Reinforcement-paradox trio (BV2147, bvid 9gdrqg; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A2, Example 3 — see bv2147_9gdrqg_irv.yaml for the setup.
The same 17 ballots with ranks mapped to 0–5 scores (5/3/1). Scores: Alma 47, Bruno 51, Cora 55 — Cora and Bruno advance, Bruno wins the automatic runoff 10–7. Same winner as the runoff procedure in this district; the reinforcement contrast appears at the combined stage (BV2149), where STAR stays with Bruno and the runoff procedure flips to Alma.
Live results: https://bettervoting.com/9gdrqg/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alma,Bruno,Cora
5,3,1
5,3,1
5,3,1
5,3,1
3,5,1
1,5,3
1,5,3
1,5,3
1,5,3
1,5,3
3,1,5
3,1,5
3,1,5
3,1,5
3,1,5
3,1,5
1,3,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2147_9gdrqg_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Alma    |  * Bruno    |   * Cora    |
-------------------------------------------------------------
          Alma > |     ---      |10 -  0 -  7 | 5 -  0 - 12 |
       * Bruno > |  7 -  0 - 10 |    ---      |10 -  0 -  7 |
        * Cora > | 12 -  0 -  5 | 7 -  0 - 10 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Alma > Bruno > Cora > Alma)

[Divergence from STAR]
  STAR                   = Bruno
  Choose-One (Plurality) = Cora   (differs from STAR)
  Approval               = Cora   (differs from STAR)
  RCV-RR                 = Cora   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: felsenthal_paradoxes_tabulated/bv2147_9gdrqg_star_RCV-RR_tabulated.txt

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Cora)
 - Runoff Round Winner   = (Bruno)
  Candidate Cora earned the highest total score,
  but Candidate Bruno won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 17 ballots.
Count × Alma,Bruno,Cora
    6 ×    3,    1,   5
    5 ×    1,    5,   3
    4 ×    5,    3,   1
    1 ×    3,    5,   1
    1 ×    1,    3,   5

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Alma       4  0  7  0  6  0  |    47   2.8
Bruno      6  0  5  0  6  0  |    51   3.0
Cora       7  0  5  0  5  0  |    55   3.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cora          -- 55 -- First place
   Bruno         -- 51 -- Second place
   Alma          -- 47
 Cora and Bruno advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 10 -- First place
   Cora          --  7
   Equal Support --  0
 Bruno wins.
   Runoff math:
     17  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     17  voters with a preference  (majority = 9)
           Bruno 10 (59%)  ·  Cora 7 (41%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bruno
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2147_9gdrqg_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md)
