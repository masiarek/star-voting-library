---
search:
  exclude: true
---

# Bloc STAR — making the first runoff buys you nothing

*Generated from [`bloc_finalist_wins_nothing.yaml`](../bloc_finalist_wins_nothing.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Ada, Cleo

## Scenario

Seven voters fill two seats from three candidates. Blake is the second-highest
scorer overall AND one of the two finalists for seat 1 — and wins no seat at
all.

  - Seat 1: scores Ada 31, Blake 23, Cleo 12. Ada and Blake are the finalists.
    Ada wins the runoff 4-0 (three voters scored Ada and Blake equally, so they
    express no preference between them).
  - Seat 2: Ada is removed and the same seven ballots are counted again.
    Blake 23, Cleo 12 — Blake still nearly doubles Cleo's score. But the seat
    is filled by the RUNOFF, not the score, and Cleo beats Blake 4-3.

Council: Ada and Cleo. Blake finishes second in the scoring round of both
rounds and goes home empty-handed. No rung of the tie-break ladder is consulted.

The lesson: reaching the automatic runoff for seat 1 is not a down payment on
seat 2. Each seat is a fresh STAR election, and the only thing that carries
over is which candidates are still in the race.

Compare bloc_score_leader_shut_out.yaml, where the candidate passed over leads
the scoring round in EVERY round.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Blake,Cleo
5,5,0   # three voters rate Ada and Blake equally
5,5,0
5,5,0
4,2,3   # four voters prefer Ada, then Cleo, then Blake
4,2,3
4,2,3
4,2,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 7 ballots to fill 2 seats.
Count × Ada,Blake,Cleo
    4 ×   4,    2,   3
    3 ×   5,    5,   0

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 31 -- First place
   Blake         -- 23 -- Second place
   Cleo          -- 12
 Ada and Blake advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 4 -- First place
   Blake         -- 0
   Equal Support -- 3
 Ada wins.
   Runoff math:
     7  ballots cast
   − 3  Equal Support (no preference between the two finalists)
     ─
     4  voters with a preference  (majority = 3)
           Ada 4 (100%)  ·  Blake 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Blake         -- 23 -- First place
   Cleo          -- 12 -- Second place
 Blake and Cleo advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cleo          -- 4 -- First place
   Blake         -- 3
   Equal Support -- 0
 Cleo wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Cleo 4 (57%)  ·  Blake 3 (43%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Ada
 Cleo
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |     Ada    |   Blake   |    Cleo   |
-----------------------------------------------------
         Ada > |    ---     |4 - 3 - 0  |7 - 0 - 0  |
       Blake > | 0 - 3 - 4  |   ---     |3 - 0 - 4  |
        Cleo > | 0 - 0 - 7  |4 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ada — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Blake — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        3  4  0  0  0  0  |    31   4.4
Blake      3  0  0  4  0  0  |    23   3.3
Cleo       0  0  4  0  0  3  |    12   1.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bloc_finalist_wins_nothing_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/bloc_shapes/cases/bloc_finalist_wins_nothing.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bloc_all_but_one](bloc_all_but_one.md) · [bloc_condorcet_winner_no_seat](bloc_condorcet_winner_no_seat.md) · [bloc_divided_majority](bloc_divided_majority.md) · [bloc_equal_support_seat](bloc_equal_support_seat.md) · [bloc_harborview_council](bloc_harborview_council.md) · [bloc_no_majority_bridge](bloc_no_majority_bridge.md) · [bloc_one_voter_council](bloc_one_voter_council.md) · [bloc_score_leader_shut_out](bloc_score_leader_shut_out.md) · [bloc_widest_field](bloc_widest_field.md)
