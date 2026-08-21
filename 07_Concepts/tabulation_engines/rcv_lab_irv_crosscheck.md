# Cross-checking our IRV cases against rcv-lab.org

**Level: reference · deep dive**

**One line:** every ranked RCV-IRV case in this library was re-counted by an outside engine — [rcv-lab.org](rcv_lab.md) — and **63 of 64 agreed**; the one that didn't turned out to be a hidden tie in one of our own cases, which is exactly what a cross-check is for.

→ the platform: [RCV Lab](rcv_lab.md) · sibling referees: [`pref_voting`](cross_checking_with_pref_voting.md) · [BetterVoting](bettervoting_and_the_engine.md) · [RCTab](rctab.md) · tool: `build_rcvlab_sankey.py`.

---

## Why bother

The [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) cases get counted three ways — this engine, BetterVoting, and `pref_voting`'s independent Copeland — because a tally that only ever agrees with itself is not evidence. The RCV-IRV cases had no such leg: the [vendored `pyrankvote` engine](../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/README.md) was the only thing counting them. This closes that gap.

## What was run

All **64** ranked cases with an IRV method, converted to RCV Lab's generic CVR CSV and re-counted by its own engine. Nothing was sampled and nothing was skipped.

| | |
|---|--:|
| Cases counted | 64 |
| Winner agrees with our answer key | **63** |
| Disagrees | **1** (a tie — see below) |
| Sankey diagrams exported | 26 |

## The one disagreement, and it was ours

[`coombs_ex20_district1`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex20_district1.md) — we say **B**, RCV Lab says **C**. Neither engine is wrong. Round 1 is C 16, **A 9, B 9**, and that tie decides the election: eliminate A and its `A>B>C` ballots elect B 18–16; eliminate B and its `B>C>A` ballots elect C 25–9. Our engine drops A, RCV Lab drops B, and **neither prints that it broke a tie**. <!-- terminology-ok: bare RCV names the product "RCV Lab" -->

The case's own description had asserted *"IRV elects B here too"* as a plain fact. It is a fact about our tiebreak, not about IRV, and the [file now says so](../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex20_district1.yaml). The reinforcement paradox the case exists to demonstrate is untouched — District II and the amalgamated file have no tie — but the claim needed narrowing, and only a second engine was ever going to catch it.

**The general lesson: a silent tiebreak reads exactly like a determinate result.** It is worth re-reading any teaching page that leans on an IRV elimination order in a small hand-built electorate.

## One difference that is not a disagreement

RCV Lab reports **round counts** on a different convention: it eliminates candidates one at a time where our engine clears a whole batch that cannot catch the next candidate up. On [`cycle_vote_on_the_rule_irv_c5_b999`](../../method_comparisons/cycle_resolution/cases/cases_pages/cycle_vote_on_the_rule_irv_c5_b999.md) it says four rounds and we say three, with every tally identical. Round *count* is a reporting convention, not a result — don't cite "it took N rounds" as a fact about an election without saying whose count. <!-- terminology-ok: bare RCV names the product "RCV Lab" -->

## The Sankey diagrams

The 26 cases that run to three or more rounds now carry a committed **`img/<stem>_sankey.svg`** beside the case, drawn by RCV Lab and exported as a self-contained SVG.

They earn their place because our engine prints rounds as a **table**, and a table cannot show where a transferred vote came *from* — which is the whole subject of every page here that argues about [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) or [exhausted ballots](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md). RCV Lab traces exact ballot provenance rather than estimating the ribbons, and it gives exhausted ballots their own column, labelled *"No Further Rankings"*. <!-- terminology-ok: bare RCV names the product "RCV Lab" -->

They are **committed as static files, not linked**: the repo does not control that site, it is [openly a beta](rcv_lab.md) whose output may change, and a stored SVG renders on GitHub, on the built site, and in a local viewer with no network at all.

## Reproducing it

