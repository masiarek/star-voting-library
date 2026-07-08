# BV2153 — Felsenthal Example 7: a 51% first-choice majority loses the approval count

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/pcttmr) · **[results ↗](https://bettervoting.com/pcttmr/results)** (election `pcttmr`).

100 voters. **Amos is ranked first by an absolute majority — 51 of 100** — and is the Condorcet winner. Everyone approves their top two, and Approval elects **Bella** (approved by all 100). Felsenthal's **Absolute Majority paradox**.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A3, **Example 7**.

## The election

```
No. of voters    Ranking                    Approves (top two)
     51          Amos  > Bella > Chad       {Amos, Bella}
     48          Bella > Chad  > Amos       {Bella, Chad}
      1          Chad  > Bella > Amos       {Chad, Bella}
```

Approval totals: **Amos 51, Bella 100, Chad 49** → Bella. The top-two cutoff makes a 51-voter majority's *first-vs-second* distinction invisible: their ballots support Bella exactly as strongly as Amos. Under any count that reads that distinction, Amos wins — IRV seats him in round one (51 is a majority) and Ranked Robin elects him as Condorcet winner (beats Bella 51–49, Chad 51–49). Tag: [majority-failure](../../00_start_here/YAML_test_case_index/PARADOX_index.md); note this is a *strategy-profile* paradox — it needs every voter to approve two — where [Ex.5's](bv2152_r6ctvy_felsenthal_ex5_approval_cw.md) cutoffs were mixed.

## Borda, worked (Felsenthal Ex.13 — the same electorate)

Felsenthal reuses exactly this 51/48/1 profile as **Example 13** (Appendix §A5) to show **Borda's** Absolute-Majority failure: Borda points (2/1/0) give **Amos 102, Bella 148, Chad 50 → Bella elected** — Borda agrees with the top-two Approval count and misses the 51-vote absolute winner for the same underlying reason: both counts weigh a voter's second preference nearly (Approval: exactly) as much as their first. No Borda tabulator exists on BetterVoting or in the LH engine, so this count lives here on paper (cross-checkable with `pref_voting`).

## The races

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| Approval (everyone approves top two) | Bella (51/100/49) | Bella | ✓ |
| IRV | Amos (round-1 majority) | Amos | ✓ |
| Ranked Robin | Amos | Amos | ✓ |
| Borda *(paper only, Ex.13)* | — | Bella (102/148/50) | n/a |

Files: [approval yaml](bv2153_pcttmr_approval.yaml) · [irv yaml](bv2153_pcttmr_irv.yaml) · [rr yaml](bv2153_pcttmr_ranked_robin.yaml) · [frozen export](bv2153_pcttmr_bv_export.json) · mirrors: [approval](felsenthal_paradoxes_tabulated/bv2153_pcttmr_approval_tabulated.txt), [irv](felsenthal_paradoxes_tabulated/bv2153_pcttmr_irv_tabulated.txt), [rr](felsenthal_paradoxes_tabulated/bv2153_pcttmr_ranked_robin_tabulated.txt).
