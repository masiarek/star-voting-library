---
search:
  exclude: true
---

# STAR elects a covered candidate — five ballots, four cities

*Generated from [`star_elects_a_covered_candidate_c4_b5.yaml`](../star_elects_a_covered_candidate_c4_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Denver

## Scenario

A candidate is COVERED when someone beats them AND beats everyone they beat: strictly redundant, on the pairwise evidence alone. The uncovered set — the candidates nobody covers — is the weakest structural filter in the tournament-solutions literature, usually leaving most of the field standing, and it is the coarsest filter that guarantees a Pareto-optimal choice. This election is five ballots where STAR's winner is outside it. Denver takes the STAR result: Austin leads the scoring round with 14 to Denver's 11, and Denver wins the automatic runoff 3-2. Now read the pairwise grid. Chicago beats Denver. And Austin — the only city Denver beats — is also beaten by Chicago. So Chicago does everything Denver does and more: Denver is COVERED by Chicago, the only covered city here, and the uncovered set is {Austin, Boston, Chicago}. Three of the four clear the bar; STAR elects the one that doesn't. Two honest halves to the lesson. Against STAR: no rule that reads only the win-loss graph would elect Denver, and "beaten by someone who also beats everyone you beat" is an objection a normal voter understands on hearing it. For STAR: covering is a purely ORDINAL verdict, and Denver is NOT Pareto-dominated — ballot 3 scores Denver 5 and Chicago 0, so no voter is overruled. Denver also outscores both Boston (9) and Chicago (10). STAR is deliberately reading the strength-of-preference information the tournament discards, and here the two kinds of evidence point different ways. Which one should govern is the actual disagreement between the score and pairwise camps; this election is small enough to hold both halves in view at once. Ranked Robin lands inside the uncovered set, as it always must: Boston and Chicago each go 2-1, so Copeland ties them — both uncovered — and the graph alone says only "one of these two." That Copeland tie is forced at this size: with exactly FOUR candidates a unique Copeland winner and a Condorcet winner are the same thing (verified exhaustively over all 64 four-candidate tournaments), so a cycle here guarantees a tie. Five candidates is the first size at which Copeland can be decisive inside a cycle (280 of the 1024 five-candidate tournaments). The tie then breaks deterministically but differently per engine, which makes this a live example of the documented LH-vs-BetterVoting split: LH's rung is total margin, and Chicago (+1) beats Boston (-1), so the report below elects CHICAGO. BetterVoting's rung is the head-to-head between the tied pair, and Boston beats Chicago 3-2, so BV would elect BOSTON. No lot is involved on either side — the two published ladders simply disagree. Say which engine you are quoting. Every ballot uses four DISTINCT scores on purpose: score-to-rank conversion is then unambiguous, no Equal Support appears in any head-to-head, and none of the comparison methods below can be dismissed as a tie-breaking artifact. Search-built and verified twice: a search over random strict score ballots for a tie-free tournament whose STAR winner is covered, confirmed by the LH engine below and by pref_voting's four independent covering variants (Gillies, Fishburn, Bordes, McKelvey — all four agree here). LH-only as committed: the STAR result is engine-independent, but the Ranked Robin comparison line depends on which tiebreak ladder you run, so the full picture is quoted against the LH engine.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Austin,Boston,Chicago,Denver
0,4,2,1
2,1,3,0
4,1,0,5
5,2,0,1
3,1,5,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Denver
  Choose-One (Plurality) = Chicago   (differs from STAR)
  RCV-IRV                = Chicago   (differs from STAR)
  Approval               = Austin   (differs from STAR)
  RCV-RR                 = Boston   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/star_elects_a_covered_candidate_c4_b5_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/star_elects_a_covered_candidate_c4_b5_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Austin)
 - Runoff Round Winner   = (Denver)
  Candidate Austin earned the highest total score, but
  Candidate Denver won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Austin,Boston,Chicago,Denver
     0,     4,      2,     1
     2,     1,      3,     0
     4,     1,      0,     5
     5,     2,      0,     1
     3,     1,      5,     4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Austin        -- 14 -- First place
   Denver        -- 11 -- Second place
   Chicago       -- 10
   Boston        --  9
 Austin and Denver advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Denver        -- 3 -- First place
   Austin        -- 2
   Equal Support -- 0
 Denver wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Denver 3 (60%)  ·  Austin 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Denver
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Austin   |   Boston   |   Chicago  | * Denver   |
----------------------------------------------------------------------
     * Austin > |     ---     | 4 - 0 - 1  | 2 - 0 - 3  | 2 - 0 - 3  |
       Boston > |  1 - 0 - 4  |    ---     | 3 - 0 - 2  | 3 - 0 - 2  |
      Chicago > |  3 - 0 - 2  | 2 - 0 - 3  |    ---     | 3 - 0 - 2  |
     * Denver > |  3 - 0 - 2  | 2 - 0 - 3  | 2 - 0 - 3  |    ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Austin > Boston > Chicago > Austin)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Austin     1  1  1  1  0  1  |    14   2.8
Boston     0  1  0  1  3  0  |     9   1.8
Chicago    1  0  1  1  0  2  |    10   2.0
Denver     1  1  0  0  2  1  |    11   2.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/star_elects_a_covered_candidate_c4_b5_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/tournament_solutions/cases/star_elects_a_covered_candidate_c4_b5.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/star_elects_a_covered_candidate_c4_b5.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Exhausted ballots (untangled)](../../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [copeland_vs_clones_c5_b3](copeland_vs_clones_c5_b3.md) · [five_answers_one_election_c4_b3](five_answers_one_election_c4_b3.md)
