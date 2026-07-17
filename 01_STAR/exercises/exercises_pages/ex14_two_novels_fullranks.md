# Exercise 14 — The transfer machine, fully ranked (BV probe variant)

*Generated from [`ex14_two_novels_fullranks.yaml`](../ex14_two_novels_fullranks.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STV (proportional, ranked ballots)](../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Austen, Camus

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/bj8dfc) · **[results ↗](https://bettervoting.com/bj8dfc/results)** (election `bj8dfc`).

## Scenario

The same nine voters as ex14_two_novels.yaml with every ballot completed
to a full ranking — 5×(Austen>Bronte>Camus>Dickens), 1×(Bronte>Camus>
Austen>Dickens), 3×(Camus>Dickens>Bronte>Austen). The added trailing
rankings are never reached by any transfer, so quota (4), rounds, and
seats are identical to the exercise: Austen elected round 1, surplus 1
to Bronte; Dickens then Bronte eliminated; Camus reaches 5. Seats:
Austen + Camus.
This variant exists as a bug probe: BetterVoting's STV tabulator
returns a server error on the exercise's truncated ballots (BV2201,
tk776t) — and, it turns out, on this fully-ranked copy too (BV2202,
bj8dfc), acquitting truncation. The bug has since been fully DIAGNOSED
(probes BV2203-2205): any STV count whose eliminations leave ONE
remaining hopeful who then reaches quota crashes — BV's IRV.ts
redistributes the winner's surplus over an empty candidate list, and
[].reduce with no initial value throws. This count is exactly that
shape (Camus elected last and alone). Full bisection, evidence table,
and ready-to-file issue: 06_Other/STV/bv_stv_sole_survivor_crash/;
narrative: ex14_transfer_machine.md.
Live on BetterVoting (Test ID BV2202): https://bettervoting.com/bj8dfc
— the vote page works; /results currently errors (the bug above).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
5:Austen>Bronte>Camus>Dickens
1:Bronte>Camus>Austen>Dickens
3:Camus>Dickens>Bronte>Austen
```

## What the engine says

Full report from the [`_tabulated` mirror](../exercises_tabulated/ex14_two_novels_fullranks_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- STV / Single Transferable Vote (multi-winner — 2 seats) ---
  Exercise 14 — The transfer machine, fully ranked (BV probe variant)
 Tabulating 9 ballots (ranked ballots).
 2 seats; Droop quota = 4 (44.4% of 9).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Austen             5  Elected
Camus              3  Hopeful
Bronte             1  Hopeful
Dickens            0  Hopeful

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Austen          3.00  Elected
Camus           3.00  Elected
Bronte          3.00  Rejected
Dickens         0.00  Rejected


Winner(s) — STV / Single Transferable Vote (multi-winner — 2 seats)
  Austen
  Camus
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex14_two_novels_fullranks.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md)
