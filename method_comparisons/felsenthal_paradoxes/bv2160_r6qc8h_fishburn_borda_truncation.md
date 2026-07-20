# BV2160 — Fishburn's Borda truncation electorate: three counts, three winners — and Borda's flips on paper

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/r6qc8h) · **[results ↗](https://bettervoting.com/r6qc8h/results)** (election `r6qc8h`).

7 voters, four candidates, a cyclic profile. The live races: **STAR → B**, **Choose-One → A**. The paradox this example exists for — Borda's **Truncation paradox** — is worked below on paper, because neither BetterVoting nor the LH engine has a Borda tabulator (Borda counts are cross-checkable with `pref_voting`).

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A5 ("Demonstrating Paradoxes Afflicting Borda's procedure"), **Example 14** — adapted from **Fishburn (1974: 543)**.

## The election

```
Voters     Preference ordering
V1–V3      A > B > C > D
V4         B > C > A > D
V5         B > C > D > A
V6–V7      C > D > A > B
```

## Borda, worked (the paper paradox)

Borda with *k* points for a top rank … 0 for unranked: **A 19, B 19, C 20, D 12 → C elected.** Now let V1–V3 — unhappy with C — **truncate C** from their ballots: **A 16, B 16, C 14, D 12** — C falls to third and A/B tie for the win. Revealing *less* of their ballots got the truncators a result they prefer: the [Truncation paradox](../../00_start_here/voting_paradoxes/truncation.md) under Borda. (Borda's vulnerability comes from unranked candidates scoring 0 — truncation is a weapon aimed at whoever you leave off.)

## The live races

Pairwise, this profile is a **cycle** (A>B 5–2, B>C 5–2, C>A 4–3) — no Condorcet winner, and the reason there's no Ranked Robin race (BV would resolve a 3-way Copeland tie at random) and no IRV race (its first elimination is a random B/C tie at 2 first-choices each).

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| STAR (5/4/2/1 map: 22/24/24/14; B and C take both finalist seats) | **B** (runoff 5–2) | B | ✓ |
| Choose-One (Plurality) | **A** (3 of 7) | A | ✓ |
| Borda *(paper only)* | — | C 20 → truncation → A/B 16 tie | n/a |

Three counts, three answers (A, B, C) from seven ballots. Files: [star yaml](cases/bv2160_r6qc8h_star.yaml) · [plurality yaml](cases/bv2160_r6qc8h_plurality.yaml) · [frozen export](cases/bv2160_r6qc8h_bv_export.json) · mirrors: [star](cases/cases_tabulated/bv2160_r6qc8h_star_tabulated.txt), [plurality](cases/cases_tabulated/bv2160_r6qc8h_plurality_tabulated.txt).
