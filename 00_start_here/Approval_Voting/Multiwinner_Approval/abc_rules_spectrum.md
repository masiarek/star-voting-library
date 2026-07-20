# ABC rules and the utilitarian–egalitarian spectrum

*Advanced level (301). The formal treatment of approval-based committee (ABC) rules, following Lackner & Skowron's [*Multi-Winner Voting with Approval Preferences*](https://link.springer.com/book/10.1007/978-3-031-09016-5) (§2.1–2.2). One running election pulls the major rules apart and lines them up on a single axis — from **utilitarian** (maximize total satisfaction) to **egalitarian** (cover as many voters as possible). Gentle version: the [101 intro](abc_rules_intro.md). All committees below are verified with Lackner's own [`abcvoting`](https://github.com/martinlackner/abcvoting).*

## The ABC-rule framework

An **election instance** is `E = (A, k)`: an approval profile `A` (each voter `i` submits an approval set `A(i) ⊆ C`) and a target committee size `k`. An **ABC rule** maps `E` to one or more **winning committees** — size-`k` subsets of `C`.

- A rule is **resolute** if it always returns exactly one committee, **irresolute** if it may return several **tied** committees.
- Real systems force a single outcome with a **tie-breaking order**. Modelling all randomness as *fixed before the election* (a pre-published linear order over committees, "maximal committee wins") turns a randomised tiebreak into a deterministic one. **This is precisely the "published lot" discipline STAR uses** for its single-winner ties (see [STAR tie-breaking](../../STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)) — same idea, lifted to committees.

## The running instance (Example 2.1)

`k = 4`, `C = {a,b,c,d,e,f,g}`, 12 ballots:

```
3 × {a,b}   3 × {a,c}   2 × {a,d}   1 × {b,c,f}   1 × {e}   1 × {f}   1 × {g}
```

Approval counts: `a=8, b=4, c=4, d=2, f=2, e=1, g=1`.

## Rule 1 — Approval Voting (AV): utilitarian

AV maximises the total number of approvals inside the committee. With `score_AV(A,c) = |{i : c ∈ A(i)}|` (how many voters approve `c`), AV picks committees `W` maximising `score_AV(A,W) = Σ_{c∈W} score_AV(A,c)` — i.e. **the `k` most-approved candidates**.

Top three are `a,b,c`; the fourth seat ties between `d` and `f` (both 2). So AV is **irresolute** here, returning **two** committees of equal AV-score 18: `{a,b,c,d}` and `{a,b,c,f}`. AV is the pure **utilitarian** rule — it maximises summed satisfaction and is *indifferent* to whether some voters are left with nothing. (`{a,b,c,d}` leaves 3 voters wholly unrepresented; `{a,b,c,f}` leaves 2 — same AV-score, so AV can't tell them apart.)

*This `av` rule is exactly the LH engine's `Approval_Multi_Winner` (bloc Approval) — see [the approval original](../../../04_Approval/multiwinner/cases/approval_bloc_4seats_c7_b12_lackner_skowron.yaml).*

## Rule 2 — Approval Chamberlin–Courant (CC): egalitarian

CC is, in the book's words, "the exact opposite of AV." It grants **as many voters as possible at least one approved winner**: it maximises `score_CC(A,W) = |{i ∈ N : A(i) ∩ W ≠ ∅}|` — the number of **covered** voters. (Introduced by Thiele, 1895; independently by Chamberlin & Courant, 1983.)

On this instance CC returns the unique **{a, e, f, g}** — the only size-4 committee that covers **all 12** voters. The price of full coverage: CC seats `e` and `g` (one approval each) and **drops `b`, `c`** (four approvals each). Egalitarian coverage, purchased with low total satisfaction.

## Rule 3 — Proportional Approval Voting (PAV): the middle

PAV is a **Thiele method**: each voter's satisfaction from a committee giving them `j` approved winners is the **harmonic** value `1 + 1/2 + ⋯ + 1/j`, and PAV maximises the sum. The diminishing returns (`1/j`) mean a voter already well-represented counts for less, which produces **proportional** committees. Here PAV returns **{a, b, c, f}** — the popular `a,b,c` plus `f` for the f-faction, leaving 2 uncovered. **seq-Phragmén**, a load-balancing proportional rule, instead returns **{a,b,c,d}** on this profile — proportional rules need not agree.

## The spectrum, on one election

| Rule | Character | Committee(s) | AV-score (Σ approvals) | Voters covered | Uncovered |
|------|-----------|--------------|:--:|:--:|:--:|
| **AV** | utilitarian | `{a,b,c,d}` \| `{a,b,c,f}` | **18** | 9 \| 10 | 3 \| 2 |
| **seq-Phragmén** | proportional | `{a,b,c,d}` | 18 | 9 | 3 |
| **PAV** | proportional | `{a,b,c,f}` | 18 | 10 | 2 |
| **CC** | egalitarian | `{a,e,f,g}` | 12 | **12** | **0** |

Reading down the table you trade **total satisfaction** (AV-score falls 18 → 12) for **coverage** (uncovered falls 3 → 0). AV sits at the utilitarian pole, CC at the egalitarian pole, and the proportional rules (PAV, Phragmén) live in between — exactly the spectrum the book uses this example to introduce.

## The shadow-STAR bridge

Reading the same approval ballots as STAR ballots (approve = 5, else 0) and running STAR's committee rules (see [the shadow-STAR page](../../../04_Approval/multiwinner/lackner_skowron_shadow_star.md)) maps the STAR family onto the *same* axis:

| STAR rule | lands like | committee |
|-----------|-----------|-----------|
| **Bloc STAR** | AV (utilitarian) | A,B,C,D |
| **Allocated Score** (STAR-PR) · **SSS** | AV-ish here (loosely proportional) | A,B,C,D |
| **RRV** | PAV (proportional) | A,B,C,F |
| *(no direct analog)* | CC (egalitarian coverage) | — |

Two lessons drop out: STAR's *runoff* adds nothing over AV on binary ballots (Bloc STAR = AV), and among STAR's proportional variants only **RRV** reaches the proportional PAV committee — while nothing in the STAR family targets CC's pure coverage objective.

## Reproduce it

```bash
pip install abcvoting
python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py \
  04_Approval/multiwinner/cases/approval_bloc_4seats_c7_b12_lackner_skowron.yaml \
  --rules av,pav,cc,seqphragmen
# av -> {A,B,C,D}|{A,B,C,F} ; pav -> {A,B,C,F} ; cc -> {A,E,F,G} ; seqphragmen -> {A,B,C,D}
```

## Going deeper

AV, PAV, and CC are all one parameterised family — the **Thiele methods** — turned by a single satisfaction dial `w`. The formal treatment (the `w`-function spectrum, PAV's harmonic worked to `83/6`, welfare vectors, seq-/rev-seq-PAV, and **how RRV is the score-ballot cousin of seq-PAV**) is in **[Thiele methods](thiele_methods.md)**.

## References

- Lackner, M. & Skowron, P. (2023), *Multi-Winner Voting with Approval Preferences*, SpringerBriefs, [doi:10.1007/978-3-031-09016-5](https://doi.org/10.1007/978-3-031-09016-5) (open access) — §2.1–2.2, Examples 2.1–2.3, Rules 1–2.
- Thiele, T. N. (1895); Chamberlin, J. R. & Courant, P. N. (1983) — the CC rule.
- `abcvoting` (Lackner et al.) — the peer-reviewed reference implementation used here.
- Companion pages: [101 intro](abc_rules_intro.md) · [shadow STAR](../../../04_Approval/multiwinner/lackner_skowron_shadow_star.md) · [Approval — multi-winner](approval_multiwinner.md).
