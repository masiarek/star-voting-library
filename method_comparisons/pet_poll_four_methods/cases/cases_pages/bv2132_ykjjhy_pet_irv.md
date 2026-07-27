# BV2132 — Pet poll (RCV-IRV): center squeeze elects Fish

*Generated from [`bv2132_ykjjhy_pet_irv.yaml`](../bv2132_ykjjhy_pet_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Fish

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

The count, step by step — the rounds and how the winner is reached:

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

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Cat
   Outside (2):        Dog, Fish
   One member ⇒ Cat is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Fish is OUTSIDE the Smith set. ✗
      Every member of the set (Cat) beats Fish head-to-head, yet
      RCV-IRV elected Fish anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 00_start_here/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2132_ykjjhy_pet_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_methods/cases/bv2132_ykjjhy_pet_irv.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2132_ykjjhy_pet_approval](bv2132_ykjjhy_pet_approval.md) · [bv2132_ykjjhy_pet_plurality](bv2132_ykjjhy_pet_plurality.md) · [bv2132_ykjjhy_pet_star](bv2132_ykjjhy_pet_star.md)
