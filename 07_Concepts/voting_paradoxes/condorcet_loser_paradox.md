# The Condorcet loser paradox

*A **Condorcet loser** loses to every other candidate head-to-head. The **Condorcet loser paradox** is a voting method electing that candidate anyway — the one contender the electorate pairwise-rejects against all comers.* (A **simple** paradox in Felsenthal's taxonomy: no hypothetical change is needed; the ballots as cast do it.)

→ Glossary: [`Condorcet loser`](../GLOSSARY.md) · Felsenthal's taxonomy: [README](README.md)

## The 7-voter demonstration

In [BV2144 — Felsenthal Example 1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md), Ana loses to Bo 3–4 and to Cal 3–4 — Ana is the Condorcet loser. Choose-One elects **Ana** anyway, because Ana's 3 first-choice votes top Bo's 2 and Cal's 2. Every voter who didn't put Ana first put Ana *last*, and the count never looks.

In the same election Ana is also the **absolute loser** (a majority ranks Ana last) — the stronger form, with [its own page](absolute_loser_paradox.md). Every absolute loser is a Condorcet loser; the reverse doesn't hold.

## Which methods are vulnerable

| Method | Vulnerable? | Why |
|---|---|---|
| Choose-One (Plurality) | Yes | A cohesive minority's favorite can top a split majority — [BV2144](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) |
| Approval | Yes (possible) | Approval counts don't consult pairwise preferences |
| RCV-IRV | No | The final round is a head-to-head; a Condorcet loser loses it |
| STAR | No | Same shield: the automatic runoff is a head-to-head the Condorcet loser cannot win |
| Ranked Robin | No | A Condorcet loser has zero pairwise wins and can never have the most |

This is a paradox where RCV-IRV genuinely does well — the repo's critiques of IRV (center squeeze, exhausted ballots, non-monotonicity) are about *other* failures, and fair treatment means saying so. See [reading_these_fairly.md](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md).

## Why it matters

Electing a Condorcet loser is the clearest possible "wrong winner": for *every* alternative individually, a majority of expressed preferences said "not this one." Choose-One is the only widely used method that can do it — and it does it with just 7 voters.
