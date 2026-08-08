# The successive-elimination procedure — one agenda, five paradoxes

*The **successive elimination** procedure (the parliamentary/amendment procedure): candidates meet in pairwise majority votes in a fixed agenda order; each round's loser is eliminated and the winner meets the next candidate; the last survivor wins.* Neither BetterVoting nor the LH engine implements this procedure — it is a parliamentary practice, not a ballot-box method — so this repo counts it with [`successive_elimination_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/successive_elimination_report.py), and **every example below is a runnable case file**.

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/successive_elimination_report.py --agenda D,A,C,B method_comparisons/felsenthal_paradoxes/cases/succ_elim_ex9_pareto.yaml
```

**Two inputs that are not the ballots.** The **agenda** is an argument, not a detail: under a cycle it picks the winner, which is Example 9's whole point, so `--agenda` is required rather than defaulted. And a tied round has to be broken by something, on which the published examples disagree — Examples 11 and 12 break toward the earlier **letter**, Example 10 calls it **random**, and parliamentary practice lets the incumbent survive (earlier on the **agenda**). `--tiebreak alpha|agenda` selects; the report re-runs the other convention whenever a round tied and tells you if the winner moves. Unlike its Minimax and Coombs siblings there is no `pref_voting` equivalent to check against, so the independent check is structural: every head-to-head comes from the LH engine's own pairwise matrix, and because the procedure is Condorcet-consistent, the report asserts it found the Condorcet winner whenever one exists.

**Source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A4. Felsenthal lists the procedure as vulnerable to the Pareto-dominated, Reinforcement, No-Show, Twin, Truncation, SCC, and Path Independence paradoxes.

## Example 9 — a Pareto-dominated winner (and three more paradoxes from the same 11 voters)

**Case:** [11 voters, four readings](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/succ_elim_ex9_pareto.md)

<!-- ballots:succ_elim_ex9_pareto -->
Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
3:A>B>C>D
2:C>A>B>D
1:C>D>A>B
5:D>A>B>C
```
<!-- /ballots -->

The social preference ordering is **cyclical** (B > C > D > A > B) — a necessary condition for electing a Pareto-dominated candidate here. With the agenda *D vs A*, *winner vs C*, *winner vs B*: D beats A **6:5**, C beats D **6:5**, B beats C **8:3** — **B wins**. But *every* voter prefers **A** to B: a Pareto-dominated candidate is elected ([`pareto`](../YAML_test_case_index/PARADOX_index.md); the Approval flavor of the same paradox is runnable: [Felsenthal Ex.6](../../method_comparisons/felsenthal_paradoxes/felsenthal_ex6_pareto.md)). The report detects that unanimity itself and flags it, rather than leaving you to check eleven ballots by eye.

The same 11 voters yield three more paradoxes by changing one datum each. Each is a flag on the same file:

| Vary | Command | Result |
|---|---|---|
| nothing | `--agenda D,A,C,B` | **B** — Pareto-dominated; all 11 voters rank A above B |
| the agenda | `--agenda A,B,C,D` | **D** — A beats B 11:0, A beats C 8:3, then D beats A 6:5 |
| the field | `--drop D --agenda A,C,B` | **A** — a non-winner's presence had decided it: [SCC](spoiler_scc.md) |
| the turnout | [the no-show file](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/succ_elim_ex9_noshow.md) | **A** — two D-voters stay home and get their better outcome |

**Path independence** is the second row: same ballots, different agenda, different winner. Under a cycle the agenda-setter, not the electorate, picks the winner — and the report says so out loud, because with no Condorcet winner it tells you to expect exactly that. The fourth row is the [No-Show paradox](no_show.md): once two D ballots are gone the cycle breaks, A is the Condorcet winner, and the agenda stops mattering at all.

## Example 10 — Reinforcement failure

**Cases:** [District I](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/succ_elim_ex10_district1.md) · [District II](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/succ_elim_ex10_district2.md) · [amalgamated](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/succ_elim_ex10_amalgamated.md)

District I (3 voters): `A>B>C>D`, `B>D>C>A`, `D>C>A>B`. District II (1 voter): `C>D>B>A`. Agenda in each district: *B vs D*, *winner vs A*, *winner vs C* — **C wins in both districts**.

