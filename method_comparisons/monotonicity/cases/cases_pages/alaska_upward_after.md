---
search:
  exclude: true
---

# Upward monotonicity (Alaska 2022) — AFTER: raise the winner, she loses

*Generated from [`alaska_upward_after.yaml`](../alaska_upward_after.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** Begich

## Scenario

The BEFORE file (alaska_upward_before) exactly, with ONE change: 7 of the 23
Palin-only ("bullet") ballots are switched to Peltola>Palin. Nothing else moves.
This gives the previous winner Peltola MORE first-place support (80 -> 87) — yet
she now LOSES. Why: the shifted votes pull Palin's first-round count (63 -> 56)
below Begich's 57, so PALIN is eliminated first instead of Begich; Palin's
ballots transfer 36 to Begich, and Begich beats Peltola in the final, 93-91.
Ranking the winner higher made the winner lose — the upward monotonicity paradox
(Graham-Squire & McCune, arXiv:2301.12075; realrcv.equal.vote/alaska22).
Model note: at this 200-voter reduction, moving 6 ballots makes an exact 57-57
Begich/Palin tie (a coarse-model artifact); 7 clears it cleanly for a tie-free,
engine-independent demonstration. The real election's figure is ~6,000 Palin-only
ballots, which crosses the threshold comfortably. Companion page:
upward_monotonicity_alaska.md.

## Parameters (from the YAML)

```yaml
voting_method: RCV_IRV
num_winners: 1
expected_winners:
- Begich
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
50:Peltola>Begich>Palin
36:Palin>Begich>Peltola
29:Begich>Palin>Peltola
25:Peltola
16:Palin
16:Begich>Peltola>Palin
12:Begich
7:Peltola>Palin
5:Peltola>Palin>Begich
4:Palin>Peltola>Begich
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Upward monotonicity (Alaska 2022) — AFTER: raise the winner, she loses
 Tabulating 200 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Peltola           87  Hopeful
Begich            57  Hopeful
Palin             56  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Begich            93  Elected
Peltola           91  Rejected
Palin              0  Rejected
Blank Votes       16  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Begich
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Begich
   Outside (2):        Peltola, Palin
   One member ⇒ Begich is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Begich is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/alaska_upward_after_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/cases/alaska_upward_after.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [alaska_upward_before](alaska_upward_before.md) · [mono_raise_delete_after](mono_raise_delete_after.md) · [mono_raise_delete_before](mono_raise_delete_before.md) · [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md) · [sf_d7_downward_after](sf_d7_downward_after.md) · [sf_d7_downward_before](sf_d7_downward_before.md)
