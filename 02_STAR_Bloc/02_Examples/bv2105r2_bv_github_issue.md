<!--
Ready-to-paste GitHub issue for  github.com/Equal-Vote/bettervoting

STATUS: DRAFT — not filed. Awaiting Adam's go-ahead.

Links point at the public masiarek/star-voting-library repo so the ballots,
the frozen exports, and the independent tabulation are all inspectable.

NOTE ON #1056: cross-referenced below as a NEIGHBOUR, not as a duplicate. #1056
is the demo-election 401 (Editable Ballots regression, closed via #1058). It
quotes the same BV2105 test document, which is exactly how this library
mis-attributed the counting defect to it for a year.
-->

---

**Title:** A partial ballot whose marks are all equal is dropped from the tally as an abstention (BV2105 `r4dqvd`, re-confirmed on `w3vvff`)

### Summary

A ballot that scores **one** candidate and leaves the rest blank is counted as an **abstention** and excluded from the tally entirely — its score never enters the totals. On a 4-ballot election this reports `nTallyVotes 2 / nAbstentions 2` where the truth is 3 tallied and 1 abstention.

This is a **tally-level** defect, which is what separates it from the neighbouring abstain tickets: #1053 and #1090 are UI-label and export-ambiguity bugs whose underlying counts were correct. Here the count itself is wrong.

First seen on `r4dqvd` in Oct 2025. Because that election is closed (and a closed election may serve a stored result), I re-cast the identical ballots on a **fresh** election, `w3vvff`, on 2026-08-04. Same wrong numbers. So this is current behavior, not a historical artifact.

### Environment

- bettervoting.com, **STAR with `num_winners: 2`** (Bloc STAR), 3 candidates, 4 ballots.
- Original: **`r4dqvd`** (BV2105, created 2025-10-31, now closed).
- Re-check: **`w3vvff`** (BV2105-r2, created 2026-08-04) — <https://bettervoting.com/w3vvff/results>

### Steps to reproduce

1. Create a STAR election, 2 winners, candidates **Vanilla, Chocolate, Strawberry**.
2. Cast four ballots — one of each *kind*:

   | Voter | Vanilla | Chocolate | Strawberry | |
   |---|:--:|:--:|:--:|---|
   | 1 | 5 | 5 | 5 | all-5s |
   | 2 | — | — | — | fully blank: a true abstention |
   | 3 | **1** | — | — | **scores one candidate — the probe** |
   | 4 | 2 | 5 | 4 | an ordinary full ballot |

   (`—` = left blank, i.e. `score: null`.)

3. Tabulate and read `summaryData`.

### Expected vs. actual

| Quantity | Expected | Actual (both `r4dqvd` and `w3vvff`) |
|---|:--:|:--:|
| `nTallyVotes` | **3** | 2 |
| `nAbstentions` | **1** (voter 2 only) | 2 |
| Vanilla's total | **8** (5 + 1 + 2) | averaged over 2 ballots — the `1` is absent |

Voter 3's ballot is discarded. You can see it is *dropped from the tally* rather than merely mislabeled: Vanilla's reported figure is an average over two ballots (5 and 2), not three — the `1` never enters the sum.

The winners are **Chocolate, Strawberry** either way, and the seat-2 score tiebreak is correct. The discarded ballot only helped Vanilla, who loses seat 2 regardless. **The result is right; the count is not** — but a cast ballot dropped from the tally can decide a closer election, which is why I'm filing it.

### Why this may be #884 working as written — and why I think it's still wrong

Stating the counter-argument first, because it's a fair one. #884 established that a ballot whose marks are **all equal** counts as an abstention. A ballot bearing a *single* mark is **trivially** all-equal, so it falls through the same test. On that reading this is policy, not a defect.

I don't think that survives contact with how the tally treats blanks. **BetterVoting counts a blank as 0.** So voter 3's ballot isn't "one mark and two unknowns" — it is `Vanilla 1, Chocolate 0, Strawberry 0`, which is **not** all-equal and which strictly prefers Vanilla to both others. Judged against the scores actually counted, the all-equal test shouldn't fire at all.

Put plainly: a voter who rated exactly one candidate expressed a preference. Recording that as "no preference" both loses the score and overstates the abstention count.

Scope: this is about partial ballots whose **non-blank marks are all equal**. Partial ballots carrying two or more distinct marks count correctly today — e.g. `26khr3`, whose `Ada 5, Bruno 1, blank` ballot is tallied normally.

### Suggested fix / acceptance criteria

Apply the all-equal abstention test to the scores **as tallied** (blanks coerced to 0), not to the non-blank marks alone.

Acceptance test, using the ballots above:

- `nTallyVotes` = 3, `nAbstentions` = 1.
- Vanilla total 8, averaged over 3 ballots.
- Voter 2's fully-blank ballot remains an abstention.
- Winners unchanged: Chocolate, Strawberry.

### Independent verification

The same four ballots through Larry Hastings' `starvote` engine (which abstains only a genuinely blank ballot) give **4 ballots, 1 abstention, Vanilla total 8**, winners Chocolate + Strawberry — i.e. the same winners BetterVoting reports, from a correct count.

- Write-up, both counts side by side: <https://github.com/masiarek/star-voting-library/blob/master/02_STAR_Bloc/02_Examples/bv2105r2_w3vvff_ice_cream_recheck.md>
- Frozen export of the 2026 re-check: <https://github.com/masiarek/star-voting-library/blob/master/02_STAR_Bloc/02_Examples/cases/bv2105r2_w3vvff_ice_cream_recheck_bv_export.json>
- Frozen export of the 2025 original: <https://github.com/masiarek/star-voting-library/blob/master/02_STAR_Bloc/02_Examples/cases/bv2105_r4dqvd_ice_cream_bloc_bv_export.json>

### Related issues

- **#884** — the all-equal abstention policy this most likely follows from. If the behavior here is intended, that's the thread to settle it on.
- **#1053** — equal-max (`5,5`) ballot labeled "Abstained" in the confirmation dialog. Same family, but a *UI* message; here the ballot is missing from the count.
- **#1090** — explicit all-`0` ballot labeled "Abstained"; JSON correct. Again UI/export, not the tally.
- **#1407** — reconciling LH and BV reports on the pets election; overlapping territory for fully-flat ballots.
- **#1056** — *not* a duplicate, listed only to prevent the confusion I fell into: it is the demo-election `401` on ballot download (Editable Ballots regression, closed via #1058) and quotes the same BV2105 test document. Different defect, same election.

Happy to supply more ballot shapes if it helps pin the predicate — e.g. `1,1,—` (two equal marks plus a blank) versus `1,—,—`, which would separate "single mark" from "all non-blank marks equal."
