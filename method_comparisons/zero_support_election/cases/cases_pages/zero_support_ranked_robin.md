---
search:
  exclude: true
---

# Zero support — nobody scored anybody (RankedRobin)

*Generated from [`zero_support_ranked_robin.yaml`](../zero_support_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cleo > Dev > Elsa — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Five nominees, three voters, and every single score is 0.

This is the degenerate limit of a tie: not "the ballots point two ways" but
"the ballots point nowhere at all". Every candidate has the same total (0),
every head-to-head is Equal Support 0-0, and every rung above the lot has
nothing to count — so whichever method is asked, the answer comes from the
published lot order and not from a vote.

It is a real shape, not only a thought experiment. A committee ballot that
goes out with five names nobody has heard of comes back like this; so does a
race where the electorate deliberately withholds support. What the file is
for is checking that the engine says so OUT LOUD rather than reporting a
winner as though somebody had chosen one.

Same three ballots are counted six ways in this folder — see the README for
what each method does with them, and which of the six admits the lot decided.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cleo,Dev,Elsa
0,0,0,0,0   # voter 1 — turned out, then scored every nominee 0
0,0,0,0,0   # voter 2 — a deliberate 0 is not a blank ballot
0,0,0,0,0   # voter 3 — the third ballot says the same thing
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 3 ballots (score ballots).

Ballots:
   the ranking Ranked Robin reads ("=" = tied); source scores follow in () per column: Ada, Ben, Cleo, Dev, Elsa
     3 × Ada=Ben=Cleo=Dev=Elsa      (0, 0, 0, 0, 0)

Round-Robin — every pair, head-to-head (For – Against):
   Ada   ties  Ben    0 – 0
   Ada   ties  Cleo   0 – 0
   Ada   ties  Dev    0 – 0
   Ada   ties  Elsa   0 – 0
   Ben   ties  Cleo   0 – 0
   Ben   ties  Dev    0 – 0
   Ben   ties  Elsa   0 – 0
   Cleo  ties  Dev    0 – 0
   Cleo  ties  Elsa   0 – 0
   Dev   ties  Elsa   0 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cleo    |   Dev    |  Elsa    |
------------------------------------------------------------------
   Ada > |    ---    |0 - 3 - 0 |0 - 3 - 0 |0 - 3 - 0 |0 - 3 - 0 |
   Ben > | 0 - 3 - 0 |   ---    |0 - 3 - 0 |0 - 3 - 0 |0 - 3 - 0 |
  Cleo > | 0 - 3 - 0 |0 - 3 - 0 |   ---    |0 - 3 - 0 |0 - 3 - 0 |
   Dev > | 0 - 3 - 0 |0 - 3 - 0 |0 - 3 - 0 |   ---    |0 - 3 - 0 |
  Elsa > | 0 - 3 - 0 |0 - 3 - 0 |0 - 3 - 0 |0 - 3 - 0 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Ada        0–0–4         2      +0             0  —
    2  Ben        0–0–4         2      +0             0  —
    3  Cleo       0–0–4         2      +0             0  —
    4  Dev        0–0–4         2      +0             0  —
    5  Elsa       0–0–4         2      +0             0  —

Winner — Ranked Robin (RCV-RR): Ada
   *** 5 candidates tie on the highest Copeland score (2): Ada, Ben, Cleo, Dev, Elsa — a dead heat (they draw head-to-head, not a cycle). Neither the 1st nor the 2nd Degree tiebreaker separates them — resolved by lot order.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (5 of 5): Ada, Ben, Cleo, Dev, Elsa
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   dead heat (its members DRAW each other head-to-head), so the strongest
   "candidate" is a set, not a person. No member beats another, so there is no
   loop for Minimax / Ranked Pairs / Schulze to disagree about — which member
   wins is left to the tiebreak, not to a cycle rule. See
   05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md.
   Ranked Robin (RCV-RR) winner Ada is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   Fine print: this set contains a pairwise DRAW, and a draw is enough to keep a
   candidate in the Smith set but not in the tighter Schwartz set — so Schwartz
   may be smaller here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/zero_support_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/zero_support_election/cases/zero_support_ranked_robin.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [one_point_bloc_star](one_point_bloc_star.md) · [zero_support_approval](zero_support_approval.md) · [zero_support_bloc_star](zero_support_bloc_star.md) · [zero_support_plurality](zero_support_plurality.md) · [zero_support_star](zero_support_star.md) · [zero_support_star_pr](zero_support_star_pr.md)
