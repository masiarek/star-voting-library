---
search:
  exclude: true
---

# BV2264 — Participation (1 of 2): the council six voters elect

*Generated from [`bv2264_j3hqvb_council_before_joiner.yaml`](../bv2264_j3hqvb_council_before_joiner.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Ada, Bruno

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/j3hqvb) · **[results ↗](https://bettervoting.com/j3hqvb/results)** (election `j3hqvb` · test `BV2264`).

## Scenario

The CONTROL half of a participation pair. Six voters fill a two-seat board by
Bloc STAR — the 0-5 STAR ballot counted once per seat: elect a winner, remove
them, re-run the same count on who is left.

  - Seat 1: scores Ada 21, Dov 18, Bruno 13, Cleo 11. Ada and Dov advance;
    Ada wins the automatic runoff 2-0, with four of the six voters expressing
    no preference between them.
  - Seat 2: Ada is removed and the same ballots are re-counted. Dov 18,
    Bruno 13, Cleo 11; Bruno beats Dov in the runoff 3-2.

Council: Ada and Bruno. No rung of the tie-break ladder is consulted.

Pair with BV2265 (th3pbp), which is these six ballots plus one honest seventh
voter — and that voter ends up with a council their own ballot rates LOWER.

Reproduced on BetterVoting (election j3hqvb): BV elects Ada then Bruno,
nTallyVotes 6, tieBreakType none — an exact match with the LH count. Frozen
export: bv2264_j3hqvb_council_before_joiner_bv_export.json.
Live results: https://bettervoting.com/j3hqvb/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Bruno,Cleo,Dov
3,5,1,3
4,5,2,4
4,0,1,4
2,2,5,1
3,1,1,1
5,0,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 6 ballots to fill 2 seats.
Ada,Bruno,Cleo,Dov
  3,    5,   1,  3
  4,    5,   2,  4
  4,    0,   1,  4
  2,    2,   5,  1
  3,    1,   1,  1
  5,    0,   1,  5

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 21 -- First place
   Dov           -- 18 -- Second place
   Bruno         -- 13
   Cleo          -- 11
 Ada and Dov advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 2 -- First place
   Dov           -- 0
   Equal Support -- 4
 Ada wins.
   Runoff math:
     6  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Ada 2 (100%)  ·  Dov 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dov           -- 18 -- First place
   Bruno         -- 13 -- Second place
   Cleo          -- 11
 Dov and Bruno advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 3 -- First place
   Dov           -- 2
   Equal Support -- 1
 Bruno wins.
   Runoff math:
     6  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Bruno 3 (60%)  ·  Dov 2 (40%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Ada
 Bruno
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |     Ada    |   Bruno   |    Cleo   |    Dov    |
-----------------------------------------------------------------
         Ada > |    ---     |3 - 1 - 2  |5 - 0 - 1  |2 - 4 - 0  |
       Bruno > | 2 - 1 - 3  |   ---     |2 - 1 - 3  |3 - 1 - 2  |
        Cleo > | 1 - 0 - 5  |3 - 1 - 2  |   ---     |1 - 1 - 4  |
         Dov > | 0 - 4 - 2  |2 - 1 - 3  |4 - 1 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ada — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        1  2  2  1  0  0  |    21   3.5
Bruno      2  0  0  1  1  2  |    13   2.2
Cleo       1  0  0  1  4  0  |    11   1.8
Dov        1  2  1  0  2  0  |    18   3.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2264_j3hqvb_council_before_joiner_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/03_Criteria/participation/cases/bv2264_j3hqvb_council_before_joiner.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2265_th3pbp_joiner_council_worse](bv2265_th3pbp_joiner_council_worse.md)
