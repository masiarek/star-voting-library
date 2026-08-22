---
search:
  exclude: true
---

# Alaska 2022 special (reduced model), Palin deleted from every ballot — RCV-IRV now elects Begich

*Generated from [`alaska_2022_irv_without_palin.yaml`](../alaska_2022_irv_without_palin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** Begich

## Scenario

The counterfactual half of the pair. Take alaska_2022_irv_with_palin.yaml and
strike PALIN — a candidate who did not win — out of every ballot. Nothing else
changes: no voter is given a preference they did not express, no ballot is
reordered, no score is invented. The 23 Palin-only ballots simply have nothing
left to say and exhaust.
RCV-IRV now elects BEGICH, 93-84 over Peltola — and those are exactly the
numbers the full election's own pairwise matrix already reported for
Begich-vs-Peltola, because with Palin gone the instant runoff IS that
head-to-head. So the loser Palin, not the ballots, decided the 2022 result.
That is a failure of Independence of Irrelevant Alternatives on a real federal
race, and it is the direct check on FairVote's claim that "RCV is highly
resistant to spoilers because it satisfies both the Independence of Irrelevant
Alternatives and Independence of Clones criteria". Clone independence is
genuinely satisfied here (4 ballots rank Peltola between the two Republicans,
so {Palin, Begich} is not a clone set); IIA is not, and IIA is the criterion
FairVote's own prose definition describes.
Reading it fairly: a real Palin withdrawal would have changed campaigns and
turnout too. This is the STRICT criterion test — hold the ballots fixed,
remove one candidate — which is what IIA asks and all a certified ballot record
can honestly support.
Lesson: ../README.md · claim check: ../../fairvote_comparison_table/README.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
50:Peltola>Begich
36:Begich
29:Begich
25:Peltola
16:Begich>Peltola
12:Begich
5:Peltola
4:Peltola>Begich
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Alaska 2022 special (reduced model), Palin deleted from every ballot — RCV-IRV now elects Begich
 Tabulating 177 ballots (ranked ballots).

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Begich            93  Elected
Peltola           84  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Begich
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 2): Begich
   Outside (1):        Peltola
   One member ⇒ Begich is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Begich is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/alaska_2022_irv_without_palin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/alaska_2022/cases/alaska_2022_irv_without_palin.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Exhausted ballots (untangled)](../../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [alaska_2022_irv_with_palin](alaska_2022_irv_with_palin.md) · [bv2213_k3fmwv_alaska_2022](bv2213_k3fmwv_alaska_2022.md)
