# BetterVoting test-case registry (repo subset)

**Auto-generated — do not edit by hand.** Run `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_bv_registry.py`.

Every BV-tracked case in this repo (a file with a `bv_test_id:` field or a `bv…` filename). Machine-readable twin: [`bv_cases.csv`](bv_cases.csv) (GitHub sorts CSV columns on click). **The master Google Sheet stays authoritative for the full BV numbering** — it also tracks non-tabulation QA (UI, roles, archive…) that has no YAML here.

**13 cases** · methods: Approval_Multi_Winner (1), Bloc STAR (8), STAR (3), allocated (1).

**Test IDs in the repo:** BV27, BV95a, BV95b, BV126, BV129, BV130, BV130-r2, BV131, BV132, BV750, BV1525, BV1815, BV2130.

Highest number here is **BV2130** → the next free number above the repo is **BV2131**. (Numbering is sparse and the master Google Sheet is authoritative for choosing the next number; this list only avoids collisions with existing repo files.)

| Test ID | BV id | Method | W | Cand | Ballots | Winners | Page | YAML |
|---------|-------|--------|:-:|:-:|:-:|---------|------|------|
| BV27 | [`jt6r76`](https://bettervoting.com/jt6r76/results) | Approval_Multi_Winner | 4 | 7 | 12 | A, B, C, D | — | [yaml](../../04_Approval/multiwinner/approval_bloc_4seats_c7_b12_lackner_skowron.yaml) |
| BV95a | [`9m6rxr`](https://bettervoting.com/9m6rxr/results) | STAR | 1 | 3 | 5 | Ada | [page](../../01_STAR/majority_criterion/bv95a_9m6rxr_favorite_survives_one_rival.md) | [yaml](../../01_STAR/majority_criterion/bv95a_9m6rxr_favorite_survives_one_rival.yaml) |
| BV95b | [`7pdq3r`](https://bettervoting.com/7pdq3r/results) | STAR | 1 | 3 | 5 | Bruno | [page](../../01_STAR/majority_criterion/bv95b_7pdq3r_favorite_loses_two_rivals.md) | [yaml](../../01_STAR/majority_criterion/bv95b_7pdq3r_favorite_loses_two_rivals.yaml) |
| BV126 | [`8fvd2x`](https://bettervoting.com/8fvd2x/results) | STAR | 1 | 3 | 7 | Amy | [page](../../01_STAR/tie_break_dead_rung/bv126_ties_every_step_8fvd2x.md) | [yaml](../../01_STAR/tie_break_dead_rung/bv126_ties_every_step_8fvd2x.yaml) |
| BV129 | [`btmydt`](https://bettervoting.com/btmydt/results) | Bloc STAR | 2 | 3 | 5 | Carmen, Andre | [page](../../02_STAR_Bloc/_main/bv129_score_tiebreak_bloc.md) | [yaml](../../02_STAR_Bloc/_main/bv129_score_tiebreak_bloc.yaml) |
| BV130 | — | Bloc STAR | 3 | 6 | 9 | Someone I Like, Santa Claus, The Lesser Evil | [page](../../02_STAR_Bloc/_main/bv130_bloc_pagination_731.md) | [yaml](../../02_STAR_Bloc/_main/bv130_bloc_pagination_731.yaml) |
| BV130-r2 | [`9ff9jk`](https://bettervoting.com/9ff9jk/results) | Bloc STAR | 3 | 6 | 4 | Dan, Ada, Eve | [page](../../02_STAR_Bloc/_main/bv130r2_dead_rung_bloc.md) | [yaml](../../02_STAR_Bloc/_main/bv130r2_dead_rung_bloc.yaml) |
| BV131 | [`kbh3d9`](https://bettervoting.com/kbh3d9/results) | Bloc STAR | 2 | 3 | 3 | Cand2, Cand3 | [page](../../02_STAR_Bloc/_main/bv131_guido_bloc.md) | [yaml](../../02_STAR_Bloc/_main/bv131_guido_bloc.yaml) |
| BV132 | [`3494cb`](https://bettervoting.com/3494cb/results) | Bloc STAR | 2 | 3 | 4 | C, B | [page](../../02_STAR_Bloc/_main/bv132_verify_votes_bloc.md) | [yaml](../../02_STAR_Bloc/_main/bv132_verify_votes_bloc.yaml) |
| BV750 | [`3yr2qd`](https://bettervoting.com/3yr2qd/results) | Bloc STAR | 2 | 3 | 3 | c, a | [page](../../02_STAR_Bloc/_main/bv750_tie_breaking_bloc.md) | [yaml](../../02_STAR_Bloc/_main/bv750_tie_breaking_bloc.yaml) |
| BV1525 | — | Bloc STAR | 4 | 5 | 16 | First, Second, Third, Fourth | [page](../../02_STAR_Bloc/_main/bv1525_condorcet_loser_bloc.md) | [yaml](../../02_STAR_Bloc/_main/bv1525_condorcet_loser_bloc.yaml) |
| BV1815 | [`fk38pk`](https://bettervoting.com/fk38pk/results) | Bloc STAR | 2 | 3 | 3 | A, C | [page](../../02_STAR_Bloc/_main/bv1815_bloc_3c2s_basic.md) | [yaml](../../02_STAR_Bloc/_main/bv1815_bloc_3c2s_basic.yaml) |
| BV2130 | [`bvhchj`](https://bettervoting.com/bvhchj/results) | allocated | 7 | 51 | 101 | Bernie Sanders (Democrat), Al Gore (Democrat), Barack Obama (Democrat), Cornel West (Independent), Chase Oliver (Libertarian), Kamala Harris (Democrat), Claudia De La Cruz (Socialism and Liberation) | [page](../../03_STAR_PR/_main/bv2130_presidential_board_star_pr.md) | [yaml](../../03_STAR_PR/_main/bv2130_presidential_board_star_pr.yaml) |
