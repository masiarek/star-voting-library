# The Alabama paradox in Proportional STAR

*Five gardeners. Four candidates. Add a seat to the committee, and someone who had one **loses** it.*

**Level: 301 · deep dive**

→ the method: [STAR-PR](../../01_Learn/STAR_PR/README.md) · what proportionality does and doesn't promise: [what "proportional" actually means](../../01_Learn/what_proportional_means.md) · the theory underneath: [the math behind proportional STAR](../../01_Learn/STAR_PR/the_math_behind_proportional_star.md)

---

## The election

A community garden is electing a committee. Five members score four candidates 0–5:

| | Aster | Basil | Clover | Dahlia |
|---|--:|--:|--:|--:|
| Gardener 1 | 3 | 3 | 2 | **4** |
| Gardener 2 | **5** | 4 | 0 | 2 |
| Gardener 3 | 1 | 0 | **4** | 3 |
| Gardener 4 | 0 | **5** | **5** | 3 |
| Gardener 5 | **5** | **5** | 0 | 0 |

Count these ballots with **Allocated Score** — the Equal Vote Coalition's recommended Proportional STAR tabulation, and the method BetterVoting runs as `STAR_PR`:

> **Two seats → Basil and Dahlia.**
> **Three seats → Aster, Basil and Clover.**

Nothing changed but the number of seats. **Dahlia was on a two-person committee and is off a three-person one.** Nobody changed a ballot. Nobody withdrew. The committee got *bigger* and she lost her place on it.

This is the **Alabama paradox** — a failure of *house-size monotonicity*. It is named for the 1880 US census, where Alabama was allotted 8 seats in a 299-seat House and 7 in a 300-seat one.

## Why it happens

The quota is the whole story. Allocated Score works out what one seat costs — the **Hare quota**, `voters ÷ seats` — and spends that many voters' ballots on each winner.

| Seats | Quota | A seat costs |
|--:|--:|---|
| 2 | 5 ÷ 2 = **2.5** | half the electorate |
| 3 | 5 ÷ 3 ≈ **1.67** | a third of it |

Changing the seat count changes the **price of a seat**, which changes *which* voters get spent on the first winner, which changes who is left to decide the second, and so on. The rounds are a chain, and the seat count is an input at every link. There is no reason the chain should end in a superset of where it ended before — and here it doesn't.

## Is that unfair?

Worth arguing honestly, because it is not obvious and the answer is not simply "yes".

**The case that it is unfair.** Dahlia's support did not shrink. The electorate did not change its mind. A rule under which *enlarging* a body can eject a sitting member offends a plain intuition about what more seats should mean — more representation, not a reshuffle. If a real council expanded from two seats to three and an incumbent lost her place while nobody's vote changed, "the arithmetic did it" would be a hard thing to say out loud at the meeting.

**The case that it is not.** Proportional representation never promised Dahlia a seat; it promised that *cohesive groups of voters* get representation in proportion to their size. At two seats, a seat is worth half the electorate and Dahlia is the best answer to "who represents the second half?" At three seats, the question is a genuinely different one — "who represents each third?" — and the answer is a different committee. Those are not the same question with one more answer bolted on; they are different questions. The paradox looks like a broken promise only if you assumed a promise that was never made.

**Where that leaves it.** Both readings are defensible, and which one governs is a *design* choice rather than a mathematical one. What is not defensible is being surprised by it after adopting the method. Anyone recommending Proportional STAR for a body whose size might change — a council that may expand, a board that adds a seat, a committee sized by turnout — should know this can happen and decide in advance whether they mind.

## It is not a bug, and it is not avoidable

This is a **theorem**, not an implementation defect. Pukelsheim's **Coherence Theorem** ([*Proportional Representation*, ch. 9](../../../07_Concepts/books/electoral_systems_and_pr.md)) proves that an apportionment method is house-size monotone *if and only if* it is a **divisor** method. Allocated Score is a **quota** method. The paradox is a structural consequence of guaranteeing quota, and it is the other half of the [Balinski–Young](../../../07_Concepts/books/electoral_systems_and_pr.md) trade: you may have the quota guarantee or house-size monotonicity, and not both.

Measured across tie-free random electorates by [`pr_alabama_paradox.py`](../../../06_Other/simulations/pr_alabama_paradox.py):

| Method | Family | Alabama paradox |
|---|---|--:|
| **Allocated Score** (`allocated`) | quota | **37.8%** |
| **Sequentially Spent Score** (`sss`) | quota | 20.8% |
| **Reweighted Range Voting** (`rrv`) | divisor | **0.0%** |

RRV's zero is not a sampling limit — it is the theorem. It is the method that *cannot* do this, and the price it pays is failing the [Hare Quota Criterion](../../01_Learn/what_proportional_means.md): a quota-sized faction cannot always force itself a seat. **Neither method is simply better.** That is the trade, stated as a number instead of an intuition.

**Read the 37.8% carefully.** Those ballots are independent uniform scores — an impartial-culture-style model, which is *known* to manufacture more paradoxes than real electorates contain ([why](../../01_Learn/simulating_pr.md)). It means "easy to construct, not a curiosity." It does **not** mean one election in three.

## Run it yourself

Identical ballots in both files; only `num_winners:` differs.

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/alabama_paradox/cases/alabama_2seats.yaml
```

| Case | Seats | Elects | File |
|---|--:|---|---|
| Two seats | 2 | **Basil, Dahlia** | [page](cases/cases_pages/alabama_2seats.md) · [yaml](cases/alabama_2seats.yaml) |
| Three seats | 3 | **Aster, Basil, Clover** | [page](cases/cases_pages/alabama_3seats.md) · [yaml](cases/alabama_3seats.yaml) |

## See also

- [What "proportional" actually means](../../01_Learn/what_proportional_means.md) — quotas, thresholds, and what proportionality does not promise
- [STAR-PR — the three methods](../../01_Learn/STAR_PR/README.md) — where the quota/divisor split is introduced
- [Bloc STAR vs Proportional STAR](../../../method_comparisons/bloc_vs_pr/README.md) — the 101 entry point, two ballots
- [Balinski & Young, *Fair Representation*](../../../07_Concepts/books/electoral_systems_and_pr.md) — the readable account of the paradoxes and the impossibility result
