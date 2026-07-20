# BV2163 — Nurmi Example 16 (2 of 2): 17 voters rank ONLY their favorite — and do better

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/74j6vv) · **[results ↗](https://bettervoting.com/74j6vv/results)** (election `74j6vv`).

The same election as [BV2162](bv2162_4htk44_nurmi_truncation.md) with one change, *ceteris paribus*: the 17 `D>C>B>A` voters **truncate** and rank only **D**. Result: RCV-IRV now elects **B** — whom those voters prefer to A, the winner their full rankings had produced. Ranking *less* of the ballot bought a *better* outcome: the **Truncation paradox**, live on BetterVoting.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A6, **Example 16**, due to **Nurmi (1999: 63)**.

## The one changed datum

```
No. of voters    BV2162 (full)         BV2163 (truncated)
     33          A > B > C > D         A > B > C > D
     29          B > A > C > D         B > A > C > D
     24          C > B > A > D         C > B > A > D
     17          D > C > B > A   →→→   D                (only the favorite)
```

D is eliminated first in both worlds — but here the 17 truncated ballots **exhaust** instead of transferring to C. So **C** (24) is eliminated instead of B, C's transfers flow to B, and **B wins**. The truncators' sincere ordering was `D>C>B>A`: they prefer B to A, so silence served them better than honesty — the [Truncation paradox](../../00_start_here/voting_paradoxes/truncation.md). (It also *accidentally repairs* BV2162's Condorcet failure: B, the pairwise champion, now wins the IRV race too.)

STAR (truncated ballots score only D: 329/373/244/171) and Ranked Robin (B still wins every head-to-head: 53–33 among voters with a preference, 62–24, 86–17) elect **B in both worlds** — pairwise and score counting give these 17 voters no truncation incentive; the elimination order is what their truncation exploits.

## Agreement

| Election | Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|---|
| BV2162 full | RCV-IRV | **A** | **A** | ✓ |
| BV2163 truncated | RCV-IRV | **B** | **B** | ✓ |
| BV2162 / BV2163 | STAR | B / B | B / B | ✓ |
| BV2162 / BV2163 | Ranked Robin | B / B | B / B | ✓ |

Files: [star](cases/bv2163_74j6vv_star.yaml) · [irv](cases/bv2163_74j6vv_irv.yaml) · [rr](cases/bv2163_74j6vv_ranked_robin.yaml) · [frozen export](cases/bv2163_74j6vv_bv_export.json) · mirrors: [star](cases/cases_tabulated/bv2163_74j6vv_star_tabulated.txt), [irv](cases/cases_tabulated/bv2163_74j6vv_irv_tabulated.txt), [rr](cases/cases_tabulated/bv2163_74j6vv_ranked_robin_tabulated.txt) · Part 1: [BV2162](bv2162_4htk44_nurmi_truncation.md).
