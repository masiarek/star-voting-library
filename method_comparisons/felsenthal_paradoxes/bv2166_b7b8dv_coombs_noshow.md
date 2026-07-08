# BV2166 — Coombs' No-Show electorate (2 of 2): two voters stay home — and STAR flips too

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/b7b8dv) · **[results ↗](https://bettervoting.com/b7b8dv/results)** (election `b7b8dv`).

The same election as [BV2165](bv2165_9vxcj7_coombs_noshow.md) with one change, *ceteris paribus*: the two `Cass>Boone>Amy` voters don't participate. Felsenthal's target is Coombs — which now elects **Cass**, the abstainers' *top* preference. The honest headline for this repo: **STAR flips too**, live and frozen. The two voters get their favorite by staying home under *both* counts.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A7, **Example 19** (continued — Felsenthal notes the same flip arises from *truncation* to Cass-only: the Truncation paradox). Full §A7 treatment: [coombs.md](../../00_start_here/voting_paradoxes/coombs.md).

## The one changed datum

```
No. of voters    BV2165 (all vote)       BV2166 (two stay home)
      4          Amy  > Boone > Cass     Amy  > Boone > Cass
      4          Boone > Cass > Amy      Boone > Cass > Amy
      5          Cass > Amy  > Boone     Cass > Amy  > Boone
      2          Cass > Boone > Amy      —      (abstain)
```

**Coombs, worked:** on 13 ballots the last-place counts become Amy 4, **Boone 5**, Cass 4 — now *Boone* is deleted, and **Cass wins**. The abstainers' ordering was `Cass>Boone>Amy`: full turnout bought their second choice (BV2165), staying home buys their first — the [No-Show paradox](../../00_start_here/voting_paradoxes/no_show.md) under Coombs.

## The live STAR flip — shown honestly

With all 15 ballots STAR elects **Boone** (41/43/51; Boone beats Cass 8–7 in the runoff). On these 13: **Amy 39, Boone 37, Cass 41** — the finalist pair changes to Cass/Amy and **Cass wins the runoff 9–4**. The absent pair's sincere ballots scored Boone a 3, which was exactly what had lifted Boone into (and through) the runoff; withholding them elects their favorite. That is a **genuine STAR participation failure** on this profile — the first live score-family entry in the no-show group. The mechanism is STAR's *runoff stage* (which costs it Moulin-style participation guarantees); a pure score count cannot be moved against an added sincere ballot. Choose-One elects Cass in both electorates, unmoved — the flip lives entirely in elimination/runoff machinery.

## Agreement

| Election | Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|---|
| BV2165 all vote | STAR | **Boone** | **Boone** | ✓ |
| BV2166 two no-shows | STAR | **Cass** | **Cass** | ✓ |
| BV2165 / BV2166 | Choose-One | Cass / Cass | Cass / Cass | ✓ |
| BV2165 / BV2166 | Coombs *(paper)* | — | Boone / Cass | n/a |

Files: [star](bv2166_b7b8dv_star.yaml) · [plurality](bv2166_b7b8dv_plurality.yaml) · [frozen export](bv2166_b7b8dv_bv_export.json) · mirrors: [star](felsenthal_paradoxes_tabulated/bv2166_b7b8dv_star_tabulated.txt), [plurality](felsenthal_paradoxes_tabulated/bv2166_b7b8dv_plurality_tabulated.txt) · Part 1: [BV2165](bv2165_9vxcj7_coombs_noshow.md).
