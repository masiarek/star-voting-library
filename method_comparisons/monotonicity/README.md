# Monotonicity — when more support makes a candidate lose

A voting method is **monotonic** if raising a candidate on some ballots can never *hurt* them. RCV-IRV fails this: moving a winner *up* can change who gets eliminated in an earlier round and cost them the election. STAR doesn't. Each set is a **before/after pair** — identical except that some voters raise candidate X.

Read the reader-friendly **pages** (`monotonicity_pages/`); the `.yaml` beside each is the tabulatable source.

| Page (read this) | What it shows | src |
|---|---|:--:|
| [RCV-IRV — before](cases/cases_pages/monotonicity_irv_before.md) | baseline: X wins | [`.yaml`](cases/monotonicity_irv_before.yaml) |
| [RCV-IRV — after](cases/cases_pages/monotonicity_irv_after.md) | some voters **raise X** → X now **loses** (the paradox) | [`.yaml`](cases/monotonicity_irv_after.yaml) |
| [STAR — before](cases/cases_pages/monotonicity_star_before.md) | the STAR counterpart: X wins | [`.yaml`](cases/monotonicity_star_before.yaml) |
| [STAR — after](cases/cases_pages/monotonicity_star_after.md) | raising X keeps X winning — no paradox | [`.yaml`](cases/monotonicity_star_after.yaml) |

The lesson: read the two IRV pages back to back, then confirm STAR is unmoved by the same change.

## The real one — the Upward Monotonicity Paradox, Alaska 2022

The synthetic pair above shows the mechanism; **[Alaska 2022 is a real election that did it](upward_monotonicity_alaska.md).** Had ~6,000 Palin-only voters ranked the *winner* Peltola first — giving her **more** first-place support — Peltola would have **lost** (those votes eliminate Palin first, and Begich then beats Peltola). This is the **upward** monotonicity paradox ("more is less"); its mirror is the **downward** paradox ("less is more"). Reproduced on a faithful 200-voter model:

| Page (read this) | What it shows | src |
|---|---|:--:|
| [Upward monotonicity (Alaska) — before](cases/cases_pages/alaska_upward_before.md) | RCV-IRV: **Peltola** wins (96–92) | [`.yaml`](cases/alaska_upward_before.yaml) |
| [Upward monotonicity (Alaska) — after](cases/cases_pages/alaska_upward_after.md) | raise Peltola on 7 ballots → **Begich** wins; Peltola **loses** | [`.yaml`](cases/alaska_upward_after.yaml) |

**[→ Full walk-through, mechanism, and why STAR / Ranked Robin can't do it](upward_monotonicity_alaska.md)** (Ranked Robin elects Begich — the Condorcet winner — *both* times, completely unmoved).

## The 301 nuance — STAR fails a *stronger* variant

STAR passes the standard monotonicity criterion (*mono-raise*), as the pair above shows. But it does **not** pass the stronger **mono-raise-delete** (Woodall 1996): raising X *and* deleting the candidates now below X on those ballots can harm X — because burying the losers can change which candidate joins X in the runoff. This pair demonstrates it on a real election (X wins → raise X and delete the loser below X → **Z** wins):

| Page (read this) | What it shows | src |
|---|---|:--:|
| [STAR mono-raise-delete — before](cases/cases_pages/mono_raise_delete_before.md) | baseline: finalists X & Y, X wins the runoff | [`.yaml`](cases/mono_raise_delete_before.yaml) |
| [STAR mono-raise-delete — after](cases/cases_pages/mono_raise_delete_after.md) | raise X, delete Y (now below X) → Y drops below Z, finalists become X & Z, **X loses** | [`.yaml`](cases/mono_raise_delete_after.yaml) |

Concept & why this is a *lab-grade* failure (not the everyday promise): [STAR & monotonicity](../../00_start_here/STAR_Voting/properties_and_limits/STAR_monotonicity.md). Up: [method_comparisons — same ballots, different methods](../)

# file: README.md
