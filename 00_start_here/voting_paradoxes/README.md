# Voting paradoxes — Felsenthal's catalog, demonstrated

This folder teaches the classic voting paradoxes one page at a time, each backed by a runnable repo election and (where possible) a live BetterVoting election. Cases are tagged in their YAML (`paradoxes: [tag, …]`) and the auto-generated registry groups every tagged case by paradox: **[PARADOX_index.md](../YAML_test_case_index/PARADOX_index.md)**.

**Primary source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / Centre for Philosophy of Natural and Social Science, LSE; revised 26 May 2010. Presented at the Leverhulme Trust *Voting Power in Practice* workshop, Château du Baffy, Normandy, 30 July – 2 August 2010.

## Felsenthal's two kinds of paradox

Felsenthal splits paradoxes into two families, and the split is worth learning before any individual paradox:

**Simple (or "straightforward") paradoxes** — the relevant data *as given* leads to a surprising, arguably undesirable outcome. The "relevant data" include the number of voters and candidates, how many must be elected, every voter's preference ordering, what voters know about each other's preferences, the order of voting, whether voting is open or secret, and how ties are broken. Nothing changes; the result is startling on its own. Example: a candidate whom a majority ranks *last* wins.

**Conditional paradoxes** — *changing one relevant datum while holding everything else constant* changes the outcome in a surprising way. Examples: a hopeless candidate drops out and the winner changes; a candidate gains support and thereby loses.

## Paradox pages (covered)

| Paradox | Also known as | Kind | Page | Demonstrated by |
|---|---|---|---|---|
| Condorcet winner paradox | Thwarted majorities | Simple | [condorcet_winner_paradox.md](condorcet_winner_paradox.md) | [BV2144 Felsenthal Ex.1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) · [BV2137 center squeeze](../../method_comparisons/center_squeeze_bv2137/bv2137_ywckmg_center_squeeze.md) |
| Condorcet loser paradox | Borda's paradox | Simple | [condorcet_loser_paradox.md](condorcet_loser_paradox.md) | [BV2144 Felsenthal Ex.1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) |
| Absolute loser paradox | — | Simple | [absolute_loser_paradox.md](absolute_loser_paradox.md) | [BV2144 Felsenthal Ex.1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) |
| SCC / spoiler | Subset choice condition; IIA failure (informal) | Conditional | [spoiler_scc.md](spoiler_scc.md) | [BV2144 Felsenthal Ex.1](../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md) · [BV2145 Felsenthal Ex.2](../../method_comparisons/felsenthal_paradoxes/bv2145_6fj2kg_felsenthal_ex2.md) · [the split-voting set](../../method_comparisons/split_voting/) |
| Non-monotonicity | More-is-less; additional-support; lack of monotonicity | Conditional | [non_monotonicity.md](non_monotonicity.md) | [BV2145→BV2146 Felsenthal Ex.2 pair](../../method_comparisons/felsenthal_paradoxes/bv2146_krk2px_felsenthal_ex2_monotonicity.md) · [the monotonicity set](../../method_comparisons/monotonicity/monotonicity_pages/monotonicity_irv_after.md) |
| Reinforcement / multiple-districts | Inconsistency paradox | Conditional | [multiple_districts.md](multiple_districts.md) | [BV2147+BV2148→BV2149 Felsenthal Ex.3 trio](../../method_comparisons/felsenthal_paradoxes/bv2149_byk9v2_felsenthal_ex3_reinforcement.md) |
| No-Show + Twin | Participation failure | Conditional | [no_show.md](no_show.md) | [BV2150→BV2151 Felsenthal Ex.4 pair](../../method_comparisons/felsenthal_paradoxes/bv2151_97hbpw_felsenthal_ex4_noshow.md) · [BV2165→BV2166 (STAR flips too)](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md) · [BV2159 (Brams)](../../method_comparisons/paradoxes_and_whoops/bv2159_f4cjpy_brams_irv_pathologies.md) |
| Truncation paradox | Preference-truncation | Conditional | [truncation.md](truncation.md) | [BV2162→BV2163 Nurmi pair](../../method_comparisons/felsenthal_paradoxes/bv2163_74j6vv_nurmi_truncation.md) · [BV2160 Borda flavor](../../method_comparisons/felsenthal_paradoxes/bv2160_r6qc8h_fishburn_borda_truncation.md) |

## Covered elsewhere in the repo (tagged, no dedicated page yet)

