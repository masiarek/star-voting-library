# Lackner & Skowron's steering committee — approval, and its shadow STAR

*Example 2.1 from Lackner & Skowron, [*Multi-Winner Voting with Approval Preferences*](https://link.springer.com/book/10.1007/978-3-031-09016-5) (SpringerBriefs, 2023, open access). An academic society elects a **k = 4** steering committee from 7 candidates `{a,b,c,d,e,f,g}` with 12 approval ballots. This page runs that exact profile through the approval rules **and** its "shadow STAR" (approve = 5, else 0) to show where the STAR family lands versus the approval family.*

## The profile

```
3 × {a, b}     3 × {a, c}     2 × {a, d}     1 × {b, c, f}
1 × {e}        1 × {f}        1 × {g}
```

Approval counts: **a = 8**, b = 4, c = 4, d = 2, f = 2, e = 1, g = 1. Candidate **a** is on 8 of 12 ballots; the small factions (`{e}`, `{f}`, `{g}`, and the lone `{b,c,f}` voter) are the ones a majoritarian committee tends to ignore.

## The committees — same voters, six rules

| Rule | Family | Character | Committee (k = 4) | 4th seat |
|------|--------|-----------|-------------------|:--:|
| **AV** (Bloc Approval) | approval | majoritarian | **a, b, c, d** | d |
| **PAV** (book, Ex. 2.4) | approval | proportional | **a, b, c, f** | **f** |
| **Bloc STAR** | STAR | majoritarian | **A, B, C, D** | D |
| **Allocated Score** (STAR-PR) | STAR | proportional-ish | **A, B, C, D** | D |
| **SSS** (Sequentially Spent Score) | STAR | proportional-ish | **A, B, C, D** | D |
| **RRV** (Reweighted Range Voting) | STAR | proportional | **A, B, C, F** | **F** |

Every rule agrees on the first three seats (a, b, c). The whole election turns on **seat 4 — d vs f** — and that single seat sorts the rules into two camps:

- **Seat D** — the *majoritarian* rules (AV, Bloc STAR) plus the *loosely* proportional STAR rules (Allocated Score, SSS). D is the 4th-strongest candidate by raw support (the two `{a,d}` voters), so once a/b/c are in, D is the "next most popular."
- **Seat F** — the *fully proportional* rules: the book's **PAV**, and in the STAR family, **RRV**. Seating F gives the two `{*,f}` voters a representative they otherwise completely lack; PAV's and RRV's objectives reward covering an unrepresented faction over adding a fourth member for the already-well-served majority.

## What the shadow STAR teaches

Reading the approval ballots as STAR ballots (approve = 5, else 0) and re-running is a clean way to see that **"STAR" and "proportional" are two different knobs**:

1. **Bloc STAR ≈ AV.** With binary ballots, STAR's runoff adds nothing over approval counting — Bloc STAR reproduces the majoritarian committee **A, B, C, D** exactly (with the same b/c and d/f ties, here broken by the published lot).
2. **STAR's *default* proportional rule is not as proportional as PAV *here*.** Allocated Score (BetterVoting's `STAR_PR`) and SSS still seat D — they don't reproduce PAV. Only **RRV** among the STAR variants recovers **A, B, C, F**, matching PAV.

So the takeaway isn't "STAR = proportional" or "STAR = majoritarian" — it's that the *proportional guarantee depends on the specific rule*, and this tiny profile pulls the STAR-family rules apart at exactly the seat where proportionality bites.

## Run them

| View | File |
|------|------|
| Approval original (Bloc Approval → a,b,c,d) | [`approval_bloc_4seats_c7_b12_lackner_skowron.yaml`](approval_bloc_4seats_c7_b12_lackner_skowron.yaml) |
| Shadow **Bloc STAR** → A,B,C,D | [`../../02_STAR_Bloc/_main/lackner_skowron_shadow_bloc_star_c7_b12.yaml`](../../02_STAR_Bloc/_main/lackner_skowron_shadow_bloc_star_c7_b12.yaml) |
| Shadow **Allocated Score** (STAR-PR) → A,B,C,D | [`../../03_STAR_PR/_main/lackner_skowron_shadow_star_pr_c7_b12.yaml`](../../03_STAR_PR/_main/lackner_skowron_shadow_star_pr_c7_b12.yaml) |
| Shadow **RRV** → A,B,C,F (matches PAV) | [`../../03_STAR_PR/_main/lackner_skowron_shadow_star_pr_rrv_c7_b12.yaml`](../../03_STAR_PR/_main/lackner_skowron_shadow_star_pr_rrv_c7_b12.yaml) |

The approval **PAV / seqPAV / Phragmén** results come from Lackner's own [`abcvoting`](https://github.com/martinlackner/abcvoting) — run the approval file through [`abcvoting_tabulation_engine/`](../../abcvoting_tabulation_engine/) (guarded on the optional `abcvoting` install) to reproduce the book's proportional committees.

## See also

- **The ABC-rules education built on this same example:** [committees & coverage — a gentle intro (101)](../../00_start_here/Approval_Voting/abc_rules_intro.md) · [ABC rules & the utilitarian–egalitarian spectrum (301)](../../00_start_here/Approval_Voting/abc_rules_spectrum.md).
- [Bloc STAR vs proportional STAR](../../00_start_here/proportional_representation/) — the majoritarian/proportional split in the STAR family.
- [Approval multi-winner](../../00_start_here/Approval_Voting/approval_multiwinner.md).
