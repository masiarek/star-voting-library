# Majority Judgment's paradoxes — the median misbehaves too (§A9 worked)

*The **Majority Judgment (MJ)** procedure (Balinski & Laraki): voters grade every candidate on a common ordinal scale; the highest **median** grade wins, with an iterative tie-breaking algorithm when medians match.* Felsenthal lists MJ as vulnerable to the Condorcet Winner, Condorcet Loser, Absolute Winner, Absolute Loser, Truncation, Reinforcement, No-Show, and Twin paradoxes — the longest list of any procedure in the appendix except successive elimination. Like Range Voting, most of them need only **two candidates**. MJ has no tabulator on BetterVoting or in the LH engine, so this repo counts it with [`grade_methods_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/grade_methods_report.py), which computes the median and the Balinski–Laraki tie-break from scratch and cross-checks both against `pref_voting` on every run. In each table below, **later letters are higher grades**.

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/grade_methods_report.py method_comparisons/felsenthal_paradoxes/cases/mj_ex25_absolute_winner_loses.yaml
```

Examples 25, 27 and 28 are runnable case files. They keep Felsenthal's letter grades, so they are **grade-ballot files, not LH election files** — letters fit neither the engine's numeric 0–5 ballot nor BetterVoting — which is why they carry a `grades:` block instead of `ballots:` and have no `_tabulated` mirror. **Example 26 is the exception and stays prose**: its grade tables are in Felsenthal & Machover's paper and were never reproduced on this page, so there is nothing here to turn into a file. Building it would mean inventing three 101-voter regions and calling them the source's, which is not a thing this repo does.

→ **The case *for* the method, and the argument underneath it:** [Grading as a rival primitive](../scores_and_ranks/grading_as_a_rival_primitive.md) — Balinski & Laraki's claim that the preference *order* is the wrong primitive, the common-language-of-grades move that buys interpersonal comparability, the Orsay 2007 field experiment, and the 2026 study that tests the premise and rejects it. Read the case for before the paradoxes below.

**Sources:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A9 — drawing on **Felsenthal & Machover (2008)**, *"The Majority Judgement voting procedure: a critical evaluation"* (the paper that discusses MJ's paradoxes at length). Balinski & Laraki's *Majority Judgment* (2011) is the case *for* the method — see the [books list](../../method_comparisons/paradoxes_and_whoops/README.md).

## Example 25 — the absolute winner loses (Felsenthal & Machover 2008: 330)

```
Grades (A–H)    V1   V2   V3    Median
      x          B    C    H      C
      y          A    F    G      F
```

**Case:** [`mj_ex25_absolute_winner_loses.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/mj_ex25_absolute_winner_loses.yaml)

**MJ elects y** (median F > C). But an absolute majority — V1 and V3 — graded **x above y**: x is the Condorcet and absolute winner, y the Condorcet and absolute loser. Same disease as [Range Voting's Example 23](range_voting.md), median flavor: one middling grade (V2's F for y) placed just right outweighs two majorities.

This is the example that matters most for the method's own argument. The median was proposed *because* a mean can be dragged by one extreme grade — and that is true. It is also beside the point: a median can still be **set** by a single well-placed grade, and here it is. Read the case for the method first at [Grading as a rival primitive](../scores_and_ranks/grading_as_a_rival_primitive.md), then this.

## Example 26 — Reinforcement failure (Felsenthal & Machover 2008: 327)

Three regions of 101 voters grade x and y on A–D. In every region the two candidates have *equal median grades*, so Balinski & Laraki's tie-breaking algorithm decides (2, 7, and 2 iterations): **y wins all three regions**. Merge the regions (13 iterations): **x wins**. Three electorates that each chose y produce a union that chooses x — the [Reinforcement paradox](multiple_districts.md), median flavor.

**No case file, deliberately.** The grade tables live in Felsenthal & Machover's paper and were never reproduced on this page, so there is nothing here to make runnable — and inventing three 101-voter regions to fit the stated iteration counts would be fabricating a source's data. When the tables are to hand this becomes a file like the others. The iterative tie-break is what makes the failure possible and what makes it opaque; `grade_methods_report.py` prints each iteration for the examples it *can* count, which is the nearest available view of the mechanism.

## Example 27 — No-Show and Twin (Felsenthal & Machover 2008: 329)

```
Grades (A–F)    V1   V2   V3   V4   V5   V6   V7    Median
      x          A    A    A    D    E    E    F       D
      y          B    B    B    C    F    F    F       C
```

**Case:** [`mj_ex27_noshow_twin.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/mj_ex27_noshow_twin.yaml)

**MJ elects x** (median D > C). V1 and V2 prefer y (they graded x the *lowest* grade). If they **abstain**, the five remaining grades are A,D,E,E,F (median E) vs y's B,C,F,F,F (median F) — **y wins**. Staying home gives them their preference: the [No-Show paradox](no_show.md). Read in reverse it's the Twin paradox: V3 votes alone, y wins; V3's two *twins* join, and x wins.

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/grade_methods_report.py --abstain V1,V2 method_comparisons/felsenthal_paradoxes/cases/mj_ex27_noshow_twin.yaml
```

`--abstain` removes voters outright, which is a different lever from the `--ungrade` used two examples down: abstaining changes the **denominator**, and that is precisely what moves a median.

## Example 28 — the Truncation paradox

```
Grades (A–J)    V1   V2   V3   V4   V5   V6   V7    Median
      x          A    A    A    J    E    D    G       D
      y          B    B    B    C    H    E    H       C
```

**Case:** [`mj_ex28_truncation.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/mj_ex28_truncation.yaml)

**MJ elects x.** V6 (x: D, y: E — prefers y) grades **only y**: x's V6-grade becomes the lowest (A), x's median collapses from D to A, and **y wins**. Grading less got V6 more: the [Truncation paradox](truncation.md), driven by the same ungraded-equals-lowest convention as [RV's Example 24](range_voting.md).

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/grade_methods_report.py --ungrade x/V6 method_comparisons/felsenthal_paradoxes/cases/mj_ex28_truncation.yaml
```

The size of that collapse is the thing to watch. A mean moves smoothly when one grade changes; a median **jumps** — one blank drops x four positions down the scale, because it changes *which* grade sits in the middle rather than nudging an average. That sensitivity is the flip side of the robustness the median is chosen for.

## What this folder takes from §A9

The median was proposed to tame the mean's intensity problem, and these examples show the cure inherits the disease: medians still let a well-placed single grade overrule an absolute majority (Ex.25), and the tie-break machinery adds a reinforcement failure that is genuinely hard to see coming (Ex.26). MJ's paradoxes need only two candidates — no cycle, no elimination order — which is Felsenthal & Machover's core critique: the pathologies live in the grading arithmetic itself.
