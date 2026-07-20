# BV2165 — Coombs' No-Show electorate (1 of 2): everyone votes

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9vxcj7) · **[results ↗](https://bettervoting.com/9vxcj7/results)** (election `9vxcj7`).

15 voters, three candidates, everyone participates. Coombs (on paper) elects **Boone**; the live races split — **STAR → Boone** (runoff 8–7), **Choose-One → Cass**. Part 2 ([BV2166](bv2166_b7b8dv_coombs_noshow.md)) removes two voters and *both* Coombs and STAR flip to their favorite.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A7 (Coombs' procedure), **Example 19**. Full §A7 treatment: [coombs.md](../../00_start_here/voting_paradoxes/coombs.md).

## The election

```
No. of voters    Preference ordering
      4          Amy  > Boone > Cass
      4          Boone > Cass > Amy
      5          Cass > Amy  > Boone
      2          Cass > Boone > Amy
```

**Coombs, worked:** no first-choice majority (4/4/7); last-place counts are **Amy 6** (4+2), Boone 5, Cass 4 — Amy is deleted, and Boone is then ranked first by 8 of 15 (his own 4 plus Amy's 4), an absolute majority — **Boone wins**. The pairwise preferences are a **cycle** (Amy>Boone 9–6, Boone>Cass 8–7, Cass>Amy 11–4), which is why there's no Ranked Robin race (random 3-way tie on BV) and no IRV race (random Amy/Boone elimination tie).

## Agreement

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| STAR (5/3/1 map: 41/43/**51** — Cass tops the scores; Boone wins the runoff 8–7) | Boone | Boone | ✓ |
| Choose-One (Plurality) | Cass (7 of 15) | Cass | ✓ |
| Coombs *(paper only)* | — | Boone (Amy deleted) | n/a |

Files: [star](cases/bv2165_9vxcj7_star.yaml) · [plurality](cases/bv2165_9vxcj7_plurality.yaml) · [frozen export](cases/bv2165_9vxcj7_bv_export.json) · mirrors: [star](cases/cases_tabulated/bv2165_9vxcj7_star_tabulated.txt), [plurality](cases/cases_tabulated/bv2165_9vxcj7_plurality_tabulated.txt) · Part 2: [BV2166 — two voters stay home](bv2166_b7b8dv_coombs_noshow.md).
