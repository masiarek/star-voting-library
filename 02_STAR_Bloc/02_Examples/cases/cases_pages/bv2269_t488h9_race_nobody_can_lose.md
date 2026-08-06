---
search:
  exclude: true
---

# BV2269 — Three candidates, three seats: a race nobody can lose

*Generated from [`bv2269_t488h9_race_nobody_can_lose.yaml`](../bv2269_t488h9_race_nobody_can_lose.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../03_STAR_PR/01_Learn/README.md) · **3 seats**

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/t488h9) · **[results ↗](https://bettervoting.com/t488h9/results)** (election `t488h9` · test `BV2269`).

## Scenario

A behaviour probe, not a lesson with a winner. Three candidates stand for
three seats, so every candidate is seated no matter how anyone votes — the
membership of the board is settled before a single ballot is cast. The
question is what a tabulator does with a contest that cannot decide anything.

THIS FILE DOES NOT TABULATE, AND THAT IS THE POINT. The LH engine refuses an
election of this shape outright:

    Error: cannot fill 3 seats from 3 candidate(s).
      num_winners must be smaller than the number of candidates.

It exits 1 and counts nothing. There is no _tabulated mirror and no
expected_winners, because the engine never produces winners. The sibling
file race_nobody_can_lose_two_seat_control.yaml holds the SAME seven ballots
with one seat removed, and counts normally — that is the control.

BetterVoting answers the other way: it accepts the race (BV2269, t488h9) and
seats all three, in score order Abby, Bruno, Celia. Seats 1 and 2 run real
STAR rounds — scoring round 28 / 23 / 16, then runoffs won 5-2 and 5-2, no
voter at Equal Support, tieBreakType "none" throughout — so the SEAT ORDER
carries real information even though the membership does not. The third
round has one candidate and nothing to run against, and BV neither prints a
phantom runoff nor leaves a silent gap: the results page reads "Celia is the
only candidate, and wins by default", and the round's JSON carries an empty
runner_up and an empty logs array.

Neither engine is wrong. LH treats "seats >= candidates" as a spoiled
premise and refuses to pretend; BV accepts it and degrades gracefully into
saying so. The shape is not exotic — an organisation creates it by accident
every time nominations exactly fill the board.

Write-ins were disabled on the BV election on purpose: a single write-in
would supply the fourth candidate the premise excludes.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Abby,Bruno,Celia
5,3,1
5,4,0
4,3,2
5,2,3
3,5,1
2,5,4
4,1,5
```

## What the engine says

*(No `_tabulated` mirror found — run the file once to generate it.)*

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/cases/bv2269_t488h9_race_nobody_can_lose.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [b484mbm_tie_every_rung](b484mbm_tie_every_rung.md) · [bloc_lot_path_dependence_a_c3_b5](bloc_lot_path_dependence_a_c3_b5.md) · [bloc_lot_path_dependence_b_c3_b5](bloc_lot_path_dependence_b_c3_b5.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv1835_8h3yrx_score_leader_no_seat](bv1835_8h3yrx_score_leader_no_seat.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv2105r2_w3vvff_ice_cream_recheck](bv2105r2_w3vvff_ice_cream_recheck.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md) · [race_nobody_can_lose_two_seat_control](race_nobody_can_lose_two_seat_control.md)
