---
search:
  exclude: true
---

# Downward monotonicity (San Francisco D7 2020) — BEFORE: Melgar wins

*Generated from [`sf_d7_downward_before.yaml`](../sf_d7_downward_before.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** Melgar

## Scenario

The real 2020 San Francisco Board of Supervisors election, District 7 (seven
candidates), reduced to the final three after four candidates are eliminated and
their votes transferred — the preference profile from Graham-Squire & McCune,
arXiv:2301.12075, Table 2. Counted by RCV-IRV: Engardio leads Round 1 with 14119
first-choices to Melgar's 11652 and Nguyen's 10855. Nguyen is eliminated; his
ballots transfer and Melgar wins the final 18561-16370. This is the BEFORE half of
a DOWNWARD-monotonicity pair — Engardio LOSES here. In the AFTER file
(sf_d7_downward_after), 800 Engardio>Nguyen>Melgar ballots are shifted DOWN to
Nguyen>Engardio>Melgar — giving the loser Engardio LESS first-place support — and
Engardio then WINS. Ranking a loser lower makes them win: the downward monotonicity
paradox. Companion page: downward_monotonicity_sf.md.
Model note: the Round-1 three-way counts (14119 / 11652 / 10855) and the final
(Melgar 18561, Engardio 16370) reproduce the paper's published figures exactly;
Melgar's own second-preference split (not published in the quoted table) is
reconstructed to complete the three-way, chosen consistent with the paper's stated
AFTER outcome (Engardio wins once Melgar is eliminated).

## Parameters (from the YAML)

```yaml
voting_method: RCV_IRV
num_winners: 1
expected_winners: [Melgar]
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
13319:Engardio>Melgar>Nguyen
800:Engardio>Nguyen>Melgar
2500:Melgar>Engardio>Nguyen
3500:Melgar>Nguyen>Engardio
5652:Melgar
6909:Nguyen>Melgar>Engardio
2251:Nguyen>Engardio>Melgar
1695:Nguyen
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Downward monotonicity (San Francisco D7 2020) — BEFORE: Melgar wins
 Tabulating 36626 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Engardio       14119  Hopeful
Melgar         11652  Hopeful
Nguyen         10855  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Melgar         18561  Elected
Engardio       16370  Rejected
Nguyen             0  Rejected
Blank Votes     1695  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Melgar
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Melgar
   Outside (2):        Engardio, Nguyen
   One member ⇒ Melgar is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Melgar is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/sf_d7_downward_before_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/cases/sf_d7_downward_before.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [alaska_upward_after](alaska_upward_after.md) · [alaska_upward_before](alaska_upward_before.md) · [mono_raise_delete_after](mono_raise_delete_after.md) · [mono_raise_delete_before](mono_raise_delete_before.md) · [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md) · [sf_d7_downward_after](sf_d7_downward_after.md)
