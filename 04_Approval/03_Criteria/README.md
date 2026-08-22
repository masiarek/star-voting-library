# 04_Approval/03_Criteria — what the approval committee rules actually guarantee

**Level: 301 · deep dive**

Chapter 2 of Lackner & Skowron's [*Multi-Winner Voting with Approval Preferences*](https://link.springer.com/book/10.1007/978-3-031-09016-5) introduces the approval-based committee (ABC) rules; this repo covers those in [`01_Learn/Multiwinner_Approval/`](../01_Learn/Multiwinner_Approval/README.md). Chapter 3 asks the harder question — **which of them keep their promises** — and answers it with one grid, Table 3.1.

This folder is that grid, **recomputed rather than copied** — plus two pages for axioms the grid does not carry: [Condorcet committees](condorcet_committees.md), which Chapter 3 discusses but does not tabulate (on approval ballots the thing it asks for usually does not exist), and [resignation monotonicity](resignation_monotonicity.md), which postdates the book. Every ✗ below is a theorem with a witness: a specific tiny approval profile on which the rule visibly misbehaves. The book prints those witnesses in Appendix A; [`abc_axiom_check.py`](../../06_Other/abcvoting_tabulation_engine/abc_axiom_check.py) replays all thirty of them through [`abcvoting`](https://github.com/martinlackner/abcvoting), Lackner's own peer-reviewed implementation, and the run is gated by [`tests/test_abc_axioms.py`](../../STARVote_LH_tabulation_engine/tests/test_abc_axioms.py).

## Table 3.1, recomputed

| Rule | Pareto efficiency | Committee monoton. | Support monoton. *with* add. voters | Support monoton. *without* add. voters | Consistency | Inclusion-strategypr. | Complexity |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **AV** | strong | ✓ | ✓ | ✓ | ✓ | ✓ | P |
| **CC** | weak | ✗ | ✓ | cand | ✓ | ? | NP-hard |
| **PAV** | strong | ✗ | ✓ | cand | ✓ | ✗ | NP-hard |
| **seq-PAV** | ✗ | ✓ | cand | cand | ✗ | ✗ | P |
| **seq-CC** | ✗ | ✓ | cand | cand | ✗ | ✗ | P |
| **rev-seq-PAV** | ✗ | ✓ | ✓ | cand | ✗ | ✗ | P |
| **Monroe** | ✗ | ✗ | ✗ | cand | ✗ | ✗ | NP-hard |
| **Greedy Monroe** | ✗ | ✗ | ✗ | cand | ✗ | ✗ | P |
| **seq-Phragmén** | ✗ | ✓ | cand | cand | ✗ | ✗ | P |
| **leximax-Phragmén** | ✗ | ✗ | cand | cand | ✗ | ? | NP-hard |
| **Method of Eq. Shares** | ✗ | ✗ | ✗ | cand | ✗ | ✗ | P |
| **MAV** | weak | ✗ | ✓ | cand | ✗ | ✗ | NP-hard |
| **SAV** | strong | ✓ | ✓ | ✓ | ✓ | ✗ | P |

`cand` = **candidate** monotonicity holds (the axiom for a single candidate) but **support** monotonicity does not (it fails for some *group* of candidates). `?` = open. Column detail on the pages below.

**Read the first row and the last row together.** AV passes everything and SAV passes everything but strategyproofness — and they are the only two rules here that do. Every rule with a serious proportionality claim (PAV, the Phragméns, Monroe, Equal Shares) buys it by failing something in this grid. That is not an argument against proportional rules; it is the price list, and Chapter 4 is where the thing being bought gets defined.

## What is verified here, and what is not

The distinction matters, so it is stated rather than implied:

- **Every ✗ is DEMONSTRATED.** Run the witness, watch the axiom break. Proof by counterexample is complete, and thirty of them replay on demand.
- **No ✓ is demonstrated, and none can be.** "No profile anywhere violates this" is a universal claim that no finite replay settles. Ticks are **cited** to the book's Propositions A.1–A.4. `--search` will hunt for a violation on random small profiles, which can only ever *fail to refute* a tick — worth running (it catches a mis-transcribed cell), not a proof.
- **Two cells are open questions**, not omissions: inclusion-strategyproofness for CC and for leximax-Phragmén. See below — the reason is more interesting than "nobody got round to it".

**Building the table this way paid for itself twice.**

The draft of [the committee-monotonicity case](cases/abc_committee_monotonicity_1seat_c3_b10.yaml) claimed all thirteen rules elect the consensus candidate at one seat. Eleven do. SAV and rev-seq-PAV pick a different candidate, because SAV divides each ballot's vote among its marks and the two factional candidates out-score the consensus one 3.5 to 3. Nothing in the printed table says that — it is only visible from a run.

And the two `?` cells turn out to be a genuine subtlety rather than a gap. Table 3.1 leaves CC and leximax-Phragmén open for strategyproofness, while Proposition A.4's prose lists **both** among the rules that fail it and gives each a counterexample — an apparent contradiction inside the book. Replaying them resolves it: for exactly those two rules the manipulated profile ends in a **tie**, so the misreport pays only under a tiebreak that lands the right way (the proposition's *"without loss of generality we assume that a tie … is resolved in favour of `{a,b}`"* is carrying the argument). Every other failing rule is manipulable outright, with a unique winner on both sides. Worked through on [the strategyproofness page](inclusion_strategyproofness.md), and pinned by a test so the cell and the explanation cannot drift apart.

