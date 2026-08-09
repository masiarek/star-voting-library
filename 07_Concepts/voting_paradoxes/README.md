# Voting paradoxes — Felsenthal's catalog, demonstrated

This folder teaches the classic voting paradoxes one page at a time, each backed by a runnable repo election and (where possible) a live BetterVoting election. Cases are tagged in their YAML (`paradoxes: [tag, …]`) and the auto-generated registry groups every tagged case by paradox: **[the paradox registry](../YAML_test_case_index/PARADOX_index.md)**.

**Primary source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / Centre for Philosophy of Natural and Social Science, LSE; revised 26 May 2010. Presented at the Leverhulme Trust *Voting Power in Practice* workshop, Château du Baffy, Normandy, 30 July – 2 August 2010.

## Felsenthal's two kinds of paradox

Felsenthal splits paradoxes into two families, and the split is worth learning before any individual paradox:

**Simple (or "straightforward") paradoxes** — the relevant data *as given* leads to a surprising, arguably undesirable outcome. The "relevant data" include the number of voters and candidates, how many must be elected, every voter's preference ordering, what voters know about each other's preferences, the order of voting, whether voting is open or secret, and how ties are broken. Nothing changes; the result is startling on its own. Example: a candidate whom a majority ranks *last* wins.

**Conditional paradoxes** — *changing one relevant datum while holding everything else constant* changes the outcome in a surprising way. Examples: a hopeless candidate drops out and the winner changes; a candidate gains support and thereby loses.

## Paradox pages (covered)

| Paradox | Also known as | Kind | Page | Demonstrated by |
|---|---|---|---|---|
| Condorcet winner paradox | Thwarted majorities | Simple | [Condorcet winner paradox](condorcet_winner_paradox.md) | [BV2144 Felsenthal Ex.1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) · [BV2137 center squeeze](../../method_comparisons/center_squeeze_bv2137/bv2137_ywckmg_center_squeeze.md) |
| Condorcet loser paradox | Borda's paradox | Simple | [Condorcet loser paradox](condorcet_loser_paradox.md) | [BV2144 Felsenthal Ex.1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) |
| Absolute loser paradox | — | Simple | [Absolute loser paradox](absolute_loser_paradox.md) | [BV2144 Felsenthal Ex.1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) |
| SCC / spoiler | Subset choice condition; IIA failure (informal) | Conditional | [SCC / spoiler](spoiler_scc.md) | [BV2144 Felsenthal Ex.1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) · [BV2145 Felsenthal Ex.2](../../method_comparisons/felsenthal_paradoxes/bv2145_6fj2kg_felsenthal_ex2.md) · [the split-voting set](../../method_comparisons/split_voting/README.md) |
| Non-monotonicity | More-is-less; additional-support; lack of monotonicity | Conditional | [Non-monotonicity](non_monotonicity.md) | [BV2145→BV2146 Felsenthal Ex.2 pair](../../method_comparisons/felsenthal_paradoxes/bv2146_krk2px_felsenthal_ex2_monotonicity.md) · [the monotonicity set](../../method_comparisons/monotonicity/cases/cases_pages/monotonicity_irv_after.md) |
| Reinforcement / multiple-districts | Inconsistency paradox | Conditional | [Reinforcement / multiple-districts](multiple_districts.md) | [BV2147+BV2148→BV2149 Felsenthal Ex.3 trio](../../method_comparisons/felsenthal_paradoxes/bv2149_byk9v2_felsenthal_ex3_reinforcement.md) |
| No-Show + Twin | Participation failure | Conditional | [No-Show + Twin](no_show.md) | [BV2150→BV2151 Felsenthal Ex.4 pair](../../method_comparisons/felsenthal_paradoxes/bv2151_97hbpw_felsenthal_ex4_noshow.md) · [BV2165→BV2166 (STAR flips too)](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md) · [BV2159 (Brams)](../../method_comparisons/paradoxes_and_whoops/bv2159_f4cjpy_brams_irv_pathologies.md) |
| Truncation paradox | Preference-truncation | Conditional | [Truncation paradox](truncation.md) | [BV2162→BV2163 Nurmi pair](../../method_comparisons/felsenthal_paradoxes/bv2163_74j6vv_nurmi_truncation.md) · [BV2160 Borda flavor](../../method_comparisons/felsenthal_paradoxes/bv2160_r6qc8h_fishburn_borda_truncation.md) |

