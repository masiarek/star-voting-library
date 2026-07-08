# Majority Judgment's paradoxes — the median misbehaves too (§A9 worked)

*The **Majority Judgment (MJ)** procedure (Balinski & Laraki): voters grade every candidate on a common ordinal scale; the highest **median** grade wins, with an iterative tie-breaking algorithm when medians match.* Felsenthal lists MJ as vulnerable to the Condorcet Winner, Condorcet Loser, Absolute Winner, Absolute Loser, Truncation, Reinforcement, No-Show, and Twin paradoxes — the longest list of any procedure in the appendix except successive elimination. Like Range Voting, most of them need only **two candidates**. MJ has no tabulator on BetterVoting or in the LH engine, so §A9 stays on paper. In each table below, **later letters are higher grades**.

**Sources:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A9 — drawing on **Felsenthal & Machover (2008)**, *"The Majority Judgement voting procedure: a critical evaluation"* (the paper that discusses MJ's paradoxes at length). Balinski & Laraki's *Majority Judgment* (2011) is the case *for* the method — see the [books list](../../method_comparisons/paradoxes_and_whoops/README.md).

## Example 25 — the absolute winner loses (Felsenthal & Machover 2008: 330)

```
Grades (A–H)    V1   V2   V3    Median
      x          B    C    H      C
      y          A    F    G      F
```

**MJ elects y** (median F > C). But an absolute majority — V1 and V3 — graded **x above y**: x is the Condorcet and absolute winner, y the Condorcet and absolute loser. Same disease as [Range Voting's Example 23](range_voting.md), median flavor: one middling grade (V2's F for y) placed just right outweighs two majorities.

## Example 26 — Reinforcement failure (Felsenthal & Machover 2008: 327)

Three regions of 101 voters grade x and y on A–D. In every region the two candidates have *equal median grades*, so Balinski & Laraki's tie-breaking algorithm decides (2, 7, and 2 iterations): **y wins all three regions**. Merge the regions (13 iterations): **x wins**. Three electorates that each chose y produce a union that chooses x — the [Reinforcement paradox](multiple_districts.md), median flavor. (Grade tables in the source; the iterative tie-break is what makes the failure possible and what makes it opaque.)

## Example 27 — No-Show and Twin (Felsenthal & Machover 2008: 329)

```
Grades (A–F)    V1   V2   V3   V4   V5   V6   V7    Median
      x          A    A    A    D    E    E    F       D
      y          B    B    B    C    F    F    F       C
```

**MJ elects x** (median D > C). V1 and V2 prefer y (they graded x the *lowest* grade). If they **abstain**: x's median drops to... the five remaining grades are A,D,E,E,F (median E) vs y's B,C,F,F,F (median F) — **y wins**. Staying home gives them their preference: the [No-Show paradox](no_show.md). Read in reverse it's the Twin paradox: V3 votes alone, y wins; V3's two *twins* join, and x wins.

## Example 28 — the Truncation paradox

```
Grades (A–J)    V1   V2   V3   V4   V5   V6   V7    Median
      x          A    A    A    J    E    D    G       D
      y          B    B    B    C    H    E    H       C
```

**MJ elects x.** V6 (x: D, y: E — prefers y) grades **only y**: x's V6-grade becomes the lowest (A), x's median collapses from D to A, and **y wins**. Grading less got V6 more: the [Truncation paradox](truncation.md), driven by the same ungraded-equals-lowest convention as [RV's Example 24](range_voting.md).

## What this folder takes from §A9

The median was proposed to tame the mean's intensity problem, and these examples show the cure inherits the disease: medians still let a well-placed single grade overrule an absolute majority (Ex.25), and the tie-break machinery adds a reinforcement failure that is genuinely hard to see coming (Ex.26). MJ's paradoxes need only two candidates — no cycle, no elimination order — which is Felsenthal & Machover's core critique: the pathologies live in the grading arithmetic itself.
