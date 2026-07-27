# Condorcet's 1788 rebuttal to Borda — the ranked profile, counted pairwise

*Generated from [`condorcet_1788_ranked_robin.yaml`](../condorcet_1788_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Peter

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/khcwm4) · **[results ↗](https://bettervoting.com/khcwm4/results)** (election `khcwm4`).

## Scenario

The same election as condorcet_1788_star.yaml, kept in its original RANKED form
and counted the way Condorcet said it should be: every pair, head-to-head.

    4 : Peter > Paul  > James
    3 : Paul  > James > Peter
    2 : Paul  > Peter > James
    2 : James > Peter > Paul

The round-robin table is the argument. Peter beats Paul 6-5 and beats James 6-5,
so Peter is the Condorcet winner. Borda's positional count elects Paul (14 points
to Peter's 12), and plurality elects Paul too (5 first choices) — both crown a
candidate who loses a direct majority contest, which was precisely the defect
Borda had accused plurality of.

Ranked Robin reads only the ORDER on each ballot, never the rank numbers, so it
cannot be led astray by positional points the way Borda is. That distinction —
same ranked ballot, different tabulation — is the whole reason "RCV" names a
ballot and not a count.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
4:Peter>Paul>James
3:Paul>James>Peter
2:Paul>Peter>James
2:James>Peter>Paul
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/condorcet_1788_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 11 ballots (ranked ballots).

Ballots:
     4 × Peter > Paul > James
     3 × Paul > James > Peter
     2 × Paul > Peter > James
     2 × James > Peter > Paul

Round-Robin — every pair, head-to-head (For – Against):
   Peter  beats Paul    6 – 5
   Peter  beats James   6 – 5
   Paul   beats James   9 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |   Peter   |  Paul    |  James   |
---------------------------------------------
  Peter > |    ---    |6 - 0 - 5 |6 - 0 - 5 |
   Paul > | 5 - 0 - 6 |   ---    |9 - 0 - 2 |
  James > | 5 - 0 - 6 |2 - 0 - 9 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Peter      2–0–0         2      +2  Paul, James
    2  Paul       1–1–0         1      +6  James
    3  James      0–2–0         0      -8  —

Winner — Ranked Robin (RCV-RR): Peter
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/borda_condorcet_1788/cases/condorcet_1788_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [condorcet_1788_irv](condorcet_1788_irv.md) · [condorcet_1788_star](condorcet_1788_star.md)
