# The successive-elimination procedure — one agenda, five paradoxes (worked tables)

*The **successive elimination** procedure (the parliamentary/amendment procedure): candidates meet in pairwise majority votes in a fixed agenda order; each round's loser is eliminated and the winner meets the next candidate; the last survivor wins.* This page covers Felsenthal's §A4 (Examples 9–12) as **worked tables only** — neither BetterVoting nor the LH engine implements this procedure, so there are no live elections or runnable YAMLs; the pairwise counts below can be checked against any of the repo's pairwise matrices by hand.

**Source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A4. Felsenthal lists the procedure as vulnerable to the Pareto-dominated, Reinforcement, No-Show, Twin, Truncation, SCC, and Path Independence paradoxes.

## Example 9 — a Pareto-dominated winner (and three more paradoxes from the same 11 voters)

```
No. of voters    Preference ordering
      3          a > b > c > d
      2          c > a > b > d
      1          c > d > a > b
      5          d > a > b > c
```

The social preference ordering is **cyclical** (b > c > d > a > b) — a necessary condition for electing a Pareto-dominated candidate here. With the agenda *d vs a*, *winner vs c*, *winner vs b*: d beats a **6:5**, c beats d **6:5**, b beats c **8:3** — **b wins**. But *every* voter prefers **a** to b: a Pareto-dominated candidate is elected ([`pareto`](../YAML_test_case_index/PARADOX_index.md); the Approval flavor of the same paradox is runnable: [Felsenthal Ex.6](../../method_comparisons/felsenthal_paradoxes/felsenthal_ex6_pareto.md)).

The same 11 voters yield three more paradoxes by changing one datum each: **SCC** — delete the non-winner d and a beats c 8:3, then b 11:0: a wins, so d's presence decided the election. **No-Show** — if two of the d-first voters stay home, a becomes the Condorcet winner and wins; both abstainers prefer a to b ([no_show.md](no_show.md)). **Path independence** — reorder the agenda to *a vs b*, *winner vs c*, *winner vs d*: a beats b 11:0, a beats c 8:3, then **d beats a 6:5** and wins. Same ballots, different agenda, different winner: under a cycle the agenda-setter, not the electorate, picks the winner.

## Example 10 — Reinforcement failure

District I (3 voters): `a>b>c>d`, `b>d>c>a`, `d>c>a>b`. District II (1 voter): `c>d>b>a`. Agenda in each district: *b vs d*, *winner vs a*, *winner vs c* — **c wins in both districts**. Amalgamate the four voters, same agenda: b beats d in round 1, b **ties** a in round 2, and if b survives, b **ties** c in round 3 — broken randomly, **b can win**, violating the Reinforcement postulate. The runnable version of this paradox (plurality-with-runoff) is the live trio [BV2147/48/49](../../method_comparisons/felsenthal_paradoxes/bv2149_byk9v2_felsenthal_ex3_reinforcement.md) ([multiple_districts.md](multiple_districts.md)).

## Example 11 — the Twin paradox (Moulin 1988b: 54)

```
No. of voters    Preference ordering
      2          a > b > c
      2          b > c > a
      1          c > a > b
      1          c > b > a
```

Agenda *a vs b*, *winner vs c*; ties break lexicographically (toward the earlier letter). Round 1: a ties b 3:3 → **a** advances; round 2: **c beats a** and wins. The single `c>b>a` voter should welcome a *twin* — another `c>b>a` voter. But with that twin added, **b becomes the Condorcet winner** and wins the procedure — and the original `c>b>a` voter prefers c (the old winner) to b: the twin's arrival made them worse off ([no_show.md](no_show.md) covers the twin's runnable runoff flavor, [BV2150/51](../../method_comparisons/felsenthal_paradoxes/bv2151_97hbpw_felsenthal_ex4_noshow.md)).

## Example 12 — the Truncation paradox

```
No. of voters    Preference ordering
      1          a > b > c > d
      1          c > b > a > d
      2          c > d > b > a
      2          d > a > b > c
```

Agenda *b vs c*, *winner vs d*, *winner vs a*; ties break toward the earlier letter. Sincere: b ties c → **b**; **d beats b**; **d beats a** — d wins, the `a>b>c>d` voter's *last* choice. Now let that voter **truncate** to just `a` (participating only where a stands): round 1 **c beats b**; round 2 **c beats d**; round 3 a ties c → **a wins**. Revealing *less* of the ballot got the voter their *first* choice instead of their last — the Truncation paradox ([`truncation`](../YAML_test_case_index/PARADOX_index.md); its IRV flavor lurks in [Whoops_05](../../method_comparisons/paradoxes_and_whoops/Whoops_05_brams_many_pathologies_irv.md)).

## Why this procedure matters anyway

Successive elimination is not a ballot-box method — it *is* how legislatures vote on amendments (compare the killer-amendment story in the [Tizkova overview](https://tereza-tizkova.medium.com/paradoxes-of-voting-systems-c9a647fc7ead)). Its paradoxes are therefore not hypothetical: agenda power, strategic absence, and strategic silence are standing features of parliamentary practice. For ballot-box methods, every paradox on this page has a runnable cousin elsewhere in this folder.
