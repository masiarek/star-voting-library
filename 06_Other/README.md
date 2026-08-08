# Other methods — what this library teaches *about* but does not promote

Standalone demos of the methods outside the equal-vote family: they're here for completeness and honest comparison, not prominence.

The folder has two halves. **Methods that earned a folder** get one — a `README.md`, concept pages, and runnable `cases/`:

| Method | Case (page) | What it shows | src |
|---|---|---|:--:|
| **[Choose-One (Plurality)](Plurality/README.md)** | [Team lunch — a dead tie](Plurality/cases/cases_pages/lunch_choose_one_dead_tie.md) | mark one box, count the marks — and a 2–2 tie the ballots can't break | [`.yaml`](Plurality/cases/lunch_choose_one_dead_tie.yaml) |
| **[RCV-IRV](RCV_IRV/README.md)** | [RCV ballot example](RCV_IRV/cases/cases_pages/RCV_ballot_example.md) | a plain ranked-ballot instant-runoff count | [`.yaml`](RCV_IRV/cases/RCV_ballot_example.yaml) |
| **[STV](STV/README.md)** | [STV — 3 seats](STV/cases/cases_pages/03a_stv_3seats.md) | proportional seats from ranked ballots (compare [proportional STAR](../03_STAR_PR/README.md) on score ballots) | [`.yaml`](STV/cases/03a_stv_3seats.yaml) |
| **[Range / Score](Range/README.md)** | [Range / Score 101](Range/cases/cases_pages/range_101_c3_b5.md) | highest total score wins — STAR without the runoff | [`.yaml`](Range/cases/range_101_c3_b5.yaml) |
| **[Majority Judgment](Majority_Judgment/README.md)** | [Majority Judgment](Majority_Judgment/concepts/majority_judgment.md) | grade in words (*To Reject … Excellent*); the highest **median** wins — the same ballot as Range, counted so one enthusiast can't drag it | [`.yaml`](Majority_Judgment/cases/mj_101_c3_b5.yaml) |
| **[3-2-1 Voting](three_two_one/README.md)** | [3-2-1 Voting](three_two_one/README.md) | Good/OK/Bad → 3 semifinalists → 2 finalists → 1 winner (Tennessee, blank = Bad) | [`.yaml`](three_two_one/cases/321_tennessee_blank_encoding_c4_b100.yaml) |
| **[Combined Approval (CAV)](Combined_Approval/README.md)** | [The newcomer nobody dislikes](Combined_Approval/cases/cases_pages/cav_library_board_c3_b12.md) | For / abstain / Against, highest net wins — and the same twelve voters reversed end-to-end when a blank counts as the bottom grade instead of the middle | [`.yaml`](Combined_Approval/cases/cav_library_board_c3_b12.yaml) |

Range overview: [Range / Score Voting](Range/concepts/range_voting.md); engine: [Range / Score voting tabulation engine](Range/Range_tabulation_engine/README.md) (pref_voting). **Majority Judgment** has no `_tabulated` mirrors or generated pages, and deliberately: its grades are *words*, so its files carry a `grades:` block rather than `ballots:` and are counted by [`grade_methods_report.py`](../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/README.md) — the count lives on the concept page. **CAV** likewise ships a clean-room engine ([`Combined_Approval/cav_tabulation.py`](Combined_Approval/cav_tabulation.py)) — no off-the-shelf tabulator exists, so every count is verified by an internal affine-invariance check *and* by `pref_voting` on the equivalent (0,1,2) profile. **3-2-1** has its own clean-room engine ([`three_two_one/three_two_one_tabulation.py`](three_two_one/three_two_one_tabulation.py)), verified against [Jameson Quinn](../07_Concepts/topics/in_memoriam_jameson_quinn.md)'s reference vectors — no off-the-shelf 3-2-1 engine exists.

**Methods too thin for a folder** share one — [`other_ranked_methods/`](other_ranked_methods/README.md) is a shelf, not a method: a concept page apiece for [Borda](other_ranked_methods/borda.md) (manufacturing scores from ranks) and [agenda voting](other_ranked_methods/agenda_voting.md) (where the *order* of the pairwise votes picks the winner). Neither has runnable cases yet; the day one does, it graduates to its own folder.

Alongside those sit the **labs and the engine** — not methods, but the tooling that compares them:

- [`simulations/`](simulations/README.md) — brute-force, utility-first method-comparison sims (FBC, runoff reversal, STAR-vs-Approval divergence).
- [`ballot_style_lab/`](ballot_style_lab/README.md) — a seeded generator of random-but-HUMAN electorates (style-gallery renderings over slanted faction utilities: harsh 0–2 graders, gentle 3–5 souls, cliff voters, bullet brigades) frozen into ten stress cases with ties, cycles and reversals: six single-winner STAR plus a multi-winner wing (a same-ballots Bloc-vs-STAR-PR twin pair, a 2-seat quota stress, and a 7-candidate / 4-seat Bloc run).
- [`abcvoting_tabulation_engine/`](abcvoting_tabulation_engine/README.md) — multi-winner Approval (ABC) rules via Martin Lackner's `abcvoting`, the independent cross-check on the LH bloc-Approval count.

Most non-EVC material lives where it teaches best: inside [method comparisons](../method_comparisons/README.md), where RCV-IRV and choose-one serve as the foil to the equal-vote methods. Concept docs: [RCV-IRV (Hare)](RCV_IRV/concepts/RCV-IRV-Hare.md), [Borda](other_ranked_methods/borda.md), and [Agenda voting](other_ranked_methods/agenda_voting.md).

# file: README.md
