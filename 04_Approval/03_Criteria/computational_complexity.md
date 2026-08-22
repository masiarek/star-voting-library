---
tags:
  - theory
  - multi-winner
---

# Computational complexity — why the rules people deploy are the ones that fail axioms

**Level: 301 · deep dive**

**One line:** Table 3.1's last column is the one that explains the others — the rules with the best axiomatic behaviour are mostly NP-hard, so practice runs the greedy stand-ins, and the greedy stand-ins are exactly the rules with the ✗ marks.

## The column

| P (polynomial time) | NP-hard |
|---|---|
| AV · seq-PAV · seq-CC · rev-seq-PAV · Greedy Monroe · seq-Phragmén · Method of Equal Shares · SAV | CC · PAV · Monroe · leximax-Phragmén · MAV |

The dichotomy is deliberately rough — the book treats it as a first cut and develops the real results in its Section 5.1. What matters at this level is **which side each rule sits on and why**.

The split is not arbitrary. Every NP-hard rule here is defined as *maximise (or minimise) something over all committees* — an integer program over `C(m,k)` candidate sets. Every polynomial rule is defined by a **procedure**: seat a winner, reweight, repeat. Optimising is hard; walking is cheap.

## The consequence that runs through the whole table

Read the complexity column against the others and one pattern dominates:

| | axiomatically strong | computationally cheap |
|---|---|---|
| **PAV** | strong Pareto, consistent, support monotone | ✗ NP-hard |
| **seq-PAV** | ✗ not Pareto, not consistent, only `cand` | ✓ P |

seq-PAV *is* PAV's deployed stand-in — greedily seat whoever adds most to the PAV score, never revisit. Everything seq-PAV loses relative to PAV, it loses **because** it is sequential: order-dependence is what breaks consistency, and irrevocability is what breaks Pareto efficiency. The same story tells CC → seq-CC, and Monroe → Greedy Monroe.

So the ✗ marks in this table are not, mostly, evidence that the field designed bad rules. They are the **residue of computability**. That is the single most useful thing to carry out of Chapter 3.

## Why greedy is respectable anyway

The reason nobody treats the sequential rules as embarrassing approximations is submodularity. Thiele satisfactions are concave (`1, ½, ⅓, …`), concavity gives diminishing returns, diminishing returns give a submodular objective — and greedy maximisation of a submodular function carries the **`1 − 1/e ≈ 63%`** approximation guarantee of Nemhauser–Wolsey–Fisher (1978). seq-PAV, RRV and the [STAR-PR](../../03_STAR_PR/README.md) variants are all instances of that greedy. The full treatment is on [Math for social choice](../../07_Concepts/topics/math_for_social_choice.md) §2, which is the page to read next.

**The Method of Equal Shares is the rule that broke the trade-off** — polynomial time *and* EJR, which is why it is the headline result of the last decade and is now running real participatory budgets. Note what it still doesn't buy: it is ✗ on Pareto efficiency, committee monotonicity, support monotonicity and consistency. Cheap and proportional, not cheap and well-behaved.

## The hardness result inside the Pareto column

One complexity theorem sits in Chapter 3 rather than Chapter 5, because it closes off an obvious repair:

> **Theorem 3.1** (Aziz & Monnot 2020). Given an instance `(A,k)` and a committee `W`, deciding whether `W` is Pareto optimal is **coNP-complete**.

The tempting patch for a rule that elects a [dominated committee](pareto_efficiency.md) is "detect the domination and output the dominating committees instead". Theorem 3.1 says you can't detect it cheaply, so the patch cannot produce a polynomial-time Pareto efficient rule.

**The asymmetry is worth keeping straight**, because it is easy to overstate the theorem: *verifying* an arbitrary committee's Pareto optimality is hard, but *finding* a Pareto optimal committee is easy — AV and SAV do it in polynomial time, every time. Hardness of checking does not imply hardness of achieving.

## Practical scale, for this repo's cases

Every case in this folder runs instantly, because "NP-hard" is a statement about growth, not about small elections. `abcvoting` solves the optimising rules exactly on teaching-sized profiles via an ILP solver; the one place it is noticeably slow is leximax-Phragmén, which is why [the axiom checker](../../06_Other/abcvoting_tabulation_engine/abc_axiom_check.py) uses profiles of a few dozen ballots at most. A real 200-candidate participatory budget is where the column starts to bite.

## Reproduce it

```bash
.venv/bin/python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py \
  04_Approval/03_Criteria/cases/abc_committee_monotonicity_2seats_c3_b10.yaml \
  --rules av,sav,pav,cc,seqpav,seqphragmen,monroe,equal-shares
```

Any `abcvoting` rule id may be passed to `--rules` — the NP-hard ones included, on cases this size.

---

**Related:** [the table](README.md) · [inclusion-strategyproofness](inclusion_strategyproofness.md) — the previous column · the full maths → [Math for social choice](../../07_Concepts/topics/math_for_social_choice.md) · the tooling → [the abcvoting engine](../../06_Other/abcvoting_tabulation_engine/README.md).
