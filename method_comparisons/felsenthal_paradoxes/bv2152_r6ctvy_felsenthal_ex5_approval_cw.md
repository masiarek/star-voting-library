# BV2152 — Felsenthal Example 5: Approval misses the Condorcet winner

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/r6ctvy) · **[results ↗](https://bettervoting.com/r6ctvy/results)** (election `r6ctvy`).

47 voters. Bert beats both rivals head-to-head — yet the approval count elects **Anna**. The paradox is the approval **cutoff**: 31 voters rank Bert second, but 31 ballots draw the approve/don't-approve line above him.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A3 ("Demonstrating the Paradoxes Afflicting the Approval Voting Procedure"), **Example 5** — due to **Felsenthal & Maoz (1988: 123, Example 2)**.

## The election

Rankings (approved candidates in braces, per the text's parentheses):

```
No. of voters    Ranking                     Approves
     18          Anna  > Bert > Carla        {Anna}
      6          Bert  > Carla > Anna        {Bert, Carla}
      8          Bert  > Anna  > Carla       {Bert, Anna}
      2          Carla > Anna  > Bert        {Carla, Anna}
     13          Carla > Bert  > Anna        {Carla}
```

Pairwise: **Bert beats Anna 27–20 and Carla 32–15** — the Condorcet winner (social ordering Bert > Anna > Carla). Approval totals: **Anna 28, Bert 14, Carla 21** → Anna wins. The 18 Anna-bullet and 13 Carla-bullet voters rank Bert second but approve only their favorite, so the pairwise favorite finishes *last* on approvals — the [Condorcet winner paradox](../../00_start_here/voting_paradoxes/condorcet_winner_paradox.md) under Approval.

## The races

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| Approval (the text's sets) | Anna (28/14/21) | Anna | ✓ |
| Ranked Robin (same voters' rankings) | Bert | Bert | ✓ |

Files: [approval yaml](bv2152_r6ctvy_approval.yaml) · [rr yaml](bv2152_r6ctvy_ranked_robin.yaml) · [frozen export](bv2152_r6ctvy_bv_export.json) · mirrors: [approval](felsenthal_paradoxes_tabulated/bv2152_r6ctvy_approval_tabulated.txt), [rr](felsenthal_paradoxes_tabulated/bv2152_r6ctvy_ranked_robin_tabulated.txt). Related LH-only case: [Ex.6 — Approval can elect a Pareto-dominated candidate](felsenthal_ex6_pareto.md).
