# BV2146 — Felsenthal Example 2 (2 of 2): more support makes the winner lose

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/krk2px) · **[results ↗](https://bettervoting.com/krk2px/results)** (election `krk2px`).

The same election as [BV2145](bv2145_6fj2kg_felsenthal_ex2.md), with exactly one change: **two voters raise Ben** from `Cleo>Ben>Ada` to `Ben>Cleo>Ada`. Strictly more support for Ben, everything else held constant — and Ben, who won part 1, now **loses**. That is the lack-of-monotonicity ("more-is-less") paradox, Felsenthal's model *conditional* paradox, confirmed live on BetterVoting.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A2, **Example 2** (continued): *"Now suppose that, ceteris paribus, the two voters whose preference ordering is c > b > a change it to b > c > a thereby increasing b's support."*

## The one changed datum

```
No. of voters    BV2145 (before)         BV2146 (after)
      3          Ada  > Ben  > Cleo      Ada  > Ben  > Cleo
      2          Ada  > Cleo > Ben       Ada  > Cleo > Ben
      4          Ben  > Ada  > Cleo      Ben  > Ada  > Cleo
      2          Ben  > Cleo > Ada       Ben  > Cleo > Ada
      4          Cleo > Ada  > Ben       Cleo > Ada  > Ben
      2          Cleo > Ben  > Ada  →→→  Ben  > Cleo > Ada   (the raise)
```

First choices go from Ada 5, Ben 6, Cleo 6 to **Ada 5, Ben 8, Cleo 4**. So the runoff procedure now eliminates **Cleo** instead of Ada — and Ada, the Condorcet winner, beats Ben head-to-head **9–8**. Ben's reward for gaining two first-choice votes is losing the election he'd won.

## Why this is the monotonicity failure

A method is *monotone* if ranking a candidate higher can never hurt them. Here the raise changed the **elimination order** — the eliminated candidate's transfers decide the final pair, so who gets eliminated *is* the election. This is IRV-specific machinery: the same raise leaves Ranked Robin and STAR unmoved (both elect Ada before and after), because neither depends on an elimination order. Compare the repo's standalone pair ([monotonicity set](../monotonicity/cases/cases_pages/monotonicity_irv_after.md)) — same paradox, different construction.

Note the composite lesson of the pair: in BV2145 the runoff robbed the *Condorcet winner*; here it punishes *Ben* for being supported more. The procedure fails both its own winner and its own logic.

## View 1 — BetterVoting

Live results: **[bettervoting.com/krk2px/results ↗](https://bettervoting.com/krk2px/results)**. BV elects **Ada** (IRV), **Ada** (Ranked Robin), **Ada** (STAR) — matching LH on all three, no tiebreaks.

## View 2 — LH engine

Runoff/IRV race ([bv2146_krk2px_irv.yaml](cases/bv2146_krk2px_irv.yaml)):

```
 Tabulating 17 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ben                8  Hopeful
Ada                5  Hopeful
Cleo               4  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Ada                9  Elected
Ben                8  Rejected
Cleo               0  Rejected

Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Ada
```

Ranked Robin ([bv2146_krk2px_ranked_robin.yaml](cases/bv2146_krk2px_ranked_robin.yaml)): the raise only swaps Ben/Cleo on two ballots, so Ada still beats Ben 9–8 and Cleo 9–8 — **Ada**, unchanged. STAR ([bv2146_krk2px_star.yaml](cases/bv2146_krk2px_star.yaml)): Ben rises 51 → 55, Cleo falls 49 → 45, Ada stays 53; the finalist pair changes to Ben/Ada but **Ada still wins the runoff 9–8** — no more-is-less. Full detail: [IRV mirror](cases/cases_tabulated/bv2146_krk2px_irv_tabulated.txt) · [RR mirror](cases/cases_tabulated/bv2146_krk2px_ranked_robin_tabulated.txt) · [STAR mirror](cases/cases_tabulated/bv2146_krk2px_star_tabulated.txt).

## Agreement

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| Runoff (IRV) | Ada | Ada | ✓ |
| Ranked Robin | Ada | Ada | ✓ |
| STAR (ranks→scores) | Ada | Ada | ✓ |

Frozen export: [bv2146_krk2px_bv_export.json](cases/bv2146_krk2px_bv_export.json) · Part 1: [BV2145 — the Condorcet winner eliminated](bv2145_6fj2kg_felsenthal_ex2.md) · Teaching page: [non_monotonicity.md](../../00_start_here/voting_paradoxes/non_monotonicity.md).
