# FairVote white paper — Washington 2010 (HONEST): STAR elects the moderate Berkey

*Generated from [`bv2231_b4yr3v_wa_2010_honest.yaml`](../bv2231_b4yr3v_wa_2010_honest.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Berkey

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/b4yr3v) · **[results ↗](https://bettervoting.com/b4yr3v/results)** (election `b4yr3v`).

## Scenario

FairVote's white paper cites the real 2010 Washington State Senate race — moderate
Democrat Jean Berkey, progressive Nick Harper, and long-shot conservative Rod Rieger,
where union-backed groups boosted Rieger to squeeze Berkey out — as a case STAR would
make "even easier" to manipulate. This is the HONEST half: scored sincerely, STAR
elects Berkey, the moderate and Condorcet winner (she beats Harper 60-40 head-to-head
and Rieger too), scoring round Berkey 385, runoff 60-40. RCV-IRV also elects Berkey.
The companion wa_2010_strategic shows the burial FairVote describes (Harper voters
score Harper 5, Rieger 4, Berkey 0) squeezing Berkey out under STAR — conceded — while,
notably, RCV-IRV on those same strategic ballots STILL elects Berkey. Concept: ../README.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Berkey,Harper,Rieger
35:5,3,1   # Berkey (moderate) base
40:4,5,0   # Harper (progressive) base — Berkey their honest 2nd
25:2,0,5   # Rieger (conservative) base
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Berkey
  Choose-One (Plurality) = Harper   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Berkey,Harper,Rieger
   40 ×      4,     5,     0
   35 ×      5,     3,     1
   25 ×      2,     0,     5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Berkey        -- 385 -- First place
   Harper        -- 305 -- Second place
   Rieger        -- 160
 Berkey and Harper advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Berkey        -- 60 -- First place
   Harper        -- 40
   Equal Support --  0
 Berkey wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Berkey 60 (60%)  ·  Harper 40 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Berkey
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Berkey   |  * Harper   |    Rieger   |
-------------------------------------------------------------
      * Berkey > |     ---      |60 -  0 - 40 |75 -  0 - 25 |
      * Harper > | 40 -  0 - 60 |    ---      |75 -  0 - 25 |
        Rieger > | 25 -  0 - 75 |25 -  0 - 75 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Berkey — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Berkey     35  40   0  25   0   0  |   385   3.9
Harper     40   0  35   0   0  25  |   305   3.1
Rieger     25   0   0   0  35  40  |   160   1.6
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2231_b4yr3v_wa_2010_honest_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/fairvote_star_whitepaper/cases/bv2231_b4yr3v_wa_2010_honest.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2229_7j2bqf_french_2017_honest](bv2229_7j2bqf_french_2017_honest.md) · [bv2230_2hqmrd_french_2017_burial](bv2230_2hqmrd_french_2017_burial.md) · [bv2232_24b623_wa_2010_burial](bv2232_24b623_wa_2010_burial.md)
