# BV2154 — Felsenthal Example 8: the absolute loser wins Approval — and three races give three winners

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/wq6yv7) · **[results ↗](https://bettervoting.com/wq6yv7/results)** (election `wq6yv7`).

15 voters. An absolute majority (8 of 15) rank **April dead last** — April is both the Condorcet loser and the absolute loser. One voter's approval-cutoff choice elects her anyway. And the same 15 ballots return **three different winners across the three races**: Approval → **April**, IRV → **Clara**, Ranked Robin → **Bruce**.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A3, **Example 8**.

## The election

```
No. of voters    Ranking                     Approves
      6          April > Bruce > Clara       {April}
      4          Bruce > Clara > April       {Bruce}
      1          Clara > April > Bruce       {Clara, April}   ← the strategic ballot
      4          Clara > Bruce > April       {Clara}
```

Social ordering **Bruce > Clara > April** (Bruce beats April 8–7 and Clara 10–5; Clara beats April 9–6). Approval totals: **April 7, Bruce 4, Clara 5** → April, the candidate a majority ranked last — the [Condorcet loser](../../00_start_here/voting_paradoxes/condorcet_loser_paradox.md) and [absolute loser](../../00_start_here/voting_paradoxes/absolute_loser_paradox.md) paradoxes under Approval, triggered by a single voter approving two. Compare [BV2144](bv2144_mxfmhm_felsenthal_ex1.md), where Choose-One does the same with bullet votes only.

The ranked races disagree with Approval *and with each other*: IRV deletes the Condorcet winner Bruce (fewest first choices, 6/4/5) and elects **Clara** 9–6 — a [Condorcet winner paradox](../../00_start_here/voting_paradoxes/condorcet_winner_paradox.md) — while Ranked Robin elects **Bruce** directly. One electorate, three winners: the tabulation, not the ballot, decides.

## The races

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| Approval (one strategic two-approval ballot) | **April** (7/4/5) | April | ✓ |
| IRV | **Clara** (Bruce deleted; 9–6) | Clara | ✓ |
| Ranked Robin | **Bruce** (Condorcet winner) | Bruce | ✓ |

Files: [approval yaml](bv2154_wq6yv7_approval.yaml) · [irv yaml](bv2154_wq6yv7_irv.yaml) · [rr yaml](bv2154_wq6yv7_ranked_robin.yaml) · [frozen export](bv2154_wq6yv7_bv_export.json) · mirrors: [approval](felsenthal_paradoxes_tabulated/bv2154_wq6yv7_approval_tabulated.txt), [irv](felsenthal_paradoxes_tabulated/bv2154_wq6yv7_irv_tabulated.txt), [rr](felsenthal_paradoxes_tabulated/bv2154_wq6yv7_ranked_robin_tabulated.txt).
