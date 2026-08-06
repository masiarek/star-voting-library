# 01_STAR/03_Criteria — what STAR guarantees, and where it doesn't

The formal side of STAR, always as **runnable elections rather than assertions**: each set below isolates one criterion or one tie behavior, small enough to check by hand. The prose companions live in [`01_Learn/properties_and_limits/`](../01_Learn/properties_and_limits/README.md) — this folder is where those claims get numbers.

Levels follow the [curriculum](../../07_Concepts/CURRICULUM.md): 🟢 101 · 🟡 201 · 🔴 301.

## Criteria

| Set | Level | What it shows |
|---|:--:|---|
| [The Majority Criterion](majority_criterion/README.md) | 🔴 301 | Two 5-voter elections isolating STAR's Majority-Criterion behavior — and the **Relaxed** Majority Criterion ("needs *two* rivals, not one"). |
| [Favorite betrayal](favorite_betrayal/README.md) | 🔴 301 | STAR is **not** formally FBC-compliant, and the leak lives in the runoff: the score you give your favorite can keep your compromise out of the top two. Rare, constructed, and conceded honestly. |
| [IIA & the cycle spoiler](iia_cycle_spoiler/README.md) | 🔴 301 | Independence of Irrelevant Alternatives, shown mechanically: in a genuine Condorcet cycle a candidate who *cannot win* still changes who does — with perfectly sincere ballots. |
| [Equal and opposite](equal_and_opposite/README.md) | 🟡 201 | The Equal Vote Coalition's **Test of Balance**: two voters with exact-opposite ballots cancel completely, so the winner never moves. What an [equally weighted vote](../01_Learn/properties_and_limits/equally_weighted_vote.md) means. |
| [None of the Above](none_of_the_above/README.md) | 🔴 301 | A protest electorate where NOTA tops the scores *and* wins the runoff — STAR counts a formal rejection like any other candidate. |

## Ties & tie-breaking

STAR resolves ties with a deterministic cascade (pairwise → five-star → lot). These two sets walk it from the happy path to the case where it runs out.

| Set | Level | What it shows |
|---|:--:|---|
| [The tie-break ladder](tie_break_ladder/README.md) | 🟡 201 | The **happy path**: elections that tie but never reach the lot, because the deterministic rungs settle it. The live companion to [the tie-breaking doc](../01_Learn/Tie_Breaking_STAR/tie_breaking.md). |
| [The dead rung](tie_break_dead_rung/README.md) | 🔴 301 | When no tied candidate holds a 5, the five-star rung reads 0–0, the cascade has nothing left, and the **lot** decides. |

The exhaustive sweep behind these two — eight ballots engineered to tie at every locus, including the fully-flat degenerate shapes — is kept off the path in [09_Parked](../09_Parked/Flat_scores_ties/README.md).

---

**Related:** the honest-limits prose → [STAR's honest limits](../01_Learn/properties_and_limits/STAR_honest_limits.md) · practice these on paper → [05_Practice](../05_Practice/README.md) · the cross-method criterion gallery → [Voting 401](../../07_Concepts/curriculum/CURRICULUM_401.md).
