---
search:
  exclude: true
---

# Resignation monotonicity — Bruno resigns, and Ana loses her seat

*Generated from [`resign_star_pr_after_bruno_c3_b5.yaml`](../resign_star_pr_after_bruno_c3_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Cleo, Dev

**Official tie-break (lot) order:** Ana > Cleo > Dev — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The same five voters and the same two seats as
`resign_star_pr_seated_c4_b5.yaml`, with one change: Bruno has resigned, so his
column is struck from every ballot and the count is re-run.

Nobody changed their mind. No ballot was re-marked. Ana's supporter never
mentioned Bruno at all. Yet Allocated Score now elects Cleo AND Dev — the two
wings of the bloc that just lost its own winner — and Ana is off the board.

The mechanism is the point: Bruno was the candidate ABSORBING the bloc's voting
power. Electing him spent their ballots down to a remainder too small to beat
Ana's full-weight vote. Take Bruno away and that power is unspent, so the bloc
buys both seats outright.

That is a failure of RESIGNATION MONOTONICITY (Oh & Peters, arXiv:2608.06156):
re-running the rule after a winner resigns must not unseat a winner who stayed.

The failure is not a tie-breaking artefact. Cleo and Dev do tie for the FIRST
seat here (10 apiece), so the lot decides which of them is seated first — but
whichever wins it, the other takes the second seat. The COMMITTEE {Cleo, Dev} is
the same under every tie-breaking order, and so is {Ana, Bruno} in the before
half; only the seating order is a coin flip.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana,Cleo,Dev
5,0,0     # the lone voter — Ana only
0,5,0     # bloc voter, Cleo wing
0,5,0     # bloc voter, Cleo wing
0,0,5     # bloc voter, Dev wing
0,0,5     # bloc voter, Dev wing
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR    = Cleo
  RCV-IRV = Dev   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/resign_star_pr_after_bruno_c3_b5_RCV-IRV_tabulated.txt

--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 5 ballots to fill 2 seats.
Count × Ana,Cleo,Dev
    2 ×   0,   5,  0
    2 ×   0,   0,  5
    1 ×   5,   0,  0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Cleo          -- 10 -- Tied for first place
   Dev           -- 10 -- Tied for first place
   Ana           --  5
 There's a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ana', 'Cleo', 'Dev']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Cleo', 'Dev']
  Resolved: ['Cleo'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: Allocated Score Voting has one
    deterministic rung per seat — the round's weighted score total —
    and the tied candidates came back equal on it, so the pre-published
    LOT order chose among them — the result here was set by lot, not by
    the votes. No head-to-head or five-star rung runs on this path: a
    tie on the weighted total goes straight to the lot. Verify the tied
    candidates' totals in the round above.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 2+1/2 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 2 ballots at score 5.

[Allocated Score Voting: Round 2]
 Tabulating 3 remaining ballots.
Count × Ana,Cleo,Dev
    2 ×   0,   5,  0
    2 ×   0,   0,  5
    1 ×   5,   0,  0

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Cleo
 Dev
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |     Ana    |    Cleo   |    Dev    |
-----------------------------------------------------
         Ana > |    ---     |1 - 2 - 2  |1 - 2 - 2  |
        Cleo > | 2 - 2 - 1  |   ---     |2 - 1 - 2  |
         Dev > | 2 - 2 - 1  |2 - 1 - 2  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Cleo, Dev (pairwise ties)

[Condorcet Loser]
  Condorcet Loser: Ana — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        1  0  0  0  0  4  |     5   1.0
Cleo       2  0  0  0  0  3  |    10   2.0
Dev        2  0  0  0  0  3  |    10   2.0
 Hare quota is 5/2.

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        1  0  0  0  0  4  |     5   1.0
Cleo       2  0  0  0  0  3  |    10   2.0
Dev        2  0  0  0  0  3  |    10   2.0
 The highest-scoring candidate wins a seat.
   Dev           -- 10 -- First place
   Ana           --  5
 Dev wins a seat.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/resign_star_pr_after_bruno_c3_b5_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/03_Criteria/cases/resign_star_pr_after_bruno_c3_b5.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abc_committee_monotonicity_1seat_c3_b10](abc_committee_monotonicity_1seat_c3_b10.md) · [abc_committee_monotonicity_2seats_c3_b10](abc_committee_monotonicity_2seats_c3_b10.md) · [cc_pareto_dominated_c4_b2](cc_pareto_dominated_c4_b2.md) · [monroe_pareto_dominated_c4_b24](monroe_pareto_dominated_c4_b24.md) · [resign_av_holds_after_kai_c6_b5](resign_av_holds_after_kai_c6_b5.md) · [resign_av_holds_c7_b5](resign_av_holds_c7_b5.md) · [resign_rrv_after_hana_c4_b5](resign_rrv_after_hana_c4_b5.md) · [resign_rrv_seated_c5_b5](resign_rrv_seated_c5_b5.md) · [resign_star_pr_seated_c4_b5](resign_star_pr_seated_c4_b5.md) · [sav_strategy_bullet_vote_c5_b2](sav_strategy_bullet_vote_c5_b2.md)
