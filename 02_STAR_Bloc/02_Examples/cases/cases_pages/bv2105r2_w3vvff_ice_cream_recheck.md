---
search:
  exclude: true
---

# BV2105-r2 — Favorite ice cream (Bloc STAR, 2 seats): the partial ballot, re-counted a year later

*Generated from [`bv2105r2_w3vvff_ice_cream_recheck.yaml`](../bv2105r2_w3vvff_ice_cream_recheck.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Chocolate, Strawberry

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/w3vvff) · **[results ↗](https://bettervoting.com/w3vvff/results)** (election `w3vvff` · test `BV2105-r2`).

## Scenario

The LH reference for BetterVoting test BV2105-r2 (election w3vvff), a deliberate
RE-RUN of BV2105 (r4dqvd) on exactly the same four ballots — cast again so they
are counted by today's tabulator rather than by the one that ran in 2025.
Live results: https://bettervoting.com/w3vvff/results
Frozen raw export: bv2105r2_w3vvff_ice_cream_recheck_bv_export.json.

The four ballots — one of each KIND of ballot:

  Vanilla,Chocolate,Strawberry
  5,5,5     an all-5s ballot (loves everything)
  -,-,-     fully blank — a TRUE abstention
  1,-,-     Vanilla=1, the rest blank — a REAL (partial) vote
  2,5,4     a full ballot

Winners: Chocolate, Strawberry — unchanged, and never in question. Chocolate
takes seat 1; seat 2 is a Vanilla/Strawberry runoff tie broken by score,
Strawberry 9 > Vanilla 8.

WHY THIS ELECTION EXISTS. BV2105 reported nTallyVotes = 2 and nAbstentions = 2:
it filed the partial "1,-,-" ballot as an abstention alongside the genuinely
blank one.

CITATION CORRECTION (2026-08-04). The library used to attribute that miscount
to bettervoting#1056. Wrong: #1056 is a DIFFERENT defect on the same demo
election — a 401 blocking JSON/CSV download and Race Details, introduced by the
Editable Ballots work (#979) and correctly closed via #1058. They share only
the BV2105 test-document name. The counting defect is a separate bug, filed
2026-08-04 as bettervoting#1478.

THE RESULT: THE MISCOUNT STILL REPRODUCES. Ballots cast through the live API on
2026-08-04 come back nTallyVotes 2 / nAbstentions 2 — identical counts to the
2025 run, with Vanilla's score again averaged over 2 ballots instead of 3.
This file is the pinned correct count.

IS IT A BUG OR THE POLICY? Stated fairly: bettervoting#884 made an ALL-EQUAL
ballot an abstention, and a ballot bearing a SINGLE mark is trivially all-equal,
so this may be that policy working as written. The counter-argument is that BV's
own tally treats a blank as 0 — so "Vanilla 1, blank, blank" is really
"Vanilla 1, Chocolate 0, Strawberry 0", which is NOT all-equal and strictly
prefers Vanilla. Scope: partial ballots whose non-blank marks are all equal.
Partial ballots with two or more distinct marks count correctly.

WHY A NEW ELECTION WAS NEEDED (rather than re-fetching r4dqvd). Re-fetching the
2025 election also returns 2/2, but r4dqvd is `closed` and its stored
ElectionResult may simply be the tally computed back in 2025 — a re-fetch cannot
tell "the bug is live" from "we are reading an old result." Only ballots cast
through today's tabulator can, which is what w3vvff is.

WHY NO OTHER CASE IN THE LIBRARY ANSWERS IT. The discriminating shape is a
ballot whose non-blank marks are ALL EQUAL — here a single "1" — because that
is what bettervoting#884's all-equal rule treats as an abstention. The only
other 2026-minted export carrying a partial ballot is BV215 (26khr3), whose
partial is "Ada 5, Bruno 1, blank": two DISTINCT marks, so it is counted either
way and settles nothing.

LH counts it correctly: 4 ballots, 1 abstention (only the fully-blank row),
Vanilla total 8 (5 + 1 + 2). The dropped ballot only helped Vanilla, the seat-2
loser, so the winners survive — this is a REPORTING/counting defect, not a wrong
result. But a discarded cast ballot can flip a closer election.

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

<!-- --8<-- [start:report] -->
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
  RCV-IRV rounds: cases_tabulated/bv2105r2_w3vvff_ice_cream_recheck_RCV-IRV_tabulated.txt

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
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

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

[Condorcet Loser]
  No strict Condorcet loser; jointly weak Condorcet losers: Vanilla, Strawberry (winless — pairwise ties) — Vanilla elected by Choose-One (Plurality)!

[Score Distribution] (how many ballots gave each star rating)
                 Score
Candidate   5  4  3  2  1  0  Abs  | Total   Avg
Vanilla     1  0  0  1  1  0    1  |     8   2.7
Chocolate   2  0  0  0  0  0    2  |    10   5.0
Strawberry  1  1  0  0  0  0    2  |     9   4.5
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2105r2_w3vvff_ice_cream_recheck_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/cases/bv2105r2_w3vvff_ice_cream_recheck.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [b484mbm_tie_every_rung](b484mbm_tie_every_rung.md) · [bloc_lot_path_dependence_a_c3_b5](bloc_lot_path_dependence_a_c3_b5.md) · [bloc_lot_path_dependence_b_c3_b5](bloc_lot_path_dependence_b_c3_b5.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv1835_8h3yrx_score_leader_no_seat](bv1835_8h3yrx_score_leader_no_seat.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv2269_t488h9_race_nobody_can_lose](bv2269_t488h9_race_nobody_can_lose.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md) · [race_nobody_can_lose_two_seat_control](race_nobody_can_lose_two_seat_control.md)
