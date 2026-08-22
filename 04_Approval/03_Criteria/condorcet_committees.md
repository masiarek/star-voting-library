---
tags:
  - criteria
  - multi-winner
  - theory
---

# Condorcet committees — the criterion that usually has nothing to satisfy

**Level: 301 · deep dive**

**One line:** lift "beats everyone head to head" from candidates to committees and you get a condition so demanding that on approval ballots it is normally satisfied by *nothing at all* — which is why it appears in Chapter 3 as a paragraph of prose rather than a column of [Table 3.1](README.md).

## The definition

The single-winner [Condorcet winner](../../05_Ranked_Robin/01_Learn/ranked_robin.md) beats every rival candidate head to head. Darmann's committee version does the same substitution the rest of this folder does — the alternatives are **committees**, not candidates:

> A committee `W` is a **Condorcet committee** if for every other committee `W'` there is a majority of voters `V ⊆ N` (`|V| > n/2`) with `|A(i) ∩ W| > |A(i) ∩ W'|` for all `i ∈ V`.

Read the quantifiers carefully, because the sentence is easy to weaken by accident. It is **not** "a majority prefers `W` on balance," and it is **not** one majority that works against every rival. Each rival committee must be beaten by a strict majority of its own, and the comparison a voter makes is purely a count: how many of my approved candidates are seated here versus there.

## Why almost nothing qualifies

The trouble is **indifference**, and it is a property of the ballot rather than of the criterion.

Take a voter who approves `{b,c}`. Committee `{b,d}` seats one of their candidates. So does `{c,e}`. The voter has *no* preference between them — one approved winner each — and so counts toward neither majority. On approval ballots that is not an edge case, it is the normal case: most voters approve a handful of candidates, most committees seat one or two of them, and most pairwise committee comparisons are therefore a tie for most voters. A criterion that needs **more than half the electorate** to hold a *strict* preference, against **every** rival committee, is asking a ballot that records very little to settle a great deal.

The numbers on this repo's two ABC profiles say it plainly:

```text
--- Condorcet committees (Darmann; section 3.2) ---

  Example 3.1 (the Monroe/Pareto profile)
    2 x {a}  1 x {a,c}  1 x {a,d}  10 x {b,c}  10 x {b,d}
    k=2, 24 voters, 6 committees, majority needs >12
    Condorcet committee: NONE
    closest is {b,c} - its weakest majority is 10/24, against {a,b}

  Example 2.1 (the Chapter 2 running instance)
    3 x {a,b}  3 x {a,c}  2 x {a,d}  1 x {b,c,f}  1 x {e}  1 x {f}  1 x {g}
    k=4, 12 voters, 35 committees, majority needs >6
    Condorcet committee: NONE
    closest is {a,b,c,d} - its weakest majority is 2/12, against {a,b,c,e}
```

Neither profile has one — and the second is not a near miss. `{a,b,c,d}` is the committee [AV elects](../01_Learn/Multiwinner_Approval/abc_rules_spectrum.md), it is a perfectly defensible answer, and against `{a,b,c,e}` it can raise **2 voters out of 12** where it needs more than 6. The two committees differ in one seat, `d` versus `e`; exactly two voters approve `d`, one approves `e`, and the other nine are indifferent. Nine indifferent voters is the whole story.

## The complexity, and where it differs from Pareto

Deciding whether a *given* committee is a Condorcet committee is **coNP-complete**, exactly as for [Pareto optimality](pareto_efficiency.md). But the two part company on the question that matters more:

| | Does one exist? | Is *this* one it? |
|---|---|---|
| **Pareto optimal committee** | always — and one is computable in polynomial time (AV, SAV) | coNP-complete |
| **Condorcet committee** | **coNP-complete to decide** | coNP-complete |

So Pareto efficiency is a bar a rule can be *built* to clear, which is why Table 3.1 can rule on it for all thirteen rules. Condorcet-committee efficiency cannot be a column in the same sense: on most profiles there is nothing to elect, and on the profiles where something exists, no one has established which rules find it. Lackner & Skowron say so directly — to their knowledge it has not been analysed which ABC rules output a Condorcet committee when one is available. **That is an open problem stated in a 2023 textbook, not a gap in this page.**

## What it is good for

Not as a rule requirement — as a **diagnostic**. When a Condorcet committee does exist, it is an unusually strong claim: a majority prefers that committee to every alternative, one rival at a time. Finding one tells you the electorate is far less divided than approval ballots usually reveal. Finding none — the ordinary result — is a fact about how little the ballot records, not a criticism of any rule that failed to elect one.

The comparison with the single-winner case is the useful one. A [Condorcet winner](../../07_Concepts/GLOSSARY.md) among candidates exists on most real ballot sets, which is why Condorcet-efficiency is a live criterion for single-winner methods and why a [Smith set](../../07_Concepts/topics/smith_set.md) is worth computing when it isn't. Among committees the same idea inverts: existence is the rare case, so the criterion informs rather than selects.

## Reproduce it

```bash
uv run 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --condorcet
```

Add `--verbose` to print every committee with its weakest majority, rather than just the closest one — that is the view that shows how flat the field is. The search is exhaustive over all `C(m,k)` committees, so it is a *proof* of non-existence on these profiles, not a failed hunt: this is the one place in this folder where a negative result is fully established rather than merely un-refuted (compare the [ticks in Table 3.1](README.md#what-is-verified-here-and-what-is-not), which are cited, not shown).

## References

- Lackner, M. & Skowron, P. (2023), *Multi-Winner Voting with Approval Preferences*, SpringerBriefs, [doi:10.1007/978-3-031-09016-5](https://doi.org/10.1007/978-3-031-09016-5) — §3.2, closing paragraph. **Lean:** neutral / academic.
- Darmann, A., *How hard is it to tell which is a Condorcet committee?*, Mathematical Social Sciences 66(3), 2013 — the definition and both coNP-completeness results.
- Sibling pages: [Pareto efficiency](pareto_efficiency.md) · [committee monotonicity](committee_monotonicity.md) · [the folder index](README.md).