## The columns

| Page | The question it asks |
|---|---|
| [Pareto efficiency](pareto_efficiency.md) | Can the rule elect a committee that **every voter** would trade away for another? |
| [Committee monotonicity](committee_monotonicity.md) | Add a seat — does the rule **add** a member, or reshuffle the whole committee? |
| [Support monotonicity](support_monotonicity.md) | More approvals for a winner: can that **cost** them their seat? And why "some group" is harder than "one candidate". |
| [Consistency](consistency.md) | Two electorates agree. Do they still agree when merged? — and the characterisation that makes this the deepest column in the table. |
| [Inclusion-strategyproofness](inclusion_strategyproofness.md) | Can a voter do better by **misreporting** her approvals? AV alone says no. |
| [Computational complexity](computational_complexity.md) | P or NP-hard — and why "just compute the optimum" is not available. |
| [Condorcet committees](condorcet_committees.md) *(§3.2, not a Table 3.1 column)* | Lift "beats everyone head to head" to committees — and find that on approval ballots there is usually **nothing** that qualifies. |
| [Resignation monotonicity](resignation_monotonicity.md) *(Oh & Peters 2026, not in the book)* | A winner **resigns** and the count is re-run. Can it unseat somebody who stayed? AV alone says no — and so, it turns out, do none of this engine's score-based PR rules. |

## The runnable cases

