# BV15 — Plurality + abstentions: the turnout undercount (Andre/Blake, 12 ballots)

*Generated from [`bv15_4h89vj_plurality_abstain.yaml`](../bv15_4h89vj_plurality_abstain.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Andre

## Scenario

A REAL BetterVoting election (BV id 4h89vj), "B15 - Basic - 2 candidates -
Plurality - Abstain". Live results: https://bettervoting.com/4h89vj/results
Frozen raw export: bv15_4h89vj_plurality_abstain_bv_export.json.

This is the Plurality instance of BetterVoting issue #740
(github.com/Equal-Vote/bettervoting/issues/740 — note: bettervoting#740, the
repo moved from star-server, the NUMBER stayed). #740 is a REPORTING gap, not
a tabulation error: BetterVoting's results widget shows only the MEANINGFUL
ballots as "voters" and drops the fully-abstained ones from the headline
turnout. The winner is right; the displayed voter count is short by exactly
the number of abstentions.

Twelve ballots, two candidates:

  Andre,Blake
  5,0   × 5   Andre  (a choose-one vote for Andre)
  0,5   × 2   Blake  (a choose-one vote for Blake)
  -,-   × 5   blank  — true abstentions (no score for anyone)

BetterVoting's own summaryData (in the frozen export) counts it CORRECTLY:
nTallyVotes = 7, nAbstentions = 5 (7 + 5 = 12 cast). Andre 5, Blake 2 -> Andre
wins. So the data is present; #740 is only that the results UI never surfaces
the 5 abstentions / the 12-ballot total — it reports the 7 as if that were
turnout.

Why this file is STAR, not Plurality: the LH engine has NO standalone
Plurality method (its methods are STAR / Bloc / SSS / RRV / Allocated, plus
auto RCV-IRV / Approval / Ranked Robin). With two candidates and choose-one
ballots every reasonable method elects the plurality leader, so we model each
"vote for X" as a STAR 5/0 ballot. STAR, Approval, and Choose-One Plurality
all name Andre here (no divergence). The point is the COUNT, and STAR's
self-reconciling runoff line prints exactly the accounting #740 is missing:
"12 ballots cast − 5 Equal Support = 7 voters with a preference." That runoff
line IS the "stats for nerds" turnout breakdown #740 asks BetterVoting to add.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Andre,Blake
5,0
5,0
5,0
5,0
5,0
0,5
0,5
-,-
-,-
-,-
-,-
-,-
```

## What the engine says

Full report from the [`_tabulated` mirror](../pet_real_bv_election_tabulated/bv15_4h89vj_plurality_abstain_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Andre   | * Blake   |
-----------------------------------------
     * Andre > |    ---     |5 - 5 - 2  |
     * Blake > | 2 - 5 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Andre — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 12 ballots. Note: 5 of 12 ballots are marked as abstentions.
Count × Andre,Blake
    5 ×     5,    0
    5 ×     -,    -
    2 ×     0,    5
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  Abs  | Total   Avg
Andre      5  0  0  0  0  2    5  |    25   3.6
Blake      2  0  0  0  0  5    5  |    10   1.4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Andre         -- 25 -- First place
   Blake         -- 10 -- Second place
 Andre and Blake advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Andre         -- 5 -- First place
   Blake         -- 2
   Equal Support -- 5
 Andre wins.
   Runoff math:
     12  ballots cast
   −  5  Equal Support (no preference between the two finalists)
     ──
      7  voters with a preference  (majority = 4)
           Andre 5 (71%)  ·  Blake 2 (29%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Andre
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/pet_real_bv_election/bv15_4h89vj_plurality_abstain.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [abstention_reconciliation_min_c2_b6](abstention_reconciliation_min_c2_b6.md) · [best_pet_c7_b461](best_pet_c7_b461.md) · [flat_scores_abstention_c3_b8](flat_scores_abstention_c3_b8.md) · [small_abstention_c2_b5](small_abstention_c2_b5.md)
