---
search:
  exclude: true
---

# Zero support — nobody scored anybody (allocated)

*Generated from [`zero_support_star_pr.yaml`](../zero_support_star_pr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Ada, Ben

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
[Divergence from STAR]
  STAR    = Ada
  RCV-IRV = Dev   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/zero_support_star_pr_RCV-IRV_tabulated.txt

--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 3 ballots to fill 2 seats.
Count × Ada,Ben,Cleo,Dev,Elsa
    3 ×   0,  0,   0,  0,   0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Ada           -- 0 -- Tied for first place
   Ben           -- 0 -- Tied for first place
   Cleo          -- 0 -- Tied for first place
   Dev           -- 0 -- Tied for first place
   Elsa          -- 0 -- Tied for first place
 There's a five-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ada', 'Ben', 'Cleo', 'Dev', 'Elsa']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ada', 'Ben', 'Cleo', 'Dev', 'Elsa']
  Resolved: ['Ada'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: Allocated Score Voting has one
    deterministic rung per seat — the round's weighted score total —
    and the tied candidates came back equal on it, so the pre-published
    LOT order chose among them — the result here was set by lot, not by
    the votes. No head-to-head or five-star rung runs on this path: a
    tie on the weighted total goes straight to the lot. Verify the tied
    candidates' totals in the round above.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 1+1/2 ballots.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Ben           -- 0 -- Tied for first place
   Cleo          -- 0 -- Tied for first place
   Dev           -- 0 -- Tied for first place
   Elsa          -- 0 -- Tied for first place
 There's a four-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ben', 'Cleo', 'Dev', 'Elsa']
  Resolved: ['Ben'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: Allocated Score Voting has one
    deterministic rung per seat — the round's weighted score total —
    and the tied candidates came back equal on it, so the pre-published
    LOT order chose among them — the result here was set by lot, not by
    the votes. No head-to-head or five-star rung runs on this path: a
    tie on the weighted total goes straight to the lot. Verify the tied
    candidates' totals in the round above.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Ada
 Ben
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |     Ada    |    Ben    |    Cleo   |    Dev    |    Elsa   |
-----------------------------------------------------------------------------
         Ada > |    ---     |0 - 3 - 0  |0 - 3 - 0  |0 - 3 - 0  |0 - 3 - 0  |
         Ben > | 0 - 3 - 0  |   ---     |0 - 3 - 0  |0 - 3 - 0  |0 - 3 - 0  |
        Cleo > | 0 - 3 - 0  |0 - 3 - 0  |   ---     |0 - 3 - 0  |0 - 3 - 0  |
         Dev > | 0 - 3 - 0  |0 - 3 - 0  |0 - 3 - 0  |   ---     |0 - 3 - 0  |
        Elsa > | 0 - 3 - 0  |0 - 3 - 0  |0 - 3 - 0  |0 - 3 - 0  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Ada, Ben, Cleo, Dev, Elsa (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        0  0  0  0  0  3  |     0   0.0
Ben        0  0  0  0  0  3  |     0   0.0
Cleo       0  0  0  0  0  3  |     0   0.0
Dev        0  0  0  0  0  3  |     0   0.0
Elsa       0  0  0  0  0  3  |     0   0.0
 Hare quota is 3/2.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/zero_support_star_pr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/zero_support_election/cases/zero_support_star_pr.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [zero_support_approval](zero_support_approval.md) · [zero_support_bloc_star](zero_support_bloc_star.md) · [zero_support_plurality](zero_support_plurality.md) · [zero_support_ranked_robin](zero_support_ranked_robin.md) · [zero_support_star](zero_support_star.md)
