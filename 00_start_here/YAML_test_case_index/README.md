# YAML test-case index — by voting method

**Auto-generated — do not edit by hand.** Run `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_index.py` to refresh (a pytest fails if it's stale).

Election YAMLs live in many folders (the test harnesses glob specific ones, so they're indexed *in place*, not moved). Each file declares a `voting_method` and `num_winners`; this catalog groups them so you can browse by method. Excludes `_tabulated` mirrors, raw `_demo_dropbox` drops, generated copies, and deliberately-malformed negative fixtures.

Titles come from each file's **`election_title`** field (the convention — add one to make a file's title explicit & searchable). Where that's missing, a file's first `#` comment line is shown *in italics* as a fallback.

**132 election files** (120 single-winner, 12 multi-winner) across 13 method(s).

| Method | Files |
|--------|------:|
| STAR | 100 |
| RCV-IRV (Hare) | 9 |
| Ranked Robin (RCV-RR / Copeland) | 5 |
| Approval | 3 |
| STV (proportional RCV) | 1 |
| Bloc STAR | 4 |
| STAR-PR (Sequential Selection) | 2 |
| Reweighted Range | 1 |
| Allocated Score (STAR-PR) | 1 |
| APPROVAL_MULTI_WINNER | 3 |
| PLURALITY | 1 |
| RANGE | 1 |
| RR | 1 |

## STAR  (100)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`Flat_scores_ties_01_baseline_clean`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_pages/Flat_scores_ties_01_baseline_clean.md) | `01_STAR/Flat_scores_ties/` | 1 | Flat scores 01 — clean top two (works-fine baseline) → _Apple_ | [`.yaml`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_01_baseline_clean.yaml) |
| [`Flat_scores_ties_02_runoff_tie_2cand`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_pages/Flat_scores_ties_02_runoff_tie_2cand.md) | `01_STAR/Flat_scores_ties/` | 1 | Flat scores 02 — runoff tie, two candidates (everyone equal) → _Almond_ | [`.yaml`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_02_runoff_tie_2cand.yaml) |
| [`Flat_scores_ties_03_runoff_tie_split`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_pages/Flat_scores_ties_03_runoff_tie_split.md) | `01_STAR/Flat_scores_ties/` | 1 | Flat scores 03 — runoff tie, an even 1-1 split → _Athens_ | [`.yaml`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_03_runoff_tie_split.yaml) |
| [`Flat_scores_ties_04_scoring_tie_2way`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_pages/Flat_scores_ties_04_scoring_tie_2way.md) | `01_STAR/Flat_scores_ties/` | 1 | Flat scores 04 — scoring-round tie for the 2nd finalist slot (2-way) → _Aral_ | [`.yaml`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_04_scoring_tie_2way.yaml) |
| [`Flat_scores_ties_05_scoring_tie_3way_xmyf7k`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_pages/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) | `01_STAR/Flat_scores_ties/` | 1 | Flat scores 05 — scoring-round 3-way tie (BV555 / → _A_ | [`.yaml`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml) |
| [`Flat_scores_ties_06_scoring_tie_4way`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_pages/Flat_scores_ties_06_scoring_tie_4way.md) | `01_STAR/Flat_scores_ties/` | 1 | Flat scores 06 — scoring-round 4-way tie (ties at every step) → _Ava_ | [`.yaml`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_06_scoring_tie_4way.yaml) |
| [`Flat_scores_ties_07_fully_flat`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_pages/Flat_scores_ties_07_fully_flat.md) | `01_STAR/Flat_scores_ties/` | 1 | Flat scores 07 — fully flat ballots (the maximal tie + abstention trap) → _Ararat_ | [`.yaml`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_07_fully_flat.yaml) |
| [`Flat_scores_ties_08_all_flat_zero_count`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_pages/Flat_scores_ties_08_all_flat_zero_count.md) | `01_STAR/Flat_scores_ties/` | 1 | Flat scores 08 — every ballot flat (BetterVoting counts 0) → _Anchovy_ | [`.yaml`](../../01_STAR/Flat_scores_ties/Flat_scores_ties_08_all_flat_zero_count.yaml) |
| [`01a_c2_b1_two-candidates`](../../01_STAR/_main/_main_pages/01a_c2_b1_two-candidates.md) | `01_STAR/_main/` | 1 | The simplest possible STAR Voting example → _Chocolate_ | [`.yaml`](../../01_STAR/_main/01a_c2_b1_two-candidates.yaml) |
| [`01a_c2_b2_two-candidates`](../../01_STAR/_main/_main_pages/01a_c2_b2_two-candidates.md) | `01_STAR/_main/` | 1 | Same as before - but this time two ballots → _Chocolate_ | [`.yaml`](../../01_STAR/_main/01a_c2_b2_two-candidates.yaml) |
| [`01b_c2_b2_two-candidates`](../../01_STAR/_main/_main_pages/01b_c2_b2_two-candidates.md) | `01_STAR/_main/` | 1 | Again, very similar - this time second ballot is 5 and 0 → _Choco_ | [`.yaml`](../../01_STAR/_main/01b_c2_b2_two-candidates.yaml) |
| [`01c_c2_b3_two-candidates`](../../01_STAR/_main/_main_pages/01c_c2_b3_two-candidates.md) | `01_STAR/_main/` | 1 | Equal support example ("I like both flavors") → _Choco_ | [`.yaml`](../../01_STAR/_main/01c_c2_b3_two-candidates.yaml) |
| [`02a_c3_b1_three-candidates`](../../01_STAR/_main/_main_pages/02a_c3_b1_three-candidates.md) | `01_STAR/_main/` | 1 | Three candidates, one ballot - single-winner STAR → _Choco_ | [`.yaml`](../../01_STAR/_main/02a_c3_b1_three-candidates.yaml) |
| [`02b_c3_b2_three-candidates`](../../01_STAR/_main/_main_pages/02b_c3_b2_three-candidates.md) | `01_STAR/_main/` | 1 | Three candidates, two ballots - single-winner STAR → _Vanilla_ | [`.yaml`](../../01_STAR/_main/02b_c3_b2_three-candidates.yaml) |
| [`03a_c3_b3_style-bullet-vote`](../../01_STAR/_main/_main_pages/03a_c3_b3_style-bullet-vote.md) | `01_STAR/_main/` | 1 | Voting styles — a valid STAR bullet vote (3 candidates) → _Vanilla_ | [`.yaml`](../../01_STAR/_main/03a_c3_b3_style-bullet-vote.yaml) |
| [`03b_c3_b3_1_style-protest-vote`](../../01_STAR/_main/_main_pages/03b_c3_b3_1_style-protest-vote.md) | `01_STAR/_main/` | 1 | Voting styles — low-score ballots → _Almond_ | [`.yaml`](../../01_STAR/_main/03b_c3_b3_1_style-protest-vote.yaml) |
| [`03b_c3_b3_2_expand_style-protest-vote`](../../01_STAR/_main/_main_pages/03b_c3_b3_2_expand_style-protest-vote.md) | `01_STAR/_main/` | 1 | Voting styles — low-score ballots (continued) → _Almond_ | [`.yaml`](../../01_STAR/_main/03b_c3_b3_2_expand_style-protest-vote.yaml) |
| [`03c_c6_b8_style-gallery`](../../01_STAR/_main/_main_pages/03c_c6_b8_style-gallery.md) | `01_STAR/_main/` | 1 | Voting styles — eight ways to fill out one 5-star ballot → _Bianca_ | [`.yaml`](../../01_STAR/_main/03c_c6_b8_style-gallery.yaml) |
| [`04b_c4_b3_display-options-all`](../../01_STAR/_main/_main_pages/04b_c4_b3_display-options-all.md) | `01_STAR/_main/` | 1 | All options demo → _Strawberry_ | [`.yaml`](../../01_STAR/_main/04b_c4_b3_display-options-all.yaml) |
| [`05a_c5_b3_unanimous-ballots`](../../01_STAR/_main/_main_pages/05a_c5_b3_unanimous-ballots.md) | `01_STAR/_main/` | 1 | Unanimous ballots (five candidates) → _Andre_ | [`.yaml`](../../01_STAR/_main/05a_c5_b3_unanimous-ballots.yaml) |
| [`06a_c9_b3_large-field-equal-support`](../../01_STAR/_main/_main_pages/06a_c9_b3_large-field-equal-support.md) | `01_STAR/_main/` | 1 | Large field (9 candidates) — STAR scales, and Equal Support decides → _Carmen_ | [`.yaml`](../../01_STAR/_main/06a_c9_b3_large-field-equal-support.yaml) |
| [`06b_c9_runoff-overturns-leader`](../../01_STAR/_main/_main_pages/06b_c9_runoff-overturns-leader.md) | `01_STAR/_main/` | 1 | Large field (9 candidates) — the runoff OVERTURNS the score leader → _Carmen_ | [`.yaml`](../../01_STAR/_main/06b_c9_runoff-overturns-leader.yaml) |
| [`09_c4_b100_tennessee-capital`](../../01_STAR/_main/_main_pages/09_c4_b100_tennessee-capital.md) | `01_STAR/_main/` | 1 | Tennessee Capital — classic STAR example → _Nashville_ | [`.yaml`](../../01_STAR/_main/09_c4_b100_tennessee-capital.yaml) |
| [`abstentions`](../../01_STAR/_main/_main_pages/abstentions.md) | `01_STAR/_main/` | 1 | Abstentions — blank and abstaining ballots in STAR → _Dog_ | [`.yaml`](../../01_STAR/_main/abstentions.yaml) |
| [`display_options_demo`](../../01_STAR/_main/_main_pages/display_options_demo.md) | `01_STAR/_main/` | 1 | Display options demo → _Don_ | [`.yaml`](../../01_STAR/_main/display_options_demo.yaml) |
| [`equal_support_runoff_demo`](../../01_STAR/_main/_main_pages/equal_support_runoff_demo.md) | `01_STAR/_main/` | 1 | Equal Support — counted in both rounds, neutral only in the tie-break → _A_ | [`.yaml`](../../01_STAR/_main/equal_support_runoff_demo.yaml) |
| [`quorum_demo_c3_b6`](../../01_STAR/_main/_main_pages/quorum_demo_c3_b6.md) | `01_STAR/_main/` | 1 | Quorum — an abstention still counts toward turnout → _Anna_ | [`.yaml`](../../01_STAR/_main/quorum_demo_c3_b6.yaml) |
| [`quorum_fail_demo_c3_b6`](../../01_STAR/_main/_main_pages/quorum_fail_demo_c3_b6.md) | `01_STAR/_main/` | 1 | Quorum FAILS — won the count, but not elected | [`.yaml`](../../01_STAR/_main/quorum_fail_demo_c3_b6.yaml) |
| [`star_ala_approval`](../../01_STAR/_main/_main_pages/star_ala_approval.md) | `01_STAR/_main/` | 1 | STAR à la Approval — 0/1 & marker ballots are legal on a STAR ballot → _D_ | [`.yaml`](../../01_STAR/_main/star_ala_approval.yaml) |
| [`three_winners_cw_score_runoff`](../../01_STAR/_main/_main_pages/three_winners_cw_score_runoff.md) | `01_STAR/_main/` | 1 | Three notions of "winner" disagree — Condorcet, Score, and Runoff → _Bob_ | [`.yaml`](../../01_STAR/_main/three_winners_cw_score_runoff.yaml) |
| [`vote_splitting`](../../01_STAR/_main/_main_pages/vote_splitting.md) | `01_STAR/_main/` | 1 | Vote splitting — two chocolates split the majority → _DarkChoco_ | [`.yaml`](../../01_STAR/_main/vote_splitting.yaml) |
| [`vote_splitting2`](../../01_STAR/_main/_main_pages/vote_splitting2.md) | `01_STAR/_main/` | 1 | Vote splitting — two chocolates split the majority → _DarkChoco_ | [`.yaml`](../../01_STAR/_main/vote_splitting2.yaml) |
| [`vote_splitting3`](../../01_STAR/_main/_main_pages/vote_splitting3.md) | `01_STAR/_main/` | 1 | Vote splitting — two chocolates split the majority → _DarkChoco_ | [`.yaml`](../../01_STAR/_main/vote_splitting3.yaml) |
| [`vote_splitting_scenario1_spoiler`](../../01_STAR/_main/_main_pages/vote_splitting_scenario1_spoiler.md) | `01_STAR/_main/` | 1 | Vote splitting — scenario 1 of 3 — the spoiler strikes → _DarkChoco_ | [`.yaml`](../../01_STAR/_main/vote_splitting_scenario1_spoiler.yaml) |
| [`vote_splitting_scenario2_bloc_leads`](../../01_STAR/_main/_main_pages/vote_splitting_scenario2_bloc_leads.md) | `01_STAR/_main/` | 1 | Vote splitting — scenario 2 of 3 — no spoiler (bloc leader wins anyway) → _DarkChoco_ | [`.yaml`](../../01_STAR/_main/vote_splitting_scenario2_bloc_leads.yaml) |
| [`vote_splitting_scenario3_outsider_wins`](../../01_STAR/_main/_main_pages/vote_splitting_scenario3_outsider_wins.md) | `01_STAR/_main/` | 1 | Vote splitting — scenario 3 of 3 — no spoiler (the outsider truly wins) → _Vanilla_ | [`.yaml`](../../01_STAR/_main/vote_splitting_scenario3_outsider_wins.yaml) |
| [`abstention_reconciliation_min_c2_b6`](../../01_STAR/pet_real_bv_election/pet_real_bv_election_pages/abstention_reconciliation_min_c2_b6.md) | `01_STAR/pet_real_bv_election/` | 1 | Abstention vs Equal Support — the minimal reconciliation case → _Dog_ | [`.yaml`](../../01_STAR/pet_real_bv_election/abstention_reconciliation_min_c2_b6.yaml) |
| [`best_pet_c7_b461`](../../01_STAR/pet_real_bv_election/pet_real_bv_election_pages/best_pet_c7_b461.md) | `01_STAR/pet_real_bv_election/` | 1 | What Makes the Best Pet? → _Dog_ | [`.yaml`](../../01_STAR/pet_real_bv_election/best_pet_c7_b461.yaml) |
| [`flat_scores_abstention_c3_b8`](../../01_STAR/pet_real_bv_election/pet_real_bv_election_pages/flat_scores_abstention_c3_b8.md) | `01_STAR/pet_real_bv_election/` | 1 | BV Abstentions and flat scores (Apple/Banana/Cherry, 8 ballots) → _Banana_ | [`.yaml`](../../01_STAR/pet_real_bv_election/flat_scores_abstention_c3_b8.yaml) |
| [`small_abstention_c2_b5`](../../01_STAR/pet_real_bv_election/pet_real_bv_election_pages/small_abstention_c2_b5.md) | `01_STAR/pet_real_bv_election/` | 1 | Equal Support vs Abstention — minimal STAR test (A/B, 5 ballots) → _A_ | [`.yaml`](../../01_STAR/pet_real_bv_election/small_abstention_c2_b5.yaml) |
| [`01a_c3_b3_more-stars-fewer-voters`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/01a_c3_b3_more-stars-fewer-voters.md) | `01_STAR/runoff_overturns_leader/` | 1 | More stars, fewer voters — the runoff overturns the score leader → _Brownie_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/01a_c3_b3_more-stars-fewer-voters.yaml) |
| [`01b_c3_b9_overturn-holds-at-scale`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/01b_c3_b9_overturn-holds-at-scale.md) | `01_STAR/runoff_overturns_leader/` | 1 | The same overturn at scale — 67% to 33% → _Brownie_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/01b_c3_b9_overturn-holds-at-scale.yaml) |
| [`02_c5_b5_leader-overturned`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/02_c5_b5_leader-overturned.md) | `01_STAR/runoff_overturns_leader/` | 1 | Five candidates — the score leader is overturned in the runoff → _Boston_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/02_c5_b5_leader-overturned.yaml) |
| [`03_c7_b3_ice-cream-live`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/03_c7_b3_ice-cream-live.md) | `01_STAR/runoff_overturns_leader/` | 1 | Ice Cream — Flavor of the Year (the real recorded race) → _ChocoAlm_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/03_c7_b3_ice-cream-live.yaml) |
| [`04_c4_b3_runoff-confirms-leader`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/04_c4_b3_runoff-confirms-leader.md) | `01_STAR/runoff_overturns_leader/` | 1 | The control case — here the runoff CONFIRMS the score leader → _Blue_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/04_c4_b3_runoff-confirms-leader.yaml) |
| [`05_c3_b5_low-scores-bv1265`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/05_c3_b5_low-scores-bv1265.md) | `01_STAR/runoff_overturns_leader/` | 1 | Low scores, switched winner — the popover example (BetterVoting BV1265) → _A_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/05_c3_b5_low-scores-bv1265.yaml) |
| [`Runoff_01_confirms_leader_r2pvc9`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/Runoff_01_confirms_leader_r2pvc9.md) | `01_STAR/runoff_overturns_leader/` | 1 | Runoff 01 — Runoff confirms the leader (control) → _Aspen_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/Runoff_01_confirms_leader_r2pvc9.yaml) |
| [`Runoff_02_atom_reversal_yx9447`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/Runoff_02_atom_reversal_yx9447.md) | `01_STAR/runoff_overturns_leader/` | 1 | Runoff 02 — the atom (smallest runoff reversal) → _Boston_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/Runoff_02_atom_reversal_yx9447.yaml) |
| [`Runoff_03_enthusiasts_vs_majority_rkgtpk`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/Runoff_03_enthusiasts_vs_majority_rkgtpk.md) | `01_STAR/runoff_overturns_leader/` | 1 | Runoff 03 — two enthusiasts vs the majority → _Eden_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml) |
| [`Runoff_04_reversal_at_scale_bfjqmg`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/Runoff_04_reversal_at_scale_bfjqmg.md) | `01_STAR/runoff_overturns_leader/` | 1 | Runoff 04 — the reversal holds at scale (67/33) → _Olive_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/Runoff_04_reversal_at_scale_bfjqmg.yaml) |
| [`Runoff_05_reversal_with_equal_support_xgkw3w`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/Runoff_05_reversal_with_equal_support_xgkw3w.md) | `01_STAR/runoff_overturns_leader/` | 1 | Runoff 05 — reversal with Equal Support → _Sage_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/Runoff_05_reversal_with_equal_support_xgkw3w.yaml) |
| [`Runoff_06_confirms_at_scale_d664xw`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/Runoff_06_confirms_at_scale_d664xw.md) | `01_STAR/runoff_overturns_leader/` | 1 | Runoff 06 — the runoff confirms the leader at scale (control) → _Wren_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/Runoff_06_confirms_at_scale_d664xw.yaml) |
| [`Runoff_07_flat_ballot_bv_bug_tf73v9`](../../01_STAR/runoff_overturns_leader/runoff_overturns_leader_pages/Runoff_07_flat_ballot_bv_bug_tf73v9.md) | `01_STAR/runoff_overturns_leader/` | 1 | Runoff 07 (WIP) — flat ballot exposes the BV abstention bug → _Blair_ | [`.yaml`](../../01_STAR/runoff_overturns_leader/Runoff_07_flat_ballot_bv_bug_tf73v9.yaml) |
| [`dead_rung_scoring_dead_cap2`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/dead_rung_scoring_dead_cap2.md) | `01_STAR/tie_break_dead_rung/` | 1 | Dead rung — scoring round, dead five-star rung, cap 2 → _Ann_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/dead_rung_scoring_dead_cap2.yaml) |
| [`dead_rung_scoring_dead_cap3`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/dead_rung_scoring_dead_cap3.md) | `01_STAR/tie_break_dead_rung/` | 1 | Dead rung — scoring round, dead five-star rung, cap 3 → _Ann_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/dead_rung_scoring_dead_cap3.yaml) |
| [`dead_rung_scoring_dead_cap4`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/dead_rung_scoring_dead_cap4.md) | `01_STAR/tie_break_dead_rung/` | 1 | Dead rung — scoring round, dead five-star rung, cap 4 → _Ann_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/dead_rung_scoring_dead_cap4.yaml) |
| [`tie_break_01_scoring_five_star_breaks`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/tie_break_01_scoring_five_star_breaks.md) | `01_STAR/tie_break_dead_rung/` | 1 | Tie-break 01 — scoring-round tie, FIVE-STAR breaks it (a 5 exists) → _Alice_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/tie_break_01_scoring_five_star_breaks.yaml) |
| [`tie_break_02_scoring_no_fives_to_lot`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/tie_break_02_scoring_no_fives_to_lot.md) | `01_STAR/tie_break_dead_rung/` | 1 | Tie-break 02 — scoring-round tie, NO fives, five-star is a dead rung → LOT → _Alice_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/tie_break_02_scoring_no_fives_to_lot.yaml) |
| [`tie_break_03_runoff_no_fives_to_lot`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/tie_break_03_runoff_no_fives_to_lot.md) | `01_STAR/tie_break_dead_rung/` | 1 | Tie-break 03 — runoff tie, score tied, NO fives → LOT → _Alice_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/tie_break_03_runoff_no_fives_to_lot.yaml) |
| [`tie_break_04_runoff_five_star_breaks`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/tie_break_04_runoff_five_star_breaks.md) | `01_STAR/tie_break_dead_rung/` | 1 | Tie-break 04 — runoff tie, score tied, FIVE-STAR breaks it (a 5 exists) → _Alice_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/tie_break_04_runoff_five_star_breaks.yaml) |
| [`tie_break_05_scoring_five_star_vs_adversarial_lot`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/tie_break_05_scoring_five_star_vs_adversarial_lot.md) | `01_STAR/tie_break_dead_rung/` | 1 | Dead rung 01 — scoring tie, five-star rung ALIVE → _Ben_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/tie_break_05_scoring_five_star_vs_adversarial_lot.yaml) |
| [`tie_break_06_scoring_dead_rung_adversarial_lot`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/tie_break_06_scoring_dead_rung_adversarial_lot.md) | `01_STAR/tie_break_dead_rung/` | 1 | Dead rung 02 — same tie, but nobody scored a 5 → _Ann_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/tie_break_06_scoring_dead_rung_adversarial_lot.yaml) |
| [`tie_break_07_runoff_five_star_vs_adversarial_lot`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/tie_break_07_runoff_five_star_vs_adversarial_lot.md) | `01_STAR/tie_break_dead_rung/` | 1 | Dead rung 03 — runoff tie broken by five-star → _Ann_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/tie_break_07_runoff_five_star_vs_adversarial_lot.yaml) |
| [`tie_break_08_runoff_dead_rung_adversarial_lot`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/tie_break_08_runoff_dead_rung_adversarial_lot.md) | `01_STAR/tie_break_dead_rung/` | 1 | Dead rung 04 — runoff tie, nobody scored a 5, lot decides → _Ben_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/tie_break_08_runoff_dead_rung_adversarial_lot.yaml) |
| [`tie_break_09_five_star_tied_nonzero`](../../01_STAR/tie_break_dead_rung/tie_break_dead_rung_pages/tie_break_09_five_star_tied_nonzero.md) | `01_STAR/tie_break_dead_rung/` | 1 | Dead rung 05 — five-star rung alive but non-separating → _Ben_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/tie_break_09_five_star_tied_nonzero.yaml) |
| [`lot_random_vs_published_jfk7pd_bv_order`](../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd_pages/lot_random_vs_published_jfk7pd_bv_order.md) | `01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/` | 1 | Lot-decided tie (BV jfk7pd) — following BetterVoting's random draw → _Ben_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd_bv_order.yaml) |
| [`lot_random_vs_published_jfk7pd_published_order`](../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd_pages/lot_random_vs_published_jfk7pd_published_order.md) | `01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/` | 1 | Lot-decided tie (BV jfk7pd) — following a deterministic published order → _Ada_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd_published_order.yaml) |
| [`three_way_dead_rung_A`](../../01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie_pages/three_way_dead_rung_A.md) | `01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/` | 1 | Three-way dead-rung tie — published order A,B,C elects A → _A_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_A.yaml) |
| [`three_way_dead_rung_B`](../../01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie_pages/three_way_dead_rung_B.md) | `01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/` | 1 | Three-way dead-rung tie — published order B,C,A elects B → _B_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_B.yaml) |
| [`three_way_dead_rung_C`](../../01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie_pages/three_way_dead_rung_C.md) | `01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/` | 1 | Three-way dead-rung tie — published order C,A,B elects C → _C_ | [`.yaml`](../../01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_C.yaml) |
| [`rrv_sample_c15_b13_three-parties`](../../03_STAR_PR/_main/_main_pages/rrv_sample_c15_b13_three-parties.md) | `03_STAR_PR/_main/` | 1 | RRV sample as single-winner STAR — three parties (Purple/Orange/Yellow) → _Orange5_ | [`.yaml`](../../03_STAR_PR/_main/rrv_sample_c15_b13_three-parties.yaml) |
| [`lot_tiebreak_bv_order.yaml`](../../YAML_library/1_positive/lot_tiebreak_bv_order.yaml) | `YAML_library/1_positive/` | 1 | Lot tiebreak — following BetterVoting's drawn order → _Ben_ | — |
| [`lot_tiebreak_published_order.yaml`](../../YAML_library/1_positive/lot_tiebreak_published_order.yaml) | `YAML_library/1_positive/` | 1 | Lot tiebreak — following the new published-lot approach → _Ada_ | — |
| [`BV_Library_star_condorcet_winner`](../../method_comparisons/BV_Library/BV_Library_pages/BV_Library_star_condorcet_winner.md) | `method_comparisons/BV_Library/` | 1 | BV parity — STAR: highest-scoring Condorcet winner → _Allison_ | [`.yaml`](../../method_comparisons/BV_Library/BV_Library_star_condorcet_winner.yaml) |
| [`BV_Library_star_runnerup_tie`](../../method_comparisons/BV_Library/BV_Library_pages/BV_Library_star_runnerup_tie.md) | `method_comparisons/BV_Library/` | 1 | BV parity — STAR: runner-up tie, Allison wins → _Allison_ | [`.yaml`](../../method_comparisons/BV_Library/BV_Library_star_runnerup_tie.yaml) |
| [`BV_Library_star_runoff`](../../method_comparisons/BV_Library/BV_Library_pages/BV_Library_star_runoff.md) | `method_comparisons/BV_Library/` | 1 | BV parity — STAR: runoff, lower total wins the runoff → _Bill_ | [`.yaml`](../../method_comparisons/BV_Library/BV_Library_star_runoff.yaml) |
| [`BV_Library_star_runoff_score_tie_five_star`](../../method_comparisons/BV_Library/BV_Library_pages/BV_Library_star_runoff_score_tie_five_star.md) | `method_comparisons/BV_Library/` | 1 | BV parity — STAR: runoff & score tie, five-star tiebreaker → _Allison_ | [`.yaml`](../../method_comparisons/BV_Library/BV_Library_star_runoff_score_tie_five_star.yaml) |
| [`BV_Library_star_runoff_tie_score_resolves`](../../method_comparisons/BV_Library/BV_Library_pages/BV_Library_star_runoff_tie_score_resolves.md) | `method_comparisons/BV_Library/` | 1 | BV parity — STAR: runoff tie broken by score → _Bill_ | [`.yaml`](../../method_comparisons/BV_Library/BV_Library_star_runoff_tie_score_resolves.yaml) |
| [`count_simplicity_star_vs_irv`](../../method_comparisons/_main/_main_pages/count_simplicity_star_vs_irv.md) | `method_comparisons/_main/` | 1 | Same winner, very different counts — STAR adds, IRV eliminates → _Carmen_ | [`.yaml`](../../method_comparisons/_main/count_simplicity_star_vs_irv.yaml) |
| [`Black_Curtain_01_c3_b5_hidden-consensus`](../../method_comparisons/black_curtain/black_curtain_pages/Black_Curtain_01_c3_b5_hidden-consensus.md) | `method_comparisons/black_curtain/` | 1 | The Black Curtain → _Cal_ | [`.yaml`](../../method_comparisons/black_curtain/Black_Curtain_01_c3_b5_hidden-consensus.yaml) |
| [`Black_Curtain_02_c3_b5_near-clones`](../../method_comparisons/black_curtain/black_curtain_pages/Black_Curtain_02_c3_b5_near-clones.md) | `method_comparisons/black_curtain/` | 1 | The Black Curtain → _Cal_ | [`.yaml`](../../method_comparisons/black_curtain/Black_Curtain_02_c3_b5_near-clones.yaml) |
| [`Black_Curtain_03_c3_b5_polarized-on-cal`](../../method_comparisons/black_curtain/black_curtain_pages/Black_Curtain_03_c3_b5_polarized-on-cal.md) | `method_comparisons/black_curtain/` | 1 | The Black Curtain → _Cal_ | [`.yaml`](../../method_comparisons/black_curtain/Black_Curtain_03_c3_b5_polarized-on-cal.yaml) |
| [`Black_Curtain_04_c4_b5_four-candidates`](../../method_comparisons/black_curtain/black_curtain_pages/Black_Curtain_04_c4_b5_four-candidates.md) | `method_comparisons/black_curtain/` | 1 | The Black Curtain → _Cal_ | [`.yaml`](../../method_comparisons/black_curtain/Black_Curtain_04_c4_b5_four-candidates.yaml) |
| [`center_squeeze_star`](../../method_comparisons/center_squeeze/center_squeeze_pages/center_squeeze_star.md) | `method_comparisons/center_squeeze/` | 1 | Center squeeze — STAR elects the consensus (Center) → _Center_ | [`.yaml`](../../method_comparisons/center_squeeze/center_squeeze_star.yaml) |
| [`center_squeeze_voteline_1d`](../../method_comparisons/center_squeeze/center_squeeze_pages/center_squeeze_voteline_1d.md) | `method_comparisons/center_squeeze/` | 1 | Center squeeze — the voteline 1D spectrum (Red / Green / Yellow) → _Green_ | [`.yaml`](../../method_comparisons/center_squeeze/center_squeeze_voteline_1d.yaml) |
| [`monotonicity_star_after`](../../method_comparisons/monotonicity/monotonicity_pages/monotonicity_star_after.md) | `method_comparisons/monotonicity/` | 1 | Monotonicity — STAR counterpart (AFTER — X still wins) → _X_ | [`.yaml`](../../method_comparisons/monotonicity/monotonicity_star_after.yaml) |
| [`monotonicity_star_before`](../../method_comparisons/monotonicity/monotonicity_pages/monotonicity_star_before.md) | `method_comparisons/monotonicity/` | 1 | Monotonicity — STAR counterpart (BEFORE — X wins) → _X_ | [`.yaml`](../../method_comparisons/monotonicity/monotonicity_star_before.yaml) |
| [`Whoops_01_tennessee_three_winners`](../../method_comparisons/paradoxes_and_whoops/paradoxes_and_whoops_pages/Whoops_01_tennessee_three_winners.md) | `method_comparisons/paradoxes_and_whoops/` | 1 | Whoops 01 — same ballots, three methods, three winners (Tennessee) → _Nashville_ | [`.yaml`](../../method_comparisons/paradoxes_and_whoops/Whoops_01_tennessee_three_winners.yaml) |
| [`Whoops_02_star_misses_condorcet`](../../method_comparisons/paradoxes_and_whoops/paradoxes_and_whoops_pages/Whoops_02_star_misses_condorcet.md) | `method_comparisons/paradoxes_and_whoops/` | 1 | Whoops 02 — STAR misses the Condorcet winner (STAR's own whoops) → _Ada_ | [`.yaml`](../../method_comparisons/paradoxes_and_whoops/Whoops_02_star_misses_condorcet.yaml) |
| [`Whoops_03_condorcet_cycle_rps`](../../method_comparisons/paradoxes_and_whoops/paradoxes_and_whoops_pages/Whoops_03_condorcet_cycle_rps.md) | `method_comparisons/paradoxes_and_whoops/` | 1 | Whoops 03 — a Condorcet cycle (rock-paper-scissors, no winner) → _Rock_ | [`.yaml`](../../method_comparisons/paradoxes_and_whoops/Whoops_03_condorcet_cycle_rps.yaml) |
| [`00_plurality_vs_majority`](../../method_comparisons/split_voting/_main/_main_pages/00_plurality_vs_majority.md) | `method_comparisons/split_voting/_main/` | 1 | Plurality vs Majority — most votes isn't more than half → _Blake_ | [`.yaml`](../../method_comparisons/split_voting/_main/00_plurality_vs_majority.yaml) |
| [`01_political_left_split`](../../method_comparisons/split_voting/_main/_main_pages/01_political_left_split.md) | `method_comparisons/split_voting/_main/` | 1 | Spoiler — a split coalition hands the seat to the minority → _Labour_ | [`.yaml`](../../method_comparisons/split_voting/_main/01_political_left_split.yaml) |
| [`02_icecream_chocolate_split`](../../method_comparisons/split_voting/_main/_main_pages/02_icecream_chocolate_split.md) | `method_comparisons/split_voting/_main/` | 1 | Spoiler — chocolate's majority splits, vanilla steals the win → _MilkChoco_ | [`.yaml`](../../method_comparisons/split_voting/_main/02_icecream_chocolate_split.yaml) |
| [`03_lunch_veggie_vs_meat`](../../method_comparisons/split_voting/_main/_main_pages/03_lunch_veggie_vs_meat.md) | `method_comparisons/split_voting/_main/` | 1 | Spoiler — the veggie majority splits, the burger wins the lunch vote → _VeggieCurry_ | [`.yaml`](../../method_comparisons/split_voting/_main/03_lunch_veggie_vs_meat.yaml) |
| [`04_star_wars_vote_split`](../../method_comparisons/split_voting/_main/_main_pages/04_star_wars_vote_split.md) | `method_comparisons/split_voting/_main/` | 1 | The Voting Dilemma — Skywalker & Leia split the Rebel vote → _Leia_ | [`.yaml`](../../method_comparisons/split_voting/_main/04_star_wars_vote_split.yaml) |
| [`05a_residual_split_bullet-voting`](../../method_comparisons/split_voting/_main/_main_pages/05a_residual_split_bullet-voting.md) | `method_comparisons/split_voting/_main/` | 1 | STAR's residual split — a coalition bullet-votes itself apart → _Cara_ | [`.yaml`](../../method_comparisons/split_voting/_main/05a_residual_split_bullet-voting.yaml) |
| [`05b_residual_split_expressive-fix`](../../method_comparisons/split_voting/_main/_main_pages/05b_residual_split_expressive-fix.md) | `method_comparisons/split_voting/_main/` | 1 | The cure — score your ally, and STAR's split disappears → _Ada_ | [`.yaml`](../../method_comparisons/split_voting/_main/05b_residual_split_expressive-fix.yaml) |
| [`star_combined`](../../method_comparisons/summability_demo/summability_demo_pages/star_combined.md) | `method_comparisons/summability_demo/` | 1 | Summability demo — STAR combined A+B (Oak; precinct subtotals add up) → _Oak_ | [`.yaml`](../../method_comparisons/summability_demo/star_combined.yaml) |
| [`star_district_A`](../../method_comparisons/summability_demo/summability_demo_pages/star_district_A.md) | `method_comparisons/summability_demo/` | 1 | Summability demo — STAR district A (Maple wins outright) → _Maple_ | [`.yaml`](../../method_comparisons/summability_demo/star_district_A.yaml) |
| [`star_district_B`](../../method_comparisons/summability_demo/summability_demo_pages/star_district_B.md) | `method_comparisons/summability_demo/` | 1 | Summability demo — STAR district B (Oak wins — a runoff reversal) → _Oak_ | [`.yaml`](../../method_comparisons/summability_demo/star_district_B.yaml) |

## RCV-IRV (Hare)  (9)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`RCV_ballot_example`](../../06_Other/RCV_IRV/RCV_IRV_pages/RCV_ballot_example.md) | `06_Other/RCV_IRV/` | 1 | RCV-IRV — a basic ranked-ballot example (3 candidates) → _A_ | [`.yaml`](../../06_Other/RCV_IRV/RCV_ballot_example.yaml) |
| [`center_squeeze_irv`](../../method_comparisons/center_squeeze/center_squeeze_pages/center_squeeze_irv.md) | `method_comparisons/center_squeeze/` | 1 | Center squeeze (RCV-IRV) — minimal 27-voter case (the moderate is eliminated) → _Left_ | [`.yaml`](../../method_comparisons/center_squeeze/center_squeeze_irv.yaml) |
| [`monotonicity_irv_after`](../../method_comparisons/monotonicity/monotonicity_pages/monotonicity_irv_after.md) | `method_comparisons/monotonicity/` | 1 | Non-monotonicity (RCV-IRV) — part 2: raising X makes X lose → _Z_ | [`.yaml`](../../method_comparisons/monotonicity/monotonicity_irv_after.yaml) |
| [`monotonicity_irv_before`](../../method_comparisons/monotonicity/monotonicity_pages/monotonicity_irv_before.md) | `method_comparisons/monotonicity/` | 1 | Non-monotonicity (RCV-IRV) — part 1: baseline, X wins → _X_ | [`.yaml`](../../method_comparisons/monotonicity/monotonicity_irv_before.yaml) |
| [`Whoops_04_ossipoff_centrist_irv`](../../method_comparisons/paradoxes_and_whoops/paradoxes_and_whoops_pages/Whoops_04_ossipoff_centrist_irv.md) | `method_comparisons/paradoxes_and_whoops/` | 1 | Whoops 04 — IRV buries the centrist (Ossipoff 303-voter) | [`.yaml`](../../method_comparisons/paradoxes_and_whoops/Whoops_04_ossipoff_centrist_irv.yaml) |
| [`Whoops_05_brams_many_pathologies_irv`](../../method_comparisons/paradoxes_and_whoops/paradoxes_and_whoops_pages/Whoops_05_brams_many_pathologies_irv.md) | `method_comparisons/paradoxes_and_whoops/` | 1 | Whoops 05 — many IRV pathologies in one election (Brams) | [`.yaml`](../../method_comparisons/paradoxes_and_whoops/Whoops_05_brams_many_pathologies_irv.yaml) |
| [`irv_combined`](../../method_comparisons/summability_demo/summability_demo_pages/irv_combined.md) | `method_comparisons/summability_demo/` | 1 | Summability demo — RCV-IRV combined A+B (B eliminated; not summable) → _A_ | [`.yaml`](../../method_comparisons/summability_demo/irv_combined.yaml) |
| [`irv_district_A`](../../method_comparisons/summability_demo/summability_demo_pages/irv_district_A.md) | `method_comparisons/summability_demo/` | 1 | Summability demo — RCV-IRV district A (B wins) → _B_ | [`.yaml`](../../method_comparisons/summability_demo/irv_district_A.yaml) |
| [`irv_district_B`](../../method_comparisons/summability_demo/summability_demo_pages/irv_district_B.md) | `method_comparisons/summability_demo/` | 1 | Summability demo — RCV-IRV district B (B wins) → _B_ | [`.yaml`](../../method_comparisons/summability_demo/irv_district_B.yaml) |

## Ranked Robin (RCV-RR / Copeland)  (5)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`ranked_robin_consensus_center`](../../05_Ranked_Robin/_main/_main_pages/ranked_robin_consensus_center.md) | `05_Ranked_Robin/_main/` | 1 | Ranked Robin (RCV-RR) — the consensus center wins the round-robin → _Ben_ | [`.yaml`](../../05_Ranked_Robin/_main/ranked_robin_consensus_center.yaml) |
| [`01_condorcet_winner`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/condorcet_vs_ranked_robin_pages/01_condorcet_winner.md) | `05_Ranked_Robin/condorcet_vs_ranked_robin/` | 1 | Condorcet winner exists — Ranked Robin elects it → _Ada_ | [`.yaml`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/01_condorcet_winner.yaml) |
| [`02_cycle_no_condorcet`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/condorcet_vs_ranked_robin_pages/02_cycle_no_condorcet.md) | `05_Ranked_Robin/condorcet_vs_ranked_robin/` | 1 | No Condorcet winner (a cycle) — Ranked Robin still elects one → _Ada_ | [`.yaml`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/02_cycle_no_condorcet.yaml) |
| [`BV_Library_ranked_robin_single_winner`](../../method_comparisons/BV_Library/BV_Library_pages/BV_Library_ranked_robin_single_winner.md) | `method_comparisons/BV_Library/` | 1 | BV parity — Ranked Robin: Condorcet winner (equal ranks allowed) → _Alice_ | [`.yaml`](../../method_comparisons/BV_Library/BV_Library_ranked_robin_single_winner.yaml) |
| [`BV_Library_ranked_robin_ties`](../../method_comparisons/BV_Library/BV_Library_pages/BV_Library_ranked_robin_ties.md) | `method_comparisons/BV_Library/` | 1 | BV parity — Ranked Robin: Copeland tie broken by tiebreak order → _Alice_ | [`.yaml`](../../method_comparisons/BV_Library/BV_Library_ranked_robin_ties.yaml) |

## Approval  (3)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`approval_101_c3_b5`](../../04_Approval/_main/_main_pages/approval_101_c3_b5.md) | `04_Approval/_main/` | 1 | Approval 101 — most approvals wins → _Bob_ | [`.yaml`](../../04_Approval/_main/approval_101_c3_b5.yaml) |
| [`BV_Library_approval_single_winner`](../../method_comparisons/BV_Library/BV_Library_pages/BV_Library_approval_single_winner.md) | `method_comparisons/BV_Library/` | 1 | BV parity — Approval: most approvals wins (single winner) → _Dave_ | [`.yaml`](../../method_comparisons/BV_Library/BV_Library_approval_single_winner.yaml) |
| [`Black_Curtain_01a_c3_b5_approval`](../../method_comparisons/black_curtain/black_curtain_pages/Black_Curtain_01a_c3_b5_approval.md) | `method_comparisons/black_curtain/` | 1 | The Black Curtain → _Bob_ | [`.yaml`](../../method_comparisons/black_curtain/Black_Curtain_01a_c3_b5_approval.yaml) |

## STV (proportional RCV)  (1)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`03a_stv_3seats`](../../06_Other/STV/STV_pages/03a_stv_3seats.md) | `06_Other/STV/` | 3 | STV — 3 seats, 7 candidates (proportional RCV) → _Housing, Schools, SmallBiz_ | [`.yaml`](../../06_Other/STV/03a_stv_3seats.yaml) |

## Bloc STAR  (4)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`00_c3_b3_bloc-baseline-2-seats`](../../02_STAR_Bloc/_main/_main_pages/00_c3_b3_bloc-baseline-2-seats.md) | `02_STAR_Bloc/_main/` | 2 | Bloc STAR baseline — 3 candidates, 2 seats (clean, no tiebreak) → _Alice, Bruno_ | [`.yaml`](../../02_STAR_Bloc/_main/00_c3_b3_bloc-baseline-2-seats.yaml) |
| [`01_c4_b2_bloc-star-2-seats`](../../02_STAR_Bloc/_main/_main_pages/01_c4_b2_bloc-star-2-seats.md) | `02_STAR_Bloc/_main/` | 2 | Bloc STAR Voting: 2-Seat Committee Election → _Don, Cal_ | [`.yaml`](../../02_STAR_Bloc/_main/01_c4_b2_bloc-star-2-seats.yaml) |
| [`bv132_verify_votes_bloc`](../../02_STAR_Bloc/_main/_main_pages/bv132_verify_votes_bloc.md) | `02_STAR_Bloc/_main/` | 2 | BV132 — verify number of votes cast (Bloc STAR, 2 seats) → _C, B_ | [`.yaml`](../../02_STAR_Bloc/_main/bv132_verify_votes_bloc.yaml) |
| [`bv1815_bloc_3c2s_basic`](../../02_STAR_Bloc/_main/_main_pages/bv1815_bloc_3c2s_basic.md) | `02_STAR_Bloc/_main/` | 2 | BV1815 — Bloc STAR, 3 candidates, 2 seats (seat 2 by score tiebreak) → _A, C_ | [`.yaml`](../../02_STAR_Bloc/_main/bv1815_bloc_3c2s_basic.yaml) |

## STAR-PR (Sequential Selection)  (2)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`02b_c5_b63_proportional-sss`](../../03_STAR_PR/_main/_main_pages/02b_c5_b63_proportional-sss.md) | `03_STAR_PR/_main/` | 3 | Proportional STAR — Sequentially Spent Score → _Alice, Ben, Dan_ | [`.yaml`](../../03_STAR_PR/_main/02b_c5_b63_proportional-sss.yaml) |
| [`03b_star_pr_3seats`](../../03_STAR_PR/_main/_main_pages/03b_star_pr_3seats.md) | `03_STAR_PR/_main/` | 3 | Proportional STAR — same 3-seat electorate as the STV demo → _Housing, Schools, SmallBiz_ | [`.yaml`](../../03_STAR_PR/_main/03b_star_pr_3seats.yaml) |

## Reweighted Range  (1)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`02c_c5_b63_proportional-rrv`](../../03_STAR_PR/_main/_main_pages/02c_c5_b63_proportional-rrv.md) | `03_STAR_PR/_main/` | 3 | Proportional — Reweighted Range Voting → _Alice, Ben, Dan_ | [`.yaml`](../../03_STAR_PR/_main/02c_c5_b63_proportional-rrv.yaml) |

## Allocated Score (STAR-PR)  (1)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`02a_c5_b63_proportional-allocated-score`](../../03_STAR_PR/_main/_main_pages/02a_c5_b63_proportional-allocated-score.md) | `03_STAR_PR/_main/` | 3 | Proportional STAR — Allocated Score Voting → _Alice, Ben, Dan_ | [`.yaml`](../../03_STAR_PR/_main/02a_c5_b63_proportional-allocated-score.yaml) |

## APPROVAL_MULTI_WINNER  (3)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`approval_bloc_2seats_c4_b6`](../../04_Approval/multiwinner/multiwinner_pages/approval_bloc_2seats_c4_b6.md) | `04_Approval/multiwinner/` | 2 | Bloc Approval — 2 seats, majority sweep → _Amy, Ben_ | [`.yaml`](../../04_Approval/multiwinner/approval_bloc_2seats_c4_b6.yaml) |
| [`approval_bloc_3seats_c6_b5`](../../04_Approval/multiwinner/multiwinner_pages/approval_bloc_3seats_c6_b5.md) | `04_Approval/multiwinner/` | 3 | Bloc Approval — 3-seat city council at-large → _Adams, Brown, Clark_ | [`.yaml`](../../04_Approval/multiwinner/approval_bloc_3seats_c6_b5.yaml) |
| [`approval_bloc_4seats_c7_b12_lackner_skowron`](../../04_Approval/multiwinner/multiwinner_pages/approval_bloc_4seats_c7_b12_lackner_skowron.md) | `04_Approval/multiwinner/` | 4 | Bloc Approval — Lackner & Skowron's running example (k=4) → _A, B, C, D_ | [`.yaml`](../../04_Approval/multiwinner/approval_bloc_4seats_c7_b12_lackner_skowron.yaml) |

## PLURALITY  (1)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`BV_Library_plurality_single_winner`](../../method_comparisons/BV_Library/BV_Library_pages/BV_Library_plurality_single_winner.md) | `method_comparisons/BV_Library/` | 1 | BV parity — Plurality (choose-one): most first-marks wins → _Dave_ | [`.yaml`](../../method_comparisons/BV_Library/BV_Library_plurality_single_winner.yaml) |

## RANGE  (1)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`range_101_c3_b5`](../../06_Other/Range/Range_pages/range_101_c3_b5.md) | `06_Other/Range/` | 1 | Range / Score Voting 101 — highest total score wins → _Beth_ | [`.yaml`](../../06_Other/Range/range_101_c3_b5.yaml) |

## RR  (1)

| Case (page) | Folder | Winners | Title / expected | src |
|------|--------|:------:|------------------|:--:|
| [`03_real_record0_c6_b5`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/condorcet_vs_ranked_robin_pages/03_real_record0_c6_b5.md) | `05_Ranked_Robin/condorcet_vs_ranked_robin/` | 1 | No Condorcet winner and Ranked Robin → _B_ | [`.yaml`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/03_real_record0_c6_b5.yaml) |
