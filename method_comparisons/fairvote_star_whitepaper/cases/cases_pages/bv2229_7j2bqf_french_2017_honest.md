# FairVote white paper — French 2017 (HONEST): STAR elects the centrist Macron

*Generated from [`bv2229_7j2bqf_french_2017_honest.yaml`](../bv2229_7j2bqf_french_2017_honest.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Macron

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/7j2bqf) · **[results ↗](https://bettervoting.com/7j2bqf/results)** (election `7j2bqf`).

## Scenario

FairVote's July 2018 white paper "Explaining FairVote's position on STAR Voting"
(Richie & Penrose) argues STAR's strategy incentives could squeeze a strong centrist
out of the runoff, using the 2017 French presidential race as its example (four
strong candidates ~20% each; Macron the broadly-preferred centrist). This is the
HONEST half: voters score sincerely (favorite 5, the compromise Macron 4, the far
wing 0). STAR elects Macron — the Condorcet winner (he beats Le Pen, Fillon and
Melenchon head-to-head) — scoring round Macron 351, runoff 51-49. RCV-IRV also
elects Macron here. The companion french_2017_strategic shows FairVote's coordinated
burial (everyone scores Macron 0 and inflates the other wings) knocking Macron out —
which STAR concedes is possible, but which requires implausible coordinated dishonesty
and is not STAR's sincere behavior. Simplified 100-voter model of the ~20%-each field.
Concept: ../README.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Macron,LePen,Fillon,Melenchon
26:5,0,3,3   # Macron base
25:4,0,1,5   # Melenchon (left) — Macron is their compromise 2nd
24:4,2,5,0   # Fillon (center-right) — Macron 2nd
25:1,5,3,0   # Le Pen (far right)
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Macron,LePen,Fillon,Melenchon
   26 ×      5,    0,     3,        3
   25 ×      4,    0,     1,        5
   25 ×      1,    5,     3,        0
   24 ×      4,    2,     5,        0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Macron        -- 351 -- First place
   Fillon        -- 298 -- Second place
   Melenchon     -- 203
   LePen         -- 173
 Macron and Fillon advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Macron        -- 51 -- First place
   Fillon        -- 49
   Equal Support --  0
 Macron wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Macron 51 (51%)  ·  Fillon 49 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Macron
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |   * Macron    |     LePen    |  * Fillon    |   Melenchon  |
--------------------------------------------------------------------------------
       * Macron > |      ---      |75 -  0 - 25  |51 -  0 - 49  |75 -  0 - 25  |
          LePen > | 25 -  0 - 75  |     ---      |25 -  0 - 75  |49 -  0 - 51  |
       * Fillon > | 49 -  0 - 51  |75 -  0 - 25  |     ---      |49 - 26 - 25  |
      Melenchon > | 25 -  0 - 75  |51 -  0 - 49  |25 - 26 - 49  |     ---      |

[Condorcet Winner]
  Condorcet Winner: Macron — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Macron     26  49   0   0  25   0  |   351   3.5
LePen      25   0   0  24   0  51  |   173   1.7
Fillon     24   0  51   0  25   0  |   298   3.0
Melenchon  25   0  26   0   0  49  |   203   2.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2229_7j2bqf_french_2017_honest_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/fairvote_star_whitepaper/cases/bv2229_7j2bqf_french_2017_honest.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2230_2hqmrd_french_2017_burial](bv2230_2hqmrd_french_2017_burial.md) · [bv2231_b4yr3v_wa_2010_honest](bv2231_b4yr3v_wa_2010_honest.md) · [bv2232_24b623_wa_2010_burial](bv2232_24b623_wa_2010_burial.md)
