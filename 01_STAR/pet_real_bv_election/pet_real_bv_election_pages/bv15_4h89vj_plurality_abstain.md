# BV15 — Plurality + abstentions: the turnout undercount (Andre/Blake, 12 ballots)

*Generated from [`bv15_4h89vj_plurality_abstain.yaml`](../bv15_4h89vj_plurality_abstain.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** Andre

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4h89vj) · **[results ↗](https://bettervoting.com/4h89vj/results)** (election `4h89vj`).

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

Twelve ballots, two candidates (choose-one):

  Andre,Blake
  1,0   × 5   Andre  (a choose-one vote for Andre)
  0,1   × 2   Blake  (a choose-one vote for Blake)
  -,-   × 5   blank  — true abstentions (no vote for anyone)

BetterVoting's own summaryData (in the frozen export) counts it CORRECTLY:
nTallyVotes = 7, nAbstentions = 5 (7 + 5 = 12 cast). Andre 5, Blake 2 -> Andre
wins. So the data is present; #740 is only that the results UI never surfaces
the 5 abstentions / the 12-ballot total — it reports the 7 as if that were
turnout.

This file matches BV's method: Plurality (choose-one, 0/1 ballots). (An earlier
version modelled it as STAR 5/0, on the mistaken belief that the LH engine had
no Plurality method — it does: single-winner Plurality tabulates via the STAR
path, multi-winner as SNTV.) The self-reconciling turnout line still prints the
accounting #740 is missing: "12 ballots cast − 5 no-preference = 7 voters with a
preference" — the "stats for nerds" turnout breakdown #740 asks BV to add.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Andre,Blake
1,0
1,0
1,0
1,0
1,0
0,1
0,1
-,-
-,-
-,-
-,-
-,-
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Choose-One / Plurality Voting Method (single winner) ---

[STAR Voting]
 Tabulating 12 ballots. Note: 5 of 12 ballots are marked as abstentions.
Count × Andre,Blake
    5 ×     1,    0
    5 ×     -,    -
    2 ×     0,    1
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Andre         -- 5 -- First place
   Blake         -- 2 -- Second place
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

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Andre
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

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

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  Abs  | Total   Avg
Andre      0  0  0  0  5  2    5  |     5   0.7
Blake      0  0  0  0  2  5    5  |     2   0.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../pet_real_bv_election_tabulated/bv15_4h89vj_plurality_abstain_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/pet_real_bv_election/bv15_4h89vj_plurality_abstain.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [abstention_reconciliation_min_c2_b6](abstention_reconciliation_min_c2_b6.md) · [best_pet_c7_b461](best_pet_c7_b461.md) · [flat_scores_abstention_c3_b8](flat_scores_abstention_c3_b8.md) · [small_abstention_c2_b5](small_abstention_c2_b5.md)
