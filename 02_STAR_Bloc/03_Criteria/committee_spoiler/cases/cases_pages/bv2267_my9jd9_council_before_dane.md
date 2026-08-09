---
search:
  exclude: true
---

# BV2267 — Committee spoiler (1 of 2): three candidates, before a fourth runs

*Generated from [`bv2267_my9jd9_council_before_dane.yaml`](../bv2267_my9jd9_council_before_dane.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Cyrus, Ari

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/my9jd9) · **[results ↗](https://bettervoting.com/my9jd9/results)** (election `my9jd9` · test `BV2267`).

## Scenario

The CONTROL half of a spoiler pair. Seven voters fill two seats from three
candidates by Bloc STAR.

  - Seat 1: scores Cyrus 17, Bea 16, Ari 11; Cyrus beats Bea in the automatic
    runoff 4-2 (one voter expresses no preference).
  - Seat 2: Cyrus is removed and the same ballots are re-counted. Bea 16,
    Ari 11; Ari beats Bea 4-3.

Council: Cyrus and Ari. No rung of the tie-break ladder is consulted.

Pair with BV2268 (6m3gxq): the very same seven ballots with a fourth candidate,
Dane, added. Dane wins no seat and the council changes anyway.

Reproduced on BetterVoting (election my9jd9): BV elects Cyrus then Ari,
nTallyVotes 7, tieBreakType none — an exact match with the LH count. Frozen
export: bv2267_my9jd9_council_before_dane_bv_export.json.
Live results: https://bettervoting.com/my9jd9/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ari,Bea,Cyrus
5,3,3
0,3,4
1,0,1
0,5,2
4,2,4
1,0,1
0,3,2
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Cyrus
  Choose-One (Plurality) = Ari   (differs from STAR)
  RCV-IRV                = Ari   (differs from STAR)
  Approval               = Bea   (differs from STAR)
  Note: 4 of 7 ballots (57%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2267_my9jd9_council_before_dane_RCV-IRV_tabulated.txt

--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 7 ballots to fill 2 seats.
Count × Ari,Bea,Cyrus
    2 ×   1,  0,    1
    1 ×   5,  3,    3
    1 ×   0,  3,    4
    1 ×   0,  5,    2
    1 ×   4,  2,    4
    1 ×   0,  3,    2

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cyrus         -- 17 -- First place
   Bea           -- 16 -- Second place
   Ari           -- 11
 Cyrus and Bea advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cyrus         -- 4 -- First place
   Bea           -- 2
   Equal Support -- 1
 Cyrus wins.
   Runoff math:
     7  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     6  voters with a preference  (majority = 4)
           Cyrus 4 (67%)  ·  Bea 2 (33%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bea           -- 16 -- First place
   Ari           -- 11 -- Second place
 Bea and Ari advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ari           -- 4 -- First place
   Bea           -- 3
   Equal Support -- 0
 Ari wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Ari 4 (57%)  ·  Bea 3 (43%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Cyrus
 Ari
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |     Ari    |    Bea    |   Cyrus   |
-----------------------------------------------------
         Ari > |    ---     |4 - 0 - 3  |1 - 3 - 3  |
         Bea > | 3 - 0 - 4  |   ---     |2 - 1 - 4  |
       Cyrus > | 3 - 3 - 1  |4 - 1 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cyrus — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Bea — loses every head-to-head matchup — elected by Approval!

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ari        1  1  0  0  2  3  |    11   1.6
Bea        1  0  3  1  0  2  |    16   2.3
Cyrus      0  2  1  2  2  0  |    17   2.4
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2267_my9jd9_council_before_dane_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/03_Criteria/committee_spoiler/cases/bv2267_my9jd9_council_before_dane.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2268_6m3gxq_spoiler_changes_council](bv2268_6m3gxq_spoiler_changes_council.md)
