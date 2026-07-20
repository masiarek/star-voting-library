# Upward monotonicity (Alaska 2022) — BEFORE: Peltola wins

*Generated from [`alaska_upward_before.yaml`](../alaska_upward_before.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Peltola

## Scenario

The real Alaska 2022 US House special, reduced ~960:1 to a faithful 200-voter
model (the same profile as method_comparisons/alaska_2022 and the burial case).
Counted by RCV-IRV: Begich has the fewest first-choices and is eliminated first,
his ballots split, and Peltola wins the final round 96-92. This is the BEFORE
half of an upward-monotonicity pair — the winner is Peltola. In the AFTER file
(alaska_upward_after), 7 Palin-only ballots are changed to Peltola>Palin, GIVING
THE WINNER MORE FIRST-PLACE SUPPORT — and Peltola then LOSES. Ranking the winner
higher turns her into a loser: the upward monotonicity paradox (Graham-Squire &
McCune, arXiv:2301.12075). Companion page: upward_monotonicity_alaska.md.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
50:Peltola>Begich>Palin
36:Palin>Begich>Peltola
29:Begich>Palin>Peltola
25:Peltola
23:Palin
16:Begich>Peltola>Palin
12:Begich
5:Peltola>Palin>Begich
4:Palin>Peltola>Begich
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/alaska_upward_before_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Upward monotonicity (Alaska 2022) — BEFORE: Peltola wins
 Tabulating 200 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Peltola           80  Hopeful
Palin             63  Hopeful
Begich            57  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Peltola           96  Elected
Palin             92  Rejected
Begich             0  Rejected
Blank Votes       12  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Peltola
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/cases/alaska_upward_before.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../00_start_here/topics/monotonicity/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [alaska_upward_after](alaska_upward_after.md) · [mono_raise_delete_after](mono_raise_delete_after.md) · [mono_raise_delete_before](mono_raise_delete_before.md) · [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md) · [sf_d7_downward_after](sf_d7_downward_after.md) · [sf_d7_downward_before](sf_d7_downward_before.md)
