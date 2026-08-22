---
search:
  exclude: true
---

# Bloc STAR — a divided majority wins nothing

*Generated from [`bloc_divided_majority.yaml`](../bloc_divided_majority.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Uma, Ugo

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/xpr4wk) · **[results ↗](https://bettervoting.com/xpr4wk/results)** (election `xpr4wk` · test `BV2289`).

## Scenario

Twelve voters fill two seats. Seven of them (58%) favour the Maya/Miles/Mina
group; five (42%) favour Uma and Ugo. The minority takes BOTH seats.

Nothing unfair happens in the count. The majority is divided — its seven voters
split three ways over three candidates and score each other's favourites 0 —
so no single one of them ever gets near the top of the scoring round:

  Uma 32, Ugo 27, Maya 15, Miles 10, Mina 10

  - Seat 1: finalists Uma and Ugo — both from the five-voter minority. Uma wins
    the runoff 5-0; the seven majority voters scored Uma and Ugo equally (1 and
    1), so they express no preference and sit the runoff out entirely.
  - Seat 2: Uma is removed. Ugo 27 still leads Maya 15. Ugo wins 9-3.

Council: Uma and Ugo. No rung of the tie-break ladder is consulted.

Two things are worth separating here. The first is ordinary vote splitting: a
group that spreads its support thin gets a weaker showing than the same group
united, and that is true under any method. The second is specific to BLOC — the
majority does not lose narrowly, it loses EVERYTHING, because each seat is
decided by the same undivided electorate and the minority wins each one on the
same 5 votes.

Note these ballots are sincere, not strategic. These voters genuinely rate only
their own candidate highly. This is not a clone-dependence failure in the
technical sense — Maya, Miles and Mina are not clones, because the voters who
like one of them do NOT like the other two.

Proportional STAR (Allocated Score) elects Maya and Uma on these same ballots —
one seat for each side, which is what 58/42 across two seats looks like.

Reproduced on BetterVoting (election xpr4wk), which counts the SAME ballots
twice. Both races match the LH count exactly: Bloc STAR elects Uma and Ugo
with tieBreakType 'none'; STAR-PR elects Maya and Uma. Frozen export:
bloc_divided_majority_bv_export.json.
Live results: https://bettervoting.com/xpr4wk/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Maya,Miles,Mina,Uma,Ugo
5,0,0,1,1   # three voters for Maya only
5,0,0,1,1
5,0,0,1,1
0,5,0,1,1   # two voters for Miles only
0,5,0,1,1
0,0,5,1,1   # two voters for Mina only
0,0,5,1,1
0,0,0,5,4   # five voters back both Uma and Ugo
0,0,0,5,4
0,0,0,5,4
0,0,0,5,4
0,0,0,5,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 12 ballots to fill 2 seats.
Count × Maya,Miles,Mina,Uma,Ugo
    5 ×    0,    0,   0,  5,  4
    3 ×    5,    0,   0,  1,  1
    2 ×    0,    5,   0,  1,  1
    2 ×    0,    0,   5,  1,  1

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Uma           -- 32 -- First place
   Ugo           -- 27 -- Second place
   Maya          -- 15
   Miles         -- 10
   Mina          -- 10
 Uma and Ugo advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Uma           -- 5 -- First place
   Ugo           -- 0
   Equal Support -- 7
 Uma wins.
   Runoff math:
     12  ballots cast
   −  7  Equal Support (no preference between the two finalists)
     ──
      5  voters with a preference  (majority = 3)
           Uma 5 (100%)  ·  Ugo 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ugo           -- 27 -- First place
   Maya          -- 15 -- Second place
   Miles         -- 10
   Mina          -- 10
 Ugo and Maya advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ugo           -- 9 -- First place
   Maya          -- 3
   Equal Support -- 0
 Ugo wins.
   Runoff math:
     12  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     12  voters with a preference  (majority = 7)
           Ugo 9 (75%)  ·  Maya 3 (25%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Uma
 Ugo
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
                 |      Maya    |    Miles    |     Mina    |     Uma     |     Ugo     |
-----------------------------------------------------------------------------------------
          Maya > |     ---      | 3 -  7 -  2 | 3 -  7 -  2 | 3 -  0 -  9 | 3 -  0 -  9 |
         Miles > |  2 -  7 -  3 |    ---      | 2 -  8 -  2 | 2 -  0 - 10 | 2 -  0 - 10 |
          Mina > |  2 -  7 -  3 | 2 -  8 -  2 |    ---      | 2 -  0 - 10 | 2 -  0 - 10 |
           Uma > |  9 -  0 -  3 |10 -  0 -  2 |10 -  0 -  2 |    ---      | 5 -  7 -  0 |
           Ugo > |  9 -  0 -  3 |10 -  0 -  2 |10 -  0 -  2 | 0 -  7 -  5 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Uma — matches the STAR winner

[Condorcet Loser]
  No strict Condorcet loser; jointly weak Condorcet losers: Miles, Mina (winless — pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Maya        3   0   0   0   0   9  |    15   1.3
Miles       2   0   0   0   0  10  |    10   0.8
Mina        2   0   0   0   0  10  |    10   0.8
Uma         5   0   0   0   7   0  |    32   2.7
Ugo         0   5   0   0   7   0  |    27   2.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bloc_divided_majority_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/bloc_shapes/cases/bloc_divided_majority.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bloc_all_but_one](bloc_all_but_one.md) · [bloc_condorcet_winner_no_seat](bloc_condorcet_winner_no_seat.md) · [bloc_equal_support_seat](bloc_equal_support_seat.md) · [bloc_finalist_wins_nothing](bloc_finalist_wins_nothing.md) · [bloc_harborview_council](bloc_harborview_council.md) · [bloc_no_majority_bridge](bloc_no_majority_bridge.md) · [bloc_one_voter_council](bloc_one_voter_council.md) · [bloc_score_leader_shut_out](bloc_score_leader_shut_out.md) · [bloc_widest_field](bloc_widest_field.md)
