# 06_Other — reference cases for other (non-EVC) methods

Standalone demos of methods this library teaches *about* but does not promote: they're here for completeness and honest comparison, not prominence. Each method gets its own subfolder.

| Method | Case (page) | What it shows | src |
|---|---|---|:--:|
| **[RCV_IRV/](RCV_IRV)** | [RCV ballot example](RCV_IRV/RCV_IRV_pages/RCV_ballot_example.md) | a plain ranked-ballot instant-runoff count | [`.yaml`](RCV_IRV/RCV_ballot_example.yaml) |
| **[STV/](STV)** | [STV — 3 seats](STV/STV_pages/03a_stv_3seats.md) | proportional seats from ranked ballots (compare [proportional STAR](../03_STAR_PR/) on score ballots) | [`.yaml`](STV/03a_stv_3seats.yaml) |
| **[Range/](Range)** | [Range / Score 101](Range/Range_pages/range_101_c3_b5.md) | highest total score wins — STAR without the runoff | [`.yaml`](Range/range_101_c3_b5.yaml) |
| **[three_two_one/](three_two_one)** | [3-2-1 Voting](three_two_one/README.md) | Good/OK/Bad → 3 semifinalists → 2 finalists → 1 winner (Tennessee, blank = Bad) | [`.yaml`](three_two_one/321_tennessee_blank_encoding_c4_b100.yaml) |

Range overview: [Range / Score Voting](../00_start_here/Range_Voting/range_voting.md); engine: [Range / Score voting tabulation engine](Range/Range_tabulation_engine/) (pref_voting). **3-2-1** has its own clean-room engine ([`three_two_one/three_two_one_tabulation.py`](three_two_one/three_two_one_tabulation.py)), verified against [Jameson Quinn](../00_start_here/topics/in_memoriam_jameson_quinn.md)'s reference vectors — no off-the-shelf 3-2-1 engine exists.

Most non-EVC material lives where it teaches best: inside [method comparisons](../method_comparisons/), where RCV-IRV and choose-one serve as the foil to the equal-vote methods. Concept docs: [RCV-IRV (Hare)](../00_start_here/RCV_IRV/RCV-IRV-Hare.md), [Borda](../00_start_here/other_ranked_methods/borda.md), and [Agenda voting](../00_start_here/other_ranked_methods/agenda_voting.md).

# file: README.md
