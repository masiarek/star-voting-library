# Favorite betrayal (RCV-IRV) — BETRAY: 2 Left voters rank their favorite SECOND, and win

*Generated from [`bv2228_bgcmxx_betray_irv.yaml`](../bv2228_bgcmxx_betray_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Center

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/bgcmxx) · **[results ↗](https://bettervoting.com/bgcmxx/results)** (election `bgcmxx`).

## Scenario

The honest election (fb_irv_honest) exactly, with ONE change: just 2 of the 12 Left
voters betray their favorite — they rank Center FIRST and Left second (Center > Left >
Right) to keep the compromise Center from being squeezed out. Now Left has the fewest
first-choices (10) and is eliminated instead of Center; Left's ballots flow to Center,
and CENTER wins the final 21-13. By ranking their true favorite second, those 2 voters
got a far better outcome (their second choice instead of their worst). That is
"favorite betrayal": under RCV-IRV, honesty is not always safe — putting your favorite
first is only safe when they're either very strong or have no chance at all. STAR and
Ranked Robin remove the incentive: see fb_star_honest, where the HONEST ballots already
elect Center. Concept: favorite_betrayal_voting_301.md.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
10:Left>Center>Right
6:Center>Left>Right
5:Center>Right>Left
13:Right>Center>Left
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2228_bgcmxx_betray_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Favorite betrayal (RCV-IRV) — BETRAY: 2 Left voters rank their favorite SECOND, and win
 Tabulating 34 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Right             13  Hopeful
Center            11  Hopeful
Left              10  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Center            21  Elected
Right             13  Rejected
Left               0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Center
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/favorite_betrayal_irv/cases/bv2228_bgcmxx_betray_irv.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2227_3xgkck_honest_irv](bv2227_3xgkck_honest_irv.md) · [bv2227_3xgkck_honest_star](bv2227_3xgkck_honest_star.md)
