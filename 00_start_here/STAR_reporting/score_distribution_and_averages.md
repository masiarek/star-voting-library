# The Score Distribution table — and the one float that sneaks in

*How the `[Score Distribution]` block is built, why the engine is otherwise obsessively float-free (exact `Fraction` arithmetic, mixed-number display), and why the **Avg** column is the single place that quietly breaks that rule — which is exactly why `1.25` can print as `1.2`.*

Part of the [STAR reporting](reporting_ties.md) notes. Companion to [Reading a STAR report](../tabulation_engines/LH_starvote/reading_a_star_report.md).

---

## The table

With `show_score_counts: true`, the LH engine prints a per-candidate score histogram between the ballot on-screen report and the Scoring Round. Example (the 6-candidate / 3-seat Bloc case):

```
[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        0  3  1  0  0  0  |    15   3.8
Ben        0  0  0  3  1  0  |     7   1.8
Cara       0  0  0  1  3  0  |     5   1.3
Dan        0  3  1  0  0  0  |    15   3.8
Eve        0  0  2  2  0  0  |    10   2.5
Finn       0  0  0  0  3  1  |     3   0.8
```

Each row is one candidate; the `Score` group header spans the star-value columns (5 down to 0); each cell is **how many ballots gave that candidate that many stars**. `Total` is the sum of stars; `Avg` is the mean stars per ballot. (When any ballot abstains on a candidate an `Abs` column appears — outside the `Score` group — and the average is taken over the ballots that actually scored the candidate.)

## The thing that looked wrong

Cara's four ballots score her **1, 2, 1, 1**. That sums to **5**, over **4** ballots, so her mean is **5 ÷ 4 = 1.25** exactly. School rounding to one decimal gives **1.3** — which is what the table shows above. That looks unremarkable now, but it is the *fixed* behavior: an earlier version of this column printed **1.2** for exactly these ballots, and understanding why is a small tour of the engine's design philosophy. Nothing was ever miscounted — the `5` and the `1.25` are both correct — the `1.2` was a pure *rounding-convention* artifact.

## Larry's design: no floats, ever

