# BV2132 — Pet poll (RCV-IRV): center squeeze elects Fish

*Generated from [`bv2132_ykjjhy_pet_irv.yaml`](../bv2132_ykjjhy_pet_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Fish

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ykjjhy) · **[results ↗](https://bettervoting.com/ykjjhy/results)** (election `ykjjhy`).

## Scenario

One of the four races in the BV2132 "Pet poll" (BetterVoting election ykjjhy). This is the RCV-IRV race (ranked ballots, instant runoff). Cat is the Condorcet winner (beats Dog 13-9 and Fish 15-7), but has the fewest first choices (6), so IRV eliminates Cat FIRST; its ballots transfer to Fish, which then beats Dog 13-9. So IRV elects Fish — a textbook center squeeze: the compromise candidate is dropped before the final round. Same electorate as the Plurality race (Dog) and the Approval/STAR races (Cat). BV also elects Fish. Live results: https://bettervoting.com/ykjjhy/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
9:Dog>Cat>Fish
7:Fish>Cat>Dog
6:Cat>Fish>Dog
```

## What the engine says

Full report from the [`_tabulated` mirror](../pet_poll_four_methods_tabulated/bv2132_ykjjhy_pet_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  BV2132 — Pet poll (RCV-IRV): center squeeze elects Fish
 Tabulating 22 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Dog                9  Hopeful
Fish               7  Hopeful
Cat                6  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Fish              13  Elected
Dog                9  Rejected
Cat                0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Fish
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_methods/bv2132_ykjjhy_pet_irv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2132_ykjjhy_pet_approval](bv2132_ykjjhy_pet_approval.md) · [bv2132_ykjjhy_pet_plurality](bv2132_ykjjhy_pet_plurality.md) · [bv2132_ykjjhy_pet_star](bv2132_ykjjhy_pet_star.md)
