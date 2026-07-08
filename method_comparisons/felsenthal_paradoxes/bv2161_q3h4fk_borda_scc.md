# BV2161 — Borda's SCC paradox: the winner flips when a loser exits

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/q3h4fk) · **[results ↗](https://bettervoting.com/q3h4fk/results)** (election `q3h4fk`).

7 voters, three candidates. Every live count picks **C** — STAR and Choose-One agree, and so does Borda's paper count. The paradox is what happens when **B, a losing candidate, drops out**: Borda flips to **A**.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A5, **Example 15**.

**Profile note (arithmetic correction):** the paper prints the third bloc as `c > a > b`, but its own Borda totals — 6, 7, 8, summing to 21 — are only consistent with `c > b > a`. This case uses the arithmetic-consistent profile:

```
No. of voters    Preference ordering
      2          A > C > B
      2          B > A > C
      3          C > B > A
```

## Borda, worked (the paper paradox)

Borda points (2/1/0): **A 6, B 7, C 8 → C elected.** Now let B — who *lost* — withdraw, *ceteris paribus*. Borda on the remaining pair: **A 4, C 3 → A elected.** A loser's exit flipped the winner: **SCC** (the subset choice condition — the formal [spoiler](../../00_start_here/voting_paradoxes/spoiler_scc.md)) violated by Borda's count.

**Honest note:** with B gone, A beats C head-to-head 4–3, so *any* method elects A in the two-candidate contest — on a cyclic profile (B>A 5–2, A>C 4–3, C>B 5–2) every method's winner is exit-sensitive. Felsenthal's specific charge is that Borda's *point arithmetic* is what did the flipping. The cycle is also why no Ranked Robin or IRV race exists here (both would hit random ties on BV).

## The live races

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| STAR (5/3/1 map: 19/21/23) | **C** (beats B 5–2 in the runoff) | C | ✓ |
| Choose-One (Plurality) | **C** (3 of 7) | C | ✓ |
| Borda *(paper only)* | — | C 8 → B exits → A 4–3 | n/a |

Files: [star yaml](bv2161_q3h4fk_star.yaml) · [plurality yaml](bv2161_q3h4fk_plurality.yaml) · [frozen export](bv2161_q3h4fk_bv_export.json) · mirrors: [star](felsenthal_paradoxes_tabulated/bv2161_q3h4fk_star_tabulated.txt), [plurality](felsenthal_paradoxes_tabulated/bv2161_q3h4fk_plurality_tabulated.txt).