The vendored `starvote` engine (Larry Hastings') represents every tabulation quantity as an exact rational, never a binary float. Right at the top:

```python
# starvote/__init__.py:90
from fractions import Fraction
```

The average score is computed as an exact `Fraction`, not a division:

```python
# starvote/__init__.py:1161
averages = {
    candidate: Fraction(score, ballot_count)
    for candidate, score in scores.items()
}
```

And it is *displayed* not as a decimal but as an exact **mixed number**, through a trio of helpers — `split_int_or_fraction_as_str`, `measure_int_or_fraction_as_str`, and `format_int_or_fraction` (`starvote/__init__.py:168`, `:213`, `:263`). Those split a `Fraction` into `integer`, `+`, `numerator`, `/denominator` parts and column-align all four. So in the engine's own scoring round, Cara's average renders as:

```
1 +1/4
```

exact, unambiguous, and impossible to round wrong. This is the same machinery that lets a proportional result print an allocation as `34 +5745/21952` (see the [BV2130 case](../../03_STAR_PR/_main/bv2130_presidential_board_star_pr.md)) instead of a lying `34.3`. Larry built the five-width alignment code specifically so he'd never have to show a lossy decimal average. **That is the "something to avoid floats" you remembered.**

## The one place it leaks

The `[Score Distribution]` table is not the engine's — it's built by the LH presentation wrapper, in `format_score_counts`, and its **Avg** column is the lone spot that steps outside the Fraction discipline:

```python
# starvote_larry_hastings.py (format_score_counts)
scored = n - abstain[c]
avg = totals[c] / scored if scored else 0.0     # <- float division
...
f"{totals[c]:>{total_w}}  {avg:>4.1f}"           # <- lossy one-decimal format
```

`totals[c] / scored` is an ordinary Python float division, and `{:.1f}` is an ordinary float format. So this column reintroduces exactly the binary float that the rest of the engine is at pains to avoid — and inherits Python's float rounding rules with it.

## Why `1.25` becomes `1.2` (banker's rounding)

Python's `format(x, '.1f')` (and `round`) use **round-half-to-even**, a.k.a. *banker's rounding*: when a value sits exactly halfway, it rounds toward the **even** final digit rather than always up. `1.25` is exactly halfway between `1.2` and `1.3`; the even neighbor is `1.2`; so it prints `1.2`. The "school rule" you used — round-half-**up** — would give `1.3`.

The two rules only ever disagree at an *exact* half, and only for some of those. In this very table, five of the six averages round identically under both rules, and only Cara's exposes the difference:

| candidate | scores | exact mean | `{:.1f}` (banker) | half-up | agree? |
|-----------|--------|:----------:|:-----------------:|:-------:|:------:|
| Ada / Dan | quarters | `15/4 = 3.75` | `3.8` | `3.8` | ✓ |
| Ben       | quarters | `7/4 = 1.75`  | `1.8` | `1.8` | ✓ |
| **Cara**  | quarters | **`5/4 = 1.25`** | **`1.2`** | **`1.3`** | ✗ |
| Eve       | halves   | `10/4 = 2.5`  | `2.5` | `2.5` | ✓ (exact) |
| Finn      | quarters | `3/4 = 0.75`  | `0.8` | `0.8` | ✓ |

The pattern: a `.x5` value diverges only when its lower tenth is **even** (so banker rounds *down* while school rounds *up*). `2.25 → 2.2` vs `2.3` diverges; `2.75 → 2.8` agrees (both round to the even `8`). That's why the surprise feels random — it depends on the parity of the digit you happen to land next to.

Two further subtleties, for completeness:

The trick only shows at all because `1.25` is one of the rare decimals that is **exactly representable** in binary floating point (it's `1 + 1/4`, a dyadic rational). A mean like `5/3 = 1.666…` is not exactly halfway anywhere, so it just rounds normally (`1.7`) and no one blinks. So the "banker's rounding" face appears precisely when the ballot count is a power of two (`n = 2, 4, 8, …`), because only then are the quarter/eighth means exact halves at the tenths place. Small hand-built teaching examples — which love `n = 4` — hit this far more often than a real 500-ballot election would.

And note it is genuinely *only* the display. The stored `Total` (`5`) is exact; the divergence is entirely in how the one-decimal string is formed.

## How to make it consistent with the rest of the engine

The clean fix is not "one decimal vs two" — it is to stop using a float at all, and take the average from an exact `Fraction(totals[c], scored)` like everything else. From that exact source there are two honest display choices:

1. **Match Larry — render the exact mixed number** (`1 +1/4`). Zero rounding, fully consistent with the engine's design, and the formatting helpers (`format_int_or_fraction`) already exist to reuse. Cost: wider and unusual for a quick-scan per-candidate column, and unwieldy for large real electorates (`34 +5745/21952` in every row).
2. **Keep a compact decimal, but round the `Fraction` deterministically** (round-half-**up**, via `decimal.Decimal(...).quantize(Decimal('0.1'), ROUND_HALF_UP)`). You still lose exactness in the display, but the result is predictable and matches the arithmetic a reader does in their head (`1.25 → 1.3`). The column stays narrow.

Recommended split: use the exact `Fraction` as the source of truth everywhere (honoring the design), render the **exact mixed number where Larry already does** (the scoring round), and in the scannable **Score Distribution `Avg`** column round half-up to one decimal. That removes the float, kills the banker's-rounding surprise, and keeps the histogram readable.

> **Status: fixed.** The `Avg` column now computes the mean as an exact rational — `Decimal(totals[c]) / Decimal(scored)` — and rounds **half-up** to one decimal (`quantize(Decimal("0.1"), ROUND_HALF_UP)`) in `format_score_counts`. No binary float is involved, and an exact `1.25` now prints as `1.3` (matching the arithmetic a reader does by hand) rather than `1.2`. The engine's own scoring-round averages remain exact `Fraction` mixed numbers as before; only this scannable histogram column trades exactness for a compact, predictable one-decimal.

## See also

- [Reading a STAR report](../tabulation_engines/LH_starvote/reading_a_star_report.md) — the rest of the output blocks.
- [BV2130 — Proportional STAR](../../03_STAR_PR/_main/bv2130_presidential_board_star_pr.md) — where the exact-`Fraction` mixed number (`34 +5745/21952`) earns its keep.
- [Reporting true ties](reporting_ties.md) · [BV vs LH reporting differences](reporting_diff_BV_LH.md).
