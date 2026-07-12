# Cross-method divergence review

_Generated 2026-07-12 19:24 by `STARVote_LH_tabulation_engine/tools_adam/scripts/build_divergence_index.py` — do not hand-edit; rebuild._

Re-tabulates every **curated single-winner STAR** election under RCV-IRV, Ranked Robin (RCV-RR / Copeland) and Approval, and flags where they disagree with STAR. Only hand-built library elections are scanned (never random ballots), and the base rate is reported, so the collection stays honest rather than cherry-picked.

## Base rate

- Scanned **147** single-winner STAR elections (skipped 86 non-eligible files: multi-winner / Approval / RR / RCV / ranked-ballot / unparseable).
- **76** (52%) diverge from STAR under at least one method; **71** agree across the board.

| Bucket | Count |
|---|---:|
| IRV_OUTLIER_RR_WITH_STAR | 17 |
| STAR_OUTLIER_RR_WITH_IRV | 2 |
| IRV_DIFFERS_ARTIFACT | 5 |
| CYCLE_OR_THREE_WAY | 21 |
| APPROVAL_OR_MINOR | 31 |

## Score→rank conversion (recorded both ways)

- **STRICT** — equal non-zero scores broken by lot/priority order (`score_ballot_to_ranking`). Feeds RCV-IRV and the `RR_strict` / `Condorcet_strict` columns.
- **WEAK** — equal scores stay equal (no preference). Feeds `RR_weak` / `Condorcet_weak` (the natural reading of a score ballot).
- **`rr_conv_sensitive`** = RR_weak ≠ RR_strict → the RR result depends on how ties are read; treat with care.
- RCV-IRV can't represent equal ranks, so there is no weak IRV. `tie_ballots` (ballots with tied non-zero scores) and `irv_fragile` (winner flips under reversed priority) flag a tie-break artifact.

## Cases by bucket

