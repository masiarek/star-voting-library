---
search:
  exclude: true
---

# BV2265 — Participation (2 of 2): one more honest voter, and the council gets worse for them

*Generated from [`bv2265_th3pbp_joiner_council_worse.yaml`](../bv2265_th3pbp_joiner_council_worse.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Ada, Dov

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/th3pbp) · **[results ↗](https://bettervoting.com/th3pbp/results)** (election `th3pbp` · test `BV2265`).

## Scenario

The same six voters and the same two-seat board as BV2264 (j3hqvb), plus a
seventh voter whose honest ballot is Ada 3, Bruno 2, Cleo 5, Dov 0.

  - Seat 1 is unchanged: scores Ada 24, Dov 18, Cleo 16, Bruno 15; Ada wins
    the runoff 3-0 (four voters express no preference). Ada is seated.
  - Seat 2 is not. The new voter's support lifted Cleo from 11 points to 16,
    which pushes Cleo past Bruno into the runoff — and Dov beats Cleo 4-2.

Council: Ada and Dov, where six voters alone elected Ada and Bruno. By the
seventh voter's own ballot the council they voted for is worth 3 (Ada 3 +
Dov 0) and the council they would have got by staying home was worth 5
(Ada 3 + Bruno 2). Helping their favourite reach the runoff is exactly what
handed the seat to the candidate they scored 0.

That is a participation failure, and the mechanism is specific to Bloc STAR:
each seat rebuilds the finalist pair from whoever is left, with no reweighting
to absorb support already spent on a seated winner. Nobody voted strategically;
no tie-break was used.

Reproduced on BetterVoting (election th3pbp): BV elects Ada then Dov,
nTallyVotes 7, tieBreakType none — an exact match with the LH count. Frozen
export: bv2265_th3pbp_joiner_council_worse_bv_export.json.
Live results: https://bettervoting.com/th3pbp/results

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
3,2,5,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 7 ballots to fill 2 seats.
Ada,Bruno,Cleo,Dov
  3,    5,   1,  3
  4,    5,   2,  4
  4,    0,   1,  4
  2,    2,   5,  1
  3,    1,   1,  1
  5,    0,   1,  5
  3,    2,   5,  0

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 24 -- First place
   Dov           -- 18 -- Second place
   Cleo          -- 16
   Bruno         -- 15
 Ada and Dov advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 3 -- First place
   Dov           -- 0
   Equal Support -- 4
 Ada wins.
   Runoff math:
     7  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Ada 3 (100%)  ·  Dov 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dov           -- 18 -- First place
   Cleo          -- 16 -- Second place
   Bruno         -- 15
 Dov and Cleo advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dov           -- 4 -- First place
   Cleo          -- 2
   Equal Support -- 1
 Dov wins.
   Runoff math:
     7  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     6  voters with a preference  (majority = 4)
           Dov 4 (67%)  ·  Cleo 2 (33%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Ada
 Dov
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
         Ada > |    ---     |4 - 1 - 2  |5 - 0 - 2  |3 - 4 - 0  |
       Bruno > | 2 - 1 - 4  |   ---     |2 - 1 - 4  |4 - 1 - 2  |
        Cleo > | 2 - 0 - 5  |4 - 1 - 2  |   ---     |2 - 1 - 4  |
         Dov > | 0 - 4 - 3  |2 - 1 - 4  |4 - 1 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ada — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        1  2  3  1  0  0  |    24   3.4
Bruno      2  0  0  2  1  2  |    15   2.1
Cleo       2  0  0  1  4  0  |    16   2.3
Dov        1  2  1  0  2  1  |    18   2.6
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2265_th3pbp_joiner_council_worse_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/03_Criteria/participation/cases/bv2265_th3pbp_joiner_council_worse.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2264_j3hqvb_council_before_joiner](bv2264_j3hqvb_council_before_joiner.md)
