# BV2105 — Favorite ice cream (Bloc STAR, 2 seats): a partial ballot mis-filed as an abstention

*Generated from [`bv2105_r4dqvd_ice_cream_bloc.yaml`](../bv2105_r4dqvd_ice_cream_bloc.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Chocolate, Strawberry

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/r4dqvd) · **[results ↗](https://bettervoting.com/r4dqvd/results)** (election `r4dqvd`).

## Scenario

The LH reference for BetterVoting test BV2105 (election r4dqvd, "Favorite ice
cream (Bloc STAR) - without end date"). Bloc STAR, 3 flavors, 2 seats, 4 ballots.
Live results: https://bettervoting.com/r4dqvd/results
Frozen raw export: bv2105_r4dqvd_ice_cream_bloc_bv_export.json.

The four ballots:

  Vanilla,Chocolate,Strawberry
  5,5,5     an all-5s ballot (loves everything)
  -,-,-     fully blank — a TRUE abstention
  1,-,-     Vanilla=1, the rest blank — a REAL (partial) vote
  2,5,4     a full ballot

Winners (both engines): Chocolate, Strawberry. Chocolate takes seat 1; seat 2
is a Vanilla/Strawberry runoff TIE (1-1) broken by score — Strawberry 9 >
Vanilla 8 — so BetterVoting's tieBreakType "score" and LH agree exactly.

THE REGRESSION (counting, not tabulation). BetterVoting's summaryData reports
nTallyVotes = 2 and nAbstentions = 2, i.e. it counts only the two FULL ballots
and files BOTH the blank ballot AND the partial "1,-,-" ballot as abstentions.
The LH engine counts 4 ballots with just 1 abstention (only the fully-blank
row); the "1,-,-" ballot is a cast vote — LH's Score Distribution shows Vanilla
with a real "1" and a total of 8. You can see BV dropped it: its per-candidate
"score" is the average over 2 ballots (Vanilla (5+2)/2 = 3, not (5+2+1)/3), so
the partial ballot never entered the tally.

Same winners here (the dropped ballot only helped Vanilla, the seat-2 loser), so
this is a REPORTING/counting regression rather than a wrong result — but a
discarded cast ballot can flip closer elections. It is the opposite-direction
sibling of BV15 / bettervoting#740: #740 DROPS abstentions from the displayed
turnout; BV2105 mis-classifies a real partial ballot AS an abstention.

Related bug: bettervoting#1056 (CLOSED / fixed). Because the upstream bug is
resolved, this case is a REGRESSION GUARD — the frozen export captures the
buggy summaryData (nTallyVotes 2 / nAbstentions 2), and this LH reference pins
the correct count (4 ballots, 1 abstention, 3 tallied) so a re-export can be
checked against it if the miscount ever returns.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Vanilla,Chocolate,Strawberry
5,5,5
-,-,-
1,-,-
2,5,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Chocolate
  Choose-One (Plurality) = Vanilla   (differs from STAR)
  RCV-IRV                = Vanilla   (differs from STAR)
  Note: 1 of 4 ballots (25%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: _main_tabulated/bv2105_r4dqvd_ice_cream_bloc_RCV-IRV_tabulated.txt

--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 4 ballots to fill 2 seats. Note: 1 of 4 ballots is marked as an abstention.
Vanilla,Chocolate,Strawberry
      5,        5,         5
      -,        -,         -
      1,        -,         -
      2,        5,         4
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Chocolate     -- 10 -- First place
   Strawberry    --  9 -- Second place
   Vanilla       --  8
 Chocolate and Strawberry advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Chocolate     -- 1 -- First place
   Strawberry    -- 0
   Equal Support -- 3
 Chocolate wins.
   Runoff math:
     4  ballots cast
   − 3  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Chocolate 1 (100%)  ·  Strawberry 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Strawberry    -- 9 -- First place
   Vanilla       -- 8 -- Second place
 Strawberry and Vanilla advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Strawberry    -- 1 -- Tied for first place
   Vanilla       -- 1 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[Bloc STAR: Round 2: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Strawberry    -- 9 -- First place
   Vanilla       -- 8
 Strawberry wins.

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Chocolate
 Strawberry
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                   |     Vanilla    | * Chocolate   | * Strawberry  |
---------------------------------------------------------------------
         Vanilla > |      ---       |  1 - 2 - 1    |  1 - 2 - 1    |
     * Chocolate > |   1 - 2 - 1    |     ---       |  1 - 3 - 0    |
    * Strawberry > |   1 - 2 - 1    |  0 - 3 - 1    |     ---       |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Vanilla, Chocolate (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                 Score
Candidate   5  4  3  2  1  0  Abs  | Total   Avg
Vanilla     1  0  0  1  1  0    1  |     8   2.7
Chocolate   2  0  0  0  0  0    2  |    10   5.0
Strawberry  1  1  0  0  0  0    2  |     9   4.5
```

</details>

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/bv2105_r4dqvd_ice_cream_bloc_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/bv2105_r4dqvd_ice_cream_bloc.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md)
