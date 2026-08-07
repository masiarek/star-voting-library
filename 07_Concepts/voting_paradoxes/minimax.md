# Minimax (Simpson-Kramer) — the "smallest worst loss" rule and its paradoxes (§A10 worked)

*The **Condorcet procedure**, a.k.a. **Minimax** or the **Simpson-Kramer rule**: elect the Condorcet winner when one exists; otherwise elect the candidate whose **worst pairwise loss** is smallest.* A genuine Condorcet method — so it never misses a Condorcet winner — but its cycle-breaking rule buys that guarantee at a price: Felsenthal lists Minimax as vulnerable to the Condorcet Loser, Absolute Loser, No-Show, Twin, Truncation, Reinforcement, and SCC paradoxes. Minimax has no tabulator on BetterVoting or in the LH engine (LH's [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) is **Copeland** — most pairwise *wins* — a different cycle-breaker), so this repo counts it with [`minimax_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/minimax_report.py), cross-checked against `pref_voting` on every run. Example 29 is backed by the live election **[BV2167](../../method_comparisons/felsenthal_paradoxes/bv2167_f3dxq9_minimax_absolute_loser.md)**; **every example below is a runnable case file** — the ballots are real YAML, not prose.

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/minimax_report.py method_comparisons/felsenthal_paradoxes/cases/minimax_ex30_noshow_before.yaml
```

**"Worst loss" is measured three ways, and the rule is ambiguous until you pick one.** *Winning votes* (how many backed the winning side) is Felsenthal's convention and what his tables print; *margins* (winner minus loser) is `pref_voting`'s default; *pairwise opposition* counts votes against whether or not the pair was lost. On an odd electorate with no pairwise ties the first two cannot disagree, which covers every example here except the 14-voter amalgamation in Example 32. The report prints both columns and says whether they agree.

**Source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A10, Examples 29–33.

> **Candidate-count fine print (important).** Every damning example below uses **four candidates**. Restrict to **exactly three** and the verdict flips: Brandt, Dong & Peters (2024) prove that at three candidates, **refinements of maximin (leximin, Nanson) are *uniquely* immune to the no-show paradox** among homogeneous Condorcet extensions, and immune to reinforcement for ≤ 7 voters — the small case where [Moulin's impossibility](no_show.md) hasn't yet applied. Minimax looks paradox-prone in the general (4+) case and uniquely well-behaved in the three-candidate case; both are true. See [Condorcet-Consistent Choice Among Three Candidates](../topics/condorcet/three_candidate_maximin.md).

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

**Cases:** [before — all 19 vote](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/minimax_ex30_noshow_before.md) → [after — three stay home](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/minimax_ex30_noshow_after.md)

| Voters | Ranking |
|---:|---|
| 5 | D > B > C > A |
| 4 | B > C > A > D |
| 3 | A > D > C > B |
| 3 | A > D > B > C |
| 4 | C > A > B > D |

19 voters, four candidates; the social ordering is cyclical (C > A > D > B > C), so Minimax reaches its second clause. Worst losses: A 13, **B 11**, C 12, D 14 → **B elected**. Now three of the four `C>A>B>D` voters stay home: worst losses become **A 10**, B 11, C 12, D 11 → **A elected** — which the absent voters prefer to B: the [No-Show paradox](no_show.md). Read forward it's the Twin paradox: with one such voter, A wins; when the three "twin brothers" join, B does.

## Example 31 — Truncation (Nurmi, private communication 24.2.2010)

**Case:** [the four `C>A>B>D` voters cut to their top two](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/minimax_ex31_truncation.md)

Same 19 voters as Example 30, but the four `C>A>B>D` voters state **only their top two**, `C>A`, saying nothing about B versus D.

**This is the one example on the page whose result depends on a convention, and the repo does not reproduce Felsenthal's winner.** He applies the **equal-probability** convention — an unstated pair counts ½ a vote to each side — which inflates B's worst loss from 11 to 13 and hands the smallest (12) to **C**, the truncators' *first* choice: the [Truncation paradox](truncation.md). This repo, the LH engine and BetterVoting all use the other convention: a voter who said nothing about B-vs-D gets **no say** in B-vs-D. Under that reading the pair simply drops out, B's worst loss stays 11, and Minimax still elects **B** — no paradox at all.

Both readings are defensible; quoting the result without the convention that produced it is not. Run it both ways:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/minimax_report.py --equal-prob method_comparisons/felsenthal_paradoxes/cases/minimax_ex31_truncation.yaml
```

## Example 32 — Reinforcement

**Cases:** District I = Example 29's ballots ([BV2167](../../method_comparisons/felsenthal_paradoxes/bv2167_f3dxq9_minimax_absolute_loser.md)) · [District II](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/minimax_ex32_district2.md) · [amalgamated](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/minimax_ex32_amalgamated.md)

District I = Example 29's 11 voters → **D wins** (above). District II = 3 voters (2 D>A>B>C, 1 B>A>C>D) → D is the absolute winner → **D wins**. Amalgamate all 14 and the matrix goes nearly flat — four of the six pairs are dead heats at 7–7 — leaving **B and D both unbeaten and tied** on a worst opposition of 7. Minimax has no further clause, so D's two clean district wins dissolve into a coin flip with a candidate who won neither district: the [Reinforcement paradox](multiple_districts.md).

The even electorate is doing real work here. With 14 voters a pair *can* draw; on Felsenthal's odd-numbered examples none can, which is also why the winning-votes and margins conventions never come apart there.

## Example 33 — SCC (adapted from Fishburn 1974: 540)

**Case:** [7 voters, then B drops out](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/minimax_ex33_scc.md)

| Voters | Ranking |
|---:|---|
| 3 | D > C > B > A |
| 2 | A > D > C > B |
| 2 | B > A > D > C |

Cyclical (A > D > C > B > A). Worst losses: A 5, B 5, C 7, **D 4** → **D elected**. Now B — a loser, four first places short of contention — drops out: **A becomes the Condorcet winner**, first on 4 of 7 ballots, and wins outright. A loser's exit flipped the winner: [SCC](spoiler_scc.md). Recount it yourself with `--drop B`:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/minimax_report.py --drop B method_comparisons/felsenthal_paradoxes/cases/minimax_ex33_scc.yaml
```

## What this folder takes from §A10

Minimax measures candidates only by their *worst moment*. In a cycle that rewards the universally-narrowly-beaten — Example 29's D is the sharpest "wrong winner" in the whole appendix, and Choose-One agrees with it. Copeland (Ranked Robin) is immune to *that* failure (D has zero wins and can never top the win count), which is a concrete illustration of why cycle-breaking rules differ in kind, not just in taste — compare [cycle_resolution.md](../../05_Ranked_Robin/01_Learn/cycle_resolution.md) and the [RR tiebreak study](../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md). The conditional paradoxes (30–33) are the familiar family: any rule keyed to a single summary statistic of the pairwise matrix can be steered by absence, silence, or district lines.