Review order is the teaching value of each bucket. Each case links to a full teaching `.md` (ballots + every method's report + a plain-English explanation) under `cases/`. Listing is **deduped** to one entry per distinct election (72 cases; identical library copies merged).

### IRV_OUTLIER_RR_WITH_STAR — 15

_RCV-IRV is the outlier — Ranked Robin AGREES with STAR (strongest teachable: the center-squeeze story, two methods against one)_

- **[09_c4_b100_tennessee-capital](cases/IRV_OUTLIER_RR_WITH_STAR/09_c4_b100_tennessee-capital.md)** — `01_STAR/_main/09_c4_b100_tennessee-capital.yaml` (4c/100b)  
    STAR=**Nashville** · IRV=Knoxville · RR=Nashville · Approval=Nashville · Score=Nashville · Condorcet=Nashville
- **[bv2184_fyy886_lunch_vote](cases/IRV_OUTLIER_RR_WITH_STAR/bv2184_fyy886_lunch_vote.md)** — `01_STAR/_main/bv2184_fyy886_lunch_vote.yaml` (3c/5b)  
    STAR=**Pizza** · IRV=Sushi · RR=Pizza · Approval=Pizza · Score=Pizza · Condorcet=Pizza  
    _also at: `YAML_library/1_positive/trash_delete.yaml`_
- **[center_squeeze_star](cases/IRV_OUTLIER_RR_WITH_STAR/center_squeeze_star.md)** — `method_comparisons/center_squeeze/center_squeeze_star.yaml` (3c/27b)  
    STAR=**Center** · IRV=Left · RR=Center · Approval=Left · Score=Center · Condorcet=Center
- **[center_squeeze_voteline_1d](cases/IRV_OUTLIER_RR_WITH_STAR/center_squeeze_voteline_1d.md)** — `method_comparisons/center_squeeze/center_squeeze_voteline_1d.yaml` (3c/998b)  
    STAR=**Green** · IRV=Yellow · RR=Green · Approval=Green · Score=Green · Condorcet=Green
- **[bv2137_ywckmg_star](cases/IRV_OUTLIER_RR_WITH_STAR/bv2137_ywckmg_star.md)** — `method_comparisons/center_squeeze_bv2137/bv2137_ywckmg_star.yaml` (3c/100b)  
    STAR=**Anderson** · IRV=Carter · RR=Anderson · Approval=Anderson · Score=Anderson · Condorcet=Anderson
- **[bv2168_6w2gq7_fairvote_40_15_40_moderate_cw](cases/IRV_OUTLIER_RR_WITH_STAR/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.md)** — `method_comparisons/fairvote_condorcet_claims/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.yaml` (3c/100b)  
    STAR=**Moderate** · IRV=Liberal · RR=Moderate · Approval=Liberal · Score=Liberal · Condorcet=Moderate
- **[bv2145_6fj2kg_star](cases/IRV_OUTLIER_RR_WITH_STAR/bv2145_6fj2kg_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2145_6fj2kg_star.yaml` (3c/17b)  
    STAR=**Ada** · IRV=Ben · RR=Ada · Approval=Ada · Score=Ada · Condorcet=Ada
- **[bv2150_dxg8pb_star](cases/IRV_OUTLIER_RR_WITH_STAR/bv2150_dxg8pb_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2150_dxg8pb_star.yaml` (3c/11b)  
    STAR=**Beth** · IRV=Carl · RR=Beth · Approval=Beth · Score=Beth · Condorcet=Beth
- **[bv2162_4htk44_star](cases/IRV_OUTLIER_RR_WITH_STAR/bv2162_4htk44_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2162_4htk44_star.yaml` (4c/103b)  
    STAR=**B** · IRV=A · RR=B · Approval=B · Score=B · Condorcet=B
- **[bv2155_cphxpt_tennessee_four_ways](cases/IRV_OUTLIER_RR_WITH_STAR/bv2155_cphxpt_tennessee_four_ways.md)** — `method_comparisons/paradoxes_and_whoops/bv2155_cphxpt_tennessee_four_ways.yaml` (4c/100b)  
    STAR=**Nashville** · IRV=Knoxville · RR=Nashville · Approval=Nashville · Score=Nashville · Condorcet=Nashville
- **[bv2132_ykjjhy_pet_star](cases/IRV_OUTLIER_RR_WITH_STAR/bv2132_ykjjhy_pet_star.md)** — `method_comparisons/pet_poll_four_methods/bv2132_ykjjhy_pet_star.yaml` (3c/22b)  
    STAR=**Cat** · IRV=Fish · RR=Cat · Approval=Cat · Score=Cat · Condorcet=Cat
- **[bv2133_dyxrbr_pet2_star](cases/IRV_OUTLIER_RR_WITH_STAR/bv2133_dyxrbr_pet2_star.md)** — `method_comparisons/pet_poll_four_winners/bv2133_dyxrbr_pet2_star.yaml` (4c/32b)  
    STAR=**Cat** · IRV=Fish · RR=Cat · Approval=Bird · Score=Cat · Condorcet=Cat
- **[04_star_wars_vote_split](cases/IRV_OUTLIER_RR_WITH_STAR/04_star_wars_vote_split.md)** — `method_comparisons/split_voting/_main/04_star_wars_vote_split.yaml` (3c/100b)  
    STAR=**Leia** · IRV=Skywalker · RR=Leia · Approval=Skywalker · Score=Leia · Condorcet=Leia
- **[bv2171_h93tm4_star](cases/IRV_OUTLIER_RR_WITH_STAR/bv2171_h93tm4_star.md)** — `method_comparisons/symmetric_centrist_all_methods/bv2171_h93tm4_star.yaml` (3c/8b)  
    STAR=**Casey** · IRV=Avery · RR=Casey · Approval=Casey · Score=Casey · Condorcet=Casey
- **[bv2172_bkwfjr_star](cases/IRV_OUTLIER_RR_WITH_STAR/bv2172_bkwfjr_star.md)** — `method_comparisons/symmetric_centrist_all_methods/bv2172_bkwfjr_star.yaml` (3c/100b)  
    STAR=**Casey** · IRV=Avery · RR=Casey · Approval=Casey · Score=Casey · Condorcet=Casey  
    _also at: `method_comparisons/symmetric_centrist_bv2170/bv2170_pp2q4q_star.yaml`_

### STAR_OUTLIER_RR_WITH_IRV — 2

_STAR is the outlier — Ranked Robin sides with RCV-IRV (show it anyway, for evenhandedness: STAR isn't always the Condorcet pick)_

- **[three_winners_cw_score_runoff](cases/STAR_OUTLIER_RR_WITH_IRV/three_winners_cw_score_runoff.md)** — `01_STAR/_main/three_winners_cw_score_runoff.yaml` (3c/5b)  
    STAR=**Bob** · IRV=Ann · RR=Ann · Approval=Bob · Score=Carl · Condorcet=Ann
- **[mono_raise_delete_before](cases/STAR_OUTLIER_RR_WITH_IRV/mono_raise_delete_before.md)** — `method_comparisons/monotonicity/mono_raise_delete_before.yaml` (3c/30b)  
    STAR=**X** · IRV=Z · RR=Z · Approval=X · Score=X · Condorcet=Z

### IRV_DIFFERS_ARTIFACT — 5

_RCV-IRV differs but it's a score->rank tie-break artifact (tied ballots and/or flips under reversed priority) — log, do NOT bark on IRV_

- **[display_options_demo](cases/IRV_DIFFERS_ARTIFACT/display_options_demo.md)** — `01_STAR/_main/display_options_demo.yaml` (4c/4b)  
    STAR=**Don** · IRV=Bob · RR=Don · Approval=Ann · Score=Bob · Condorcet=Don  
    _flags: 2 tied-score ballot(s); IRV flips on reversed priority; RR conv-sensitive (weak=Don, strict=Bob)_
- **[star_ala_approval](cases/IRV_DIFFERS_ARTIFACT/star_ala_approval.md)** — `01_STAR/_main/star_ala_approval.yaml` (4c/8b)  
    STAR=**D** · IRV=A · RR=D · Approval=A · Score=D · Condorcet=D  
    _flags: 4 tied-score ballot(s); IRV flips on reversed priority; RR conv-sensitive (weak=D, strict=A)_
- **[bv95b_7pdq3r_favorite_loses_two_rivals](cases/IRV_DIFFERS_ARTIFACT/bv95b_7pdq3r_favorite_loses_two_rivals.md)** — `01_STAR/majority_criterion/bv95b_7pdq3r_favorite_loses_two_rivals.yaml` (3c/5b)  
    STAR=**Bruno** · IRV=Ada · RR=Ada · Approval=Bruno · Score=Bruno · Condorcet=Ada  
    _flags: 2 tied-score ballot(s)_
- **[tie_break_05_scoring_five_star_vs_adversarial_lot](cases/IRV_DIFFERS_ARTIFACT/tie_break_05_scoring_five_star_vs_adversarial_lot.md)** — `01_STAR/tie_break_dead_rung/tie_break_05_scoring_five_star_vs_adversarial_lot.yaml` (3c/5b)  
    STAR=**Ben** · IRV=Cara · RR=Ann · Approval=Ann · Score=Ann · Condorcet=none  
    _flags: 2 tied-score ballot(s); IRV flips on reversed priority; RR conv-sensitive (weak=Ann, strict=Cara)_
- **[tie_break_06_scoring_dead_rung_adversarial_lot](cases/IRV_DIFFERS_ARTIFACT/tie_break_06_scoring_dead_rung_adversarial_lot.md)** — `01_STAR/tie_break_dead_rung/tie_break_06_scoring_dead_rung_adversarial_lot.yaml` (3c/5b)  
    STAR=**Ann** · IRV=Cara · RR=Ann · Approval=Ann · Score=Ann · Condorcet=none  
    _flags: 2 tied-score ballot(s); IRV flips on reversed priority; RR conv-sensitive (weak=Ann, strict=Cara)_

### CYCLE_OR_THREE_WAY — 19

_Condorcet cycle / three-way split — genuinely hard case, no clean villain_

- **[lot_random_vs_published_jfk7pd_bv_order](cases/CYCLE_OR_THREE_WAY/lot_random_vs_published_jfk7pd_bv_order.md)** — `01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd_bv_order.yaml` (2c/2b)  
    STAR=**Ben** · IRV=Ada · RR=Ben · Approval=Ben · Score=Ben · Condorcet=none  
    _also at: `YAML_library/1_positive/lot_tiebreak_bv_order.yaml`_
- **[three_way_dead_rung_A](cases/CYCLE_OR_THREE_WAY/three_way_dead_rung_A.md)** — `01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_A.yaml` (3c/3b)  
    STAR=**A** · IRV=B · RR=A · Approval=A · Score=A · Condorcet=none  
    _also at: `01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_C.yaml`_
- **[tie_break_04_runoff_five_star_breaks](cases/CYCLE_OR_THREE_WAY/tie_break_04_runoff_five_star_breaks.md)** — `01_STAR/tie_break_dead_rung/tie_break_04_runoff_five_star_breaks.yaml` (2c/2b)  
    STAR=**Alice** · IRV=Ben · RR=Alice · Approval=Alice · Score=Alice · Condorcet=none
- **[tie_break_07_runoff_five_star_vs_adversarial_lot](cases/CYCLE_OR_THREE_WAY/tie_break_07_runoff_five_star_vs_adversarial_lot.md)** — `01_STAR/tie_break_dead_rung/tie_break_07_runoff_five_star_vs_adversarial_lot.yaml` (2c/2b)  
    STAR=**Ann** · IRV=Ben · RR=Ben · Approval=Ben · Score=Ben · Condorcet=none
- **[tie_break_08_runoff_dead_rung_adversarial_lot](cases/CYCLE_OR_THREE_WAY/tie_break_08_runoff_dead_rung_adversarial_lot.md)** — `01_STAR/tie_break_dead_rung/tie_break_08_runoff_dead_rung_adversarial_lot.yaml` (2c/2b)  
    STAR=**Ben** · IRV=Ann · RR=Ben · Approval=Ben · Score=Ben · Condorcet=none
- **[tie_break_09_five_star_tied_nonzero](cases/CYCLE_OR_THREE_WAY/tie_break_09_five_star_tied_nonzero.md)** — `01_STAR/tie_break_dead_rung/tie_break_09_five_star_tied_nonzero.yaml` (2c/2b)  
    STAR=**Ben** · IRV=Ann · RR=Ben · Approval=Ben · Score=Ben · Condorcet=none
- **[BV_Library_star_runoff_tie_score_resolves](cases/CYCLE_OR_THREE_WAY/BV_Library_star_runoff_tie_score_resolves.md)** — `method_comparisons/BV_Library/BV_Library_star_runoff_tie_score_resolves.yaml` (2c/2b)  
    STAR=**Bill** · IRV=Bill · RR=Allison · Approval=Allison · Score=Bill · Condorcet=none
- **[bv2147_9gdrqg_star](cases/CYCLE_OR_THREE_WAY/bv2147_9gdrqg_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2147_9gdrqg_star.yaml` (3c/17b)  
    STAR=**Bruno** · IRV=Bruno · RR=Cora · Approval=Cora · Score=Cora · Condorcet=none
- **[bv2149_byk9v2_star](cases/CYCLE_OR_THREE_WAY/bv2149_byk9v2_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2149_byk9v2_star.yaml` (3c/32b)  
    STAR=**Bruno** · IRV=Alma · RR=Cora · Approval=Cora · Score=Cora · Condorcet=none
- **[bv2160_r6qc8h_star](cases/CYCLE_OR_THREE_WAY/bv2160_r6qc8h_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2160_r6qc8h_star.yaml` (4c/7b)  
    STAR=**B** · IRV=A · RR=C · Approval=B · Score=B · Condorcet=none
- **[bv2165_9vxcj7_star](cases/CYCLE_OR_THREE_WAY/bv2165_9vxcj7_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2165_9vxcj7_star.yaml` (3c/15b)  
    STAR=**Boone** · IRV=Boone · RR=Cass · Approval=Cass · Score=Cass · Condorcet=none
- **[bv2167_f3dxq9_star](cases/CYCLE_OR_THREE_WAY/bv2167_f3dxq9_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2167_f3dxq9_star.yaml` (4c/11b)  
    STAR=**B** · IRV=C · RR=A · Approval=B · Score=B · Condorcet=none
- **[monotonicity_star_after](cases/CYCLE_OR_THREE_WAY/monotonicity_star_after.md)** — `method_comparisons/monotonicity/monotonicity_star_after.yaml` (3c/34b)  
    STAR=**X** · IRV=Z · RR=X · Approval=X · Score=X · Condorcet=none
- **[monotonicity_star_before](cases/CYCLE_OR_THREE_WAY/monotonicity_star_before.md)** — `method_comparisons/monotonicity/monotonicity_star_before.yaml` (3c/34b)  
    STAR=**X** · IRV=X · RR=Y · Approval=Y · Score=Y · Condorcet=none
- **[bv2138_cxrf8v_star](cases/CYCLE_OR_THREE_WAY/bv2138_cxrf8v_star.md)** — `method_comparisons/no_condorcet_bv2138/bv2138_cxrf8v_star.yaml` (5c/921b)  
    STAR=**Brad** · IRV=Dave · RR=Abby · Approval=Erin · Score=Abby · Condorcet=none
- **[bv2156_3grpbb_star_misses_condorcet](cases/CYCLE_OR_THREE_WAY/bv2156_3grpbb_star_misses_condorcet.md)** — `method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.yaml` (3c/100b)  
    STAR=**Ada** · IRV=Ada · RR=Cleo · Approval=Ada · Score=Ada · Condorcet=Cleo  
    _flags: 25 tied-score ballot(s); IRV flips on reversed priority_
- **[bv2174_yyhr66_noshow_baseline](cases/CYCLE_OR_THREE_WAY/bv2174_yyhr66_noshow_baseline.md)** — `method_comparisons/participation_no_show/bv2174_yyhr66_noshow_baseline.yaml` (3c/54b)  
    STAR=**Bruno** · IRV=Bruno · RR=Celia · Approval=Celia · Score=Celia · Condorcet=none
- **[bv2175_9dhv8y_noshow_showup](cases/CYCLE_OR_THREE_WAY/bv2175_9dhv8y_noshow_showup.md)** — `method_comparisons/participation_no_show/bv2175_9dhv8y_noshow_showup.yaml` (3c/62b)  
    STAR=**April** · IRV=Celia · RR=April · Approval=April · Score=April · Condorcet=none
- **[bv2176_p8dp28_star](cases/CYCLE_OR_THREE_WAY/bv2176_p8dp28_star.md)** — `method_comparisons/postit_rcv_example/bv2176_p8dp28_star.yaml` (4c/20b)  
    STAR=**Blue** · IRV=Purple · RR=Blue · Approval=Pink · Score=Purple · Condorcet=none

### APPROVAL_OR_MINOR — 31

_Only Approval (or a minor method) differs — usually a threshold story, not an IRV one_

- **[03b_c3_b3_1_style-protest-vote](cases/APPROVAL_OR_MINOR/03b_c3_b3_1_style-protest-vote.md)** — `01_STAR/_main/03b_c3_b3_1_style-protest-vote.yaml` (3c/3b)  
    STAR=**Almond** · IRV=Almond · RR=Almond · Approval=Choco · Score=Almond · Condorcet=Almond
- **[03b_c3_b3_2_expand_style-protest-vote](cases/APPROVAL_OR_MINOR/03b_c3_b3_2_expand_style-protest-vote.md)** — `01_STAR/_main/03b_c3_b3_2_expand_style-protest-vote.yaml` (3c/3b)  
    STAR=**Almond** · IRV=Almond · RR=Almond · Approval=Choco · Score=Almond · Condorcet=Almond
- **[04b_c4_b3_display-options-all](cases/APPROVAL_OR_MINOR/04b_c4_b3_display-options-all.md)** — `01_STAR/_main/04b_c4_b3_display-options-all.yaml` (4c/3b)  
    STAR=**Strawberry** · IRV=Strawberry · RR=Strawberry · Approval=Vanilla · Score=Strawberry · Condorcet=Strawberry
- **[bv2182_tg4779_faq_runoff_reversal](cases/APPROVAL_OR_MINOR/bv2182_tg4779_faq_runoff_reversal.md)** — `01_STAR/_main/bv2182_tg4779_faq_runoff_reversal.yaml` (3c/10b)  
    STAR=**Almond** · IRV=Almond · RR=Almond · Approval=Berry · Score=Berry · Condorcet=Almond  
    _flags: 1 tied-score ballot(s)_
- **[bv95a_9m6rxr_favorite_survives_one_rival](cases/APPROVAL_OR_MINOR/bv95a_9m6rxr_favorite_survives_one_rival.md)** — `01_STAR/majority_criterion/bv95a_9m6rxr_favorite_survives_one_rival.yaml` (3c/5b)  
    STAR=**Ada** · IRV=Ada · RR=Ada · Approval=Bruno · Score=Bruno · Condorcet=Ada  
    _flags: 2 tied-score ballot(s)_
- **[01a_c3_b3_more-stars-fewer-voters](cases/APPROVAL_OR_MINOR/01a_c3_b3_more-stars-fewer-voters.md)** — `01_STAR/runoff_overturns_leader/01a_c3_b3_more-stars-fewer-voters.yaml` (3c/3b)  
    STAR=**Brownie** · IRV=Brownie · RR=Brownie · Approval=Almond · Score=Almond · Condorcet=Brownie
- **[01b_c3_b9_overturn-holds-at-scale](cases/APPROVAL_OR_MINOR/01b_c3_b9_overturn-holds-at-scale.md)** — `01_STAR/runoff_overturns_leader/01b_c3_b9_overturn-holds-at-scale.yaml` (3c/9b)  
    STAR=**Brownie** · IRV=Brownie · RR=Brownie · Approval=Almond · Score=Almond · Condorcet=Brownie
- **[02_c5_b5_leader-overturned](cases/APPROVAL_OR_MINOR/02_c5_b5_leader-overturned.md)** — `01_STAR/runoff_overturns_leader/02_c5_b5_leader-overturned.yaml` (5c/5b)  
    STAR=**Boston** · IRV=Boston · RR=Boston · Approval=Austin · Score=Austin · Condorcet=Boston
- **[03_c7_b3_ice-cream-live](cases/APPROVAL_OR_MINOR/03_c7_b3_ice-cream-live.md)** — `01_STAR/runoff_overturns_leader/03_c7_b3_ice-cream-live.yaml` (7c/3b)  
    STAR=**ChocoAlm** · IRV=ChocoAlm · RR=ChocoAlm · Approval=ChocoDrk · Score=ChocoDrk · Condorcet=ChocoAlm
- **[05_c3_b5_low-scores-bv1265](cases/APPROVAL_OR_MINOR/05_c3_b5_low-scores-bv1265.md)** — `01_STAR/runoff_overturns_leader/05_c3_b5_low-scores-bv1265.yaml` (3c/5b)  
    STAR=**A** · IRV=A · RR=A · Approval=C · Score=C · Condorcet=A  
    _flags: 1 tied-score ballot(s)_
- **[Runoff_02_atom_reversal_yx9447](cases/APPROVAL_OR_MINOR/Runoff_02_atom_reversal_yx9447.md)** — `01_STAR/runoff_overturns_leader/Runoff_02_atom_reversal_yx9447.yaml` (3c/3b)  
    STAR=**Boston** · IRV=Boston · RR=Boston · Approval=Austin · Score=Austin · Condorcet=Boston
- **[Runoff_03_enthusiasts_vs_majority_rkgtpk](cases/APPROVAL_OR_MINOR/Runoff_03_enthusiasts_vs_majority_rkgtpk.md)** — `01_STAR/runoff_overturns_leader/Runoff_03_enthusiasts_vs_majority_rkgtpk.yaml` (5c/5b)  
    STAR=**Eden** · IRV=Eden · RR=Eden · Approval=Dakota · Score=Dakota · Condorcet=Eden
- **[Runoff_04_reversal_at_scale_bfjqmg](cases/APPROVAL_OR_MINOR/Runoff_04_reversal_at_scale_bfjqmg.md)** — `01_STAR/runoff_overturns_leader/Runoff_04_reversal_at_scale_bfjqmg.yaml` (3c/9b)  
    STAR=**Olive** · IRV=Olive · RR=Olive · Approval=Maple · Score=Maple · Condorcet=Olive
- **[Runoff_05_reversal_with_equal_support_xgkw3w](cases/APPROVAL_OR_MINOR/Runoff_05_reversal_with_equal_support_xgkw3w.md)** — `01_STAR/runoff_overturns_leader/Runoff_05_reversal_with_equal_support_xgkw3w.yaml` (3c/5b)  
    STAR=**Sage** · IRV=Sage · RR=Sage · Approval=Rosa · Score=Rosa · Condorcet=Sage  
    _flags: 2 tied-score ballot(s); IRV flips on reversed priority_
- **[Runoff_07_flat_ballot_bv_bug_tf73v9](cases/APPROVAL_OR_MINOR/Runoff_07_flat_ballot_bv_bug_tf73v9.md)** — `01_STAR/runoff_overturns_leader/Runoff_07_flat_ballot_bv_bug_tf73v9.yaml` (3c/4b)  
    STAR=**Blair** · IRV=Blair · RR=Blair · Approval=Alex · Score=Alex · Condorcet=Blair  
    _flags: 1 tied-score ballot(s); IRV flips on reversed priority_
- **[reversal_jarring_c3_b100](cases/APPROVAL_OR_MINOR/reversal_jarring_c3_b100.md)** — `01_STAR/runoff_overturns_leader/reversal_jarring_c3_b100.yaml` (3c/100b)  
    STAR=**Rye** · IRV=Rye · RR=Rye · Approval=Uma · Score=Uma · Condorcet=Rye
- **[bv2180_fp62p2_ice_cream_ladder](cases/APPROVAL_OR_MINOR/bv2180_fp62p2_ice_cream_ladder.md)** — `01_STAR/tie_break_ladder/bv2180_fp62p2_ice_cream_ladder.yaml` (6c/2b)  
    STAR=**Strawberry** · IRV=Strawberry · RR=Strawberry · Approval=Chocolate · Score=Strawberry · Condorcet=none  
    _flags: 2 tied-score ballot(s)_
- **[BV_Library_star_runoff_score_tie_five_star](cases/APPROVAL_OR_MINOR/BV_Library_star_runoff_score_tie_five_star.md)** — `method_comparisons/BV_Library/BV_Library_star_runoff_score_tie_five_star.yaml` (2c/2b)  
    STAR=**Allison** · IRV=Allison · RR=Allison · Approval=Bill · Score=Allison · Condorcet=none
- **[count_simplicity_star_vs_irv](cases/APPROVAL_OR_MINOR/count_simplicity_star_vs_irv.md)** — `method_comparisons/_main/count_simplicity_star_vs_irv.yaml` (5c/40b)  
    STAR=**Carmen** · IRV=Carmen · RR=Carmen · Approval=Andre · Score=Carmen · Condorcet=Carmen
- **[Black_Curtain_01_c3_b5_hidden-consensus](cases/APPROVAL_OR_MINOR/Black_Curtain_01_c3_b5_hidden-consensus.md)** — `method_comparisons/black_curtain/Black_Curtain_01_c3_b5_hidden-consensus.yaml` (3c/5b)  
    STAR=**Cal** · IRV=Cal · RR=Cal · Approval=Bob · Score=Bob · Condorcet=Cal
- **[Black_Curtain_02_c3_b5_near-clones](cases/APPROVAL_OR_MINOR/Black_Curtain_02_c3_b5_near-clones.md)** — `method_comparisons/black_curtain/Black_Curtain_02_c3_b5_near-clones.yaml` (3c/5b)  
    STAR=**Cal** · IRV=Cal · RR=Cal · Approval=Ann · Score=Cal · Condorcet=Cal
- **[Black_Curtain_03_c3_b5_polarized-on-cal](cases/APPROVAL_OR_MINOR/Black_Curtain_03_c3_b5_polarized-on-cal.md)** — `method_comparisons/black_curtain/Black_Curtain_03_c3_b5_polarized-on-cal.yaml` (3c/5b)  
    STAR=**Cal** · IRV=Cal · RR=Cal · Approval=Ann · Score=Ann · Condorcet=Cal
- **[bv2173_gmfv4c_edelman_saari_cancellation](cases/APPROVAL_OR_MINOR/bv2173_gmfv4c_edelman_saari_cancellation.md)** — `method_comparisons/edelman_condorcet_myth/bv2173_gmfv4c_edelman_saari_cancellation.yaml` (3c/81b)  
    STAR=**Ada** · IRV=Ada · RR=Ada · Approval=Ben · Score=Ben · Condorcet=Ada
- **[bv2148_h87k6v_star](cases/APPROVAL_OR_MINOR/bv2148_h87k6v_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2148_h87k6v_star.yaml` (3c/15b)  
    STAR=**Bruno** · IRV=Bruno · RR=Bruno · Approval=Cora · Score=Bruno · Condorcet=Bruno
- **[bv2161_q3h4fk_star](cases/APPROVAL_OR_MINOR/bv2161_q3h4fk_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2161_q3h4fk_star.yaml` (3c/7b)  
    STAR=**C** · IRV=C · RR=C · Approval=B · Score=C · Condorcet=none
- **[bv2164_xbqq8t_star](cases/APPROVAL_OR_MINOR/bv2164_xbqq8t_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2164_xbqq8t_star.yaml` (4c/33b)  
    STAR=**Arlo** · IRV=Arlo · RR=Arlo · Approval=Bree · Score=Bree · Condorcet=Arlo
- **[bv2166_b7b8dv_star](cases/APPROVAL_OR_MINOR/bv2166_b7b8dv_star.md)** — `method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_star.yaml` (3c/13b)  
    STAR=**Cass** · IRV=Cass · RR=Cass · Approval=Amy · Score=Cass · Condorcet=none
- **[mono_raise_delete_after](cases/APPROVAL_OR_MINOR/mono_raise_delete_after.md)** — `method_comparisons/monotonicity/mono_raise_delete_after.yaml` (3c/30b)  
    STAR=**Z** · IRV=Z · RR=Z · Approval=X · Score=X · Condorcet=Z
- **[bv2157_mmcmpy_condorcet_cycle_rps](cases/APPROVAL_OR_MINOR/bv2157_mmcmpy_condorcet_cycle_rps.md)** — `method_comparisons/paradoxes_and_whoops/bv2157_mmcmpy_condorcet_cycle_rps.yaml` (3c/100b)  
    STAR=**Rock** · IRV=Rock · RR=Rock · Approval=Paper · Score=Rock · Condorcet=none
- **[bv2178_8kg698_star](cases/APPROVAL_OR_MINOR/bv2178_8kg698_star.md)** — `method_comparisons/postit_rcv_example/bv2178_8kg698_star.yaml` (4c/20b)  
    STAR=**Blue** · IRV=Blue · RR=Blue · Approval=Pink · Score=Purple · Condorcet=Blue
- **[star_district_B](cases/APPROVAL_OR_MINOR/star_district_B.md)** — `method_comparisons/summability_demo/star_district_B.yaml` (3c/3b)  
    STAR=**Oak** · IRV=Oak · RR=Oak · Approval=Pine · Score=Pine · Condorcet=Oak

## Full table

See `divergence.csv` for the machine-readable version (all columns, including the strict/weak split).