## Covered elsewhere in the repo (tagged, no dedicated page yet)

| Paradox | Also known as | Kind | Repo home |
|---|---|---|---|
| Condorcet's paradox (cycle) | Cyclical majorities | Simple | [BV2157 (rock-paper-scissors)](../../method_comparisons/paradoxes_and_whoops/bv2157_mmcmpy_condorcet_cycle_rps.md) · [cycle resolution](../../05_Ranked_Robin/01_Learn/cycle_resolution.md) |
| Clone dependence / teaming | Cloning paradox | Conditional | [Ranked Robin & clone independence](../../05_Ranked_Robin/01_Learn/rr_clone_independence.md) |
| Favorite betrayal | — | Conditional | [Favorite betrayal](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) |
| Absolute Majority paradox | Majority criterion failure | Simple | [BV2153 Felsenthal Ex.7](../../method_comparisons/felsenthal_paradoxes/bv2153_pcttmr_felsenthal_ex7_absolute_majority.md) |
| Pareto-dominated winner | Pareto violation | Simple | [Felsenthal Ex.6 (LH-only)](../../method_comparisons/felsenthal_paradoxes/felsenthal_ex6_pareto.md) |

## Deliberately not listed: the runoff reversal

The most-asked-about omission. STAR's automatic runoff overturning the scoring leader — "the top-scorer lost!" — is not in this catalog or the registry, on purpose. In Felsenthal's terms nothing paradoxical has happened: no datum changed, and the elected candidate is the finalist a majority of deciding voters prefers — which is exactly the job the "AR" in STAR exists to do. It makes a fine attack line (the [mudroom collection](../../method_comparisons/mudroom/_star_whoops.md) keeps it honest), but a designed mechanism doing its designed job is a **feature demonstration**, and it is taught as one: [when the runoff overturns the scoring leader](../../01_STAR/02_Examples/runoff_overturns_leader/README.md).

The same bar keeps *strategy backfires* out. [Tactical maximization](../../01_STAR/03_Criteria/tactical_maximization/README.md) — hedged 5s silencing the hedgers' own voice in the runoff — is a criteria lesson, not a paradox: the backfire is even monotone (the raised score helps exactly the candidate it was given to). STAR earns genuine registry entries where it genuinely fails; the no-show pair above catches STAR flipping too, and those cases are tagged like any other. The `paradoxes:` vocabulary itself is controlled by [`build_paradox_index.py`](../../STARVote_LH_tabulation_engine/tools_adam/scripts/build_paradox_index.py), which fails the build on an unknown tag rather than minting a new paradox by accident — extend its VOCAB only for a Felsenthal-style pathology, never for a feature demonstration or a strategy backfire (settled 2026-08-09, when a stray `runoff-reversal` tag was removed rather than adopted).

## Minimal instances and how our examples compare

