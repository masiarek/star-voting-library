# Inclusion-strategyproofness — the column where AV stands alone

**Level: 301 · deep dive**

**One line:** twelve of the thirteen rules in Table 3.1 can be gamed by a voter who simply *narrows an honest ballot*, and the one that can't is plain Approval Voting — which is the strongest honest thing this repo can say for bloc Approval, and worth saying precisely because the rest of the case for it is weak.

## Why approval ballots get a second chance at this

[Gibbard–Satterthwaite](../../07_Concepts/topics/gibbard_satterthwaite_theorem.md) kills strategyproofness for every reasonable *ranked* single-winner rule. It does not apply here: an approval ballot is a much more restricted object than a linear order, so the impossibility doesn't reach, and strategyproofness is genuinely on the table. Table 3.1 is where the field cashes that in — and mostly finds it doesn't help.

## Two definitions, and why the weaker one is the interesting one

Both come from Peters (2018), and both assume a resolute rule. `A′` is an **i-variant** of `A`: only voter `i` changed her ballot.

> **Definition 3.6 — cardinality-strategyproofness.** `|R(A,k) ∩ A(i)| ≥ |R(A′,k) ∩ A(i)|`. Voter `i` can never *increase the number* of her approved candidates on the committee by misreporting.

> **Definition 3.7 — inclusion-strategyproofness.** `R(A,k) ∩ A(i)` is never a **strict subset** of `R(A′,k) ∩ A(i)`. Voter `i` can never get a committee containing *all* the approved candidates she already had **plus more**.

Cardinality is the stronger axiom (it implies inclusion), and the reason to state the weaker one is that it makes fewer assumptions about the voter. Cardinality-strategyproofness assumes she only counts her winners and cannot tell them apart. Inclusion-strategyproofness allows her to have real preferences *among* the candidates she approves — so a manipulation only counts as successful when it is unambiguously better: she keeps everyone she had and gains someone.

**A rule failing the weaker axiom is therefore the serious finding**, and twelve rules fail it.

## The smallest witness: SAV, two voters

<!-- ballots:sav_strategy_bullet_vote_c5_b2 -->
The ballots as marked — a filled **Yes** is a `1` in that candidate's column, a filled **No** a `0`:

| # | Ballot as marked | A | B | C | D | E |
|:--:|:--|:--:|:--:|:--:|:--:|:--:|
| 1 | <img src="cases/img/sav_strategy_bullet_vote_c5_b2_ballot_1.png" width="260" style="min-width:260px" alt="A Yes/No Approval ballot — voter 1 — sincerely approves A, B, C: A Yes, B Yes, C Yes, D No, E No."> | 1 | 1 | 1 | 0 | 0 |
| 2 | <img src="cases/img/sav_strategy_bullet_vote_c5_b2_ballot_2.png" width="260" style="min-width:260px" alt="A Yes/No Approval ballot — voter 2 — approves D and E: A No, B No, C No, D Yes, E Yes."> | 0 | 0 | 0 | 1 | 1 |
<!-- /ballots -->

One seat. [SAV](../01_Learn/Multiwinner_Approval/satisfaction_approval_voting.md) gives each **ballot** one vote and splits it evenly among that ballot's marks. Voter 1's three marks are worth `1/3` each; voter 2's two marks are worth `1/2` each:

```text
honest       SAV scores: d = e = 1/2 ; a = b = c = 1/3     -> {d}
voter 1 reports {a} alone
             SAV scores: a = 1 ; d = e = 1/2               -> {a}
```

Voter 1 goes from a committee containing **none** of her approved candidates to one containing A. She did it by *deleting two honest approvals* — no lie about anyone she dislikes, just a narrower truth.

**The mechanism is SAV's own selling point.** Dividing a vote by ballot length is what lets SAV distinguish these two ballots at all — plain AV ties all five candidates at one approval each and cannot separate them. The same division is what makes shortening a ballot pay. You cannot have the discrimination without the incentive.

