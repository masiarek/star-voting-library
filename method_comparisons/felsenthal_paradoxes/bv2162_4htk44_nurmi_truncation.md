# BV2162 — Nurmi Example 16 (1 of 2): everyone ranks fully, and RCV-IRV misses the Condorcet winner

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4htk44) · **[results ↗](https://bettervoting.com/4htk44/results)** (election `4htk44`).

103 voters, four candidates, every ballot ranking all four. **B beats every rival head-to-head** — yet instant runoff elects **A**. Part 2 ([BV2163](bv2163_74j6vv_nurmi_truncation.md)) is the sting: 17 voters improve their own outcome by ranking *fewer* candidates. Three races: **STAR → B**, **RCV-IRV → A**, **Ranked Robin → B**.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A6 — the "Alternative Vote" procedure, the British name for instant-runoff / **RCV-IRV** (used once here; RCV-IRV everywhere else). **Example 16**, due to **Nurmi (1999: 63)**. Felsenthal's other §A6 paradoxes reuse Examples 2–4, already live as [BV2145/46](bv2145_6fj2kg_felsenthal_ex2.md), [BV2147–49](bv2149_byk9v2_felsenthal_ex3_reinforcement.md) and [BV2150/51](bv2150_dxg8pb_felsenthal_ex4_noshow.md).

## The election

```
No. of voters    Preference ordering
     33          A > B > C > D
     29          B > A > C > D
     24          C > B > A > D
     17          D > C > B > A
```

**B is the Condorcet winner**: beats A 70–33, C 62–41, D 86–17. Under RCV-IRV nobody holds a first-count majority (33/29/24/17), so **D** is eliminated — his 17 ballots transfer to C (41) — then **B** (29) is eliminated, and **A wins 62**. A [Condorcet winner failure](../../00_start_here/voting_paradoxes/condorcet_winner_paradox.md) on sincere, complete ballots; STAR (5/4/2/1 map: 346/407/312/171, runoff 70–33) and Ranked Robin both elect B.

## Agreement

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| STAR (ranks→scores) | B | B | ✓ |
| RCV-IRV | **A** | **A** | ✓ |
| Ranked Robin | B | B | ✓ |

Files: [star](bv2162_4htk44_star.yaml) · [irv](bv2162_4htk44_irv.yaml) · [rr](bv2162_4htk44_ranked_robin.yaml) · [frozen export](bv2162_4htk44_bv_export.json) · mirrors: [star](felsenthal_paradoxes_tabulated/bv2162_4htk44_star_tabulated.txt), [irv](felsenthal_paradoxes_tabulated/bv2162_4htk44_irv_tabulated.txt), [rr](felsenthal_paradoxes_tabulated/bv2162_4htk44_ranked_robin_tabulated.txt) · Part 2: [BV2163 — the truncation](bv2163_74j6vv_nurmi_truncation.md).
