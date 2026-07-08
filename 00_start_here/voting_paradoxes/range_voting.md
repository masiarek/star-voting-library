# Range Voting's paradoxes — when the mean overrules the majority (§A8 worked)

*The **Range Voting (RV)** procedure: voters grade every candidate on a cardinal scale (Felsenthal uses 1–10); the highest **mean** grade wins.* Felsenthal lists RV as vulnerable to the Condorcet Winner, Condorcet Loser, Absolute Winner, Absolute Loser, and Truncation paradoxes — and notes the striking fact that, unlike every other procedure except Majority Judgment, most of RV's paradoxes need only **two candidates**. These examples stay on paper: Felsenthal's 1–10 grades don't map onto BetterVoting's 0–5 STAR ballot without changing his numbers. (For the repo's broader Range-Voting material see [00_start_here/Range_Voting](../Range_Voting/).)

**Source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A8.

## Example 23 — four paradoxes with two candidates

```
Grades (1–10)   V1   V2   V3   V4   V5    Mean
      x          2    2    2    3   10    3.8
      y          1    1    1   10    7    4.0
```

**RV elects y** (mean 4.0 > 3.8). But an absolute majority — V1, V2, V3, V5 — graded **x above y**, and an absolute majority (V1–V3) gave y the *lowest possible grade*: x is the Condorcet **and** absolute winner, y the Condorcet **and** absolute loser. One enthusiastic 10 from V4 outvotes three quiet majorities: the mean lets *intensity* overrule *count*.

**The STAR observation.** With two candidates, STAR's automatic runoff *is* the head-to-head: on these ballots the scoring round would rank y first (means), and the runoff would elect **x** 4–1. The runoff stage exists precisely to give the majority the last word after the scores speak — this example is the clearest possible illustration of why STAR is Score *Then Automatic Runoff* and not Score alone. (Not runnable on BV without altering the grades; the arithmetic above is Felsenthal's, verifiable by hand.)

## Example 24 — the Truncation paradox under RV

```
Grades (1–10)   V1   V2   V3   V4   V5   V6   V7    Mean
      x          1    1    1   10    5    4    7    4.143
      y          2    2    2    3    8    5    8    4.286
```

**RV elects y.** V4 (who graded x 10, y 3) can do better by **not grading y at all**: under the procedure's convention an ungraded candidate takes the lowest grade (1) on that ballot, dropping y's mean to 4.0 — **x wins**. Saying *less* about y served V4 better than honest grading: the [Truncation paradox](truncation.md), RV flavor. The mechanism is the same as Borda's ([BV2160](../../method_comparisons/felsenthal_paradoxes/bv2160_r6qc8h_fishburn_borda_truncation.md)): wherever an unmarked candidate scores bottom, silence is a weapon.

## What this folder takes from §A8

Two lessons travel. First, mean-based counting concentrates power in extreme grades — a single 10 can outweigh three majorities — which is why STAR keeps the runoff. Second, RV's truncation exposure comes from the ungraded-equals-lowest convention, not from cardinal ballots as such: STAR (0 is simply the scale's floor, and blanks mean 0 openly) and Approval don't reward hiding a grade the same way. Where STAR's own vulnerabilities lie, this folder shows them live instead: [BV2156 (Condorcet miss)](../../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md) and [BV2166 (participation)](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md).
