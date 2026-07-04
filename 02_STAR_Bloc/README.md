# 02_STAR_Bloc — Bloc STAR (multi-winner, majoritarian)

**Bloc STAR** fills multiple seats by running single-winner STAR repeatedly: elect a winner, remove them, re-run on the same ballots. The same majority can win every seat — that's the point (and the caveat): Bloc is **majoritarian**, not proportional. For proportional seats, see [`../03_STAR_PR/`](../03_STAR_PR).

Cases live in [`_main/`](_main). Concept docs: [`../00_start_here/proportional_representation/`](../00_start_here/proportional_representation) (which contrasts Bloc against the proportional methods).

## Bloc test-case index

In-repo index of the Bloc STAR reference cases (the LH ground truth for the corresponding rows in the *BetterVoting – test cases* master sheet). Each YAML carries `expected_winners` and is auto-checked by `test_method_positive.py`; BV-backed cases also keep a frozen `_bv_export.json` and a two-view `.md`.

| BV id | Scenario | Seats | Tie? | BV status / issue | Case |
|-------|----------|:--:|------|-------------------|------|
| — | Pure baseline (no tiebreak) | 2 | none | — | [`00_c3_b3_bloc-baseline-2-seats.yaml`](_main/00_c3_b3_bloc-baseline-2-seats.yaml) |
| BV1815 | 3c/2s — seat 2 by **score** tiebreak | 2 | runoff (seat 2) | Passed | [page](_main/bv1815_bloc_3c2s_basic.md) · [yaml](_main/bv1815_bloc_3c2s_basic.yaml) |
| BV132 | verify votes cast — flat ballots dropped | 2 | flat/no-pref | Failed · [#1073](https://github.com/Equal-Vote/bettervoting/issues/1073) | [page](_main/bv132_verify_votes_bloc.md) · [yaml](_main/bv132_verify_votes_bloc.yaml) |
| BV131 | Guido example — **hidden lot-decided tie** (seat 1) | 2 | lot (seat 1) | "Passed" (but a coin toss; `tieBreakType` mislabeled `none`) | [page](_main/bv131_guido_bloc.md) · [yaml](_main/bv131_guido_bloc.yaml) |
| BV129 | 3c/2w — seat 2 by **score** tiebreak | 2 | runoff (seat 2) | count OK; "Failed" = method-name label [#1086](https://github.com/Equal-Vote/bettervoting/issues/1086) | [page](_main/bv129_score_tiebreak_bloc.md) · [yaml](_main/bv129_score_tiebreak_bloc.yaml) |
| BV126 | "ties every step" | — | yes | Failed · [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052) | *pending* |
| BV750 | tie-breaking | — | yes | Failed | *pending* |
| BV130 | 6c/3w | 3 | — | Failed · star-server#731 | *pending* |
| BV1525 | 4 winners, 16 ballots | 4 | — | re-do | *pending* |
| BV2105 | Favorite ice cream demo | 2 | — | Failed (regression) | *pending* |

The authoritative, cross-method tracker is the Google Sheet *BetterVoting – test cases* (its **YAML File** column links back to these files); this table is just the Bloc slice, kept beside the cases.

**Conversation scripts:** the Larry ↔ Adam STAR series is indexed in [Conversation scripts — index](../00_start_here/conversation_scripts.md) (start with [What's so good about STAR](../00_start_here/STAR_Voting/whats_so_good_about_STAR_Voting.md)).

# file: README.md
