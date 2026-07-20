# BV2164 — Coombs deletes the Condorcet winner first

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/xbqq8t) · **[results ↗](https://bettervoting.com/xbqq8t/results)** (election `xbqq8t`).

33 voters, four candidates. **Arlo beats every rival head-to-head** — and Coombs' procedure eliminates him *first*, because the same broad electorate that ranks him high everywhere also ranks him dead last on 12 ballots, the most of anyone. Live races: **STAR → Arlo**, **Choose-One → Bree**, **Ranked Robin → Arlo**; Coombs → Bree, worked below.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A7 ("Demonstrating Paradoxes Afflicting Coombs' Procedure" — eliminate whoever is ranked **last** by the most voters, unless someone holds a first-choice majority), **Example 17**. Full §A7 treatment: [coombs.md](../../00_start_here/voting_paradoxes/coombs.md).

## The election

```
No. of voters    Preference ordering
     11          Arlo > Bree > Cole > Dana
     12          Bree > Cole > Dana > Arlo
      2          Bree > Arlo > Dana > Cole
      4          Cole > Arlo > Dana > Bree
      4          Dana > Arlo > Bree > Cole
```

**Arlo is the Condorcet winner** (beats Bree 19–14, Cole 17–16, Dana 17–16; social ordering Arlo > Bree > Cole > Dana).

## Coombs, worked (the paper paradox)

Nobody holds a first-choice majority (11/14/4/4), so Coombs deletes the candidate ranked **last by the most voters**: last-place counts are **Arlo 12**, Dana 11, Cole 6, Bree 4 — **the Condorcet winner is the first candidate deleted**. With Arlo gone, Bree is ranked first by an absolute majority and wins. Felsenthal conjectures four candidates are the *minimum* for a Coombs Condorcet failure (with three, the pattern can't assemble). Also worked on [coombs.md](../../00_start_here/voting_paradoxes/coombs.md): Example 18's *monotonicity* twist — four voters raise Bree (`Cole>Arlo>Dana>Bree` → `Cole>Arlo>Bree>Dana`) and Bree **loses** under Coombs (Dana, then Cole are deleted instead, and Arlo wins); the live races are unchanged by that raise, so no separate election exists.

## Agreement

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| STAR (5/4/2/1 map: 107/**126**/96/67 — Bree tops the scores; Arlo wins the runoff 19–14) | Arlo | Arlo | ✓ |
| Choose-One (Plurality) | Bree (14 of 33) | Bree | ✓ |
| Ranked Robin | Arlo | Arlo | ✓ |
| Coombs *(paper only)* | — | Bree (Arlo deleted first) | n/a |

No IRV race: its first elimination is a random Cole/Dana 4–4 tie on BV. Files: [star](cases/bv2164_xbqq8t_star.yaml) · [plurality](cases/bv2164_xbqq8t_plurality.yaml) · [rr](cases/bv2164_xbqq8t_ranked_robin.yaml) · [frozen export](cases/bv2164_xbqq8t_bv_export.json) · mirrors: [star](cases/cases_tabulated/bv2164_xbqq8t_star_tabulated.txt), [plurality](cases/cases_tabulated/bv2164_xbqq8t_plurality_tabulated.txt), [rr](cases/cases_tabulated/bv2164_xbqq8t_ranked_robin_tabulated.txt).
