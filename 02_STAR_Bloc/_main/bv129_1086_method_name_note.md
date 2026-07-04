<!--
Ready-to-paste comment for github.com/Equal-Vote/bettervoting/issues/1086
(the "STAR vs Bloc STAR" method-name label). Paste everything below the line.
Full detail lives in the BV129 case page it links to.
-->

---

The result is correct — this is only the exported method **name**, but it's a
slippery one. The method is stored as plain `"STAR"` in two places, with the seat
count in a separate field:

```json
Election.races[0].voting_method : "STAR"     num_winners : 2
Results[0].votingMethod         : "STAR"
```

So "Bloc STAR" is never written down — it's only implied by *STAR ballot + more
than one seat*. Two consequences:

- **The name alone is ambiguous.** `votingMethod: "STAR"` is single-winner STAR at
  1 seat and **Bloc STAR** at 2. A consumer that keys on the method name without
  also reading `num_winners` will mistabulate.
- **Editing one field silently changes the method.** Bump `num_winners` between 1
  and 2 without touching `votingMethod`, and the election flips between STAR and
  Bloc STAR with nothing in the name to flag it.

I don't think the *stored* value is necessarily wrong, though: `votingMethod` names
the ballot / tabulation family (STAR = 0–5 scores) and `num_winners` names the
seats, so "Bloc STAR" is arguably a **derived** label. If so, the tightest fix is
display-side: **derive and show "Bloc STAR" (STAR + more than one seat) wherever the
method is named**, rather than changing the stored field.

Worked reference — ballots, the exact export lines, and a strict engine that
**refuses** `voting_method: STAR` + `num_winners: 2` rather than guessing:
<https://github.com/masiarek/YAML/blob/master/02_STAR_Bloc/_main/bv129_score_tiebreak_bloc.md>
