---
search:
  exclude: true
---

# Resignation monotonicity — Hana resigns, and Gus loses his seat

*Generated from [`resign_rrv_after_hana_c4_b5.yaml`](../resign_rrv_after_hana_c4_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Reweighted Range Voting (proportional STAR)](../../../../03_STAR_PR/01_Learn/README.md) · **3 seats** · **Expected winners:** Fern, Ivan, Juno

## Scenario

The same five voters and the same three seats as
`resign_rrv_seated_c5_b5.yaml`, with Hana's column struck after she resigns.

RRV now elects Fern, Ivan and Juno. Gus — whose single supporter never
mentioned Hana, and who was seated before — is out, and his seat goes to the
slate that just lost its own winner.

Same failure as the Allocated Score pair on this page, in the second of the
engine's proportional score rules: re-running the count after a resignation
unseats a winner who stayed. Unique answer under every tie-breaking order.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Fern,Gus,Ivan,Juno
5,0,0,0     # Fern only
0,5,0,0     # Gus only
0,0,5,0     # was Hana + Ivan
0,0,0,5     # was Hana + Juno
5,0,5,5     # Fern + the rest of the slate
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Reweighted Range Voting Method (3 winners) ---

[Reweighted Range Voting]
 Tabulating 5 ballots to fill 3 seats.
Fern,Gus,Ivan,Juno
   5,  0,   0,   0
   0,  5,   0,   0
   0,  0,   5,   0
   0,  0,   0,   5
   5,  0,   5,   5

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Fern          -- 10 -- Tied for first place
   Ivan          -- 10 -- Tied for first place
   Juno          -- 10 -- Tied for first place
   Gus           --  5
 There's a three-way tie for first.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Fern', 'Gus', 'Ivan', 'Juno']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Fern', 'Ivan', 'Juno']
  Resolved: ['Fern'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: Reweighted Range Voting has one
    deterministic rung per seat — the round's weighted score total —
    and the tied candidates came back equal on it, so the pre-published
    LOT order chose among them — the result here was set by lot, not by
    the votes. No head-to-head or five-star rung runs on this path: a
    tie on the weighted total goes straight to the lot. Verify the tied
    candidates' totals in the round above.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 2 ballots reweighted from 1 to 1/2.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Ivan          -- 7+1/2 -- Tied for first place
   Juno          -- 7+1/2 -- Tied for first place
   Gus           -- 5
 There's a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ivan', 'Juno']
  Resolved: ['Ivan'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: Reweighted Range Voting has one
    deterministic rung per seat — the round's weighted score total —
    and the tied candidates came back equal on it, so the pre-published
    LOT order chose among them — the result here was set by lot, not by
    the votes. No head-to-head or five-star rung runs on this path: a
    tie on the weighted total goes straight to the lot. Verify the tied
    candidates' totals in the round above.

[Reweighted Range Voting: Round 2: Reweighing Ballots]
 Reweighted 2 ballots:
   1 ballot reweighted from 1 to 1/2.
   1 ballot reweighted from 1/2 to 1/3.

[Reweighted Range Voting: Round 3: Score round]
 The highest-scoring candidate wins a seat.
   Juno          -- 6+2/3 -- First place
   Gus           -- 5
 Juno wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (3 winners)]
 Fern
 Ivan
 Juno
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 3-winner count below,
        so no Top-2 finalists are marked.
               |     Fern   |    Gus    |    Ivan   |    Juno   |
-----------------------------------------------------------------
        Fern > |    ---     |2 - 2 - 1  |1 - 3 - 1  |1 - 3 - 1  |
         Gus > | 1 - 2 - 2  |   ---     |1 - 2 - 2  |1 - 2 - 2  |
        Ivan > | 1 - 3 - 1  |2 - 2 - 1  |   ---     |1 - 3 - 1  |
        Juno > | 1 - 3 - 1  |2 - 2 - 1  |1 - 3 - 1  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Fern, Ivan, Juno (pairwise ties)

[Condorcet Loser]
  Condorcet Loser: Gus — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Fern       2  0  0  0  0  3  |    10   2.0
Gus        1  0  0  0  0  4  |     5   1.0
Ivan       2  0  0  0  0  3  |    10   2.0
Juno       2  0  0  0  0  3  |    10   2.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/resign_rrv_after_hana_c4_b5_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/03_Criteria/cases/resign_rrv_after_hana_c4_b5.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abc_committee_monotonicity_1seat_c3_b10](abc_committee_monotonicity_1seat_c3_b10.md) · [abc_committee_monotonicity_2seats_c3_b10](abc_committee_monotonicity_2seats_c3_b10.md) · [cc_pareto_dominated_c4_b2](cc_pareto_dominated_c4_b2.md) · [monroe_pareto_dominated_c4_b24](monroe_pareto_dominated_c4_b24.md) · [resign_av_holds_after_kai_c6_b5](resign_av_holds_after_kai_c6_b5.md) · [resign_av_holds_c7_b5](resign_av_holds_c7_b5.md) · [resign_rrv_seated_c5_b5](resign_rrv_seated_c5_b5.md) · [resign_star_pr_after_bruno_c3_b5](resign_star_pr_after_bruno_c3_b5.md) · [resign_star_pr_seated_c4_b5](resign_star_pr_seated_c4_b5.md) · [sav_strategy_bullet_vote_c5_b2](sav_strategy_bullet_vote_c5_b2.md)
