---
tags:
  - criteria
  - multi-winner
---

# Committee monotonicity — add a seat, keep the winner

**Level: 301 · deep dive**

**One line:** if one more seat becomes available, a committee-monotone rule tells you *who to add*; a rule without the property may answer "start over", and the candidate who won outright at one seat can vanish at two.

## The definition

> **Definition 3.2.** A resolute ABC rule `R` is **committee monotone** if for every instance `(A, k)`, the winning committee at size `k` is a subset of the winning committee at size `k+1`.

Two things about the shape of this axiom are worth noticing before the counterexample:

- **It is defined for resolute rules only.** A rule returning several tied committees needs a stronger statement (Elkind et al. call the variants *upward-* and *downward-accretive*); the book sidesteps that by fixing a tiebreaking order. This repo does the same, and says which one — see [the table's resoluteness note](README.md).
- **A committee-monotone rule is secretly a ranking.** If every size-`k` winner sits inside the size-`k+1` winner, the rule has really produced an ordered list of candidates and is reading the top `k` off it. That equivalence is the reason the axiom is easy for AV and the sequential rules — they *are* built as ordered lists — and hard for everything that optimises over whole committees.

## The witness: eleven rules agree at one seat, five change their mind at two

Ten voters, three candidates. Two approve only A, three approve A and C, three approve B and C, two approve only B.

<!-- ballots:abc_committee_monotonicity_1seat_c3_b10 -->
*(No ballot art for `abc_committee_monotonicity_1seat_c3_b10` — draw it with `build_style_ballot_images.py --from-yaml 04_Approval/03_Criteria/cases/abc_committee_monotonicity_1seat_c3_b10.yaml`.)*

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
A,B,C
1,0,0   # 2 voters — approve A only
1,0,0
1,0,1   # 3 voters — approve A and C
1,0,1
1,0,1
0,1,1   # 3 voters — approve B and C
0,1,1
0,1,1
0,1,0   # 2 voters — approve B only
0,1,0
```
<!-- /ballots -->

Approval counts: **C 6, A 5, B 5**. C is the consensus candidate — the only one a majority approves, and nobody's enemy.

**At one seat**, eleven of the thirteen rules elect C:

```text
k=1
  AV {c}   CC {c}   PAV {c}   seq-PAV {c}   seq-CC {c}   Monroe {c}
  Greedy Monroe {c}   seq-Phragmén {c}   leximax-Phragmén {c}
  Method of Eq. Shares {c}   MAV {c}
  rev-seq-PAV {a} | {b}      SAV {a} | {b}
```

**At two seats**, on the very same ballots:

```text
k=2
  AV                    {a,c} | {b,c}      <- C kept
  seq-PAV               {a,c} | {b,c}      <- C kept
  seq-CC                {a,c} | {b,c}      <- C kept
  seq-Phragmén          {a,c} | {b,c}      <- C kept
  Method of Eq. Shares  {a,c} | {b,c}      <- C kept
  CC                    {a,b}              <- C DROPPED
  PAV                   {a,b}              <- C DROPPED
  Monroe                {a,b}              <- C DROPPED
  leximax-Phragmén      {a,b}              <- C DROPPED
  MAV                   {a,b}              <- C DROPPED
```

Five rules add a seat and remove the winner. That is Proposition A.2, and it is the ✗ in the committee-monotonicity column.

**The reasoning behind the drop is not a bug.** At one seat, C is the best single representative: six voters get someone. At two seats, `{A,B}` represents *all ten* voters, while `{A,C}` leaves the two B-only voters with nobody. A rule chasing coverage or proportionality is right to prefer `{A,B}` — the two answers are each correct for their own question, and committee monotonicity is the demand that they be correct *for the same question*.

Note also which two rules pick differently at one seat: **SAV and rev-seq-PAV** elect A or B rather than C, because [SAV](../01_Learn/Multiwinner_Approval/satisfaction_approval_voting.md) splits each ballot's single vote among its marks, scoring A and B at 3.5 against C's 3. Both are still committee monotone here — their `{a}` sits inside their `{a,b}`. The property is about *stability across sizes*, not about agreeing with anyone else.

The repo's Approval count on the two-seat file, showing AV keeping C:

<!-- report:abc_committee_monotonicity_2seats_c3_b10 -->
```text
--- Approval Voting (2 winners) ---
 Tabulating 10 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C      (1 = approve; 0 = not approved)
     2 × 1,0,0
     3 × 1,0,1
     3 × 0,1,1
     2 × 0,1,0

   C -- 6 (60%) -- Elected
   A -- 5 (50%) -- Elected
   B -- 5 (50%)
  Note: A, B each have 5 approvals and tie for the last 1 seat.
        Candidate priority order (A > B) broke the tie: A elected, B not elected.

[Approval Distribution] (how many candidates each ballot approved)
   16 approvals across 10 ballots — average 1.6 of 3 (range 1–2).
     approved 1: 4 ballots
     approved 2: 6 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   C    |   A    |   B    |
   -------------------------------
   C  |   --   |  50%   |  50%   |
   A  |  60%   |   --   |   0%   |
   B  |  60%   |   0%   |   --   |

Winners — Approval Voting (2 winners)
  C, A
```
<!-- /report -->

## The Method of Equal Shares needs its own witness

The ten-voter profile above does **not** break Equal Shares — it keeps C. MES fails the axiom on a different, even smaller profile (four voters, six candidates): `1×{a,d,e}`, `1×{a,c}`, `1×{b,e}`, `1×{c,d,f}`.

```text
k=3  ->  {a,c,e}
k=4  ->  {a,b,c,d}      <- e dropped
```

Worth knowing because MES is the rule of the moment — polynomial time *and* EJR, deployed in Polish and Swiss participatory budgeting (see [math for social choice](../../07_Concepts/topics/math_for_social_choice.md)). It is genuinely excellent, and it is not committee monotone.

**Greedy Monroe** needs its own witness too, for a reason that also explains an oddity in Chapter 3: it is the one rule in the book that fails **anonymity**, because it breaks ties using a fixed order over *voters*. That is also why it is the only rule with no irresolute form at all.

## Why the axiom is worth wanting — and worth giving up

The case *for* is concrete. A hiring round that may fund one more post; a purchase list that may afford one more item; a shortlist that may be extended. In each, "who else?" has to have an answer that doesn't undo the answer already acted on. A rule that reshuffles gives, in the book's phrase, "a useless recommendation".

The case *against* is that the axiom costs proportionality. Committee-monotone rules are typically less proportional — the book flags this as observed rather than proven — and the intuition is clean: a rule forced to build committees incrementally cannot look at the whole committee as a bundle, and proportionality is a property of bundles. Look at the table: every committee-monotone rule (AV, seq-PAV, seq-CC, rev-seq-PAV, seq-Phragmén, SAV) is sequential, and the strongest proportional rules (PAV, Monroe, leximax-Phragmén, Equal Shares) all fail.

**So this is not a criterion to score rules on. It is a question about your setting**: does the committee size stand still? If yes, set the axiom aside and buy proportionality with the budget. If no, you need it and you should know what you are paying.

## Where this bites in this repo

- **Bloc Approval and [Bloc STAR](../../02_STAR_Bloc/README.md) are the "just take the top k" rules**, and they are committee monotone for the same reason they are majoritarian: they read a ranking off a single scoring round. The property and the criticism have one cause.
- **[STAR-PR](../../03_STAR_PR/README.md)'s variants are sequential** (Allocated Score, SSS, RRV all seat one winner at a time with reweighting), which puts them structurally on the committee-monotone side — the same side as seq-PAV, whose score-ballot cousin RRV is. The book does not cover score rules, so this is an observation about their shape, not a cited result.
- **The apportionment cousin of this axiom is house monotonicity**, and its failure is the [Alabama paradox](../../03_STAR_PR/03_Criteria/alabama_paradox/README.md) — a state losing a seat because the House got bigger. Same shape, different domain, and the Alabama case is the friendlier way in.

## Reproduce it

```bash
.venv/bin/python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --verbose
```

Seven committee-monotonicity witnesses replay: the ten-voter profile against CC, PAV, Monroe, leximax-Phragmén and MAV, plus the dedicated profiles for Equal Shares and Greedy Monroe.

---

**Related:** [the table](README.md) · [Pareto efficiency](pareto_efficiency.md) — the previous column · [support monotonicity](support_monotonicity.md) — the next · [Alabama paradox](../../03_STAR_PR/03_Criteria/alabama_paradox/README.md) — the same failure in apportionment.
