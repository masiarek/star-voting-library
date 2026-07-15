# BV215 — None of the Above wins (STAR) — with a null abstention

*Generated from [`bv215_26khr3_nota_wins.yaml`](../bv215_26khr3_nota_wins.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** None of the Above

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/26khr3) · **[results ↗](https://bettervoting.com/26khr3/results)** (election `26khr3`).

## Scenario

A protest electorate. Four voters reject both real candidates and give the full
five stars to **None of the Above**; two voters back Ada (5) over Bruno (1). None
of the Above tops the score round (20 vs Ada 10 vs Bruno 2) and then wins the
automatic runoff 4-2 over Ada — so **None of the Above is elected**.

Three teaching points in one ballot set:
1. **None of the Above is a real candidate** on BetterVoting (id `c-nota`), scored
   0-5 like anyone else — not a spoiler flag. Here it simply wins, and *neither*
   BetterVoting nor the LH engine gives a NOTA win any special handling (no
   "re-run / no winner" state). Whether that's the intended behaviour is an open
   BetterVoting question.
2. **Flat 0 vs null abstention.** Most rejections here are an explicit `0`. Ballot
   2 instead leaves None of the Above **unscored** — BetterVoting stores that as
   `score: null` ("didn't score this candidate"), which is distinct from `0`. In
   LH that per-candidate abstention is the `&` marker (tabulates as 0, but kept
   separate in the record). A single unscored candidate does **not** make the
   ballot an abstention (BetterVoting reported nAbstentions = 0).
3. **BV vs LH agree.** Both elect None of the Above with identical score/runoff
   numbers.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Ada,Bruno,None of the Above
5,1,0
5,1,&
0,0,5
0,0,5
0,0,5
0,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 6 ballots.
Count × Ada,Bruno,None of the Above
    4 ×   0,    0,                5
    1 ×   5,    1,                0
    1 ×   5,    1,                &

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   None of the Above -- 20 -- First place
   Ada               -- 10 -- Second place
   Bruno             --  2
 None of the Above and Ada advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   None of the Above -- 4 -- First place
   Ada               -- 2
   Equal Support     -- 0
 None of the Above wins.
   Runoff math:
     6  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     6  voters with a preference  (majority = 4)
           None of the Above 4 (67%)  ·  Ada 2 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 None of the Above
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                          |         * Ada         |         Bruno        | * None of the Above  |
-------------------------------------------------------------------------------------------------
                  * Ada > |          ---          |      2 - 4 - 0       |      2 - 0 - 4       |
                  Bruno > |       0 - 4 - 2       |         ---          |      2 - 0 - 4       |
    * None of the Above > |       4 - 0 - 2       |      4 - 0 - 2       |         ---          |

[Condorcet Winner]
  Condorcet Winner: None of the Above — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                        Score
Candidate          5  4  3  2  1  0  Abs  | Total   Avg
Ada                2  0  0  0  0  4    0  |    10   1.7
Bruno              0  0  0  0  2  4    0  |     2   0.3
None of the Above  4  0  0  0  0  1    1  |    20   4.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../none_of_the_above_tabulated/bv215_26khr3_nota_wins_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/none_of_the_above/bv215_26khr3_nota_wins.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../00_start_here/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)