```bash
python3 STARVote_LH_tabulation_engine/tools_adam/scripts/build_rcvlab_sankey.py emit --out /tmp/rcvlab
```

That writes one CVR CSV per case. Upload each at [rcv-lab.org](https://rcv-lab.org/) → Analysis → *Ballot data (CVRs)* → Tabulate → Visualize → Sankey, collect `{stem, winners, rounds, svg}` into a JSON array, then:

```bash
python3 STARVote_LH_tabulation_engine/tools_adam/scripts/build_rcvlab_sankey.py install results.json
```

which re-checks every winner against the YAML answer key and writes the art. Three things about that loop are worth knowing before repeating it, all of them silent failures:

1. **Their generic CSV eats the first column as a ballot ID.** The docs say "one column per candidate" and mean *starting at column two*. A bare candidate header loses the first candidate and returns a confident wrong winner — our Post-it case came back "Green in 2 rounds" instead of Purple in 3. `emit` always writes a leading `BallotID` column; the site then reports *"In CVR but not in config: BallotID"*, which is the sign it parsed correctly.
2. **The filename must contain `cvr`**, or the site raises a `confirm()` that an automated browser suppresses, silently rejecting the file.
3. **The derived config is computed once and never refreshed.** Load a second CVR without pressing **Reset** and it is scored against the *first* file's candidate list, silently producing an empty 0-round election.

## Scope

Ranked ballots only. RCV Lab counts IRV, STV and bloc, plus plurality/approval/cumulative for comparison — **no STAR, no Ranked Robin**. It can never check the methods this library is mostly about; for those, [`pref_voting`](cross_checking_with_pref_voting.md) and [BetterVoting](bettervoting_and_the_engine.md) remain the referees.

## The full ledger

Counted 2026-08-08. ✅ = winner matches our `expected_winners`.

| Case (page) | Rounds | Ours | RCV Lab | | Art | src |
|---|--:|---|---|:-:|---|:--:|
| [`ballot_expressiveness_c9_irv_top5`](../../method_comparisons/ballot_expressiveness/cases/cases_pages/ballot_expressiveness_c9_irv_top5.md) | 8 | Ben | Ben | ✅ | — | [`.yaml`](../../method_comparisons/ballot_expressiveness/cases/ballot_expressiveness_c9_irv_top5.yaml) |
| [`bv2280_37yf8x_irv_full`](../../method_comparisons/ballot_expressiveness/cases/cases_pages/bv2280_37yf8x_irv_full.md) | 8 | Ben | Ben | ✅ | [Sankey](../../method_comparisons/ballot_expressiveness/cases/img/bv2280_37yf8x_irv_full_sankey.svg) | [`.yaml`](../../method_comparisons/ballot_expressiveness/cases/bv2280_37yf8x_irv_full.yaml) |
| [`crowded_field_c7_irv`](../../method_comparisons/crowded_field/cases/cases_pages/crowded_field_c7_irv.md) | 6 | Clara | Clara | ✅ | [Sankey](../../method_comparisons/crowded_field/cases/img/crowded_field_c7_irv_sankey.svg) | [`.yaml`](../../method_comparisons/crowded_field/cases/crowded_field_c7_irv.yaml) |
| [`burlington_2009_irv`](../../method_comparisons/burlington_2009/cases/cases_pages/burlington_2009_irv.md) | 5 | Kiss | Kiss | ✅ | [Sankey](../../method_comparisons/burlington_2009/cases/img/burlington_2009_irv_sankey.svg) | [`.yaml`](../../method_comparisons/burlington_2009/cases/burlington_2009_irv.yaml) |
| [`burlington_2009_raise_kiss_nonmono`](../../method_comparisons/burlington_2009/cases/cases_pages/burlington_2009_raise_kiss_nonmono.md) | 5 | Montroll | Montroll | ✅ | [Sankey](../../method_comparisons/burlington_2009/cases/img/burlington_2009_raise_kiss_nonmono_sankey.svg) | [`.yaml`](../../method_comparisons/burlington_2009/cases/burlington_2009_raise_kiss_nonmono.yaml) |
| [`street_trees_five_rounds_c6_b100`](../../06_Other/RCV_IRV/cases/cases_pages/street_trees_five_rounds_c6_b100.md) | 5 | Birch | Birch | ✅ | [Sankey](../../06_Other/RCV_IRV/cases/img/street_trees_five_rounds_c6_b100_sankey.svg) | [`.yaml`](../../06_Other/RCV_IRV/cases/street_trees_five_rounds_c6_b100.yaml) |
| [`bv2138_cxrf8v_irv`](../../method_comparisons/no_condorcet_bv2138/cases/cases_pages/bv2138_cxrf8v_irv.md) | 4 | Dave | Dave | ✅ | [Sankey](../../method_comparisons/no_condorcet_bv2138/cases/img/bv2138_cxrf8v_irv_sankey.svg) | [`.yaml`](../../method_comparisons/no_condorcet_bv2138/cases/bv2138_cxrf8v_irv.yaml) |
| [`bv2183_dfw8rj_forced_exhaustion_ceiling`](../../method_comparisons/paradoxes_and_whoops/cases/cases_pages/bv2183_dfw8rj_forced_exhaustion_ceiling.md) | 4 | Ada | Ada | ✅ | [Sankey](../../method_comparisons/paradoxes_and_whoops/cases/img/bv2183_dfw8rj_forced_exhaustion_ceiling_sankey.svg) | [`.yaml`](../../method_comparisons/paradoxes_and_whoops/cases/bv2183_dfw8rj_forced_exhaustion_ceiling.yaml) |
| [`bv2278_8cdkkc_five_way_irv`](../../method_comparisons/kissel_single_elimination_rcv/cases/cases_pages/bv2278_8cdkkc_five_way_irv.md) | 4 | A | A | ✅ | [Sankey](../../method_comparisons/kissel_single_elimination_rcv/cases/img/bv2278_8cdkkc_five_way_irv_sankey.svg) | [`.yaml`](../../method_comparisons/kissel_single_elimination_rcv/cases/bv2278_8cdkkc_five_way_irv.yaml) |
| [`bv2281_qycpbx_ossipoff_irv`](../../method_comparisons/rangevoting_irv_examples/cases/cases_pages/bv2281_qycpbx_ossipoff_irv.md) | 4 | D | D | ✅ | [Sankey](../../method_comparisons/rangevoting_irv_examples/cases/img/bv2281_qycpbx_ossipoff_irv_sankey.svg) | [`.yaml`](../../method_comparisons/rangevoting_irv_examples/cases/bv2281_qycpbx_ossipoff_irv.yaml) |
| [`crowded_field_c5_irv`](../../method_comparisons/crowded_field/cases/cases_pages/crowded_field_c5_irv.md) | 4 | Elsa | Elsa | ✅ | [Sankey](../../method_comparisons/crowded_field/cases/img/crowded_field_c5_irv_sankey.svg) | [`.yaml`](../../method_comparisons/crowded_field/cases/crowded_field_c5_irv.yaml) |
| [`cycle_vote_on_the_rule_irv_c5_b999`](../../method_comparisons/cycle_resolution/cases/cases_pages/cycle_vote_on_the_rule_irv_c5_b999.md) | 4 | Ranked Pairs | Ranked Pairs | ✅ | [Sankey](../../method_comparisons/cycle_resolution/cases/img/cycle_vote_on_the_rule_irv_c5_b999_sankey.svg) | [`.yaml`](../../method_comparisons/cycle_resolution/cases/cycle_vote_on_the_rule_irv_c5_b999.yaml) |
| [`batch_all_out_round2_c4_b6`](../../06_Other/RCV_IRV/cases/cases_pages/batch_all_out_round2_c4_b6.md) | 3 | Alex | Alex | ✅ | [Sankey](../../06_Other/RCV_IRV/cases/img/batch_all_out_round2_c4_b6_sankey.svg) | [`.yaml`](../../06_Other/RCV_IRV/cases/batch_all_out_round2_c4_b6.yaml) |
| [`bv2133_dyxrbr_pet2_irv`](../../method_comparisons/pet_poll_four_winners/cases/cases_pages/bv2133_dyxrbr_pet2_irv.md) | 3 | Fish | Fish | ✅ | [Sankey](../../method_comparisons/pet_poll_four_winners/cases/img/bv2133_dyxrbr_pet2_irv_sankey.svg) | [`.yaml`](../../method_comparisons/pet_poll_four_winners/cases/bv2133_dyxrbr_pet2_irv.yaml) |
| [`bv2162_4htk44_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2162_4htk44_irv.md) | 3 | A | A | ✅ | [Sankey](../../method_comparisons/felsenthal_paradoxes/cases/img/bv2162_4htk44_irv_sankey.svg) | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2162_4htk44_irv.yaml) |
| [`bv2163_74j6vv_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2163_74j6vv_irv.md) | 3 | B | B | ✅ | [Sankey](../../method_comparisons/felsenthal_paradoxes/cases/img/bv2163_74j6vv_irv_sankey.svg) | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2163_74j6vv_irv.yaml) |
| [`bv2170_pp2q4q_irv`](../../method_comparisons/symmetric_centrist_bv2170/cases/cases_pages/bv2170_pp2q4q_irv.md) | 3 | Avery | Avery | ✅ | [Sankey](../../method_comparisons/symmetric_centrist_bv2170/cases/img/bv2170_pp2q4q_irv_sankey.svg) | [`.yaml`](../../method_comparisons/symmetric_centrist_bv2170/cases/bv2170_pp2q4q_irv.yaml) |
| [`bv2176_p8dp28_irv`](../../method_comparisons/postit_rcv_example/cases/cases_pages/bv2176_p8dp28_irv.md) | 3 | Purple | Purple | ✅ | [Sankey](../../method_comparisons/postit_rcv_example/cases/img/bv2176_p8dp28_irv_sankey.svg) | [`.yaml`](../../method_comparisons/postit_rcv_example/cases/bv2176_p8dp28_irv.yaml) |
| [`bv2178_8kg698_irv`](../../method_comparisons/postit_rcv_example/cases/cases_pages/bv2178_8kg698_irv.md) | 3 | Blue | Blue | ✅ | [Sankey](../../method_comparisons/postit_rcv_example/cases/img/bv2178_8kg698_irv_sankey.svg) | [`.yaml`](../../method_comparisons/postit_rcv_example/cases/bv2178_8kg698_irv.yaml) |
| [`bv2277_tqfdbg_mayor_irv`](../../method_comparisons/kissel_single_elimination_rcv/cases/cases_pages/bv2277_tqfdbg_mayor_irv.md) | 3 | Cora | Cora | ✅ | [Sankey](../../method_comparisons/kissel_single_elimination_rcv/cases/img/bv2277_tqfdbg_mayor_irv_sankey.svg) | [`.yaml`](../../method_comparisons/kissel_single_elimination_rcv/cases/bv2277_tqfdbg_mayor_irv.yaml) |
| [`bv2282_hf3ckp_brams_irv`](../../method_comparisons/rangevoting_irv_examples/cases/cases_pages/bv2282_hf3ckp_brams_irv.md) | 3 | B | B | ✅ | [Sankey](../../method_comparisons/rangevoting_irv_examples/cases/img/bv2282_hf3ckp_brams_irv_sankey.svg) | [`.yaml`](../../method_comparisons/rangevoting_irv_examples/cases/bv2282_hf3ckp_brams_irv.yaml) |
| [`coombs_ex18_monotonicity`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex18_monotonicity.md) | 3 | Arlo | Arlo | ✅ | [Sankey](../../method_comparisons/felsenthal_paradoxes/cases/img/coombs_ex18_monotonicity_sankey.svg) | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex18_monotonicity.yaml) |
| [`coombs_ex21_twin_after`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex21_twin_after.md) | 3 | B | B | ✅ | [Sankey](../../method_comparisons/felsenthal_paradoxes/cases/img/coombs_ex21_twin_after_sankey.svg) | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex21_twin_after.yaml) |
| [`coombs_ex21_twin_before`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex21_twin_before.md) | 3 | B | B | ✅ | [Sankey](../../method_comparisons/felsenthal_paradoxes/cases/img/coombs_ex21_twin_before_sankey.svg) | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex21_twin_before.yaml) |
| [`coombs_ex22_scc`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex22_scc.md) | 3 | A | A | ✅ | [Sankey](../../method_comparisons/felsenthal_paradoxes/cases/img/coombs_ex22_scc_sankey.svg) | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex22_scc.yaml) |
| [`irv_combined`](../../method_comparisons/summability_demo/cases/cases_pages/irv_combined.md) | 3 | A | A | ✅ | [Sankey](../../method_comparisons/summability_demo/cases/img/irv_combined_sankey.svg) | [`.yaml`](../../method_comparisons/summability_demo/cases/irv_combined.yaml) |
| [`put_two_universes_c3_b4`](../../06_Other/RCV_IRV/cases/cases_pages/put_two_universes_c3_b4.md) | 3 | Anna | Anna | ✅ | [Sankey](../../06_Other/RCV_IRV/cases/img/put_two_universes_c3_b4_sankey.svg) | [`.yaml`](../../06_Other/RCV_IRV/cases/put_two_universes_c3_b4.yaml) |
| [`alaska_buried_c3_b200`](../../method_comparisons/condorcet_burial_alaska/cases/cases_pages/alaska_buried_c3_b200.md) | 2 | Peltola | Peltola | ✅ | — | [`.yaml`](../../method_comparisons/condorcet_burial_alaska/cases/alaska_buried_c3_b200.yaml) |
| [`alaska_sincere_c3_b200`](../../method_comparisons/condorcet_burial_alaska/cases/cases_pages/alaska_sincere_c3_b200.md) | 2 | Peltola | Peltola | ✅ | — | [`.yaml`](../../method_comparisons/condorcet_burial_alaska/cases/alaska_sincere_c3_b200.yaml) |
| [`alaska_upward_after`](../../method_comparisons/monotonicity/cases/cases_pages/alaska_upward_after.md) | 2 | Begich | Begich | ✅ | — | [`.yaml`](../../method_comparisons/monotonicity/cases/alaska_upward_after.yaml) |
| [`alaska_upward_before`](../../method_comparisons/monotonicity/cases/cases_pages/alaska_upward_before.md) | 2 | Peltola | Peltola | ✅ | — | [`.yaml`](../../method_comparisons/monotonicity/cases/alaska_upward_before.yaml) |
| [`balance_base_irv_c3_b9`](../../06_Other/RCV_IRV/equal_vote_balance/cases/cases_pages/balance_base_irv_c3_b9.md) | 2 | Bruno | Bruno | ✅ | — | [`.yaml`](../../06_Other/RCV_IRV/equal_vote_balance/cases/balance_base_irv_c3_b9.yaml) |
| [`balance_plus_opposite_c3_b15`](../../06_Other/RCV_IRV/equal_vote_balance/cases/cases_pages/balance_plus_opposite_c3_b15.md) | 2 | Ada | Ada | ✅ | — | [`.yaml`](../../06_Other/RCV_IRV/equal_vote_balance/cases/balance_plus_opposite_c3_b15.yaml) |
| [`batch_all_out_condorcet_c3_b3`](../../06_Other/RCV_IRV/cases/cases_pages/batch_all_out_condorcet_c3_b3.md) | 2 | Amy | Amy | ✅ | — | [`.yaml`](../../06_Other/RCV_IRV/cases/batch_all_out_condorcet_c3_b3.yaml) |
| [`batch_all_out_cycle_c3_b3`](../../06_Other/RCV_IRV/cases/cases_pages/batch_all_out_cycle_c3_b3.md) | 2 | Amy | Amy | ✅ | — | [`.yaml`](../../06_Other/RCV_IRV/cases/batch_all_out_cycle_c3_b3.yaml) |
| [`bv2132_ykjjhy_pet_irv`](../../method_comparisons/pet_poll_four_methods/cases/cases_pages/bv2132_ykjjhy_pet_irv.md) | 2 | Fish | Fish | ✅ | — | [`.yaml`](../../method_comparisons/pet_poll_four_methods/cases/bv2132_ykjjhy_pet_irv.yaml) |
| [`bv2137_ywckmg_irv`](../../method_comparisons/center_squeeze_bv2137/cases/cases_pages/bv2137_ywckmg_irv.md) | 2 | Carter | Carter | ✅ | — | [`.yaml`](../../method_comparisons/center_squeeze_bv2137/cases/bv2137_ywckmg_irv.yaml) |
| [`bv2145_6fj2kg_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2145_6fj2kg_irv.md) | 2 | Ben | Ben | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2145_6fj2kg_irv.yaml) |
| [`bv2146_krk2px_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2146_krk2px_irv.md) | 2 | Ada | Ada | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2146_krk2px_irv.yaml) |
| [`bv2147_9gdrqg_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2147_9gdrqg_irv.md) | 2 | Bruno | Bruno | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2147_9gdrqg_irv.yaml) |
| [`bv2149_byk9v2_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2149_byk9v2_irv.md) | 2 | Alma | Alma | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2149_byk9v2_irv.yaml) |
| [`bv2150_dxg8pb_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2150_dxg8pb_irv.md) | 2 | Carl | Carl | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2150_dxg8pb_irv.yaml) |
| [`bv2151_97hbpw_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2151_97hbpw_irv.md) | 2 | Beth | Beth | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2151_97hbpw_irv.yaml) |
| [`bv2154_wq6yv7_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2154_wq6yv7_irv.md) | 2 | Clara | Clara | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2154_wq6yv7_irv.yaml) |
| [`bv2222_rfyk46_510_thin_irv`](../../method_comparisons/star_5_1_0_challenge/cases/cases_pages/bv2222_rfyk46_510_thin_irv.md) | 2 | Ana | Ana | ✅ | — | [`.yaml`](../../method_comparisons/star_5_1_0_challenge/cases/bv2222_rfyk46_510_thin_irv.yaml) |
| [`bv2223_dyh93j_510_real_irv`](../../method_comparisons/star_5_1_0_challenge/cases/cases_pages/bv2223_dyh93j_510_real_irv.md) | 2 | Ana | Ana | ✅ | — | [`.yaml`](../../method_comparisons/star_5_1_0_challenge/cases/bv2223_dyh93j_510_real_irv.yaml) |
| [`bv2227_3xgkck_honest_irv`](../../method_comparisons/favorite_betrayal_irv/cases/cases_pages/bv2227_3xgkck_honest_irv.md) | 2 | Right | Right | ✅ | — | [`.yaml`](../../method_comparisons/favorite_betrayal_irv/cases/bv2227_3xgkck_honest_irv.yaml) |
| [`bv2228_bgcmxx_betray_irv`](../../method_comparisons/favorite_betrayal_irv/cases/cases_pages/bv2228_bgcmxx_betray_irv.md) | 2 | Center | Center | ✅ | — | [`.yaml`](../../method_comparisons/favorite_betrayal_irv/cases/bv2228_bgcmxx_betray_irv.yaml) |
| [`condorcet_1788_irv`](../../method_comparisons/borda_condorcet_1788/cases/cases_pages/condorcet_1788_irv.md) | 2 | Peter | Peter | ✅ | — | [`.yaml`](../../method_comparisons/borda_condorcet_1788/cases/condorcet_1788_irv.yaml) |
| [`coombs_ex20_amalgamated`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex20_amalgamated.md) | 2 | B | B | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex20_amalgamated.yaml) |
| [`coombs_ex20_district1`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex20_district1.md) | 2 | B | C | ⚠️ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex20_district1.yaml) |
| [`irv_district_A`](../../method_comparisons/summability_demo/cases/cases_pages/irv_district_A.md) | 2 | B | B | ✅ | — | [`.yaml`](../../method_comparisons/summability_demo/cases/irv_district_A.yaml) |
| [`irv_district_B`](../../method_comparisons/summability_demo/cases/cases_pages/irv_district_B.md) | 2 | B | B | ✅ | — | [`.yaml`](../../method_comparisons/summability_demo/cases/irv_district_B.yaml) |
| [`margins_irv`](../../method_comparisons/copeland_vs_borda_margins/cases/cases_pages/margins_irv.md) | 2 | Cocoa | Cocoa | ✅ | — | [`.yaml`](../../method_comparisons/copeland_vs_borda_margins/cases/margins_irv.yaml) |
| [`omr_opposition_decides`](../../method_comparisons/ordered_majority_rule/cases/cases_pages/omr_opposition_decides.md) | 2 | B | B | ✅ | — | [`.yaml`](../../method_comparisons/ordered_majority_rule/cases/omr_opposition_decides.yaml) |
| [`reversal_irv_original`](../../method_comparisons/reversal_symmetry/cases/cases_pages/reversal_irv_original.md) | 2 | A | A | ✅ | — | [`.yaml`](../../method_comparisons/reversal_symmetry/cases/reversal_irv_original.yaml) |
| [`reversal_irv_reversed`](../../method_comparisons/reversal_symmetry/cases/cases_pages/reversal_irv_reversed.md) | 2 | A | A | ✅ | — | [`.yaml`](../../method_comparisons/reversal_symmetry/cases/reversal_irv_reversed.yaml) |
| [`sf_d7_downward_after`](../../method_comparisons/monotonicity/cases/cases_pages/sf_d7_downward_after.md) | 2 | Engardio | Engardio | ✅ | — | [`.yaml`](../../method_comparisons/monotonicity/cases/sf_d7_downward_after.yaml) |
| [`sf_d7_downward_before`](../../method_comparisons/monotonicity/cases/cases_pages/sf_d7_downward_before.md) | 2 | Melgar | Melgar | ✅ | — | [`.yaml`](../../method_comparisons/monotonicity/cases/sf_d7_downward_before.yaml) |
| [`tilted_cycle_c3_b5_irv`](../../method_comparisons/minimal_tilted_cycle/cases/cases_pages/tilted_cycle_c3_b5_irv.md) | 2 | Cara | Cara | ✅ | — | [`.yaml`](../../method_comparisons/minimal_tilted_cycle/cases/tilted_cycle_c3_b5_irv.yaml) |
| [`bv2148_h87k6v_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2148_h87k6v_irv.md) | 1 | Bruno | Bruno | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2148_h87k6v_irv.yaml) |
| [`bv2153_pcttmr_irv`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/bv2153_pcttmr_irv.md) | 1 | Amos | Amos | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/bv2153_pcttmr_irv.yaml) |
| [`coombs_ex20_district2`](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex20_district2.md) | 1 | B | B | ✅ | — | [`.yaml`](../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex20_district2.yaml) |
| [`crowded_field_c3_irv`](../../method_comparisons/crowded_field/cases/cases_pages/crowded_field_c3_irv.md) | 1 | Diego | Diego | ✅ | — | [`.yaml`](../../method_comparisons/crowded_field/cases/crowded_field_c3_irv.yaml) |

---

*Up: [tabulation engines](README.md) · [07_Concepts](../README.md) · related: [RCV Lab](rcv_lab.md) · [RCTab](rctab.md) · [cross-checking with `pref_voting`](cross_checking_with_pref_voting.md).*
