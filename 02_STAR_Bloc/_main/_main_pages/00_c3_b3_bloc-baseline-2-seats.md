# Bloc STAR baseline — 3 candidates, 2 seats (clean, no tiebreak)

*Generated from [`00_c3_b3_bloc-baseline-2-seats.yaml`](../00_c3_b3_bloc-baseline-2-seats.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Alice, Bruno

## Scenario

The smallest Bloc STAR election that actually decides something: 3 candidates,
2 seats, so exactly one candidate is excluded. (A 2-candidate / 2-seat race
would be a non-election — both win no matter how anyone votes.)

Bloc STAR fills seats by running single-winner STAR once per seat: elect a
winner, remove them, re-run on the same ballots.
  - Seat 1: score all three. Alice (14) and Bruno (12) are the top two and
    advance; in the runoff Alice is preferred 2-1, so Alice takes seat 1.
  - Seat 2: remove Alice and re-run on the remaining two. Bruno (12) beats
    Clara (3) in the runoff 3-0 and takes seat 2.
Clara (total 3) is excluded. Both seats are decided cleanly by the ballots —
no rung of the tie-break ladder is ever consulted. This is the control the
Bloc tie probes vary from. Bloc is majoritarian: a cohesive majority can take
every seat.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Bruno,Clara
5,3,1
4,5,2
5,4,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/00_c3_b3_bloc-baseline-2-seats_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Alice   | * Bruno   |   Clara   |
-----------------------------------------------------
     * Alice > |    ---     |2 - 0 - 1  |3 - 0 - 0  |
     * Bruno > | 1 - 0 - 2  |   ---     |3 - 0 - 0  |
       Clara > | 0 - 0 - 3  |0 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Alice — matches the STAR winner

--- Bloc STAR Voting Method (2 winners) ---
[Bloc STAR]
 Tabulating 3 ballots.
Alice,Bruno,Clara
    5,    3,    1
    4,    5,    2
    5,    4,    0

[Score Distribution] (number of ballots giving each score)
       5  4  3  2  1  0  | Total   Avg
Alice  2  1  0  0  0  0  |    14   4.7
Bruno  1  1  1  0  0  0  |    12   4.0
Clara  0  0  0  1  1  1  |     3   1.0
 Want to fill 2 seats.

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alice         -- 14 -- First place
   Bruno         -- 12 -- Second place
   Clara         --  3
 Alice and Bruno advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alice         -- 2 -- First place
   Bruno         -- 1
   Equal Support -- 0
 Alice wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Alice 2 (67%)  ·  Bruno 1 (33%)

──────────────────────────────────────────────────
[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 12 -- First place
   Clara         --  3 -- Second place
 Bruno and Clara advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 3 -- First place
   Clara         -- 0
   Equal Support -- 0
 Bruno wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Bruno 3 (100%)  ·  Clara 0 (0%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Alice
 Bruno
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/00_c3_b3_bloc-baseline-2-seats.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md)
