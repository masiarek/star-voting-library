# Favorite betrayal (RCV-IRV) — HONEST: Left voters rank their favorite first, and their WORST wins

*Generated from [`bv2227_3xgkck_honest_irv.yaml`](../bv2227_3xgkck_honest_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Right

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/3xgkck) · **[results ↗](https://bettervoting.com/3xgkck/results)** (election `3xgkck`).

## Scenario

The plainest form of the favorite-betrayal incentive, the one RCV voters keep asking
about ("is it smart to rank my favorite second?"). Three candidates on a spectrum:
Left, Center, Right. 34 voters. The 12 Left voters vote honestly — Left > Center >
Right. But Center, everyone's second choice and the Condorcet winner, has the FEWEST
first-choices (9) and is eliminated first; Center's ballots split, and RIGHT wins the
final 18-16. The Left voters' sincere ballots elected their LEAST-favorite candidate.
See the companion fb_irv_betray (2 of those Left voters rank Center first and Center
wins) and fb_star_honest (STAR/Ranked Robin elect Center from these same honest
preferences — no betrayal needed). Concept: favorite_betrayal_voting_301.md.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:Left>Center>Right
5:Center>Right>Left
4:Center>Left>Right
13:Right>Center>Left
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2227_3xgkck_honest_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Favorite betrayal (RCV-IRV) — HONEST: Left voters rank their favorite first, and their WORST wins
 Tabulating 34 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Right             13  Hopeful
Left              12  Hopeful
Center             9  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Right             18  Elected
Left              16  Rejected
Center             0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Right
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/favorite_betrayal_irv/cases/bv2227_3xgkck_honest_irv.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2227_3xgkck_honest_star](bv2227_3xgkck_honest_star.md) · [bv2228_bgcmxx_betray_irv](bv2228_bgcmxx_betray_irv.md)