The repo's Approval control on this file, showing the five-way tie:

<!-- report:sav_strategy_bullet_vote_c5_b2 -->
```text
--- Approval Voting (single winner) ---
 Tabulating 2 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C, D, E      (1 = approve; 0 = not approved)
     1 × 1,1,1,0,0
     1 × 0,0,0,1,1

   A -- 1 (50%) -- Elected
   B -- 1 (50%)
   C -- 1 (50%)
   D -- 1 (50%)
   E -- 1 (50%)
  Note: A, B, C, D, E each have 1 approval and tie for the last 1 seat.
        Candidate priority order (A > B > C > D > E) broke the tie: A elected, B, C, D, E not elected.

[Approval Distribution] (how many candidates each ballot approved)
   5 approvals across 2 ballots — average 2.5 of 5 (range 2–3).
     approved 2: 1 ballot
     approved 3: 1 ballot

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   A    |   B    |   C    |   D    |   E    |
   -------------------------------------------------
   A  |   --   |  100%  |  100%  |   0%   |   0%   |
   B  |  100%  |   --   |  100%  |   0%   |   0%   |
   C  |  100%  |  100%  |   --   |   0%   |   0%   |
   D  |   0%   |   0%   |   0%   |   --   |  100%  |
   E  |   0%   |   0%   |   0%   |  100%  |   --   |

Winner — Approval Voting (single winner)
  A
```
<!-- /report -->

## Every other rule, same shape

The book gives a witness per rule (Proposition A.4), and all eleven replay. A representative sample:

| Rule | honest ballot → committee | misreport → committee | what she gains |
|---|---|---|---|
| **CC** | `{a,b}` → `{a,c}` | `{b}` → `{a,b}` | keeps `a`, gains `b` |
| **PAV** | `{c,d,e}` → `{b,c,f}` | `{e}` → `{b,c,e}` | keeps `c`, gains `e` |
| **seq-PAV** | `{a,b}` → `{b,c,f}` | `{a}` → `{a,b,f}` | keeps `b`, gains `a` |
| **rev-seq-PAV** | `{a,b,c}` → `{b,d}` | `{a}` → `{a,b}` | keeps `b`, gains `a` |
| **Monroe** | `{b,d}` → `{a,b,e}` | `{f}` → `{b,d,f}` | keeps `b`, gains `d` |
| **seq-Phragmén** | `{a,b,c}` → `{b,f}` | `{c}` → `{b,c}` | keeps `b`, gains `c` |
| **Method of Eq. Shares** | `{b,c,d}` → `{b,d,e}` | `{c}` → `{b,c,d}` | keeps `b,d`, gains `c` |
| **MAV** | `{a,b,c}` → `{a,b,d}` | `{c}` → `{a,b,c}` | keeps `a,b`, gains `c` |

