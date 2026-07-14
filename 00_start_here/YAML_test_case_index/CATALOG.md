# Test-case catalog — slice the elections & races every way

*Generated — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_catalog.py`.*

Two grains underlie every view here:

- **Election** = the container: one electorate casting into **1..N races**, with a `bvid` (or LH-only). *Single-race* = one contest; *contested* = several.
- **Race** = the atom that gets tabulated: exactly **one method, one seat count, one candidate set, one ballot type, one winner set**. This is the fact table ([`races.csv`](races.csv)).

Each race carries derived facets so you can slice: **ballot type** (score / ranked / approval / choose-one), **seat class** (single- vs multi-winner), and **character** (majoritarian / proportional / Condorcet). BV-only races with no yaml (e.g. Bloc Plurality) are pulled in from the frozen exports.

**Totals:** 218 elections, 307 races. Full drill-down: [`races.csv`](races.csv) · [`elections.csv`](elections.csv). Related: [BV registry](BV_registry.md) · [multi-race index](multirace_elections.md) · [by method](README.md).

## Elections

| Election | Title | Races | Kind | Voters | Methods | Backing |
|---|---|--:|---|--:|---|---|
| 2jrfpg | BV2169 — FairVote's hypothetical, electorate shifted | 2 | contested (multi-race) | 100 | IRV, STAR | BV |
| 3grpbb | BV2156 — STAR's own miss — the Condorcet winner scor | 2 | contested (multi-race) | 100 | RankedRobin, STAR | BV |
| 3x4vrv | BV2135 — Block & Limited voting, reproduced as bloc  | 2 | contested (multi-race) | 10 | Plurality | BV |
| 4htk44 | BV2162 — Nurmi's truncation electorate (1 of 2) — ev | 3 | contested (multi-race) | 103 | IRV, RankedRobin, STAR | BV |
| 6fj2kg | BV2145 — Felsenthal's runoff paradoxes (1 of 2) — th | 3 | contested (multi-race) | 17 | IRV, RankedRobin, STAR | BV |
| 6w2gq7 | BV2168 — FairVote's Condorcet hypothetical, counted  | 2 | contested (multi-race) | 100 | IRV, STAR | BV |
| 74j6vv | BV2163 — Nurmi's truncation electorate (2 of 2) — 17 | 3 | contested (multi-race) | 103 | IRV, RankedRobin, STAR | BV |
| 8kg698 | BV2178 — The Post-it election's round-2 switch, made | 4 | contested (multi-race) | 20 | IRV, Plurality, RankedRobin, STAR | BV |
| 97hbpw | BV2151 — Felsenthal's No-Show paradox (2 of 2) — two | 3 | contested (multi-race) | 9 | IRV, RankedRobin, STAR | BV |
| 9gdrqg | BV2147 — Felsenthal's Reinforcement paradox (I of II | 2 | contested (multi-race) | 17 | IRV, STAR | BV |
| 9vxcj7 | BV2165 — Coombs' No-Show electorate (1 of 2) — every | 2 | contested (multi-race) | 15 | Plurality, STAR | BV |
| example_tennessee | Tennessee capital — RCV-IRV engine demo | 2 | contested (multi-race) | 100 | IRV, STAR | LH-only |
| b7b8dv | BV2166 — Coombs' No-Show electorate (2 of 2) — two v | 2 | contested (multi-race) | 13 | Plurality, STAR | BV |
| bkwfjr | BV2172 — The Condorcet centrist, full form (100 vote | 7 | contested (multi-race) | 100 | Approval, IRV, Plurality, RankedRobin, STAR, STAR_PR, STV | BV |
| bvhchj | Presidential Board Election | 2 | contested (multi-race) | 102 | Plurality, STAR_PR | BV |
| byk9v2 | BV2149 — Felsenthal's Reinforcement paradox (III of  | 2 | contested (multi-race) | 32 | IRV, STAR | BV |
| cphxpt | BV2155 — Tennessee capital, four ways — one electora | 4 | contested (multi-race) | 100 | IRV, Plurality, RankedRobin, STAR | BV |
| cxrf8v | BV2138 — One Ranked Electorate, Many Tabulations — t | 4 | contested (multi-race) | 921 | IRV, RankedRobin, STAR, STV | BV |
| dxg8pb | BV2150 — Felsenthal's No-Show paradox (1 of 2) — eve | 3 | contested (multi-race) | 11 | IRV, RankedRobin, STAR | BV |
| dyxrbr | BV2133 — Pet poll II: four methods, four winners | 4 | contested (multi-race) | 32 | Approval, IRV, Plurality, STAR | BV |
| f3dxq9 | BV2167 — Minimax elects the absolute loser — the can | 2 | contested (multi-race) | 11 | Plurality, STAR | BV |
| f4cjpy | BV2159 — Brams' 21-voter sampler — IRV elects B whil | 3 | contested (multi-race) | 21 | IRV, RankedRobin, STAR | BV |
| gr72hd | BV2158 — Ossipoff's buried centrist — the candidate  | 4 | contested (multi-race) | 303 | IRV, Plurality, RankedRobin, STAR | BV |
| gvdy42 | 2026 California Governor Election | 2 | contested (multi-race) | 319 | IRV, STAR | BV |
| h87k6v | BV2148 — Felsenthal's Reinforcement paradox (II of I | 2 | contested (multi-race) | 15 | IRV, STAR | BV |
| h93tm4 | BV2171 — The Condorcet centrist, minimal form (8 vot | 7 | contested (multi-race) | 8 | Approval, IRV, Plurality, RankedRobin, STAR, STAR_PR, STV | BV |
| jfrk9t | BV655 - “equal opposition” vote - the “Same-Score Ba | 2 | contested (multi-race) | 2 | STAR | BV |
| kcf8vf | BV2134 — Pets Governance: six positions, six methods | 6 | contested (multi-race) | 22 | Approval, Plurality, RankedRobin, STAR, STAR_PR, STV | BV |
| krk2px | BV2146 — Felsenthal's runoff paradoxes (2 of 2) — mo | 3 | contested (multi-race) | 17 | IRV, RankedRobin, STAR | BV |
| mmcmpy | BV2157 — Rock, Paper, Scissors — a Condorcet cycle:  | 3 | contested (multi-race) | 100 | Approval, IRV, STAR | BV |
| mxfmhm | BV2144 — Felsenthal's plurality paradoxes — the abso | 2 | contested (multi-race) | 7 | Plurality, STAR | BV |
| p8dp28 | BV2176 — The Post-it RCV example (20 voters) — RCV-I | 3 | contested (multi-race) | 20 | IRV, RankedRobin, STAR | BV |
| pcttmr | BV2153 — Felsenthal's Absolute Majority paradox — a  | 3 | contested (multi-race) | 100 | Approval, IRV, RankedRobin | BV |
| pp2q4q | BV2170 — The centrist a majority prefers, squeezed o | 4 | contested (multi-race) | 100 | IRV, Plurality, RankedRobin, STAR | BV |
| q3h4fk | BV2161 — Borda's SCC paradox electorate — the winner | 2 | contested (multi-race) | 7 | Plurality, STAR | BV |
| r6ctvy | BV2152 — Felsenthal & Maoz's Approval paradox — the  | 2 | contested (multi-race) | 47 | Approval, RankedRobin | BV |
| r6qc8h | BV2160 — Fishburn's Borda truncation electorate — ST | 2 | contested (multi-race) | 7 | Plurality, STAR | BV |
| v8r66y | BV2177 — The Post-it election, seven ways — all four | 7 | contested (multi-race) | 20 | Approval, IRV, Plurality, RankedRobin, STAR, STAR_PR, STV | BV |
| wq6yv7 | BV2154 — Felsenthal's Approval paradox — the absolut | 3 | contested (multi-race) | 15 | Approval, IRV, RankedRobin | BV |
| xbqq8t | BV2164 — Coombs deletes the Condorcet winner first — | 3 | contested (multi-race) | 33 | Plurality, RankedRobin, STAR | BV |
| ykjjhy | BV2132 — Pet poll: four methods, three winners | 4 | contested (multi-race) | 22 | Approval, IRV, Plurality, STAR | BV |
| ywckmg | BV2137 — Center Squeeze — the centrist Condorcet win | 4 | contested (multi-race) | 100 | IRV, RankedRobin, STAR, STV | BV |
| 26khr3 | NOTA test — None of the Above wins (with a null abst | 1 | single-race | 6 | STAR | BV |
| 3494cb | BV132 - verify number of votes vast - bloc STAR voti | 1 | single-race | 4 | STAR | BV |
| 3r3yf7 | BV2141 — Ranked Robin — a Copeland tie that needs al | 1 | single-race | 81 | RankedRobin | BV |
| 3w6v4b | Equal Support vs Abstention — minimal STAR test (A/B | 1 | single-race | 5 | STAR | BV |
| 3yr2qd | Block STAR | 1 | single-race | 3 | STAR | BV |
| 48hjkv | BV2140 — Ranked Robin worked example — most pairwise | 1 | single-race | 35 | RankedRobin | BV |
| 4gfwdq | BV2142 — Ranked Robin clone independence (1 of 2) —  | 1 | single-race | 33 | RankedRobin | BV |
| 4h89vj | B15 - Basic - 2 candidates - Plurality - Abstain | 1 | single-race | 12 | Plurality | BV |
| 6hv7jf | BV1570 - deactivate selection - plurality voting - C | 1 | single-race | 3 | Plurality | BV |
| 6xhfp8 | BV11 - Valid Ballot - Full and Equal Support (2 Cand | 1 | single-race | 3 | STAR | BV |
| 7pdq3r | BV95b - Majority Criterion: favorite loses (backs tw | 1 | single-race | 5 | STAR | BV |
| 8fvd2x | BV126 - “ties every time - every step” - Multiple ti | 1 | single-race | 7 | STAR | BV |
| 9dhv8y | No-show paradox (2 of 2) — the 8 April fans vote; RC | 1 | single-race | 62 | STAR | BV |
| 9ff9jk | BV130 — 6 candidates / 3 winners, Bloc STAR | 1 | single-race | 4 | STAR | BV |
| 9m6rxr | BV95a - Majority Criterion: favorite survives (backs | 1 | single-race | 5 | STAR | BV |
| 9pr3wr | BV2143 — Ranked Robin clone independence (2 of 2) —  | 1 | single-race | 33 | RankedRobin | BV |
| 00_c3_b3_bloc-baseline-2-seats | Bloc STAR baseline — 3 candidates, 2 seats (clean, n | 1 | single-race | 3 | STAR | LH-only |
| 00_plurality_vs_majority | Plurality vs Majority — most votes isn't more than h | 1 | single-race | 100 | STAR | LH-only |
| 01_c3_b3_ann-bob-cal | Ann, Bob, Cal - the canonical leading example (singl | 1 | single-race | 3 | STAR | LH-only |
| 01_c4_b2_bloc-star-2-seats | Bloc STAR Voting: 2-Seat Committee Election | 1 | single-race | 2 | STAR | LH-only |
| 01_condorcet_winner | Condorcet winner exists — Ranked Robin elects it | 1 | single-race | 5 | RankedRobin | LH-only |
| 01_political_left_split | Spoiler — a split coalition hands the seat to the mi | 1 | single-race | 100 | STAR | LH-only |
| 01a_c2_b1_two-candidates | The simplest possible STAR Voting example | 1 | single-race | 1 | STAR | LH-only |
| 01a_c3_b3_more-stars-fewer-voters | More stars, fewer voters — the runoff overturns the  | 1 | single-race | 3 | STAR | LH-only |
| 01b_c2_b2_two-candidates | Again, very similar - this time second ballot is 5 a | 1 | single-race | 2 | STAR | LH-only |
| 01b_c3_b9_overturn-holds-at-scale | The same overturn at scale — 67% to 33% | 1 | single-race | 9 | STAR | LH-only |
| 01c_c2_b3_two-candidates | Equal support example ("I like both flavors") | 1 | single-race | 3 | STAR | LH-only |
| 02_c5_b5_leader-overturned | Five candidates — the score leader is overturned in  | 1 | single-race | 5 | STAR | LH-only |
| 02_cycle_no_condorcet | No Condorcet winner (a cycle) — Ranked Robin still e | 1 | single-race | 7 | RankedRobin | LH-only |
| 02_icecream_chocolate_split | Spoiler — chocolate's majority splits, vanilla steal | 1 | single-race | 100 | STAR | LH-only |
| 02a_c3_b1_three-candidates | Three candidates, one ballot - single-winner STAR | 1 | single-race | 1 | STAR | LH-only |
| 02a_c5_b63_proportional-allocated-score | Proportional STAR — Allocated Score Voting | 1 | single-race | 63 | STAR_PR | LH-only |
| 02b_c3_b2_three-candidates | Three candidates, two ballots - single-winner STAR | 1 | single-race | 2 | STAR | LH-only |
| 02b_c5_b63_proportional-sss | Proportional STAR — Sequentially Spent Score | 1 | single-race | 63 | STAR_PR | LH-only |
| 02c_c5_b63_proportional-rrv | Proportional — Reweighted Range Voting | 1 | single-race | 63 | STAR_PR | LH-only |
| 03_c7_b3_ice-cream-live | Ice Cream — Flavor of the Year (the real recorded ra | 1 | single-race | 3 | STAR | LH-only |
| 03_lunch_veggie_vs_meat | Spoiler — the veggie majority splits, the burger win | 1 | single-race | 100 | STAR | LH-only |
| 03_real_record0_c6_b5 | No Condorcet winner and Ranked Robin | 1 | single-race | 5 | RankedRobin | LH-only |
| 03a_c3_b3_style-bullet-vote | Voting styles — a valid STAR bullet vote (3 candidat | 1 | single-race | 3 | STAR | LH-only |
| 03a_stv_3seats | STV — 3 seats, 7 candidates (proportional RCV) | 1 | single-race | 100 | STV | LH-only |
| 03b_c3_b3_1_style-protest-vote | Voting styles — low-score ballots | 1 | single-race | 3 | STAR | LH-only |
| 03b_c3_b3_2_expand_style-protest-vote | Voting styles — low-score ballots (continued) | 1 | single-race | 3 | STAR | LH-only |
| 03b_star_pr_3seats | Proportional STAR — same 3-seat electorate as the ST | 1 | single-race | 100 | STAR_PR | LH-only |
| 03c_c6_b8_style-gallery | Voting styles — eight ways to fill out one 5-star ba | 1 | single-race | 8 | STAR | LH-only |
| 04_c4_b3_runoff-confirms-leader | The control case — here the runoff CONFIRMS the scor | 1 | single-race | 3 | STAR | LH-only |
| 04_star_wars_vote_split | The Voting Dilemma — Skywalker & Leia split the Rebe | 1 | single-race | 100 | STAR | LH-only |
| 04b_c4_b3_display-options-all | All options demo | 1 | single-race | 3 | STAR | LH-only |
| 05_c3_b5_low-scores-bv1265 | Low scores, switched winner — the popover example (B | 1 | single-race | 5 | STAR | LH-only |
| 05a_c5_b3_unanimous-ballots | Unanimous ballots (five candidates) | 1 | single-race | 3 | STAR | LH-only |
| 05a_residual_split_bullet-voting | STAR's residual split — a coalition bullet-votes its | 1 | single-race | 100 | STAR | LH-only |
| 05b_residual_split_expressive-fix | The cure — score your ally, and STAR's split disappe | 1 | single-race | 100 | STAR | LH-only |
| 06a_c9_b3_large-field-equal-support | Large field (9 candidates) — STAR scales, and Equal  | 1 | single-race | 3 | STAR | LH-only |
| 06b_c9_runoff-overturns-leader | Large field (9 candidates) — the runoff OVERTURNS th | 1 | single-race | 3 | STAR | LH-only |
| 09_c4_b100_tennessee-capital | Tennessee Capital — classic STAR example | 1 | single-race | 100 | STAR | LH-only |
| 321_tennessee_blank_encoding_c4_b100 | Tennessee capital by 3-2-1 Voting (blank = Bad) | 1 | single-race | 100 | 3-2-1 | LH-only |
| BV_Library_approval_single_winner | BV parity — Approval: most approvals wins (single wi | 1 | single-race | 10 | Approval | LH-only |
| BV_Library_plurality_single_winner | BV parity — Plurality (choose-one): most first-marks | 1 | single-race | 14 | Plurality | LH-only |
| BV_Library_ranked_robin_single_winner | BV parity — Ranked Robin: Condorcet winner (equal ra | 1 | single-race | 11 | RankedRobin | LH-only |
| BV_Library_ranked_robin_ties | BV parity — Ranked Robin: Copeland tie broken by tie | 1 | single-race | 6 | RankedRobin | LH-only |
| BV_Library_star_condorcet_winner | BV parity — STAR: highest-scoring Condorcet winner | 1 | single-race | 10 | STAR | LH-only |
| BV_Library_star_pr_basic_two_seats | BV parity — STAR_PR (Allocated Score): basic two-sea | 1 | single-race | 10 | STAR_PR | LH-only |
| BV_Library_star_pr_fractional_surplus | BV parity — STAR_PR (Allocated Score): fractional su | 1 | single-race | 12 | STAR_PR | LH-only |
| BV_Library_star_pr_voters_fewer_than_seats | BV parity — STAR_PR (Allocated Score): fewer voters  | 1 | single-race | 2 | STAR_PR | LH-only |
| BV_Library_star_runnerup_tie | BV parity — STAR: runner-up tie, Allison wins | 1 | single-race | 10 | STAR | LH-only |
| BV_Library_star_runoff | BV parity — STAR: runoff, lower total wins the runof | 1 | single-race | 2 | STAR | LH-only |
| BV_Library_star_runoff_score_tie_five_star | BV parity — STAR: runoff & score tie, five-star tieb | 1 | single-race | 2 | STAR | LH-only |
| BV_Library_star_runoff_tie_score_resolves | BV parity — STAR: runoff tie broken by score | 1 | single-race | 2 | STAR | LH-only |
| Black_Curtain_01_c3_b5_hidden-consensus | The Black Curtain | 1 | single-race | 5 | STAR | LH-only |
| Black_Curtain_01a_c3_b5_approval | The Black Curtain | 1 | single-race | 5 | Approval | LH-only |
| Black_Curtain_02_c3_b5_near-clones | The Black Curtain | 1 | single-race | 5 | STAR | LH-only |
| Black_Curtain_03_c3_b5_polarized-on-cal | The Black Curtain | 1 | single-race | 5 | STAR | LH-only |
| Black_Curtain_04_c4_b5_four-candidates | The Black Curtain | 1 | single-race | 5 | STAR | LH-only |
| Flat_scores_ties_01_baseline_clean | Flat scores 01 — clean top two (works-fine baseline) | 1 | single-race | 2 | STAR | LH-only |
| Flat_scores_ties_02_runoff_tie_2cand | Flat scores 02 — runoff tie, two candidates (everyon | 1 | single-race | 2 | STAR | LH-only |
| Flat_scores_ties_03_runoff_tie_split | Flat scores 03 — runoff tie, an even 1-1 split | 1 | single-race | 2 | STAR | LH-only |
| Flat_scores_ties_04_scoring_tie_2way | Flat scores 04 — scoring-round tie for the 2nd final | 1 | single-race | 3 | STAR | LH-only |
| Flat_scores_ties_05_scoring_tie_3way_xmyf7k | Flat scores 05 — scoring-round 3-way tie (BV555, xmy | 1 | single-race | 2 | STAR | LH-only |
| Flat_scores_ties_06_scoring_tie_4way | Flat scores 06 — scoring-round 4-way tie (ties at ev | 1 | single-race | 2 | STAR | LH-only |
| Flat_scores_ties_07_fully_flat | Flat scores 07 — fully flat ballots (the maximal tie | 1 | single-race | 2 | STAR | LH-only |
| Flat_scores_ties_08_all_flat_zero_count | Flat scores 08 — every ballot flat (BetterVoting cou | 1 | single-race | 5 | STAR | LH-only |
| RCV_ballot_example | RCV-IRV — a basic ranked-ballot example (3 candidate | 1 | single-race | 100 | IRV | LH-only |
| abstention_reconciliation_min_c2_b6 | Abstention vs Equal Support — the minimal reconcilia | 1 | single-race | 6 | STAR | LH-only |
| abstentions | Abstentions — blank and abstaining ballots in STAR | 1 | single-race | 6 | STAR | LH-only |
| approval_bloc_2seats_c4_b6 | Bloc Approval — 2 seats, majority sweep | 1 | single-race | 6 | Approval | LH-only |
| approval_bloc_3seats_c6_b5 | Bloc Approval — 3-seat city council at-large | 1 | single-race | 5 | Approval | LH-only |
| center_squeeze_irv | Center squeeze (RCV-IRV) — minimal 27-voter case (th | 1 | single-race | 27 | IRV | LH-only |
| center_squeeze_star | Center squeeze — STAR elects the consensus (Center) | 1 | single-race | 27 | STAR | LH-only |
| center_squeeze_voteline_1d | Center squeeze — the voteline 1D spectrum (Red / Gre | 1 | single-race | 998 | STAR | LH-only |
| clone_teaming_01_pre | Clone independence (1/2) — before cloning: A, B, C t | 1 | single-race | 33 | RankedRobin | LH-only |
| clone_teaming_02_post | Clone independence (2/2) — teaming: A runs clones an | 1 | single-race | 33 | RankedRobin | LH-only |
| count_simplicity_star_vs_irv | Same winner, very different counts — STAR adds, IRV  | 1 | single-race | 40 | STAR | LH-only |
| dead_heat_lot_tiebreak | Ranked Robin — a dead heat that runs the whole tiebr | 1 | single-race | 4 | RankedRobin | LH-only |
| dead_rung_scoring_dead_cap2 | Dead rung — scoring round, dead five-star rung, cap  | 1 | single-race | 2 | STAR | LH-only |
| dead_rung_scoring_dead_cap3 | Dead rung — scoring round, dead five-star rung, cap  | 1 | single-race | 2 | STAR | LH-only |
| dead_rung_scoring_dead_cap4 | Dead rung — scoring round, dead five-star rung, cap  | 1 | single-race | 2 | STAR | LH-only |
| display_options_demo | Display options demo | 1 | single-race | 4 | STAR | LH-only |
| edelman_perfect_component_c3_b30 | A perfect 'Condorcet component' (30 voters) — every  | 1 | single-race | 30 | STAR | LH-only |
| equal_support_runoff_demo | Equal Support — counted in both rounds, neutral only | 1 | single-race | 100 | STAR | LH-only |
| felsenthal_ex6_pareto_approval | Felsenthal Ex.6 — Approval can elect a Pareto-domina | 1 | single-race | 3 | Approval | LH-only |
| felsenthal_ex6_ranked_robin | Felsenthal Ex.6 — Ranked Robin: the Pareto-dominant  | 1 | single-race | 3 | RankedRobin | LH-only |
| irv_combined | Summability demo — RCV-IRV combined A+B (B eliminate | 1 | single-race | 26 | IRV | LH-only |
| irv_district_A | Summability demo — RCV-IRV district A (B wins) | 1 | single-race | 13 | IRV | LH-only |
| irv_district_B | Summability demo — RCV-IRV district B (B wins) | 1 | single-race | 13 | IRV | LH-only |
| lackner_skowron_shadow_bloc_star_c7_b12 | Shadow STAR (Bloc) — Lackner & Skowron's running exa | 1 | single-race | 12 | STAR | LH-only |
| lackner_skowron_shadow_star_pr_c7_b12 | Shadow STAR-PR (Allocated Score) — Lackner & Skowron | 1 | single-race | 12 | STAR_PR | LH-only |
| lackner_skowron_shadow_star_pr_rrv_c7_b12 | Shadow STAR-PR (RRV) — Lackner & Skowron's running e | 1 | single-race | 12 | STAR_PR | LH-only |
| lot_random_vs_published_jfk7pd_bv_order | Lot-decided tie (BV jfk7pd) — following BetterVoting | 1 | single-race | 2 | STAR | LH-only |
| lot_random_vs_published_jfk7pd_published_order | Lot-decided tie (BV jfk7pd) — following a determinis | 1 | single-race | 2 | STAR | LH-only |
| lot_tiebreak_bv_order | Lot tiebreak — following BetterVoting's drawn order | 1 | single-race | 2 | STAR | LH-only |
| lot_tiebreak_published_order | Lot tiebreak — following the new published-lot appro | 1 | single-race | 2 | STAR | LH-only |
| mmp_sntv | Multi-member plurality — SNTV (3 seats): the minorit | 1 | single-race | 10 | Plurality | LH-only |
| monotonicity_irv_after | Non-monotonicity (RCV-IRV) — part 2: raising X makes | 1 | single-race | 34 | IRV | LH-only |
| monotonicity_irv_before | Non-monotonicity (RCV-IRV) — part 1: baseline, X win | 1 | single-race | 34 | IRV | LH-only |
| monotonicity_star_after | Monotonicity — STAR counterpart (AFTER — X still win | 1 | single-race | 34 | STAR | LH-only |
| monotonicity_star_before | Monotonicity — STAR counterpart (BEFORE — X wins) | 1 | single-race | 34 | STAR | LH-only |
| options_examples | Display-options reference — every reporting toggle ( | 1 | single-race | 100 | STAR | LH-only |
| quorum_demo_c3_b6 | Quorum — an abstention still counts toward turnout | 1 | single-race | 6 | STAR | LH-only |
| quorum_fail_demo_c3_b6 | Quorum FAILS — won the count, but not elected | 1 | single-race | 6 | STAR | LH-only |
| range_101_c3_b5 | Range / Score Voting 101 — highest total score wins | 1 | single-race | 5 | Range | LH-only |
| ranked_robin_consensus_center | Ranked Robin (RCV-RR) — the consensus center wins th | 1 | single-race | 13 | RankedRobin | LH-only |
| reversal_convincing_c3_b100 | Runoff reversal, the convincing case — an intense mi | 1 | single-race | 100 | STAR | LH-only |
| reversal_jarring_c3_b100 | Runoff reversal, the jarring case — the near-consens | 1 | single-race | 100 | STAR | LH-only |
| rr_combined | Summability demo — Combined (A+B), counted by Ranked | 1 | single-race | 26 | RankedRobin | LH-only |
| rr_district_A | Summability demo — District A, counted by Ranked Rob | 1 | single-race | 13 | RankedRobin | LH-only |
| rr_district_B | Summability demo — District B, counted by Ranked Rob | 1 | single-race | 13 | RankedRobin | LH-only |
| rrv_sample_c15_b13_three-parties | RRV sample as single-winner STAR — three parties (Pu | 1 | single-race | 13 | STAR | LH-only |
| star_ala_approval | STAR à la Approval — 0/1 & marker ballots are legal  | 1 | single-race | 8 | STAR | LH-only |
| star_combined | Summability demo — STAR combined A+B (Oak; precinct  | 1 | single-race | 6 | STAR | LH-only |
| star_district_A | Summability demo — STAR district A (Maple wins outri | 1 | single-race | 3 | STAR | LH-only |
| star_district_B | Summability demo — STAR district B (Oak wins — a run | 1 | single-race | 3 | STAR | LH-only |
| three_way_dead_rung_A | Three-way dead-rung tie — published order A,B,C elec | 1 | single-race | 3 | STAR | LH-only |
| three_way_dead_rung_B | Three-way dead-rung tie — published order B,C,A elec | 1 | single-race | 3 | STAR | LH-only |
| three_way_dead_rung_C | Three-way dead-rung tie — published order C,A,B elec | 1 | single-race | 3 | STAR | LH-only |
| three_winners_cw_score_runoff | Three notions of "winner" disagree — Condorcet, Scor | 1 | single-race | 5 | STAR | LH-only |
| tie_break_01_scoring_five_star_breaks | Tie-break 01 — scoring-round tie, FIVE-STAR breaks i | 1 | single-race | 2 | STAR | LH-only |
| tie_break_02_scoring_no_fives_to_lot | Tie-break 02 — scoring-round tie, NO fives, five-sta | 1 | single-race | 2 | STAR | LH-only |
| tie_break_03_runoff_no_fives_to_lot | Tie-break 03 — runoff tie, score tied, NO fives → LO | 1 | single-race | 2 | STAR | LH-only |
| tie_break_04_runoff_five_star_breaks | Tie-break 04 — runoff tie, score tied, FIVE-STAR bre | 1 | single-race | 2 | STAR | LH-only |
| tie_break_05_scoring_five_star_vs_adversarial_lot | Dead rung 01 — scoring tie, five-star rung ALIVE | 1 | single-race | 5 | STAR | LH-only |
| tie_break_06_scoring_dead_rung_adversarial_lot | Dead rung 02 — same tie, but nobody scored a 5 | 1 | single-race | 5 | STAR | LH-only |
| tie_break_07_runoff_five_star_vs_adversarial_lot | Dead rung 03 — runoff tie broken by five-star | 1 | single-race | 2 | STAR | LH-only |
| tie_break_08_runoff_dead_rung_adversarial_lot | Dead rung 04 — runoff tie, nobody scored a 5, lot de | 1 | single-race | 2 | STAR | LH-only |
| tie_break_09_five_star_tied_nonzero | Dead rung 05 — five-star rung alive but non-separati | 1 | single-race | 2 | STAR | LH-only |
| vote_splitting | Vote splitting — two chocolates split the majority | 1 | single-race | 36 | STAR | LH-only |
| vote_splitting2 | Vote splitting — two chocolates split the majority | 1 | single-race | 360 | STAR | LH-only |
| vote_splitting3 | Vote splitting — two chocolates split the majority | 1 | single-race | 21 | STAR | LH-only |
| vote_splitting_scenario1_spoiler | Vote splitting — scenario 1 of 3 — the spoiler strik | 1 | single-race | 90 | STAR | LH-only |
| vote_splitting_scenario2_bloc_leads | Vote splitting — scenario 2 of 3 — no spoiler (bloc  | 1 | single-race | 36 | STAR | LH-only |
| vote_splitting_scenario3_outsider_wins | Vote splitting — scenario 3 of 3 — no spoiler (the o | 1 | single-race | 62 | STAR | LH-only |
| bfjqmg | Runoff_04 — the reversal holds at scale (67/33) | 1 | single-race | 9 | STAR | BV |
| btmydt | BV129 - 3 cand - 2 winners (Bloc STAR) | 1 | single-race | 5 | STAR | BV |
| d664xw | Runoff_06 - Runoff confirms the leader at scale (con | 1 | single-race | 5 | STAR | BV |
| dfw8rj | BV2183 — Forced Ballot Exhaustion — a 2-rank cap dis | 1 | single-race | 50 | IRV | BV |
| dkj9dx | BV1525 - Condorcet loser ties for seat 1 (Bloc STAR, | 1 | single-race | 16 | STAR | BV |
| dq2dmm | BV Abstentions and flat scores | 1 | single-race | 8 | STAR | BV |
| ff6mk3 | BV135 - Approval 101 — most approvals wins | 1 | single-race | 5 | Approval | BV |
| fk38pk | BV1815 - STAR Bloc - 3 candidates - 2 seats (basic / | 1 | single-race | 3 | STAR | BV |
| fp62p2 | BV2180 — Ice Cream, six flavors — a STAR tie in both | 1 | single-race | 2 | STAR | BV |
| fyy886 | BV2184 — The Team Lunch Vote — a beginner's STAR exa | 1 | single-race | 5 | STAR | BV |
| gmfv4c | Edelman's 'Myth of the Condorcet Winner' 81 voters — | 1 | single-race | 81 | STAR | BV |
| jfk7pd | The BV recipe (the "crazy" scenario) | 1 | single-race | 2 | STAR | BV |
| jt6r76 | BV27 - Lackner & Skowron steering committee (Approva | 1 | single-race | 12 | Approval | BV |
| kbh3d9 | Guido example - bloc STAR | 1 | single-race | 3 | STAR | BV |
| my82v6 | 01a_c2_b2 — two candidates, two ballots (Chocolate/V | 1 | single-race | 2 | STAR | BV |
| pet | What Makes the Best Pet? | 1 | single-race | 461 | STAR | BV |
| r2pvc9 | Runoff confirms the leader (control)  | 1 | single-race | 3 | STAR | BV |
| r4dqvd | BV2105 - Favorite ice cream (Bloc STAR) - without en | 1 | single-race | 4 | STAR | BV |
| rkgtpk | Runoff_03 — the 201-level reversal in a bigger field | 1 | single-race | 5 | STAR | BV |
| tf73v9 | Runoff_07 (WIP) — flat ballot exposes the BV abstent | 1 | single-race | 4 | STAR | BV |
| tg4779 | BV2182 — Why STAR Has an Automatic Runoff — a Runoff | 1 | single-race | 10 | STAR | BV |
| vqyqkr | Tennessee capital — Ranked Robin (RR/Condorcet = Nas | 1 | single-race | 100 | RankedRobin | BV |
| xgkw3w | Runoff_05 - Reversal with Equal Support | 1 | single-race | 5 | STAR | BV |
| y3tvxm | BV2136 — Village Council by SNTV — a concentrated mi | 1 | single-race | 9 | Plurality | BV |
| yhxy7q | BV130 - original steering committee (Bloc STAR, k=3; | 1 | single-race | 9 | STAR | BV |
| yx9447 | Runoff_02 The atom — smallest runoff reversal | 1 | single-race | 3 | STAR | BV |
| yyhr66 | No-show paradox (1 of 2) — 8 April fans stay home; R | 1 | single-race | 54 | STAR | BV |

## Cuts

Counts per facet with example elections; drill into [`races.csv`](races.csv) to filter/sort the full set (GitHub renders CSV with sortable, filterable columns — it's the closest thing to a database view).

### By single vs multi-race

Whether a race sits in a single-contest election or a **contested** (multi-race) one — same electorate, several races.

| single vs multi-race | # races | example elections |
|---|--:|---|
| single-race | 176 | 00_c3_b3_bloc-baseline-2-seats, 00_plurality_vs_majority, 01_c3_b3_ann-bob-cal, 01_c4_b2_bloc-star-2-seats |
| contested (multi-race) | 131 | 2jrfpg, 3grpbb, 3x4vrv, 4htk44 |

### By seat class

**Single-winner** (num_winners = 1) vs **multi-winner** (a body of seats).

| seat class | # races | example elections |
|---|--:|---|
| single-winner | 272 | 00_plurality_vs_majority, 01_c3_b3_ann-bob-cal, 01_condorcet_winner, 01_political_left_split |
| multi-winner | 35 | 00_c3_b3_bloc-baseline-2-seats, 01_c4_b2_bloc-star-2-seats, 02a_c5_b63_proportional-allocated-score, 02b_c5_b63_proportional-sss |

### By ballot type

What the voter marks: **score** (0–5), **ranked** (A>B>C), **approval** (0/1), or **choose-one**.

| ballot type | # races | example elections |
|---|--:|---|
| score | 179 | 00_c3_b3_bloc-baseline-2-seats, 00_plurality_vs_majority, 01_c3_b3_ann-bob-cal, 01_c4_b2_bloc-star-2-seats |
| ranked | 85 | 01_condorcet_winner, 02_cycle_no_condorcet, 03_real_record0_c6_b5, 03a_stv_3seats |
| choose-one | 25 | 3x4vrv, 4h89vj, 6hv7jf, 8kg698 |
| approval | 17 | BV_Library_approval_single_winner, Black_Curtain_01a_c3_b5_approval, approval_bloc_2seats_c4_b6, approval_bloc_3seats_c6_b5 |
| ? | 1 | 321_tennessee_blank_encoding_c4_b100 |

### By character

A rough teaching cut: **majoritarian** (a majority can take every seat), **proportional** (seats track factions — STAR-PR, STV), or **Condorcet** (elects the pairwise winner — Ranked Robin).

| character | # races | example elections |
|---|--:|---|
| majoritarian | 245 | 00_c3_b3_bloc-baseline-2-seats, 00_plurality_vs_majority, 01_c3_b3_ann-bob-cal, 01_c4_b2_bloc-star-2-seats |
| Condorcet | 41 | 01_condorcet_winner, 02_cycle_no_condorcet, 03_real_record0_c6_b5, 3grpbb |
| proportional | 21 | 02a_c5_b63_proportional-allocated-score, 02b_c5_b63_proportional-sss, 02c_c5_b63_proportional-rrv, 03a_stv_3seats |

### By method (family)

Canonical method family — e.g. Bloc STAR and STAR both normalize to STAR; allocated/sss/rrv to STAR_PR.

| method (family) | # races | example elections |
|---|--:|---|
| STAR | 164 | 00_c3_b3_bloc-baseline-2-seats, 00_plurality_vs_majority, 01_c3_b3_ann-bob-cal, 01_c4_b2_bloc-star-2-seats |
| RankedRobin | 41 | 01_condorcet_winner, 02_cycle_no_condorcet, 03_real_record0_c6_b5, 3grpbb |
| IRV | 37 | 2jrfpg, 4htk44, 6fj2kg, 6w2gq7 |
| Plurality | 25 | 3x4vrv, 4h89vj, 6hv7jf, 8kg698 |
| Approval | 17 | BV_Library_approval_single_winner, Black_Curtain_01a_c3_b5_approval, approval_bloc_2seats_c4_b6, approval_bloc_3seats_c6_b5 |
| STAR_PR | 14 | 02a_c5_b63_proportional-allocated-score, 02b_c5_b63_proportional-sss, 02c_c5_b63_proportional-rrv, 03b_star_pr_3seats |
| STV | 7 | 03a_stv_3seats, bkwfjr, cxrf8v, h93tm4 |
| Range | 1 | range_101_c3_b5 |
| 3-2-1 | 1 | 321_tennessee_blank_encoding_c4_b100 |

### By backing (BV vs LH-only)

**BV** = reproduced on BetterVoting (has a frozen export). **LH-only** = tabulated only by our engine (a migration candidate). **LH-only (exception)** = genuinely can't go to BV (marked `lh_only_reason` in the yaml). Goal: keep plain LH-only near zero — reproduce on BV unless it's a marked exception.

| backing (BV vs LH-only) | # races | example elections |
|---|--:|---|
| BV | 138 | 26khr3, 2jrfpg, 3494cb, 3grpbb |
| LH-only | 134 | 00_c3_b3_bloc-baseline-2-seats, 00_plurality_vs_majority, 01_c3_b3_ann-bob-cal, 01_c4_b2_bloc-star-2-seats |
| BV (no yaml) | 34 | 2jrfpg, 3grpbb, 6w2gq7, 8kg698 |
| LH-only (exception) | 1 | dead_heat_lot_tiebreak |

### Genuine LH-only exceptions

Cases that **cannot** be reproduced on BetterVoting — a real reason (missing BV method / non-deterministic tie-break), not a coverage gap:

| Case | Method | Why it can't go to BV |
|---|---|---|
| Ranked Robin — a dead heat that runs the who | RankedRobin | BetterVoting breaks this exact tie at RANDOM (head-to-head is also tied), so its winner can't be frozen/reproduced. LH resolves it deterministically by margin then lot — the whole point of the case — so it is LH-only by design. |

## How this is organized (for adding cases)

- **One yaml = one race.** A single-race election is one yaml; a **contested election is several yamls that share `bv_election_id`** (its bvid). The catalog groups them by that id.
- **Facets are DERIVED, not hand-tagged** — from `voting_method` (→ family + ballot type + character) and `num_winners` (→ seat class). So a case shows up in the right cuts automatically; just set those two fields correctly.
- **BV-only races** (a race that exists on BetterVoting but has no LH yaml, e.g. Bloc Plurality) are read from the frozen `*_bv_export.json` and appear tagged `BV (no yaml)`.
- **Naming:** BV-backed case files carry the bvid (`bv<testid>_<bvid>_<descriptor>`); LH-only files use a descriptive name. A contested election keeps its races in one folder with a lead `.md` and a `README.md`.
- **To add a case:** drop the yaml(s), run the engine (writes the `_tabulated` mirror), then regenerate the indexes (`build_yaml_pages`, `build_bv_registry`, `build_multirace_index`, `build_catalog`). The pre-commit hook refreshes the generated indexes automatically.