Our worked examples come from **Felsenthal (2010)** and are chosen for teaching clarity — small, memorable, named casts — not for provable minimality. **Brandt, Matthäus & Saile, *"Minimal voting paradoxes"*, Journal of Theoretical Politics 34(4), 2022** ([DOI](https://doi.org/10.1177/09516298221122104) · [open PDF](https://pub.dss.in.tum.de/brandt-research/minpara.pdf)) settle the companion question with integer-linear-programming: the *smallest* electorate — (candidates *m*, voters *n*) — that forces each paradox, for 13 ranked rules. Cross-checking our pages against their Table 3:

| Our example | Rule · paradox | Ours (*m*, *n*) | Paper minimal | Status |
|---|---|---|---|---|
| [BV2144 (Felsenthal Ex.1)](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) | Plurality · Condorcet winner | 3, 7 | 3, 7 | ✅ **provably minimal** |
| [BV2144](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) | Plurality · Condorcet loser | 3, 7 | 3, 7 | ✅ **provably minimal** |
| [BV2144](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) | Plurality · absolute loser | 3, 7 | 3, 7 | ✅ **provably minimal** |
| [BV2144](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) | Plurality · SCC / subset choice | 3, 7 | 3, 7 | ✅ **provably minimal** |
| [BV2145→46 (Ex.2)](../../method_comparisons/felsenthal_paradoxes/bv2146_krk2px_felsenthal_ex2_monotonicity.md) | IRV · non-monotonicity (add'l support) | 3, 17 | 3, 17 | ✅ **provably minimal** (at 3 cand.) |
| [BV2150→51 (Ex.4)](../../method_comparisons/felsenthal_paradoxes/bv2151_97hbpw_felsenthal_ex4_noshow.md) | IRV · no-show | 3, 11 | 3, 11 | ✅ **provably minimal** |
| [Coombs Ex.19](coombs.md#example-19-no-show-and-truncation-live-pair-bv2165-bv2166) ([BV2165/66](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md)) | Coombs · no-show | 3, 15 | 3, 15 | ✅ **provably minimal** (at 3 cand.) |
| [BV2147/48→49 (Ex.3)](../../method_comparisons/felsenthal_paradoxes/bv2149_byk9v2_felsenthal_ex3_reinforcement.md) | Plurality-runoff · reinforcement | 3, 32 | 3, 15 | larger (Felsenthal's electorate) |
| [Coombs Ex.17](coombs.md#example-17-the-condorcet-winner-is-deleted-first-live-bv2164) ([BV2164](../../method_comparisons/felsenthal_paradoxes/bv2164_xbqq8t_coombs_cw.md)) | Coombs · Condorcet winner | 4, 33 | 3, 13 / 4, 9 | larger — **and refutes a conjecture** (below) |
| [Coombs Ex.20](coombs.md#example-20-reinforcement-paper-only-source-typo-flagged) | Coombs · reinforcement | 3, 41 | 3, 13 | larger |
| [Coombs Ex.22](coombs.md#example-22-scc-paper-only) | Coombs · SCC | 4, 29 | 4, 7 | larger |
| [Minimax Ex.29](minimax.md#example-29-minimax-elects-the-condorcet-and-absolute-loser-live-bv2167) ([BV2167](../../method_comparisons/felsenthal_paradoxes/bv2167_f3dxq9_minimax_absolute_loser.md)) | Maximin · Condorcet & absolute loser | 4, 11 | 4, 9 | slightly larger |
| [Minimax Ex.30](minimax.md#example-30-no-show-and-twin-hannu-nurmi-private-communication-2222010) | Maximin · no-show | 4, 19 | 4, 9 | larger |
| [Minimax Ex.32](minimax.md#example-32-reinforcement) | Maximin · reinforcement | 4, 14 | 3, 15 / 5, 9 | comparable |
| [Minimax Ex.33](minimax.md#example-33-scc-adapted-from-fishburn-1974-540) | Maximin · SCC | 4, 7 | 3, 7 | one candidate more |

**Two takeaways.** (1) The BV2144 quartet and the monotonicity/no-show pairs are already the mathematically smallest possible — a nice, citable validation that the sharpest teaching cases are also the tightest. (2) The larger cases are Felsenthal's own historical electorates; we keep them for their named casts and live BV backing, but now have a reference for how far they *could* shrink. The paper studies only ranked rules and Felsenthal's *nine* paradoxes, so our **truncation** pages (score/ranked, and 103-voter Nurmi), **range voting** and **majority judgment** (score methods), and **successive-elimination** examples fall outside its scope — no minimal to compare against.

## Planned (from the wider literature)

Ostrogorski's paradox, Anscombe's paradox, the paradox of multiple elections, dedicated pages for the Absolute-Majority and Pareto-dominated paradoxes, and Simpson's paradox — each gets a page + a tagged case as examples are built.

**Every worked-tables page is now runnable.** Four procedures that no engine here could count — Coombs (§A7), Minimax (§A10), successive elimination (§A4), and the two grade methods, Range Voting (§A8) and Majority Judgment (§A9) — have tabulators in [`tools_adam/pref_voting_tabulation_engine/`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/README.md), each cross-checked against `pref_voting` where a counterpart exists:

| Page | Tool | Levers it exposes |
|---|---|---|
| [coombs.md](coombs.md) | `coombs_report.py` | `--drop` (SCC) |
| [minimax.md](minimax.md) | `minimax_report.py` | `--drop`, `--equal-prob` (truncation convention) |
| [successive_elimination.md](successive_elimination.md) | `successive_elimination_report.py` | `--agenda` (path independence), `--tiebreak`, `--drop` |
| [range_voting.md](range_voting.md) · [majority_judgment.md](majority_judgment.md) | `grade_methods_report.py` | `--ungrade` (truncation), `--abstain` (no-show) |

**These pages are the case *against* a method — start with the method.** Each of the two grade procedures has a front door that shows its ballot, its count worked on a small election, and its pros and cons: [Range / Score Voting](../../06_Other/Range/concepts/range_voting.md) and [Majority Judgment](../../06_Other/Majority_Judgment/concepts/majority_judgment.md). Landing on a paradox first is landing in the middle of an argument.

**Every example on those pages is a case file**, ballots or grades in YAML rather than in a parenthetical. All 27 counts reproduce Felsenthal's published results, with three documented exceptions that the pages state rather than smooth over: **Minimax Ex.31**'s winner depends on a truncation convention; **successive elimination Ex.10**'s amalgamated round 1 is a 2:2 tie, not the win the page used to assert, so its reinforcement failure holds only under one tie-break reading; and **MJ Ex.26** has no case file at all, because its grade tables live in the source and were never reproduced here.

The [summability demo](../../method_comparisons/summability_demo/README.md) is the operational cousin of reinforcement (district-by-district counting) and is cross-linked from [multiple_districts.md](multiple_districts.md).

## Further reading

Felsenthal (2010), above, is the backbone. Felsenthal & Maoz (1988) supply Examples 5 and 6 of its Approval appendix; Fishburn (1974: 543) and Nurmi (1999: 63) supply the Borda and RCV-IRV truncation examples (14 and 16). Also consulted for this set: P.C. Fishburn, *"Paradoxes of Voting"*, American Political Science Review 68 (1974) — five paradoxes with computer-simulated frequencies; Fishburn & Brams, *"Paradoxes of Preferential Voting"*, Mathematics Magazine 56 (1983) — no-show, thwarted-majorities, multiple-districts, more-is-less; Plassmann & Tideman, *"How frequently do different voting rules encounter voting paradoxes in three-candidate elections?"* — empirical frequencies; Brandt, Matthäus & Saile, *"Minimal voting paradoxes"* (J. Theoretical Politics 34(4), 2022) — the ILP-computed *smallest* electorate for each paradox across 13 ranked rules, cross-checked against our examples above; Brandt, Geist & Strobel (2016) on the complementary question of paradox *frequency* (Ehrhart theory, simulations, empirical data); Gehrlein & Lepelley on the interpretations of majority rule with 3+ candidates — complete and transitive individual preferences, and Condorcet's (1785) view of cyclic preferences as a "contradiction of terms"; and a friendly popular overview: [Tizkova, "Paradoxes of voting systems" (Medium, 2024)](https://tereza-tizkova.medium.com/paradoxes-of-voting-systems-c9a647fc7ead) — Arrow, cycles, monotonicity, killer amendments, median voter.

Adam's working docs (Google): [Index — topic pages / FAQ](https://docs.google.com/document/u/0/d/1ChP00lDS4c8v30KxqZ8dC5EnqHVmQnjrbISQZBWWPVs/edit) · [Condorcet Paradox](https://docs.google.com/document/d/1YpBuOfTKP8IQM4BRBNheOALHs_Ea0-mBYU1VoJnwqm0/edit) · [Truncation Paradox](https://docs.google.com/document/d/16JjV_KmSEexEhIoKAYcKolzzVzHStIf13VjMry-EJHs/edit) · [Majoritarian Failure](https://docs.google.com/document/d/1jmOmEmbLBZVZtzEV57y9QXENL7L6A-NjGRqKEBvUpAs/edit) · [Compromise Voting Failure](https://docs.google.com/document/d/18GgX5WHTu5HuVMwtu6gXeK5hZJ23cyUui24w4ZLaEBQ/edit) · [compare STAR and score voting](https://docs.google.com/document/d/1gOLvcX2OYZQ7K4sXaWyZnthl17ar9hkNjO_25wlViBI/edit?tab=t.0)
