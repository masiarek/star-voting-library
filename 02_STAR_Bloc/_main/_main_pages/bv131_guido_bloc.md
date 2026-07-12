# BV131 — Guido example (Bloc STAR): seat 1 is a hidden lot-decided tie

*Generated from [`bv131_guido_bloc.yaml`](../bv131_guido_bloc.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Cand2, Cand3

**Official tie-break (lot) order:** Cand2 > Cand1 > Cand3 — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The LH reference for BetterVoting test BV131 ("Guido example", real election
kbh3d9). The sheet marks it Passed, but seat 1 is actually a PERFECT lot-decided
tie — the Bloc analog of jfk7pd.

Bloc STAR, 3 candidates, 2 seats. Totals: Cand1=6, Cand2=6, Cand3=5.
  - Seat 1: Cand1 and Cand2 tie at 6 and advance. In the runoff they tie 1-1;
    score is 6-6; five-star is 1-1 each. Every deterministic rung ties, so the
    LOT decides. BetterVoting drew Cand2 at random (its round-0 logs:
    runoff_tied -> runoff_score_tie -> runoff_five_star_tie -> runoff_random ->
    Cand2). This file pins the lot order [Cand2, Cand1, Cand3] to REPRODUCE
    BV's Cand2.
  - Seat 2: remove Cand2 -> Cand1 (6) and Cand3 (5) advance; Cand3 wins the
    runoff 2-1.
Winners: Cand2, Cand3 (reproducing BV).

Two findings worth flagging:
  1. Non-reproducible, like jfk7pd: with the column-order fallback (no lot
     order) LH would elect Cand1 for seat 1, not Cand2 — same ballots, different
     winner, decided only by the tie-break order (cf. #1063).
  2. Reporting mislabel: BV's top-level `tieBreakType` is "none", even though its
     own round-0 `tieBreakType` is "random". A reader of the summary can't tell
     that seat 1 was a coin toss.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Cand1,Cand2,Cand3
1,5,2
0,0,1
5,1,2
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR               = Cand2
  RCV-IRV            = Cand3   (differs from STAR)
  RCV-RR (Condorcet) = Cand3   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: _main_tabulated/bv131_guido_bloc_RCV-IRV_tabulated.txt
  RCV-RR round-robin: _main_tabulated/bv131_guido_bloc_RCV-RR_tabulated.txt

--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 3 ballots to fill 2 seats.
Cand1,Cand2,Cand3
    1,    5,    2
    0,    0,    1
    5,    1,    2

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cand1         -- 6 -- First place
   Cand2         -- 6 -- Second place
   Cand3         -- 5
 Cand1 and Cand2 advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cand1         -- 1 -- Tied for first place
   Cand2         -- 1 -- Tied for first place
   Equal Support -- 1
 There's a two-way tie for first.

[Bloc STAR: Round 1: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Cand1         -- 6 -- Tied for first place
   Cand2         -- 6 -- Tied for first place
 There's still a two-way tie for first.

[Bloc STAR: Round 1: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Cand1         -- 1 -- Tied for first place
   Cand2         -- 1 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Cand2', 'Cand1', 'Cand3']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Cand1', 'Cand2']
  Resolved: ['Cand2'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cand1         -- 6 -- First place
   Cand3         -- 5 -- Second place
 Cand1 and Cand3 advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cand3         -- 2 -- First place
   Cand1         -- 1
   Equal Support -- 0
 Cand3 wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Cand3 2 (67%)  ·  Cand1 1 (33%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Cand2
 Cand3
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Cand1   | * Cand2   |   Cand3   |
-----------------------------------------------------
     * Cand1 > |    ---     |1 - 1 - 1  |1 - 0 - 2  |
     * Cand2 > | 1 - 1 - 1  |   ---     |1 - 0 - 2  |
       Cand3 > | 2 - 0 - 1  |2 - 0 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cand3 — STAR elected Cand2 instead (Cand3 was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Cand1      1  0  0  0  1  1  |     6   2.0
Cand2      1  0  0  0  1  1  |     6   2.0
Cand3      0  0  0  2  1  0  |     5   1.7
```

</details>

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/bv131_guido_bloc_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/bv131_guido_bloc.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md)