**Notice what almost every manipulation is.** In eight of the eleven the misreport is a *bullet vote* or near-bullet vote — the voter drops most of her honest approvals and concentrates. This is the same incentive that shows up all over approval-style voting, and this repo has it in the STAR setting too: see [bullet voting's backfire](../../01_STAR/05_Practice/ex06_bullet_backfire.md) and [tactical maximization](../../01_STAR/03_Criteria/tactical_maximization/README.md). What the table adds is that under every proportional approval rule the incentive is **structural**, not incidental — the very reweighting that produces proportionality is what makes a shorter ballot more powerful.

## AV's proof, and its limits

AV passes both axioms, and the argument is short enough to hold in your head. Decompose any ballot change into single steps. Disapproving a candidate you truly like can let at most one new candidate onto the committee — and only by removing the one you dropped, so you don't gain. Approving a candidate you dislike can let that candidate replace someone — which doesn't help you either. No single step helps, so no sequence does.

Then the caveats, which matter more than the result:

- **Only under a fixed tiebreaking order on candidates.** Ties are where manipulation lives, and AV's guarantee is stated on the resolute rule.
- **Only for dichotomous preferences.** If a voter actually prefers some approved candidates to others — the realistic case — AV is *not* strategyproof. Her strategic problem simply moves to where the approval threshold goes, which is [the approval voter's real decision](../01_Learn/README.md) and is not modelled by these axioms at all.
- **Strategyproofness is incompatible with proportionality.** Chapter 4 shows even weak proportionality clashes with these axioms. AV's clean row is possible *because* AV promises nothing proportional.

So: **AV is strategyproof in exactly the sense the model defines, and that sense is narrower than the word suggests.** Stating the caveats is not undercutting the claim; it is what keeps the claim usable in an argument.

## Two open cells — and what looked at first like a contradiction

CC and leximax-Phragmén carry `?` in this column. But read Proposition A.4's opening sentence and it lists **both** among the rules that fail inclusion-strategyproofness, and Appendix A hands each one a counterexample. Table and appendix appear to disagree.

They don't, and the reconciliation is worth the detour, because it is a point about counterexamples generally. Build the two witnesses and look at what the **manipulated** profile returns:

| Rule | honest winner | manipulated winners | pays off? |
|---|---|---|---|
| **CC** | `{a,c}` (unique) | `{a,b}` **\|** `{a,c}` | `{a,b}` yes · `{a,c}` **no** |
| **leximax-Phragmén** | `{b,c,d}` (unique) | `{a,b,c}` **\|** `{a,b,d}` **\|** `{a,c,d}` | first two yes · `{a,c,d}` **no** |
| PAV *(for contrast)* | `{b,c,f}` (unique) | `{b,c,e}` (unique) | unconditional |

For CC and leximax-Phragmén the misreport lands the election in a **tie**, and the manipulation pays only if the tiebreak resolves the right way. That is exactly what the proposition's phrase *"without loss of generality we assume that a tie between committee `{a,b}` and `{a,c}` is resolved in favour of `{a,b}`"* is doing — it is choosing the tiebreak that makes the counterexample work. So the honest statement is: **these two rules are manipulable under *some* tiebreaking orders, and whether they are manipulable under *every* one is open.** Every other failing rule in the table is manipulable outright, with a unique winner on both sides.

For PAV, seq-PAV, Monroe, MAV and the rest, no such caveat: the manipulated profile has a unique winner and the misreport pays whatever the tiebreak.

This is machine-checked rather than argued — [`abc_axiom_check.py`](../../06_Other/abcvoting_tabulation_engine/abc_axiom_check.py) computes the paying and non-paying tied committees for every strategy witness and fails if a rule's tiebreak-dependence stops matching its cell, so the `?` and the explanation can't drift apart.

**The transferable lesson:** a counterexample that needs a particular tiebreak is a weaker object than one that doesn't, and the difference is invisible in a grid of ticks and crosses. It only shows up if you run it.

## For this repo's methods

- **Neither STAR nor RCV-IRV is on this grid**, and the nearest single-winner relatives are the [Favorite Betrayal Criterion](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) and later-no-harm — kept distinct from each other and from this, per the [terminology policy](../../07_Concepts/tips/TIPS_terminology.md).
- **The transferable lesson is the trade, not the ranking.** Every rule here that resists manipulation is one that gives up proportionality, and every rule that delivers proportionality can be gamed by narrowing a ballot. That is the honest frame for comparing bloc and proportional methods — better than a checklist, and it cuts against the simple rules as often as for them.

## Reproduce it

```bash
.venv/bin/python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --verbose
```

Twelve inclusion-strategyproofness witnesses replay — one per failing rule.

---

**Related:** [the table](README.md) · [consistency](consistency.md) — the previous column · [computational complexity](computational_complexity.md) — the last · [Gibbard–Satterthwaite](../../07_Concepts/topics/gibbard_satterthwaite_theorem.md) · [SAV](../01_Learn/Multiwinner_Approval/satisfaction_approval_voting.md).
