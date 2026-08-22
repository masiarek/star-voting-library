---
tags:
  - criteria
  - multi-winner
  - theory
---

# Consistency — two electorates that agree should keep agreeing

**Level: 301 · deep dive**

**One line:** the shallowest-looking column in Table 3.1 is the deepest, because consistency doesn't merely *describe* a class of rules — it **defines** one, and the four rules that pass are exactly the ones you can write as a sum of per-voter scores.

## The definition

> **Definition 3.4.** An ABC rule `R` satisfies **consistency** if for every `k ≥ 1` and disjoint profiles `A`, `A′`: if `R(A,k) ∩ R(A′,k) ≠ ∅`, then `R(A + A′, k) = R(A,k) ∩ R(A′,k)`.

In words: split the electorate in two, count each half, and look at the committees that won in **both**. Consistency says the merged election must elect precisely those, and nothing else. It is the multi-winner form of the Smith–Young axiom that characterises single-winner scoring rules — the same property this repo demonstrates for STAR in [Two districts, one office](../../01_STAR/05_Practice/ex01_two_districts.md).

## Monroe's failure, worked

Two profiles, two seats. Profile `A` (4 voters):

```text
{a,y}   {a,y}   {b,y}   {b,y}
```

Profile `A′` (12 voters):

```text
{y}  {a}  {a,x} {a,x} {a,x} {a,x}   {y}  {b,y}  {b,x} {b,x} {b,x} {b,x}
```

Monroe's winners:

| electorate | winning committees | Monroe-score |
|---|---|:--:|
| `A` | `{a,b}`, `{a,y}`, `{b,y}` | 4 |
| `A′` | `{a,b}` | 10 |
| **shared** | **`{a,b}`** | — |
| `A + A′` | **`{x,y}`** (score 15) — `{a,b}` scores only 14 | — |

Both halves could elect `{a,b}`; merged, Monroe elects `{x,y}` and `{a,b}` is not even winning. Replayed by the checker:

```text
Consistency (Def. 3.4)
  [REPRODUCED] Monroe   Example 3.2   both elect {a,b}; merged elects {x,y}
```

The mechanism is the same one that costs Monroe [Pareto efficiency](pareto_efficiency.md): its score depends on **partitioning voters into equal constituencies**, and a partition of the merged electorate is not the union of partitions of the halves. Any rule whose score is not a plain sum over voters is exposed here.

## The result that makes this column matter

Consistency is not just another row of ticks. It is one of five axioms that **pin down a whole class of rules**:

> **Theorem 3.2** (Lackner & Skowron). An ABC ranking rule is an **ABC scoring rule** if and only if it satisfies anonymity, neutrality, consistency, weak efficiency, and continuity.

An **ABC scoring rule** (Definition 3.5) gives each voter a score `f(|A(i) ∩ W|, |A(i)|)` — how many of her approved candidates are seated, and how many she approved in total — and elects the committee maximising the sum. Since anonymity, neutrality, weak efficiency and continuity are satisfied by every sensible rule, the theorem reads, practically: **consistent = summable over voters.**

That explains the entire column at a glance:

| Rule | consistent? | why |
|---|:--:|---|
| **AV**, **CC**, **PAV** | ✓ | Thiele methods — a sum of per-voter satisfactions by construction |
| **SAV** | ✓ | an ABC scoring rule that is *not* a Thiele method — its `f` depends on `|A(i)|`, the ballot's own length |
| seq-PAV, seq-CC, rev-seq-PAV, seq-Phragmén, leximax-Phragmén | ✗ | **sequential** — the outcome depends on the order seats were filled, which is not a sum over voters |
| Monroe, Greedy Monroe | ✗ | scored by a **partition** of voters into constituencies |
| Method of Equal Shares | ✗ | scored by a **budget process** over rounds |
| MAV | ✗ | scored by the **worst** voter, and a max is not a sum |

**SAV is the interesting entry**, and it is why Definition 3.5's `f` takes two arguments rather than one. A Thiele method may only look at how many of your approved candidates won. SAV also looks at how many you approved, dividing your single vote among your marks — which is outside the Thiele family but still a plain per-voter sum, so it stays consistent. The class of consistent rules is strictly larger than the Thiele class, and SAV is the witness.

## The honest reading

- **Consistency is a real virtue and a weak one.** It is worth having, and it holds for rules with very different characters — utilitarian AV, egalitarian CC, proportional PAV. It cannot tell you which one to use, so it belongs in an argument about *form*, never in an argument about *fairness*.
- **Failing it is not disqualifying.** Every sequential rule fails, and sequential rules are what actually gets deployed, because [the optimising versions are NP-hard](computational_complexity.md). seq-PAV is PAV's practical stand-in and it is inconsistent; that is the price of computability, and it is a price the field pays knowingly.
- **The characterisation is the transferable idea.** "Which axioms force a rule into a known algebraic form" is the shape of the deepest results in social choice — [May's theorem](../../07_Concepts/topics/mays_theorem.md), [Arrow](../../07_Concepts/topics/arrow_theorem_and_star.md), Smith–Young. Theorem 3.2 is that shape, for committees.

## Reproduce it

```bash
.venv/bin/python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --verbose
```

The consistency section replays Example 3.2 — the three Monroe counts above, computed from the profiles rather than quoted.

---

**Related:** [the table](README.md) · [support monotonicity](support_monotonicity.md) — the previous column · [inclusion-strategyproofness](inclusion_strategyproofness.md) — the next · consistency for a single-winner method → [Two districts, one office](../../01_STAR/05_Practice/ex01_two_districts.md) · [Thiele methods](../01_Learn/Multiwinner_Approval/thiele_methods.md) · [SAV](../01_Learn/Multiwinner_Approval/satisfaction_approval_voting.md).
