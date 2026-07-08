# The Condorcet winner paradox

*A **Condorcet winner** beats every other candidate head-to-head. The **Condorcet winner paradox** is a voting method failing to elect that candidate — the electorate's proven pairwise favorite loses.* (Felsenthal classifies this as a **simple** paradox: the ballots as cast already produce the surprising result.)

→ Glossary: [`Condorcet winner`](../GLOSSARY.md) · Felsenthal's taxonomy: [README](README.md)

## The 7-voter demonstration

In [BV2144 — Felsenthal Example 1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md), Bo beats Ana 4–3 and Cal 5–2 head-to-head — Bo is the Condorcet winner. Choose-One counts only first choices (Ana 3, Bo 2, Cal 2) and elects **Ana**, a candidate Bo defeats outright. Seven voters are enough.

The same election's STAR race elects Bo: the runoff is itself a head-to-head, so the pairwise favorite that reaches the finalist pair wins it.

## Which methods are vulnerable

| Method | Vulnerable? | Why / where demonstrated |
|---|---|---|
| Choose-One (Plurality) | Yes | First-choice counts ignore every pairwise fact — [BV2144](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) |
| RCV-IRV | Yes | Center squeeze eliminates the broad favorite early — [BV2137 center squeeze](../../method_comparisons/center_squeeze_bv2137/bv2137_ywckmg_center_squeeze.md), [center_squeeze_irv](../../method_comparisons/center_squeeze/center_squeeze_pages/center_squeeze_irv.md), [BV2158 (Ossipoff)](../../method_comparisons/paradoxes_and_whoops/bv2158_gr72hd_ossipoff_centrist_irv.md) |
| STAR | Rarely | Usually elects the Condorcet winner, but can miss one — honestly shown in [BV2156 (STAR's miss)](../../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md) |
| Ranked Robin | No | Elects the Condorcet winner by construction whenever one exists — [ranked_robin.md](../RCV_Ranked_Robin/ranked_robin.md) |

Note the IRV-specific wording: center squeeze is a property of **IRV's elimination order**, not of ranked ballots — Ranked Robin counts the *same* ballots and finds the Condorcet winner.

## Why it matters

"Beats everyone head-to-head" is the strongest simple claim a candidate can make on the ballots. A method that can reject that candidate is rejecting the electorate's own pairwise verdicts — which is exactly what voters point to when they feel a result was wrong.
