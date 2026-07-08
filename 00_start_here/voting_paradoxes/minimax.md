# Minimax (Simpson-Kramer) — the "smallest worst loss" rule and its paradoxes (§A10 worked)

*The **Condorcet procedure**, a.k.a. **Minimax** or the **Simpson-Kramer rule**: elect the Condorcet winner when one exists; otherwise elect the candidate whose **worst pairwise loss** is smallest.* A genuine Condorcet method — so it never misses a Condorcet winner — but its cycle-breaking rule buys that guarantee at a price: Felsenthal lists Minimax as vulnerable to the Condorcet Loser, Absolute Loser, No-Show, Twin, Truncation, Reinforcement, and SCC paradoxes. Minimax has no tabulator on BetterVoting or in the LH engine (LH's [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) is **Copeland** — most pairwise *wins* — a different cycle-breaker; `pref_voting` can cross-check Minimax), so §A10 is worked here, with Example 29 backed by the live election **[BV2167](../../method_comparisons/felsenthal_paradoxes/bv2167_f3dxq9_minimax_absolute_loser.md)**.

**Source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A10, Examples 29–33.

## Example 29 — Minimax elects the Condorcet AND absolute loser (live: [BV2167](../../method_comparisons/felsenthal_paradoxes/bv2167_f3dxq9_minimax_absolute_loser.md))

```
No. of voters    Preference ordering
      2          D > A > C > B
      3          D > B > A > C
      3          C > B > A > D
      1          B > A > C > D
      2          A > C > B > D
```

A, B, C form a top cycle (B>A 7–4, A>C 8–3, C>B 7–4) and **D loses every matchup 5–6** — the Condorcet loser, and the absolute loser (6 of 11 rank D last). Minimax elects **D**: worst-loss margins are A 7, B 7, C 8, **D 6** — losing to *everyone narrowly* beats winning some and losing one badly. Live on the same ballots: STAR → B, Choose-One → **D** (5 first choices — agreeing with Minimax).

## Example 30 — No-Show and Twin (Hannu Nurmi, private communication 22.2.2010)

19 voters, four candidates (5 d>b>c>a, 4 b>c>a>d, 3 a>d>c>b, 3 a>d>b>c, 4 c>a>b>d); the social ordering is cyclical (c>a>d>b>c). Worst losses: a 13, **b 11**, c 12, d 14 → **b elected**. Now three of the four `c>a>b>d` voters stay home: worst losses become **a 10**, b 11, c 12, d 11 → **a elected** — which the absent voters prefer to b: the [No-Show paradox](no_show.md). Read forward it's the Twin paradox: with one such voter, a wins; when the three "twin brothers" join, b does.

## Example 31 — Truncation (Nurmi, private communication 24.2.2010)

Same 19 voters as Example 30, but the four `c>a>b>d` voters state **only their top two** (c and a). Under the equal-probability convention for their unstated b-vs-d preference, the outranking matrix shifts and **c's worst loss (12) becomes the smallest — c elected**, the truncators' *first* choice, instead of b. Saying less about the bottom of the ballot promoted the top: the [Truncation paradox](truncation.md).

## Example 32 — Reinforcement

District I = Example 29's 11 voters → **d wins** (above). District II = 3 voters (2 d>a>b>c, 1 b>a>c>d) → d is the absolute winner → **d wins**. Amalgamate all 14: the worst losses of b and d **tie at 7**, so Minimax must draw lots between them — d's two clean district wins dissolve into a coin flip: the [Reinforcement paradox](multiple_districts.md).

## Example 33 — SCC (adapted from Fishburn 1974: 540)

7 voters (3 d>c>b>a, 2 a>d>c>b, 2 b>a>d>c); cyclical (a>d>c>b>a). Worst losses: a 5, b 5, c 7, **d 4** → **d elected**. Now b — a loser — drops out: **a becomes the absolute winner** (first on 4 of 7 ballots) and wins. A loser's exit flipped the winner: [SCC](spoiler_scc.md).

## What this folder takes from §A10

Minimax measures candidates only by their *worst moment*. In a cycle that rewards the universally-narrowly-beaten — Example 29's D is the sharpest "wrong winner" in the whole appendix, and Choose-One agrees with it. Copeland (Ranked Robin) is immune to *that* failure (D has zero wins and can never top the win count), which is a concrete illustration of why cycle-breaking rules differ in kind, not just in taste — compare [cycle_resolution.md](../RCV_Ranked_Robin/cycle_resolution.md) and the [RR tiebreak study](../RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md). The conditional paradoxes (30–33) are the familiar family: any rule keyed to a single summary statistic of the pairwise matrix can be steered by absence, silence, or district lines.
