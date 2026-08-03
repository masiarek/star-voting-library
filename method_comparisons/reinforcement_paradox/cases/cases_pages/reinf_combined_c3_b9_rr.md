---
search:
  exclude: true
---

# Reinforcement — combined 9 voters, counted by Ranked Robin (Cara wins)

*Generated from [`reinf_combined_c3_b9_rr.yaml`](../reinf_combined_c3_b9_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn) · **1 seat** · **Expected winner:** Cara

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/t4by6x) · **[results ↗](https://bettervoting.com/t4by6x/results)** (election `t4by6x`).

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

North (6 voters) + South (3 voters) merged, from Brandt, Dong & Peters,
"Condorcet-Consistent Choice Among Three Candidates" (2024), Theorem 2
(P1 + P2). Ada was a winner in BOTH districts (outright in South, a co-winner
in North's dead-heat cycle) — so reinforcement/consistency says Ada should win
the merged election. Instead a NEW Condorcet winner appears:

    Cara beats Ada 5–4 · Cara beats Ben 5–4 · Ada beats Ben 7–2

Cara beats everyone head-to-head, so every Condorcet method — Ranked Robin
included — elects Cara. Ada, the only candidate who won both parts, loses. That
is the reinforcement paradox, which the paper proves is unavoidable for EVERY
Condorcet extension once there are ≥ 8 voters.

The same 9 ballots counted by STAR: reinf_combined_c3_b9_star.yaml (the
scoring round leads Ada, but the runoff flips to Cara — STAR's runoff catches
the same pairwise flip). Additive methods (Score/Approval/Plurality) instead
keep Ada and show no paradox — see the folder README.

## Parameters (from the YAML)

```yaml
bv_test_id: BV2254
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Ada>Ben>Cara
2:Ben>Cara>Ada
3:Cara>Ada>Ben
2:Ada>Cara>Ben
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 9 ballots (ranked ballots).

Ballots:
     2 × Ada > Ben > Cara
     2 × Ben > Cara > Ada
     3 × Cara > Ada > Ben
     2 × Ada > Cara > Ben

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    7 – 2
   Cara  beats Ada    5 – 4
   Cara  beats Ben    5 – 4

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |7 - 0 - 2 |4 - 0 - 5 |
   Ben > | 2 - 0 - 7 |   ---    |4 - 0 - 5 |
  Cara > | 5 - 0 - 4 |5 - 0 - 4 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Cara       2–0–0         2      +2  Ada, Ben
    2  Ada        1–1–0         1      +4  Ben
    3  Ben        0–2–0         0      -6  —

Winner — Ranked Robin (RCV-RR): Cara
   beats every opponent head-to-head — the Condorcet winner.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Cara
   Outside (2):        Ada, Ben
   One member ⇒ Cara is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Cara is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/reinf_combined_c3_b9_rr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reinforcement_paradox/cases/reinf_combined_c3_b9_rr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [reinf_combined_ben_c3_b9_rr](reinf_combined_ben_c3_b9_rr.md) · [reinf_combined_c3_b9_star](reinf_combined_c3_b9_star.md) · [reinf_combined_cara_c3_b9_rr](reinf_combined_cara_c3_b9_rr.md) · [reinf_north_c3_b6_rr](reinf_north_c3_b6_rr.md) · [reinf_south_ben_c3_b3_rr](reinf_south_ben_c3_b3_rr.md) · [reinf_south_c3_b3_rr](reinf_south_c3_b3_rr.md) · [reinf_south_cara_c3_b3_rr](reinf_south_cara_c3_b3_rr.md)
