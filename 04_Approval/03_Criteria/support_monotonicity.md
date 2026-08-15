# Support monotonicity — can more approvals cost you your seat?

**Level: 301 · deep dive**

**One line:** the obvious demand is that extra support never hurts a winner; the non-obvious finding is that it holds for *one* candidate far more often than for a *group*, and that gap is what the word `cand` marks in Table 3.1.

## Two columns, two definitions

Support can grow in two different ways, and the rules do not treat them alike, so the table gives each its own column:

- **With additional voters** — a **new** voter joins, approving exactly the set `X`. Written `A+X`.
- **Without additional voters** — an **existing** voter widens her ballot to also approve `X`. Written `Aᵢ+X`.

> **Definition 3.3** (Sánchez-Fernández & Fisteus). `R` satisfies **support monotonicity without additional voters** if for every instance `(A,k)`, voter `i`, and candidate set `X ⊆ C`: (1) if `X ⊆ W` for *all* winning committees `W`, then `X ⊆ W′` for all `W′` winning in `Aᵢ+X`; and (2) if `X ⊆ W` for *some* winning `W`, then `X ⊆ W′` for some `W′` winning in `Aᵢ+X`. **With additional voters** is the same with `A+X` in place of `Aᵢ+X`.

**When `X` is a single candidate `{c}`, the axiom is called candidate monotonicity** — and that is the whole content of the table's `cand` entries:

| symbol | meaning |
|---|---|
| ✓ | support monotonicity holds — for **any** set `X` |
| `cand` | candidate monotonicity holds (single `X = {c}`) but support monotonicity fails for some larger group |
| ✗ | fails even for a single candidate |

Read the "without additional voters" column and this is nearly the whole story: **only AV and SAV are ✓, and everything else is `cand`.** Not one of the eleven other rules can promise that a *group* already seated stays seated when a voter adds her approval of exactly that group.

## Why a group is harder than a candidate

The intuition that makes candidate monotonicity feel obvious — "more support can only help" — is true of the candidate you approve and false of the *arrangement* around them. Approving a whole slate does two things at once: it raises each member's standing, and it changes how much your ballot is worth to the rules that reweight. Under any rule with diminishing returns (every Thiele method, every load-balancing rule), a voter who now approves three winners is a **satisfied** voter, and her remaining influence shrinks. She can push her slate in and simultaneously stop being the reason any of them stays.

That is not a pathology of one rule; it is the mechanism proportionality is *built on*. Which is why the column is a near-uniform `cand`.

## Witness — seq-CC loses a candidate when a voter joins to support him

Support monotonicity **with** additional voters. Twelve voters, three seats:

```text
3 × {a}    1 × {a,c,d}    1 × {b}    2 × {b,c}    1 × {b,d}    2 × {c}    2 × {d}
```

seq-CC elects **{a,c,d}**. Now one more voter arrives approving exactly `{a,d}` — a subset of the winning committee, so by the axiom `a` and `d` must both survive:

```text
before          {a,c,d}
+1 × {a,d}      {a,b,c}      <- d is gone
```

The new voter supported `a` and `d`; `d` lost the seat. seq-CC is therefore only `cand` in that column.

## Witness — seq-PAV, without a new voter

The other column. Nine voters, three seats:

```text
1 × {c,d}   1 × {a,c}   1 × {a,d}   1 × {a,f}   1 × {b,c}   2 × {b,f}   1 × {c,e}
```

seq-PAV elects **{a,c,f}**. Voter 1 now widens her honest `{c,d}` to `{a,c,d,f}` — she has *added* approvals for `a` and `f`, both sitting winners:

```text
before                    {a,c,f}
voter 1 adds {a,f}        {a,b,c}      <- f is gone
```

She strengthened `a` and `f`; `f` fell out. Note what this is **not**: it is not strategic. She reported *more* honest support and was punished for it, which is a different complaint from [strategyproofness](inclusion_strategyproofness.md) and lands on a rule (seq-PAV) that is otherwise well-behaved.

## The three rules that fail even for one candidate

Monroe, Greedy Monroe and the Method of Equal Shares are ✗ in the "with additional voters" column — **a single new voter approving a single sitting winner can remove him.** For Equal Shares:

```text
1×{b,d}  1×{a,b}  1×{b,d,e}  1×{a,e}  2×{c,d,e}  1×{c,e}  1×{a,c,e}  1×{b,c,d}

k=3        ->  {a,d,e}
+1 × {a}   ->  {b,c,e}        <- a is gone
```

The book is unusually blunt about what to make of this: the failure "can be seen as a serious argument against these rules" *if* you care about fair treatment of candidates — and a non-issue if the candidates are inanimate (items in a budget, features on a roadmap), which is exactly where Equal Shares is deployed. **The axiom's importance is domain-dependent, and saying so is not hedging.**

## What this repo should and shouldn't claim

- **This is not the monotonicity that sinks IRV.** [Monotonicity](../../07_Concepts/topics/monotonicity/README.md) in the single-winner sense — raising a candidate on your ballot must not defeat them — is a *ranked-ballot* pathology with a famous [IRV witness](../../06_Other/RCV_IRV/README.md). The axiom on this page is its committee-shaped relative, defined over approval sets and seat counts. They rhyme; they are not the same theorem, and citing one for the other is a real error.
- **AV and SAV pass both columns outright.** For bloc Approval that is a clean, citable virtue: adding approvals for a sitting winner can never unseat them, individually or as a group.
- **Every proportional approval rule is `cand` at best.** When this repo recommends proportional rules — and it does — that is the accompanying honest sentence.

## Reproduce it

```bash
.venv/bin/python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --verbose
```

Seven support-monotonicity witnesses replay: three for the *with additional voters* column (seq-CC, Greedy Monroe, Equal Shares) and four for *without* (seq-PAV, seq-CC, Equal Shares, Greedy Monroe).

---

**Related:** [the table](README.md) · [committee monotonicity](committee_monotonicity.md) — the previous column · [consistency](consistency.md) — the next · single-winner monotonicity → [the monotonicity hub](../../07_Concepts/topics/monotonicity/README.md).
