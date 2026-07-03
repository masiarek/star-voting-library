# Monotonicity — when more support makes a candidate lose

A voting method is **monotonic** if raising a candidate on some ballots can never
*hurt* them. RCV-IRV fails this: moving a winner *up* can change who gets eliminated
in an earlier round and cost them the election. STAR doesn't. Each set is a
**before/after pair** — identical except that some voters raise candidate X.

Read the reader-friendly **pages** (`monotonicity_pages/`); the `.yaml` beside each
is the tabulatable source.

| Page (read this) | What it shows | src |
|---|---|:--:|
| [RCV-IRV — before](monotonicity_pages/monotonicity_irv_before.md) | baseline: X wins | [`.yaml`](monotonicity_irv_before.yaml) |
| [RCV-IRV — after](monotonicity_pages/monotonicity_irv_after.md) | some voters **raise X** → X now **loses** (the paradox) | [`.yaml`](monotonicity_irv_after.yaml) |
| [STAR — before](monotonicity_pages/monotonicity_star_before.md) | the STAR counterpart: X wins | [`.yaml`](monotonicity_star_before.yaml) |
| [STAR — after](monotonicity_pages/monotonicity_star_after.md) | raising X keeps X winning — no paradox | [`.yaml`](monotonicity_star_after.yaml) |

The lesson: read the two IRV pages back to back, then confirm STAR is unmoved by the
same change. Up: [`../README_method_comparisons.md`](../README_method_comparisons.md)

# file: README_monotonicity.md
