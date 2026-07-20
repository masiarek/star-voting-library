# STAR's runoff is spoiler-sensitive under a Condorcet cycle

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/g3f7r2) · **[results ↗](https://bettervoting.com/g3f7r2/results)** (election `g3f7r2`, Test ID BV2212).

**One line:** when the head-to-head results form a Condorcet cycle, a candidate who *cannot win* can still decide *who does* — because their presence changes which two candidates meet in STAR's automatic runoff. This is STAR's honest Independence-of-Irrelevant-Alternatives (IIA) limit, shown mechanically, on perfectly sincere ballots.

This is the sharpest fair criticism of STAR from the [r/EndFPTP thread](https://www.reddit.com/r/EndFPTP/comments/1uyjqgf/) that prompted it (user *Excellent_Air8235*) — not a strawman, and worth teaching honestly alongside STAR's strengths. See also the broader [STAR — Honest Limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md).

---

## The setup — 23 voters, three rotating factions, all sincere

Three candidates (**Alice, Ben, Carla**) and three blocs, each voting its true preference — favorite **5**, compromise **3**, last choice **0**. No strategy anywhere.

| Count | Alice | Ben | Carla | Sincere order |
|------:|:-----:|:---:|:-----:|:--------------|
| **10** | 5 | 3 | 0 | Alice > Ben > Carla |
| **6**  | 0 | 5 | 3 | Ben > Carla > Alice |
| **7**  | 3 | 0 | 5 | Carla > Alice > Ben |

The three factions rotate, so **every candidate beats one rival head-to-head and loses to the other** — a Condorcet cycle with no Condorcet winner:

- Alice ▸ Ben (17–6)
- Ben ▸ Carla (16–7)
- Carla ▸ Alice (13–10)

---

## What STAR does — Alice wins

Scoring round totals **Alice 71, Ben 60, Carla 53**, so the finalists are **Alice and Ben**, and Alice takes the runoff 17–6. STAR elects **Alice** — cleanly, with no tie-break (BetterVoting reports `tieBreakType: none`, and BV's own count agrees: elected = Alice).

## The IIA failure — delete Ben, and Carla wins

Ben finishes **second** and loses the runoff — he never had a path to victory. Remove him from the ballot and change *nothing else*:

| Count | Alice | Carla |
|------:|:-----:|:-----:|
| 10 | 5 | 0 |
| 6  | 0 | 3 |
| 7  | 3 | 5 |

Now the finalists are **Alice (71) and Carla (53)**, and the runoff **flips**: Carla beats Alice **13–10**, so STAR elects **Carla**.

> A losing candidate (Ben) determined whether **Alice or Carla** wins — with not one voter changing a single score. STAR's ballot is cardinal, but its *finish* is ordinal (a top-two runoff), and inside a Condorcet cycle the choice of finalists is itself sensitive to a third candidate who can't win. That's the IIA failure, located precisely in the runoff **stage**.

It is a real, honest cost — and note what it is **not**: it needs no dishonest ballots (these are fully sincere), and it only bites when the electorate has *no* Condorcet winner at all (a genuine three-way cycle). When a Condorcet winner exists, STAR's runoff can't be spoiled this way.

---

## Bonus — one election, three different winners

The same 23 sincere ballots, counted three ways, split every method apart:

| Method | Winner | Why |
|---|:---:|---|
| **STAR** | **Alice** | Finalists Alice (71) & Ben (60); Alice wins the runoff 17–6 |
| **RCV-IRV** | **Carla** | Ben has the fewest first choices, is eliminated, and his 6 ballots transfer to Carla (13 vs Alice's 10) |
| **Ranked Robin** (Copeland) | **Alice** | Every candidate is 1–1 in the cycle; LH breaks the Copeland tie by margin → Alice's +11 win is largest |

Because the Ranked Robin result is a **tie-break**, it is **not freezable on BetterVoting** — LH breaks the Copeland tie deterministically (by margin), but BetterVoting breaks it **randomly**, so a live BV RR race here couldn't be reproduced. This case therefore ships **STAR-only** on BetterVoting (same reasoning as [BV830](../tie_break_ladder/bv830_vb3xv2_no_condorcet_tie_score.md)). The RR angle stays LH-side commentary.

---

## View 1 — BetterVoting

Live results: **[bettervoting.com/g3f7r2/results](https://bettervoting.com/g3f7r2/results)**. BetterVoting's STAR count agrees with LH exactly — **elected: Alice**, finalists Alice (71) & Ben (60), runoff 17–6, `tieBreakType: none`. The frozen export (Election + Ballots + Results) is [`bv2212_g3f7r2_cycle_spoiler_bv_export.json`](cases/bv2212_g3f7r2_cycle_spoiler_bv_export.json); its `winsAgainst` data encodes the same cycle (Alice▸Ben, Ben▸Carla, Carla▸Alice).

## View 2 — the LH tabulation (on-screen report)

```
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Alice    |   * Ben     |    Carla    |
-------------------------------------------------------------
       * Alice > |     ---      |17 -  0 -  6 |10 -  0 - 13 |
         * Ben > |  6 -  0 - 17 |    ---      |16 -  0 -  7 |
         Carla > | 13 -  0 - 10 | 7 -  0 - 16 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Alice > Ben > Carla > Alice)

[Divergence from STAR]
  STAR    = Alice
  RCV-IRV = Carla   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.

--- STAR Voting Method (single winner) ---
 Tabulating 23 ballots.
Count × Alice,Ben,Carla
   10 ×     5,  3,    0
    7 ×     3,  0,    5
    6 ×     0,  5,    3

Scoring Round
   Alice         -- 71 -- First place
   Ben           -- 60 -- Second place
   Carla         -- 53
 Alice and Ben advance.

Automatic Runoff Round
   Alice         -- 17 -- First place
   Ben           --  6
   Equal Support --  0
 Alice wins.
   Voters with a preference: 23 of 23 (no Equal Support).
   Alice 17 (74%) vs Ben 6 (26%); majority = 12.

Winner — STAR Voting Method (single winner)
 Alice
```

Full engine detail: [`iia_cycle_spoiler_tabulated/bv2212_g3f7r2_cycle_spoiler_tabulated.txt`](cases/cases_tabulated/bv2212_g3f7r2_cycle_spoiler_tabulated.txt) · run it: [`bv2212_g3f7r2_cycle_spoiler.yaml`](cases/bv2212_g3f7r2_cycle_spoiler.yaml).