| Case | What it shows | Page | YAML |
|---|---|---|---|
| CC elects a dominated committee | Two voters, four candidates: the smallest Pareto failure in the book | [page](cases/cases_pages/cc_pareto_dominated_c4_b2.md) | [`cc_pareto_dominated_c4_b2.yaml`](cases/cc_pareto_dominated_c4_b2.yaml) |
| Monroe elects a committee everyone would trade away | Example 3.1 — equal-sized constituencies vs. Pareto | [page](cases/cases_pages/monroe_pareto_dominated_c4_b24.md) | [`monroe_pareto_dominated_c4_b24.yaml`](cases/monroe_pareto_dominated_c4_b24.yaml) |
| Committee monotonicity (1 of 2) — one seat | The consensus candidate takes the single seat | [page](cases/cases_pages/abc_committee_monotonicity_1seat_c3_b10.md) | [`abc_committee_monotonicity_1seat_c3_b10.yaml`](cases/abc_committee_monotonicity_1seat_c3_b10.yaml) |
| Committee monotonicity (2 of 2) — two seats | Add a seat, and five rules drop the one-seat winner | [page](cases/cases_pages/abc_committee_monotonicity_2seats_c3_b10.md) | [`abc_committee_monotonicity_2seats_c3_b10.yaml`](cases/abc_committee_monotonicity_2seats_c3_b10.yaml) |
| SAV rewards a bullet vote | Two voters: narrowing an honest ballot wins the seat | [page](cases/cases_pages/sav_strategy_bullet_vote_c5_b2.md) | [`sav_strategy_bullet_vote_c5_b2.yaml`](cases/sav_strategy_bullet_vote_c5_b2.yaml) |
| Resignation (1 of 6) — STAR-PR seats the lone voter | Allocated Score gives the four-voter bloc one seat and the lone voter the other | [page](cases/cases_pages/resign_star_pr_seated_c4_b5.md) | [`resign_star_pr_seated_c4_b5.yaml`](cases/resign_star_pr_seated_c4_b5.yaml) |
| Resignation (2 of 6) — Bruno resigns, Ana is evicted | Re-run the same count minus one column and the bloc takes both seats | [page](cases/cases_pages/resign_star_pr_after_bruno_c3_b5.md) | [`resign_star_pr_after_bruno_c3_b5.yaml`](cases/resign_star_pr_after_bruno_c3_b5.yaml) |
| Resignation (3 of 6) — RRV's three seats | Reweighted Range Voting elects two one-supporter winners and a slate leader | [page](cases/cases_pages/resign_rrv_seated_c5_b5.md) | [`resign_rrv_seated_c5_b5.yaml`](cases/resign_rrv_seated_c5_b5.yaml) |
| Resignation (4 of 6) — Hana resigns, Gus is evicted | The vacated seat goes to the slate that lost its own winner | [page](cases/cases_pages/resign_rrv_after_hana_c4_b5.md) | [`resign_rrv_after_hana_c4_b5.yaml`](cases/resign_rrv_after_hana_c4_b5.yaml) |
| Resignation (5 of 6) — the Approval control | Oh & Peters' Example 3.3, counted by plain multi-winner Approval | [page](cases/cases_pages/resign_av_holds_c7_b5.md) | [`resign_av_holds_c7_b5.yaml`](cases/resign_av_holds_c7_b5.yaml) |
| Resignation (6 of 6) — Kai resigns, Approval holds | Every survivor keeps their seat, where PAV and Equal Shares cannot | [page](cases/cases_pages/resign_av_holds_after_kai_c6_b5.md) | [`resign_av_holds_after_kai_c6_b5.yaml`](cases/resign_av_holds_after_kai_c6_b5.yaml) |

Each case file's own count is plain **Approval** — the control, showing what AV does with the same ballots. The rule under test is counted by `abcvoting`, because CC, PAV, Monroe, leximax-Phragmén, Equal Shares, MAV and SAV exist in neither the [LH engine](../../STARVote_LH_tabulation_engine/README.md) nor [BetterVoting](https://bettervoting.com/). That is also why these cases are LH-only.

## Reproduce the whole table

```bash
.venv/bin/python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --verbose
```

Add `--search 400` to hunt for a Pareto violation among the rules the book marks *strong*; a hit would refute the table, a miss proves nothing.

## References

- Lackner, M. & Skowron, P. (2023), *Multi-Winner Voting with Approval Preferences*, SpringerBriefs, [doi:10.1007/978-3-031-09016-5](https://doi.org/10.1007/978-3-031-09016-5) (open access) — Chapter 3 and Appendix A, Propositions A.1–A.4.
- Sánchez-Fernández, L. & Fisteus, J. A. (2019), "Monotonicity axioms in approval-based multi-winner voting rules" — the source of the support-monotonicity analysis.
- Peters, D. (2018), "Proportionality and strategyproofness in multiwinner elections" — the source of the two strategyproofness notions.

---

**Related:** the rules themselves → [Multiwinner Approval](../01_Learn/Multiwinner_Approval/README.md) · the spectrum they sit on → [ABC rules and the utilitarian–egalitarian spectrum](../01_Learn/Multiwinner_Approval/abc_rules_spectrum.md) · the single-winner criteria grid → [Criteria at a glance](../../07_Concepts/topics/criteria_at_a_glance.md) · the maths behind the complexity column → [Math for social choice](../../07_Concepts/topics/math_for_social_choice.md).
