# Monotonicity — when more support makes a candidate lose

A voting method is **monotonic** if raising a candidate on some ballots can never *hurt* them. RCV-IRV fails this: moving a winner *up* can change who gets eliminated in an earlier round and cost them the election. STAR doesn't. Each set is a **before/after pair** — identical except that some voters raise candidate X.

Read the reader-friendly **pages** (`monotonicity_pages/`); the `.yaml` beside each is the tabulatable source.

| Page (read this) | What it shows | src |
|---|---|:--:|
| [RCV-IRV — before](monotonicity_pages/monotonicity_irv_before.md) | baseline: X wins | [`.yaml`](monotonicity_irv_before.yaml) |
| [RCV-IRV — after](monotonicity_pages/monotonicity_irv_after.md) | some voters **raise X** → X now **loses** (the paradox) | [`.yaml`](monotonicity_irv_after.yaml) |
| [STAR — before](monotonicity_pages/monotonicity_star_before.md) | the STAR counterpart: X wins | [`.yaml`](monotonicity_star_before.yaml) |
| [STAR — after](monotonicity_pages/monotonicity_star_after.md) | raising X keeps X winning — no paradox | [`.yaml`](monotonicity_star_after.yaml) |

The lesson: read the two IRV pages back to back, then confirm STAR is unmoved by the same change.

## The 301 nuance — STAR fails a *stronger* variant

STAR passes the standard monotonicity criterion (*mono-raise*), as the pair above shows. But it does **not** pass the stronger **mono-raise-delete** (Woodall 1996): raising X *and* deleting the candidates now below X on those ballots can harm X — because burying the losers can change which candidate joins X in the runoff. This pair demonstrates it on a real election (X wins → raise X and delete the loser below X → **Z** wins):

| Page (read this) | What it shows | src |
|---|---|:--:|
| [STAR mono-raise-delete — before](monotonicity_pages/mono_raise_delete_before.md) | baseline: finalists X & Y, X wins the runoff | [`.yaml`](mono_raise_delete_before.yaml) |
| [STAR mono-raise-delete — after](monotonicity_pages/mono_raise_delete_after.md) | raise X, delete Y (now below X) → Y drops below Z, finalists become X & Z, **X loses** | [`.yaml`](mono_raise_delete_after.yaml) |

Concept & why this is a *lab-grade* failure (not the everyday promise): [STAR & monotonicity](../../00_start_here/STAR_Voting/properties_and_limits/STAR_monotonicity.md). Up: [method_comparisons — same ballots, different methods](../)

# file: README.md