| Paradox | Also known as | Kind | Repo home |
|---|---|---|---|
| Condorcet's paradox (cycle) | Cyclical majorities | Simple | [BV2157 (rock-paper-scissors)](../../method_comparisons/paradoxes_and_whoops/bv2157_mmcmpy_condorcet_cycle_rps.md) · [cycle_resolution.md](../RCV_Ranked_Robin/cycle_resolution.md) |
| Clone dependence / teaming | Cloning paradox | Conditional | [rr_clone_independence.md](../RCV_Ranked_Robin/rr_clone_independence.md) |
| Favorite betrayal | — | Conditional | [favorite_betrayal_voting_301.md](../STAR_Voting/favorite_betrayal_voting_301.md) |
| Absolute Majority paradox | Majority criterion failure | Simple | [BV2153 Felsenthal Ex.7](../../method_comparisons/felsenthal_paradoxes/bv2153_pcttmr_felsenthal_ex7_absolute_majority.md) |
| Pareto-dominated winner | Pareto violation | Simple | [Felsenthal Ex.6 (LH-only)](../../method_comparisons/felsenthal_paradoxes/felsenthal_ex6_pareto.md) |

## Planned (from the wider literature)

Ostrogorski's paradox, Anscombe's paradox, the paradox of multiple elections, dedicated pages for the Absolute-Majority and Pareto-dominated paradoxes, and Simpson's paradox — each gets a page + a tagged case as examples are built. Procedures without tabulators anywhere in the stack get worked-tables pages: [successive_elimination.md](successive_elimination.md) (Felsenthal §A4), [coombs.md](coombs.md) (§A7 — with Ex.17 and the Ex.19 no-show pair live as BV2164–66), [range_voting.md](range_voting.md) (§A8 — the mean vs the majority, two candidates suffice; includes why STAR's runoff exists), [majority_judgment.md](majority_judgment.md) (§A9, per Felsenthal & Machover 2008 — the median inherits the mean's diseases plus a tie-break reinforcement failure), and [minimax.md](minimax.md) (§A10 — Simpson-Kramer's smallest-worst-loss rule electing the Condorcet-and-absolute loser, Ex.29 live as BV2167). The [summability demo](../../method_comparisons/summability_demo/README.md) is the operational cousin of reinforcement (district-by-district counting) and is cross-linked from [multiple_districts.md](multiple_districts.md).

## Further reading

Felsenthal (2010), above, is the backbone. Felsenthal & Maoz (1988) supply Examples 5 and 6 of its Approval appendix; Fishburn (1974: 543) and Nurmi (1999: 63) supply the Borda and RCV-IRV truncation examples (14 and 16). Also consulted for this set: P.C. Fishburn, *"Paradoxes of Voting"*, American Political Science Review 68 (1974) — five paradoxes with computer-simulated frequencies; Fishburn & Brams, *"Paradoxes of Preferential Voting"*, Mathematics Magazine 56 (1983) — no-show, thwarted-majorities, multiple-districts, more-is-less; Plassmann & Tideman, *"How frequently do different voting rules encounter voting paradoxes in three-candidate elections?"* — empirical frequencies; Brandt, Geist & Strobel on minimal voter/candidate counts for each paradox (computational optimization); Gehrlein & Lepelley on the interpretations of majority rule with 3+ candidates — complete and transitive individual preferences, and Condorcet's (1785) view of cyclic preferences as a "contradiction of terms"; and a friendly popular overview: [Tizkova, "Paradoxes of voting systems" (Medium, 2024)](https://tereza-tizkova.medium.com/paradoxes-of-voting-systems-c9a647fc7ead) — Arrow, cycles, monotonicity, killer amendments, median voter.

Adam's working docs (Google): [Index — topic pages / FAQ](https://docs.google.com/document/u/0/d/1ChP00lDS4c8v30KxqZ8dC5EnqHVmQnjrbISQZBWWPVs/edit) · [Condorcet Paradox](https://docs.google.com/document/d/1YpBuOfTKP8IQM4BRBNheOALHs_Ea0-mBYU1VoJnwqm0/edit) · [Truncation Paradox](https://docs.google.com/document/d/16JjV_KmSEexEhIoKAYcKolzzVzHStIf13VjMry-EJHs/edit) · [Majoritarian Failure](https://docs.google.com/document/d/1jmOmEmbLBZVZtzEV57y9QXENL7L6A-NjGRqKEBvUpAs/edit) · [Compromise Voting Failure](https://docs.google.com/document/d/18GgX5WHTu5HuVMwtu6gXeK5hZJ23cyUui24w4ZLaEBQ/edit) · [compare STAR and score voting](https://docs.google.com/document/d/1gOLvcX2OYZQ7K4sXaWyZnthl17ar9hkNjO_25wlViBI/edit?tab=t.0)
