# Exercise 14 — The transfer machine: a book club buys two novels (STV)

*Generated from [`ex14_two_novels.yaml`](../ex14_two_novels.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STV (proportional, ranked ballots)](../../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Austen, Camus

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/tk776t) · **[results ↗](https://bettervoting.com/tk776t/results)** (election `tk776t`).

## Scenario

A nine-member book club buys TWO novels by ranked ballot, counted with
STV (the proportional cousin of RCV-IRV). Droop quota = floor(9/3)+1 =
4. Round 1: Austen has 5 first choices — over quota — and is elected;
her ONE surplus vote transfers (as fractions of the five ballots that
elected her) to their next choice, Bronte. Standings: Bronte 2, Camus
3, Dickens 0. Nobody reaches quota, so the machine turns to
eliminations: Dickens (0) first, then Bronte (2) — whose pile, INCLUDING
the fraction that arrived from Austen's surplus, moves on to Camus.
Camus reaches 5 and takes the second seat. Seats: Austen + Camus. The
drill follows one ballot through the whole journey — surplus, then
elimination — to see how STV keeps a vote moving until it lands.
Exercise: ex14_transfer_machine.md. Ballots and cast (novelists as
candidates) are this repo's own.
Live on BetterVoting (Test ID BV2201): https://bettervoting.com/tk776t
— the vote page works, but BV's STV tabulator currently returns a
server error on /results for this election, and for its fully-ranked
probe twin BV2202 (bj8dfc, ex14_two_novels_fullranks.yaml) — a live BV
bug, since DIAGNOSED: the count ends with Camus reaching quota as the
sole remaining hopeful, and BV's IRV.ts redistributes his surplus over
an empty candidate list ([].reduce with no initial value throws). Full
bisection (BV2203-2205) and ready-to-file issue:
06_Other/STV/bv_stv_sole_survivor_crash/. The seats above are the LH
engine's; BV STV races whose endgame leaves a hopeful standing
(ywckmg, kcf8vf, 39py93) compute fine.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
5:Austen>Bronte>Camus>Dickens
1:Bronte>Camus
3:Camus>Dickens
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/ex14_two_novels_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- STV / Single Transferable Vote (multi-winner — 2 seats) ---
  Exercise 14 — The transfer machine: a book club buys two novels (STV)
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
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex14_two_novels.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
