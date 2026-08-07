# Range Voting's paradoxes — when the mean overrules the majority (§A8 worked)

> **New to Range Voting? Start with the method itself → [Range / Score Voting](../../06_Other/Range/concepts/range_voting.md).** That page shows the ballot (with pictures of how voters mark it), the one-line count, the pros and cons, and where Range sits in the scored family **Approval → Range → STAR**. *This* page assumes all that and goes straight to where the mean misbehaves.

*The **Range Voting (RV)** procedure: voters grade every candidate on a cardinal scale (Felsenthal uses 1–10); the highest **mean** grade wins.* Felsenthal lists RV as vulnerable to the Condorcet Winner, Condorcet Loser, Absolute Winner, Absolute Loser, and Truncation paradoxes — and notes the striking fact that, unlike every other procedure except Majority Judgment, most of RV's paradoxes need only **two candidates**. (More of the repo's Range material: the [concept folder](../../06_Other/Range/concepts/README.md), its [glossary](../../06_Other/Range/concepts/glossary_range.md), and the [Range tabulation engine](../../06_Other/Range/Range_tabulation_engine/README.md).)

Both examples are **runnable case files**, counted by [`grade_methods_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/grade_methods_report.py) and cross-checked against `pref_voting` on every run:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/grade_methods_report.py method_comparisons/felsenthal_paradoxes/cases/range_ex23_mean_overrules_majority.yaml
```

They keep Felsenthal's 1–10 grades rather than being rescaled, so they are **grade-ballot files, not LH election files** — the engine's YAML path validates scores against STAR's 0–5 and BetterVoting's ballot is 0–5 too, and rescaling would change his numbers. That is why these carry a `grades:` block instead of `ballots:`, and why they have no `_tabulated` mirror: the count lives here and in the tool.

**Source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A8.

## Example 23 — four paradoxes with two candidates

| Grades (1–10) | V1 | V2 | V3 | V4 | V5 | Mean |
|---|---:|---:|---:|---:|---:|---:|
| **x** | 2 | 2 | 2 | 3 | 10 | 3.8 |
| **y** | 1 | 1 | 1 | 10 | 7 | **4.0** |

**RV elects y** (mean 4.0 > 3.8). But an absolute majority — V1, V2, V3, V5 — graded **x above y**, and an absolute majority (V1–V3) gave y the *lowest possible grade*: x is the Condorcet **and** absolute winner, y the Condorcet **and** absolute loser. One enthusiastic 10 from V4 outvotes three quiet majorities: the mean lets *intensity* overrule *count*.

**The STAR observation.** With two candidates, STAR's automatic runoff *is* the head-to-head: on these ballots the scoring round would rank y first (means), and the runoff would elect **x** 4–1. The runoff stage exists precisely to give the majority the last word after the scores speak — this example is the clearest possible illustration of why STAR is Score *Then Automatic Runoff* and not Score alone.

**Case:** [`range_ex23_mean_overrules_majority.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/range_ex23_mean_overrules_majority.yaml). The report finds all four paradoxes from the grades alone — it computes the head-to-head (x above y on 4 of 5 ballots), names x the Condorcet winner and y the Condorcet loser, flags that Range elects the Condorcet loser, and detects y as the absolute loser on 3 of 5 bottom grades. Worth noting what it also shows: on *this* profile **Majority Judgment elects x**, the majority's choice. The median gets Example 23 right and fails on its own examples instead — see [Ex.25](majority_judgment.md).

## Example 24 — the Truncation paradox under RV

| Grades (1–10) | V1 | V2 | V3 | V4 | V5 | V6 | V7 | Mean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **x** | 1 | 1 | 1 | 10 | 5 | 4 | 7 | 4.143 |
| **y** | 2 | 2 | 2 | 3 | 8 | 5 | 8 | **4.286** |

**RV elects y.** V4 (who graded x 10, y 3) can do better by **not grading y at all**: under the procedure's convention an ungraded candidate takes the lowest grade (1) on that ballot, dropping y's mean to 4.0 — **x wins**. Saying *less* about y served V4 better than honest grading: the [Truncation paradox](truncation.md), RV flavor. The mechanism is the same as Borda's ([BV2160](../../method_comparisons/felsenthal_paradoxes/bv2160_r6qc8h_fishburn_borda_truncation.md)): wherever an unmarked candidate scores bottom, silence is a weapon.

**Case:** [`range_ex24_truncation.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/range_ex24_truncation.yaml). Strike the one cell and watch it flip — the flag names a *cell*, `candidate/voter`, not a whole ballot, because V4 keeps grading x:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/grade_methods_report.py --ungrade y/V4 method_comparisons/felsenthal_paradoxes/cases/range_ex24_truncation.yaml
```

## What this folder takes from §A8

Two lessons travel. First, mean-based counting concentrates power in extreme grades — a single 10 can outweigh three majorities — which is why STAR keeps the runoff. Second, RV's truncation exposure comes from the ungraded-equals-lowest convention, not from cardinal ballots as such: STAR (0 is simply the scale's floor, and blanks mean 0 openly) and Approval don't reward hiding a grade the same way. Where STAR's own vulnerabilities lie, this folder shows them live instead: [BV2156 (Condorcet miss)](../../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md) and [BV2166 (participation)](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md).