Amalgamate the four voters, same agenda, and **all three rounds tie 2:2**. The winner is therefore decided entirely by the tie-break convention: earlier-letter gives **C**, agreeing with both districts and producing *no* paradox at all; earlier-on-the-agenda gives **B**, which neither district chose, and that is the Reinforcement failure. Felsenthal calls the break random and claims only that b *can* win — which is exactly right, and narrower than it first reads.

> **Correction.** This page previously said "b beats d in round 1." It does not; that round is a 2:2 tie like the other two. Running the file is what caught it.

The runnable ballot-box version of this paradox (plurality-with-runoff) is the live trio [BV2147/48/49](../../method_comparisons/felsenthal_paradoxes/bv2149_byk9v2_felsenthal_ex3_reinforcement.md) ([multiple_districts.md](multiple_districts.md)).

## Example 11 — the Twin paradox (Moulin 1988b: 54)

**Cases:** [before](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/succ_elim_ex11_twin_before.md) → [after the twin joins](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/succ_elim_ex11_twin_after.md)

<!-- ballots:succ_elim_ex11_twin_before -->
Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:A>B>C
2:B>C>A
1:C>A>B
1:C>B>A
```
<!-- /ballots -->

Agenda *A vs B*, *winner vs C*; ties break lexicographically (toward the earlier letter). Round 1: A ties B 3:3 → **A** advances; round 2: **C beats A** 4:2 and wins. The single `C>B>A` voter should welcome a *twin* — another `C>B>A` voter. But with that twin added, **B becomes the Condorcet winner** (beating A 4:3 and C 4:3) and wins the procedure — and the original `C>B>A` voter prefers C, the old winner, to B: the twin's arrival made them worse off ([no_show.md](no_show.md) covers the twin's runnable runoff flavor, [BV2150/51](../../method_comparisons/felsenthal_paradoxes/bv2151_97hbpw_felsenthal_ex4_noshow.md)).

Nothing insincere happened. No preference changed, no candidate entered or left, and the added ballot was a perfect copy of one already cast — the most ordinary thing a supporter can do, and it cost their side the election.

## Example 12 — the Truncation paradox

**Cases:** [sincere](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/succ_elim_ex12_sincere.md) → [truncated](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/succ_elim_ex12_truncated.md)

<!-- ballots:succ_elim_ex12_sincere -->
Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
1:A>B>C>D
1:C>B>A>D
2:C>D>B>A
2:D>A>B>C
```
<!-- /ballots -->

Agenda *B vs C*, *winner vs D*, *winner vs A*; ties break toward the earlier letter. Sincere: B ties C 3:3 → **B**; **D beats B** 4:2; **D beats A** 4:2 — D wins, the `A>B>C>D` voter's *last* choice. Now let that voter **truncate** to just `A` (participating only where A stands): round 1 **C beats B** 3:2; round 2 **C beats D** 3:2; round 3 A ties C 3:3 → **A wins**. Revealing *less* of the ballot got the voter their *first* choice instead of their last — the Truncation paradox ([`truncation`](../YAML_test_case_index/PARADOX_index.md); its IRV flavor lurks in [BV2159 (Brams)](../../method_comparisons/paradoxes_and_whoops/bv2159_f4cjpy_brams_irv_pathologies.md)).

Two honest caveats the file makes visible. The final round is a 3:3 tie, so A's win leans on the earlier-letter convention — under the agenda-order reading C survives instead, still an improvement on D for the truncator but not their first choice. And the voter never misrepresents anything: they withhold a preference rather than invert one, which is why the lever exists at all in a procedure that lets a ballot sit out a round.

## Why this procedure matters anyway

Successive elimination is not a ballot-box method — it *is* how legislatures vote on amendments (compare the killer-amendment story in the [Tizkova overview](https://tereza-tizkova.medium.com/paradoxes-of-voting-systems-c9a647fc7ead)). Its paradoxes are therefore not hypothetical: agenda power, strategic absence, and strategic silence are standing features of parliamentary practice. For ballot-box methods, every paradox on this page has a runnable cousin elsewhere in this folder.
